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
    original_input = [int(x) for x in input().split(',')]
    desired_output = 19690720
        
    for noun in range(0, 100):
        for verb in range(0, 100):
            vals = original_input.copy()
            vals[1] = noun
            vals[2] = verb
            if run_program(vals) == desired_output:
                print(str(100 * noun + verb))
                return

    print('No answer.')


if __name__ == '__main__':
    main()
