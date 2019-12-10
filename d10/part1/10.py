import math
import sys

def angle(pt1, pt2):
    return math.atan2(pt2[1] - pt1[1], pt2[0] - pt1[0])

def main():
    A = set()
    y = 0
    for line in sys.stdin:
        for x in range(0, len(line)):
            if line[x] == '#':
                A.add((x, y))
        y += 1

    answer = 0
    for a in A:
        angles = set()
        for b in A:
            if b == a:
                continue
            angles.add(angle(a, b))
        answer = max(answer, len(angles))

    print(answer)
    

if __name__ == '__main__':
    main()
