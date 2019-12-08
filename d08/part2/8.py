def count(array, digit):
    return len(list(filter(lambda x : x == digit, array)))

def main():
    width = 25
    height = 6
    area = width * height

    values = [int(x) for x in list(input())]
    layers = []
    for i in range(0, int(len(values) / area)):
        layers.append(values[(i * area):((i + 1) * area)])
    
    decode = []
    for i in range(0, area):
        if i % width == 0:
            print()

        for layer in layers:
            if layer[i] != 2:
                if layer[i] == 0:
                    print(' ', end='')
                else:
                    print('#', end='')
                break
    print()
    # I can see YGRYZ

if __name__ == '__main__':
    main()
