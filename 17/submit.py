import sys




def part1(A, B, C, program):
    n = len(program)

    output = []

    def getCombo(opcode):
        if opcode < 4:
            return opcode
        elif opcode == 4:
            return A
        elif opcode == 5:
            return B
        elif opcode == 6:
            return C
        elif opcode == 7:
            return 0

    i = 0
    while i < n:
        instruction = program[i]
        operand = program[i+1]

        if instruction == 0:
            result = A // (2 ** getCombo(operand))
            A = result
            i += 2
        elif instruction == 1:
            result = B ^ operand
            B = result
            i += 2
        elif instruction == 2:
            result = getCombo(operand) % 8
            B = result
            i += 2
        elif instruction == 3:
            if A > 0:
                i = operand
            else:
                i += 2
        elif instruction == 4:
            result = B ^ C
            B = result
            i += 2
        elif instruction == 5:
            result = getCombo(operand) % 8
            output.append(result)
            i += 2
        elif instruction == 6:
            result = A // (2 ** getCombo(operand))
            B = result
            i += 2
        elif instruction == 7:
            result = A // (2 ** getCombo(operand))
            C = result
            i += 2
        print(f'Instruction: {instruction}, Operand: {operand} => A: {A}, B: {B}, C: {C}')
    return ",".join([str(s) for s in output])




def simulate(A, B, C, program, n):
    def getCombo(opcode):
        if opcode < 4:
            return opcode
        elif opcode == 4:
            return A
        elif opcode == 5:
            return B
        elif opcode == 6:
            return C
        elif opcode == 7:
            return 0

    i = 0
    while i < n:
        instruction = program[i]
        operand = program[i+1]

        if instruction == 0:
            result = A // (2 ** getCombo(operand))
            A = result
            i += 2
        elif instruction == 1:
            result = B ^ operand
            B = result
            i += 2
        elif instruction == 2:
            result = getCombo(operand) % 8
            B = result
            i += 2
        elif instruction == 3:
            if A > 0:
                i = operand
            else:
                i += 2
        elif instruction == 4:
            result = B ^ C
            B = result
            i += 2
        elif instruction == 5:
            result = getCombo(operand) % 8
            return result
            # i += 2
        elif instruction == 6:
            result = A // (2 ** getCombo(operand))
            B = result
            i += 2
        elif instruction == 7:
            result = A // (2 ** getCombo(operand))
            C = result
            i += 2

def part2(A, B, C, program):
    # the 8 here is purely based on input.txt because of the 0 3 instruction
    noRepeatProgram = program[:-2]
    n = len(noRepeatProgram)
    lastA = None
    for i in range(1, 8):
        x = simulate(i, 0, 0, noRepeatProgram, n)
        if x == 0:
            lastA = i
            break
    j = n
    while j > -1:
        print(j, lastA)
        for i in range(lastA * 8, (lastA * 8) + 8):
            x = simulate(i, 0, 0, noRepeatProgram, n)
            if x == program[j]:
                lastA = i
                break
        j -= 1

    return lastA


if __name__ == "__main__":
    data = []
    with open(sys.argv[1], 'r') as f:
        A = int(f.readline().split(': ')[1].strip())
        B = int(f.readline().split(': ')[1].strip())
        C = int(f.readline().split(': ')[1].strip())
        f.readline()
        program = [int(p) for p in f.readline().split(': ')[1].strip().split(',')]

    if sys.argv[2] == "part1":
        print(f'Part 1 Answer = {part1(A, B, C, program)}')
    if sys.argv[2] == "part2":
        print(f'Part 2 Answer = {part2(A, B, C, program)}')