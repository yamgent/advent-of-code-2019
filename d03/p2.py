# logic taken from https://www.reddit.com/r/adventofcode/comments/e5bz2w/2019_day_3_solutions/f9iz68s/
# as seen in `input_size.py`, the input is not huge enough to prevent brute force

a = input().split(',')
b = input().split(',')

x_delta = {'U': 0, 'D': 0, 'L': -1, 'R': 1 }
y_delta = {'U': 1, 'D': -1, 'L': 0, 'R': 0 }

a_pts = {}
b_pts = {}

for wire, pts in [(a, a_pts), (b, b_pts)]:
    x, y = 0, 0
    steps = 0

    for w in wire:
        direction = w[0]
        count = int(w[1:])
        while count > 0:
            x += x_delta[direction]
            y += y_delta[direction]
            steps += 1

            if (x, y) != (0, 0) and (x, y) not in pts:
                pts[(x, y)] = steps

            count -= 1

intersect = set(a_pts) & set(b_pts)
answer = 999999999

for pt in intersect:
    answer = min(answer, a_pts[pt] + b_pts[pt])

print(answer)
