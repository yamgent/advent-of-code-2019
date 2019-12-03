class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_manhattan(self):
        return abs(self.x) + abs(self.y)


class HLine:
    def __init__(self, p1, p2):
        if p1.y != p2.y:
            print('Error: Should not use HLine on a non-horizontal line!')
            exit(1)
        self.y = p1.y
        self.x1 = min(p1.x, p2.x)
        self.x2 = max(p1.x, p2.x)
        self.start1 = self.x1 == p1.x

    def get_start_pt(self):
        if self.start1:
            return Point(self.x1, self.y)
        return Point(self.x2, self.y)

    def get_steps(self):
        return self.x2 - self.x1

    def __repr__(self):
        return 'HLine: ({1}, {0}) to ({2}, {0})'.format(self.y, self.x1, self.x2)

    def intersects(self, other):
        if type(other) is HLine:
            if self.y != other.y:
                return None
            if self.x2 < other.x1:
                return None
            if self.x1 > other.x2:
                return None
            
            # intersected
            all_x = [self.x1, self.x2, other.x1, other.x2]
            all_x.sort()
            in1 = all_x[1]
            in2 = all_x[2]
            if in2 < 0:
                return Point(in2, self.y)
            if in1 > 0:
                return Point(in1, self.y)
            return Point(0, self.y)

        elif type(other) is VLine:
            if self.y > other.y2:
                return None
            if self.y < other.y1:
                return None
            if other.x > self.x2:
                return None
            if other.x < self.x1:
                return None
            return Point(other.x, self.y)
            
        else:
            print('Error: Don\'t call intersects() on non-line objects!')
            exit(1)


class VLine:
    def __init__(self, p1, p2):
        if p1.x != p2.x:
            print('Error: Should not use VLine on a non-vertical line!')
            exit(1)
        self.x = p1.x
        self.y1 = min(p1.y, p2.y)
        self.y2 = max(p1.y, p2.y)
        self.start1 = self.y1 == p1.y

    def get_start_pt(self):
        if self.start1:
            return Point(self.x, self.y1)
        return Point(self.x, self.y2)

    def get_steps(self):
        return self.y2 - self.y1

    def __repr__(self):
        return 'VLine: ({0}, {1}) to ({0}, {2})'.format(self.x, self.y1, self.y2)

    def intersects(self, other):
        if type(other) is HLine:
            # no need to duplicate the same logic
            return other.intersects(self)

        elif type(other) is VLine:
            if self.x != other.x:
                return None
            if self.y2 < other.y1:
                return None
            if self.y1 > other.y2:
                return None
            
            # intersected
            all_y = [self.y1, self.y2, other.y1, other.y2]
            all_y.sort()
            in1 = all_y[1]
            in2 = all_y[2]
            if in2 < 0:
                return Point(self.x, in2)
            if in1 > 0:
                return Point(self.x, in1)
            return Point(self.x, 0)

        else:
            print('Error: Don\'t call intersects() on non-line objects!')
            exit(1)


def get_end_point(start, inst):
    direction = inst[0]
    count = int(inst[1:])

    if direction == 'R':
        return Point(start.x + count, start.y)
    elif direction == 'L':
        return Point(start.x - count, start.y)
    elif direction == 'U':
        return Point(start.x, start.y + count)
    elif direction == 'D':
        return Point(start.x, start.y - count)
    else:
        print('Input error: direction ' + direction)
        exit(1)


def get_line(start, end):
    if start.x == end.x:
        return VLine(start, end)
    elif start.y == end.y:
        return HLine(start, end)
    else:
        print('We cannot handle strange lines ' + start + ' ' + end)
        exit(1)


def get_dist(pt1, pt2):
    if pt1.x == pt2.x:
        return abs(pt2.y - pt1.y)
    elif pt1.y == pt2.y:
        return abs(pt2.x - pt1.x)
    else:
        print('We cannot handle strange lines ' + start + ' ' + end)
        exit(1)


def main():
    wire1 = [x for x in input().split(',')]
    wire2 = [x for x in input().split(',')]

    pt_start = Point(0, 0)
    pt_end = Point(0, 0)

    wire1_lines = []
    for w in wire1:
        pt_end = get_end_point(pt_start, w)
        wire1_lines.append(get_line(pt_start, pt_end))
        pt_start = pt_end

    answer = 999999999
    pt_start = Point(0, 0)
    pt_end = Point(0, 0)
    wire2_steps = 0

    for w in wire2:
        pt_end = get_end_point(pt_start, w)
        current_line = get_line(pt_start, pt_end)

        wire1_steps = 0

        for l in wire1_lines:
            intersect = current_line.intersects(l)
            pt1_start = l.get_start_pt()

            # there could be cases where both HLine / both VLine intersect
            # with each other, and (0, 0) happens to be part of the
            # intersection point. That case is ambiguous (how to handle
            # this case is not clear), but it seems that the answer didn't
            # require us to handle this case anyway
            if intersect is not None and intersect.get_manhattan() != 0:
                answer = min(answer, wire1_steps + wire2_steps + get_dist(pt1_start, intersect) + get_dist(pt_start, intersect))
                break
            wire1_steps += l.get_steps()

        wire2_steps += current_line.get_steps()
        pt_start = pt_end

    print(answer)


if __name__ == '__main__':
    main()
