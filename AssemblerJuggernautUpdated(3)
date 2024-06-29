# This is the Assembler for the Juggernaut CPU in Minecraft
# Build by Jobe, WildScaryFox, JediZach, Saturnxcode, Tarmalot and Death_Slice
# Code written by Jobe


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
# / -> No Operand in that position
# Numbers are an Immediate unless they have a Prefix
 
# ISA OpCodeList
op_code_list = {
    'nop': '0', 'add': '1', 'sub': '2', 'nota': '3', 'neg': '4','mp': '5', 'nimp': '6', 'and': '7', 
    'or': '8','xor': '9','nand': '10', 'nor': '11', 'xnor': '12', 'bsu': '13', 'bsd': '14','bsur': '15',
    'bsdr': '16','addca': '17', 'jmp': '18','branch': '19', 'jmpr': '20', 'branchr': '21','ldi': '22','mov': '23',
    'rldi': '24','str': '25','ldr': '26','pin': '27','pout': '28','pinr': '29','poutr': '30','incr': '31',
    'decr': '32','mult': '33','div': '34','mod': '35','sqr': '36','sqrt': '37','cmpr': '38','lflgre': '39',
    'lflgra': '40','lpre': '41','rpre': '42','lpra': '43','rpra': '44','psh': '45','pop': '46','call': '47',
    'rtrn': '48','rnd': '49','swp': '50','': '51','': '52','': '53','': '54','': '55',
    '': '56','': '57','': '58','': '59','': '60','': '61','stl': '62','hlt': '63',
}
 
# Main
max_lines = 0
 
# Talks to the user
print()
print("| This is the Assembler for the Juggernaut CPU, made entirely in Minecraft.")
print("| Juggernaut has been built by: Jobe, WildScaryFox, JediZach, Saturnxcode, Tarmalot and Death_Slice")
print()
wait(.5)
print("How many Lines of Code do you need (the maximum is 65536 lines):")
 
# Take input from user and convert str to int
input_a = input()
input_a = int(input_a)

stop = 0
input_lines = []  # Initialize an empty list to hold the input lines
 
# Helper function to convert operand to binary
def operand_to_binary(operand):
    if operand.startswith('$'):
        # Assuming register addresses are in the form $0, $1, ..., $15 and need to be 4-bit binary -> first 4 bits of reg will always be 0000XXXX
        return format(int(operand[1:]), '08b')
    elif operand.startswith('@'):
        # Assuming RAM needs to be treated as immediate values
        return format(int(operand[1:]), '08b')  
    elif operand.startswith(' '):
        # If there is no Operand needed in Line
        return "00000000"
    elif operand.startswith('&'):
        return format(int(operand[1:]), '08b')
    else:
        # Immediate value
        return format(int(operand), '08b')  

def check_line():
    global stop
    # Checks whether the number of lines is allowed
    if input_a > 65536:
        print()
        print("The number", input_a, "is above the limit of 65536")
        stop += 1
        return
    elif input_a < 0:
        print()
        print("The number", input_a, "is negative")
        stop += 1
        return
    else: 
        stop = 0

check_line()
 
def display_inputs(inputs):
    # Function to display current inputs
    print("\nCurrent Inputs:")
    for index, line in enumerate(inputs, start=+1):
        print(f"{index}: {line}")
    print()

def assemble(input_lines):
    for index, line in enumerate(input_lines, start=1):
        tokens = line.split()
        if tokens:
            opcode = tokens[0]
            operands = tokens[1:]
            if opcode in op_code_list:
                binary_opcode = format(int(op_code_list[opcode]), '08b')
                binary_operands = [operand_to_binary(op) for op in operands]
                # Combine the binary parts
                final_binary_instruction = binary_opcode + ''.join(binary_operands)
                # Format the final binary instruction to be 4 8-bit strings
                formatted_instruction = ' '.join(final_binary_instruction[i:i+8] for i in range(0, len(final_binary_instruction), 8))
                
                print(formatted_instruction)
            else:
                print(f"Unknown opcode: '{opcode}'")
                return()
    print("You can now copy this into the Schematic Generator")

if stop == 0:
    print("The ISA:")
    print()
    print("\n".join(op_code_list.keys())) 
    print()
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
    print()
    # Print the variables to verify
    for index in range(1, len(input_lines)+1):
        print(f"line {index}:", globals()[f"line_{index}"])
    
    while True:
        print("Press Enter to continue or press # to stop and edit the Code.")
        action = input().strip()
        
        if action == "":  # Check if the input is the Enter key (empty string)
            print("Enter key detected, Assembling your Code.")
            assemble(input_lines)  
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
