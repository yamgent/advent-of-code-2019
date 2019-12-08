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
    
    fewest = count(layers[0], 0)
    answer = count(layers[0], 1) * count(layers[0], 2)

    for layer in layers:
        zeroes = count(layer, 0)
        if zeroes < fewest:
            fewest = zeroes
            answer = count(layer, 1) * count(layer, 2)

    print(answer)


if __name__ == '__main__':
    main()
