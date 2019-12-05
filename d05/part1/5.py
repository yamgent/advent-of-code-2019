def main():
    content = open('5.in').read()
    c = [int(x) for x in content.split(',')]
    ptr = 0
    while True:
        opcode = c[ptr]
        if opcode == 99:
            break
        elif opcode == 3:
            # input
            c[c[ptr+1]] = int(input())
            ptr += 2
        elif opcode == 4:
            # output
            print(str(c[c[ptr+1]]))
            ptr += 2
        elif opcode == 104:
            print(str(c[ptr+1]))
            ptr += 2
        elif opcode == 1:
            c[c[ptr+3]] = c[c[ptr+1]] + c[c[ptr+2]]
            ptr += 4
        elif opcode == 101:
            c[c[ptr+3]] = c[ptr+1] + c[c[ptr+2]]
            ptr += 4
        elif opcode == 1001:
            c[c[ptr+3]] = c[c[ptr+1]] + c[ptr+2]
            ptr += 4
        elif opcode == 1101:
            c[c[ptr+3]] = c[ptr+1] + c[ptr+2]
            ptr += 4
        elif opcode == 2:
            c[c[ptr+3]] = c[c[ptr+1]] * c[c[ptr+2]]
            ptr += 4
        elif opcode == 102:
            c[c[ptr+3]] = c[ptr+1] * c[c[ptr+2]]
            ptr += 4
        elif opcode == 1002:
            c[c[ptr+3]] = c[c[ptr+1]] * c[ptr+2]
            ptr += 4
        elif opcode == 1102:
            c[c[ptr+3]] = c[ptr+1] * c[ptr+2]
            ptr += 4
        else:
            print('Invalid opcode {}'.format(opcode))
            return


if __name__ == '__main__':
    main()
