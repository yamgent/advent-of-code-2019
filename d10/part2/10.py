import heapq
import math
import sys

def angle(pt1, pt2):
    val = math.atan2(pt2[1] - pt1[1], pt2[0] - pt1[0])
    val += math.pi / 2
    if val < 0:
        val += 2 * math.pi
    return val


def dist(pt1, pt2):
    return (pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2

def main():
    A = set()
    y = 0
    for line in sys.stdin:
        for x in range(0, len(line)):
            if line[x] == '#':
                A.add((x, y))
        y += 1

    # part 1
    answer_amount = 0
    answer_position = (-1, -1)

    for a in A:
        angles = set()

        for b in A:
            if b == a:
                continue
            angles.add(angle(a, b))

        if answer_amount < len(angles):
            answer_amount = len(angles)
            answer_position = a

    print(answer_amount)
    print(answer_position)

    # part 2
    arrangement = {}
    for a in A:
        if a == answer_position:
            continue

        heapq.heappush(arrangement.setdefault(angle(answer_position, a), []), (dist(answer_position, a), a))

    # print(arrangement)
    total_destroyed = 0
    while len(arrangement) > 0:
        angles = sorted(list(arrangement.keys()))

        for a in angles:
            pos = heapq.heappop(arrangement[a])
            
            if len(arrangement[a]) == 0:
                del arrangement[a]
                
            total_destroyed += 1

            # if total_destroyed < 10:    # testing
            #     print(str(a))
            #     print('{}: Destroy {}'.format(total_destroyed, pos))
            
            if total_destroyed == 200:
                d, c = pos
                print(str(c[0] * 100 + c[1]))
                break
                
        if total_destroyed >= 200:
            break

if __name__ == '__main__':
    main()
