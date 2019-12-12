import sys

def main():
    p = []
    v = []

    for line in sys.stdin:
        values = [int(x.strip()[2:]) for x in line[1:-2].split(',')]
        assert len(values) == 3
        p.append([values[0], values[1], values[2]])
        v.append([0, 0, 0])

    e = 0
    STEPS = 1000

    for t in range(STEPS):

        for i in range(len(p)):
            p1 = p[i]
            for j in range(len(p)):
                if i == j:
                   continue
                p2 = p[j]
                for x in range(3):
                    v[i][x] += 1 if p1[x] < p2[x] else (-1 if p1[x] > p2[x] else 0)

        for i in range(len(p)):
            for x in range(3):
                p[i][x] += v[i][x]

        # for debug
        if False:
            print('After {} steps:'.format(t + 1))
            for i in range(len(p)):
                print('pos={}, vel={}'.format(p[i], v[i]))
            print()

    e = 0

    for i in range(len(p)):
        pot = sum(map(lambda x: abs(x), p[i]))
        kin = sum(map(lambda x: abs(x), v[i]))
        tot = pot * kin
        e += tot

    print(e)


if __name__ == '__main__':
    main()
