from itertools import permutations

class Computer:
    def __init__(self, program):
        self.program = program.copy()
        self.ptr = 0
        self.halt = False
        self.last = 0

    def get(self, mode, pos):
        if mode == 0:
            return self.program[self.program[pos]]
        return self.program[pos]

    def set(self, pos, value):
        # set is always in position mode
        self.program[self.program[pos]] = value

    def run(self, input_values):
        if self.halt:
            return True, self.last

        current_input_index = 0

        while True:
            val = self.program[self.ptr]
            if val == 99:
                self.halt = True 
                return True, self.last
            elif val == 3:
                # input
                assert current_input_index < len(input_values)
                self.set(self.ptr + 1, input_values[current_input_index])
                current_input_index += 1
                self.ptr += 2
            else:
                op = val % 10
                para = [int(val/100) % 10, int(val/1000) % 10, int(val/10000) % 10]

                if op == 4:
                    self.ptr += 2
                    self.last = self.get(para[0], self.ptr - 1)
                    return False, self.last 
                elif op == 1:
                    self.set(self.ptr + 3, self.get(para[0], self.ptr + 1) + self.get(para[1], self.ptr + 2))
                    self.ptr += 4
                elif op == 2:
                    self.set(self.ptr + 3, self.get(para[0], self.ptr + 1) * self.get(para[1], self.ptr + 2))
                    self.ptr += 4
                elif op == 5:
                    self.ptr = self.get(para[1], self.ptr + 2) if self.get(para[0], self.ptr + 1) != 0 else self.ptr + 3
                elif op == 6:
                    self.ptr = self.get(para[1], self.ptr + 2) if self.get(para[0], self.ptr + 1) == 0 else self.ptr + 3
                elif op == 7:
                    self.set(self.ptr + 3, 1 if self.get(para[0], self.ptr + 1) < self.get(para[1], self.ptr + 2) else 0)
                    self.ptr += 4
                elif op == 8:
                    self.set(self.ptr + 3, 1 if self.get(para[0], self.ptr + 1) == self.get(para[1], self.ptr + 2) else 0)
                    self.ptr += 4
                else:
                    print('Invalid opcode {}'.format(op))
                    self.halt = True
                    return True, self.last
        

def run_amp(program, phases):
    A = Computer(program)
    B = Computer(program)
    C = Computer(program)
    D = Computer(program)
    E = Computer(program)
    
    h_a, a = A.run([phases[0], 0])
    h_b, b = B.run([phases[1], a])
    h_c, c = C.run([phases[2], b])
    h_d, d = D.run([phases[3], c])
    h_e, e = E.run([phases[4], d]) 

    while not h_e:
        h_a, a = A.run([e])
        h_b, b = B.run([a])
        h_c, c = C.run([b])
        h_d, d = D.run([c])
        h_e, e = E.run([d])

        if h_e:
            return e 

    return e 


def main():
    c = [int(x) for x in input().split(',')]
    result = 0

    for p in permutations(range(5, 10)):
        result = max(result, run_amp(c, p))

    print(result)


if __name__ == '__main__':
    main()
