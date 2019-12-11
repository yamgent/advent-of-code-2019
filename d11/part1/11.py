from itertools import permutations

class Computer:
    def __init__(self, program):
        self.program = program.copy()
        self.program.extend([0] * 1000)
        self.ptr = 0
        self.halt = False
        self.last = 0
        self.relative = 0

    def get(self, mode, pos):
        if mode == 2:
            return self.program[self.relative + self.program[pos]]
        if mode == 0:
            return self.program[self.program[pos]]
        return self.program[pos]

    def set(self, mode, pos, value):
        if mode == 2:
            self.program[self.relative + self.program[pos]] = value
            return
        # set cannot be in mode 1, so this is mode 0
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
            else:
                op = val % 10
                para = [int(val/100) % 10, int(val/1000) % 10, int(val/10000) % 10]

                if op == 3:
                    # input
                    assert current_input_index < len(input_values)
                    self.set(para[0], self.ptr + 1, input_values[current_input_index])
                    current_input_index += 1
                    self.ptr += 2
                elif op == 4:
                    self.ptr += 2
                    self.last = self.get(para[0], self.ptr - 1)
                    return False, self.last 
                elif op == 1:
                    self.set(para[2], self.ptr + 3, self.get(para[0], self.ptr + 1) + self.get(para[1], self.ptr + 2))
                    self.ptr += 4
                elif op == 2:
                    self.set(para[2], self.ptr + 3, self.get(para[0], self.ptr + 1) * self.get(para[1], self.ptr + 2))
                    self.ptr += 4
                elif op == 5:
                    self.ptr = self.get(para[1], self.ptr + 2) if self.get(para[0], self.ptr + 1) != 0 else self.ptr + 3
                elif op == 6:
                    self.ptr = self.get(para[1], self.ptr + 2) if self.get(para[0], self.ptr + 1) == 0 else self.ptr + 3
                elif op == 7:
                    self.set(para[2], self.ptr + 3, 1 if self.get(para[0], self.ptr + 1) < self.get(para[1], self.ptr + 2) else 0)
                    self.ptr += 4
                elif op == 8:
                    self.set(para[2], self.ptr + 3, 1 if self.get(para[0], self.ptr + 1) == self.get(para[1], self.ptr + 2) else 0)
                    self.ptr += 4
                elif op == 9:
                    self.relative += self.get(para[0], self.ptr + 1)
                    self.ptr += 2
                else:
                    print('Invalid opcode {}'.format(op))
                    self.halt = True
                    return True, self.last
        

def main():
    # c = [int(x) for x in open('9.in').read().strip().split(',')]
    c = [int(x) for x in input().split(',')]
    a = Computer(c)
    
    visited = set()
    white = set()

    pos = (0, 0)
    direction = 0
    forward = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while True:
        halted, result = a.run([1 if pos in white else 0])
        
        if halted:
            break

        visited.add(pos)

        if result == 0 and pos in white:
            white.remove(pos)
        if result == 1 and pos not in white:
            white.add(pos)

        halted, result = a.run([])

        if result == 0:
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4

        pos = (pos[0] + forward[direction][0], pos[1] + forward[direction][1])

        if halted:
            break
            
    print(len(visited))

if __name__ == '__main__':
    main()
