from itertools import permutations

class Computer:
    def __init__(self, program):
        self.program = program.copy()

    def get(self, mode, pos):
        if mode == 0:
            return self.program[self.program[pos]]
        return self.program[pos]

    def set(self, pos, value):
        # set is always in position mode
        self.program[self.program[pos]] = value

    def run(self, input_values):
        current_input_index = 0
        result = []

        ptr = 0
        while True:
            val = self.program[ptr]
            if val == 99:
                return result
            elif val == 3:
                # input
                assert current_input_index < len(input_values)
                self.set(ptr + 1, input_values[current_input_index])
                current_input_index += 1
                ptr += 2
            else:
                op = val % 10
                para = [int(val/100) % 10, int(val/1000) % 10, int(val/10000) % 10]

                if op == 4:
                    result.append(self.get(para[0], ptr + 1))
                    ptr += 2
                elif op == 1:
                    self.set(ptr + 3, self.get(para[0], ptr + 1) + self.get(para[1], ptr + 2))
                    ptr += 4
                elif op == 2:
                    self.set(ptr + 3, self.get(para[0], ptr + 1) * self.get(para[1], ptr + 2))
                    ptr += 4
                elif op == 5:
                    ptr = self.get(para[1], ptr + 2) if self.get(para[0], ptr + 1) != 0 else ptr + 3
                elif op == 6:
                    ptr = self.get(para[1], ptr + 2) if self.get(para[0], ptr + 1) == 0 else ptr + 3
                elif op == 7:
                    self.set(ptr + 3, 1 if self.get(para[0], ptr + 1) < self.get(para[1], ptr + 2) else 0)
                    ptr += 4
                elif op == 8:
                    self.set(ptr + 3, 1 if self.get(para[0], ptr + 1) == self.get(para[1], ptr + 2) else 0)
                    ptr += 4
                else:
                    print('Invalid opcode {}'.format(op))
                    return
        

def run_amp(program, phases):
    A = Computer(program)
    B = Computer(program)
    C = Computer(program)
    D = Computer(program)
    E = Computer(program)

    a = A.run([phases[0], 0])
    b = B.run([phases[1], a[0]])
    c = C.run([phases[2], b[0]])
    d = D.run([phases[3], c[0]])
    e = E.run([phases[4], d[0]]) 

    return e[0]


def main():
    c = [int(x) for x in input().split(',')]
    result = 0

    for p in permutations(range(0, 5)):
        result = max(result, run_amp(c, p))

    print(result)


if __name__ == '__main__':
    main()
