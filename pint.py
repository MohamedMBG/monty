stack = []

def push(line_number, arg):
    try:
        stack.append(int(arg))
    except ValueError:
        print(f"L{line_number}: usage: push integer")
        exit(1)

def pint(line_number):
    if len(stack) > 0:
        print(stack[-1])
    else:
        print(f"L{line_number}: can't pint, stack empty")
        exit(1)

def process_instructions(instructions):
    for line_number, instruction in enumerate(instructions, start=1):
        opcode = instruction[0]
        if opcode == "push":
            push(line_number, instruction[1])
        elif opcode == "pint":
            pint(line_number)

# Sample bytecode instructions
instructions = [
    ["push", "1"],
    ["pint"],
    ["push", "2"],
    ["pint"],
    ["push", "3"],
    ["pint"]
]

process_instructions(instructions)
