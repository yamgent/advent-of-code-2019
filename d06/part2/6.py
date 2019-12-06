from collections import deque
import sys

def bfs(p):
    q = deque() 
    q.append(('YOU', 0))

    visited = set()

    while len(q) > 0:
        k, l = q.pop()
        
        if k == 'SAN':
            return l - 2
        for c in p[k]:
            if c not in visited:
                q.append((c, l + 1))

        visited.add(k)

    return 0


def main():
    p = {}

    for l in sys.stdin:
        l = l[:-1] # remove newline
        if l == '':
            continue

        a, b = l.split(')')
        if a in p:
            p[a].append(b)
        else:
            p[a] = [b]
        
        if b in p:
            p[b].append(a)
        else:
            p[b] = [a]

    print(bfs(p))
    
if __name__ == '__main__':
    main()
