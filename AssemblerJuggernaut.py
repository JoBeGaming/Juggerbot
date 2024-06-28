#This is the Assembler for the Juggernaut CPU in Minecraft
#Build by Jobe, WildScaryFox, JediZach, Saturnxcode and Death_Slice
#Code written by Jobe


# Imports
import sys
import time as t
import math as m

def wait(seconds):
    t.sleep(seconds)
 
# Prefixes
# $ -> Register Address
# @ -> Ram Address
# & -> I/O Port Address
# Numbers are an Immediate unless they have a Prefix
 
# ISA OpCodeList
OpCodeList = {
    'nop': '0', 'add': '1', 'sub': '2', 'nota': '3', 'neg': '4',
    'imp': '5', 'nimp': '6', 'and': '7', 'or': '8', 'xor': '9',
    'nand': '10', 'nor': '11', 'xnor': '12', 'bsu': '13', 'bsd': '14',
    'bsur': '15', 'bsdr': '16', 'addca': '15', 'bsdr': '15', 'jmp': '16',
    'branch': '17', 'jmpr': '18', 'branchr': '19',
}
 
# Main
maxlines = 0
 
# Talks to the user
print("This is the Assembler for the Juggernaut CPU, made entirely in Minecraft.")
print("Juggernaut has been built by: Jobe, WildScaryFox, JediZach, Saturnxcode and Death_Slice")
wait(.5)
print("How many Lines of Code do you need (the maximum is 65536 lines)?")
print("It is not suggested to go above 500 lines though.")
 
# Take input from user and convert str to int
input_a = input()
input_a = int(input_a)

stop = 0
 
def checkline():
    global stop
    # Checks whether the number of lines is allowed
    if input_a > 65536:
        print("The number", input_a, "is above the limit of 65536")
        stop += 1
        return
    elif input_a < 0:
        print("The number", input_a, "is negative")
        stop += 1
        return
 
checkline()
 
def display_inputs(inputs):
    # Function to display current inputs
    print("\nCurrent Inputs:")
    for index, line in enumerate(inputs, start=1):
        print(f"{index}: {line}")
    print("")
 
CodeLines = input_a

def assemble(input_lines,CodeLines):
    for index in range(1, len(input_lines) + 1):
        print(f"line {index}:", globals()[f"line_{index}"])

if stop == 0:
    input_lines = []  # Initialize an empty list to hold the input lines
    print("The ISA:")
    print("\n".join(OpCodeList.keys()))
    print("Please enter up to", input_a, "lines of input (Press Enter twice to finish early):")
    
    # Read up to 65536 lines of input from the Terminal
    for i in range(1, input_a + 1):
        try:
            line = input(f"{i} | ")
            if line == "":
                break
            input_lines.append(line)
        except EOFError:
            break
    
    for index, line in enumerate(input_lines, start=1):
        # Assign each line to a new variable
        globals()[f"line_{index}"] = line
    
    print("Here is the code you wrote (To verify):")
    # Print the variables to verify
    for index in range(1, len(input_lines) + 1):
        print(f"line {index}:", globals()[f"line_{index}"])
    
    while True:
        print("Press Enter to continue or press # to stop and edit the Code.")
        action = input().strip()
        
        if action == "":  # Check if the input is the Enter key (empty string)
            print("Enter key detected, Assembling your Code.")
            assemble(input_lines,CodeLines)  
            break
        elif action == "#":
            print("# key detected, you can now edit your Code")
            display_inputs(input_lines)
            edit_index = input("Enter the line number to edit (or 'c' to continue): ").strip()
            
            if edit_index.lower() == 'c':
                continue
            elif edit_index.isdigit() and 1 <= int(edit_index) <= len(input_lines):
                new_input = input(f"Edit line {edit_index}: ")
                input_lines[int(edit_index) - 1] = new_input
                display_inputs(input_lines)
            else:
                print("Invalid line number.")
        else:
            print("Invalid input, please press Enter to continue or # to edit the Code.")
            