import sys

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) / gcd(a, b)


def main():
    p = [[], [], []]
    v = [[], [], []]

    ip = []
    iv = []

    cycle = [-1] * 3

    for line in sys.stdin:
        values = [int(x.strip()[2:]) for x in line[1:-2].split(',')]
        assert len(values) == 3
        for x in range(3):
            p[x].append(values[x])
            v[x].append(0)

    for x in range(3):
        ip.append(p[x].copy())
        iv.append(v[x].copy())

    t = 0

    while True:
        if all(map(lambda x: x != -1, cycle)):
            break

        t += 1
        for x in range(3):
            if cycle[x] != -1:
                continue

            for i in range(len(p[x])):
                for j in range(len(p[x])):
                    if i == j:
                        continue
                    v[x][i] += 1 if p[x][i] < p[x][j] else (-1 if p[x][i] > p[x][j] else 0)

            for i in range(len(p[x])):
                p[x][i] += v[x][i]
                    
            if p[x] == ip[x] and v[x] == iv[x]:
                cycle[x] = t

    #print(cycle)
    print('{}'.format(int(lcm(cycle[0], lcm(cycle[1], cycle[2])))))

if __name__ == '__main__':
    main()
