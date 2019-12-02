# if running 1202 program, question wants us to change some stuff first
# (only used for p1.in.txt test case)
running_1202 = True

def run_program(vals):
    op_ptr = 0

    while op_ptr < len(vals) and vals[op_ptr] != 99:
        if vals[op_ptr] == 1:
            vals[vals[op_ptr + 3]] = vals[vals[op_ptr + 1]] + vals[vals[op_ptr + 2]] 
            op_ptr += 4
        elif vals[op_ptr] == 2:
            vals[vals[op_ptr + 3]] = vals[vals[op_ptr + 1]] * vals[vals[op_ptr + 2]] 
            op_ptr += 4
        else:
            print('Error: Invalid input given.')
            return -1

    return vals[0]


def main():
    vals = [int(x) for x in input().split(',')]

    if running_1202:  
        vals[1] = 12
        vals[2] = 2

    print(run_program(vals))


if __name__ == '__main__':
    main()
