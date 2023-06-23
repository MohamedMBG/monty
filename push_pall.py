stack = []

def push(line_number, arg):
    try:
        stack.append(int(arg))
    except ValueError:
        print(f"L{line_number}: usage: push integer")
        exit(1)

def pall():
    for item in reversed(stack):
        print(item)

def process_instructions(instructions):
    for line_number, instruction in enumerate(instructions, start=1):
        opcode = instruction[0]
        if opcode == "push":
            push(line_number, instruction[1])
        elif opcode == "pall":
            pall()

# Sample bytecode instructions
instructions = [
    ["push", "1"],
    ["push", "2"],
    ["push", "3"],
    ["pall"]
]

process_instructions(instructions)
