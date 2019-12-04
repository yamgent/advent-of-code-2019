def meet(number):
    digits = list(str(number))

    seen_repeat = False

    for i in range(0, len(digits) - 1):
        if digits[i] > digits[i+1]:
            return False
        if digits[i] == digits[i+1]:
            seen_repeat = True

    return seen_repeat


def main():
    a, b = [int(x) for x in input().split('-')]
    result = 0

    for i in range(a, b + 1):
        if meet(i):
            result += 1

    print(result)


if __name__ == '__main__':
    main()
