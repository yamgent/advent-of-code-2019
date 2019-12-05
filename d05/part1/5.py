c = []

def get(mode, pos):
    if mode == 0:
        return c[c[pos]]
    return c[pos]


def main():
    content = open('5.in').read()
    global c
    c = [int(x) for x in content.split(',')]

    ptr = 0
    while True:
        val = c[ptr]
        if val == 99:
            break
        elif val == 3:
            # input
            c[c[ptr+1]] = int(input())
            ptr += 2
        else:
            op = val % 10
            para = [int(val/100) % 10, int(val/1000) % 10, int(val/10000) % 10]

            if op == 4:
                print(str(get(para[0], ptr + 1)))
                ptr += 2
            elif op == 1:
                c[c[ptr + 3]] = get(para[0], ptr + 1) + get(para[1], ptr + 2)
                ptr += 4
            elif op == 2:
                c[c[ptr + 3]] = get(para[0], ptr + 1) * get(para[1], ptr + 2)
                ptr += 4
            else:
                print('Invalid opcode {}'.format(opcode))
                return


if __name__ == '__main__':
    main()
