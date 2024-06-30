# This is the Assembler for the Juggernaut CPU in Minecraft
# Build by Jobe, WildScaryFox, JediZach, Saturnxcode, Tarmalot and Death_Slice
# Code written by Jobe


# Imports
import sys
import time as t

# Prefixes
# $ -> Register Address
# @ -> Ram Address
# & -> I/O Port Address
# / -> No Operand in that position
# Numbers are an Immediate unless they have a Prefix
 
# ISA OpCodeList
op_code_list = {
    'nop': '0', 'add': '1', 'sub': '2', 'nota': '3', 'neg': '4','imp': '5', 'nimp': '6', 'and': '7', 
    'or': '8','xor': '9','nand': '10', 'nor': '11', 'xnor': '12', 'bsu': '13', 'bsd': '14','bsur': '15',
    'bsdr': '16','addca': '17', 'jmp': '18','branch': '19', 'jmpr': '20', 'branchr': '21','ldi': '22','mov': '23',
    'rldi': '24','str': '25','ldr': '26','pin': '27','pout': '28','pinr': '29','poutr': '30','incr': '31',
    'decr': '32','mult': '33','div': '34','mod': '35','sqr': '36','sqrt': '37','cmpr': '38','lflgre': '39',
    'lflgra': '40','lpre': '41','rpre': '42','lpra': '43','rpra': '44','psh': '45','pop': '46','call': '47',
    'rtrn': '48','rnd': '49','swp': '50','': '51','': '52','': '53','': '54','': '55',
    '': '56','': '57','': '58','': '59','': '60','': '61','stl': '62','hlt': '63'
}
 
# ISA Contents
operand_list = {
    'nop': {'1':'/','2':'/','3':'/'},'add': {'1':'$','2':'$','3':'$'},'sub': {'1':'$','2':'$','3':'$'},'nota': {'1':'$','2':'/','3':'$'},'neg': {'1':'$','2':'/','3':'$'},'imp': {'1':'/','2':'/','3':'/'},'nimp': {'1':'/','2':'/','3':'/'},'and': {'1':'/','2':'/','3':'/'},
    'or': {'1':'/','2':'/','3':'/'},'xor': {'1':'/','2':'/','3':'/'},'nand': {'1':'/','2':'/','3':'/'},'nor': {'1':'/','2':'/','3':'/'},'xnor': {'1':'/','2':'/','3':'/'},'bsu': {'1':'/','2':'/','3':'/'},'bsd': {'1':'/','2':'/','3':'/'},'bsur': {'1':'/','2':'/','3':'/'},
    'bsdr': {'1':'/','2':'/','3':'/'},'addca': {'1':'/','2':'/','3':'/'},'jmp': {'1':'/','2':'/','3':'/'},'branch': {'1':'/','2':'/','3':'/'},'jmpr': {'1':'/','2':'/','3':'/'},'branchr': {'1':'/','2':'/','3':'/'},'ldi': {'1':'/','2':'/','3':'/'},'mov': {'1':'/','2':'/','3':'/'},
    'rldi': {'1':'/','2':'/','3':'/'},'str': {'1':'/','2':'/','3':'/'},'ldr': {'1':'/','2':'/','3':'/'},'pin': {'1':'/','2':'/','3':'/'},'pout': {'1':'/','2':'/','3':'/'},'pinr': {'1':'/','2':'/','3':'/'},'poutr': {'1':'/','2':'/','3':'/'},'incr': {'1':'/','2':'/','3':'/'},
    'decr': {'1':'/','2':'/','3':'/'},'mult': {'1':'/','2':'/','3':'/'},'div': {'1':'/','2':'/','3':'/'},'mod': {'1':'/','2':'/','3':'/'},'sqr': {'1':'/','2':'/','3':'/'},'sqrt': {'1':'/','2':'/','3':'/'},'cmpr': {'1':'/','2':'/','3':'/'},'lflgre': {'1':'/','2':'/','3':'/'},
    'lflgra': {'1':'/','2':'/','3':'/'},'lpre': {'1':'/','2':'/','3':'/'},'rpre': {'1':'/','2':'/','3':'/'},'lpra': {'1':'/','2':'/','3':'/'},'rpra': {'1':'/','2':'/','3':'/'},'psh': {'1':'/','2':'/','3':'/'},'pop': {'1':'/','2':'/','3':'/'},'call': {'1':'/','2':'/','3':'/'},
    'rtrn': {'1':'/','2':'/','3':'/'},'rnd': {'1':'/','2':'/','3':'/'},'swp': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},
    '': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},'': {'1':'/','2':'/','3':'/'},'stl': {'1':'/','2':'/','3':'/'},'hlt': {'1':'/','2':'/','3':'/'}
}

# Prefix to description mapping
prefix_description = {
    '$': 'Register Address',
    '@': 'RAM Address',
    '&':'I/O Port Address',
    '/':'No Operand'
}

# Main
max_lines = 0
input_a = 0
stop = 0
input_lines = []  # Initialize an empty list to hold the input lines
 
# Talks to the user
def talk():
    print()
    print("| This is the Assembler for the Juggernaut CPU, made entirely in Minecraft.")
    print("| Juggernaut has been built by: Jobe, WildScaryFox, JediZach, Saturnxcode, Tarmalot and Death_Slice")
    print()
    t.sleep(.5)
    print("How many Lines of Code do you need (the maximum is 65536 lines):")

# Take input from user and convert str to int
def LineNumber():
    global input_a
    try: 
        input_a = int(input())
        return
    except ValueError:
        print()
        print("That is not a Number")
        print("Please try again")
        LineNumber()

talk()
LineNumber()

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

def is_valid_prefix(opcode, operand_prefix, operand_position): # Check if the prefix of the Operands is valid
    if opcode in op_code_list: # Check if the Opcode itself is valid
        allowed_prefix = operand_list[opcode].get(operand_position)
        if allowed_prefix == operand_prefix:
            return True
    return False

# Helper function to convert operand to binary
def operand_to_binary(operand):
    value =int(operand[1:])
    try:
        if 0 <= value <255:
            if operand.startswith('$'):
                # Assuming register addresses are in the form $0, $1, ..., $15 and need to be 4-bit binary -> first 4 bits of reg will always be 0000XXXX
                return format(int(operand[1:]), '08b')
            elif operand.startswith('@'):
                # Assuming RAM needs to be treated as immediate values
                return format(int(operand[1:]), '08b')  
            elif operand.startswith('&'):
                # Assuming IO needs to be treated as immediate values
                return format(int(operand[1:]), '08b')
            elif operand.startswith("/"):
                # If there is no Operand needed in Line
                return "00000000"
            elif operand.isdigit():
                # immediate
                return format(int(operand), '08b')
            else: 
                print(f"Unknown Operand format in {operand}")
        elif value > 255:
            print(f"The Operand {value} is bigger than 255.")
        elif value < 0:
            print(f"The Operand {value} is smaller than 0.")
    except ValueError as e:
        print(f"Error assembling line {index}: {e}")

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
                try:
                    binary_opcode = format(int(op_code_list[opcode]), '08b')
                    binary_operands = []
                    for i,operands in enumerate(operands):
                        operand_prefix = operand[0]
                        operand_position = f'pos_{(0+i)}' # Generates reg_a, reg_b, reg_c
                        if not is_valid_prefix(opcode, operand_prefix, operand_position):
                            print(f"Invalid prefix '{operand_prefix}'for {operand_position} of {opcode} instruction in line {index}.")
                        binary_operands.append(operand_to_binary(operand))
                        # Combine the binary parts
                        final_binary_instruction = binary_opcode + ''.join(binary_operands)
                        # Format the final binary instruction to be 4 8-bit strings
                        formatted_instruction = ' '.join(final_binary_instruction[i:i+4] for i in range(0, len(final_binary_instruction), 4))
                        print(formatted_instruction)
                except ValueError as e:
                    print(f"Error assembling line {index}: {e}")
            else:
                print(f"Unknown opcode: '{opcode}'")
                return()
    print("You can now copy this into the Schematic Generator")

if stop == 0:
    print()
    print("The ISA:")
    print()
    print("\n".join(op_code_list.keys())) 
    print()
    print("Please enter up to", input_a, "lines of input (Press Enter twice to finish early):")
    
    for i in range(1, input_a + 1):   # Read up to 65536 lines of input from the Terminal
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
