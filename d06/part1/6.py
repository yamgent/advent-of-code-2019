import sys

def dfs(p, k, l, visited):
    if k in visited:
        return 0

    visited.add(k)

    if k not in p or len(p[k]) == 0:
        return l
    
    result = l
    
    for c in p[k]:
        result += dfs(p, c, l + 1, visited)

    return result


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

    print(dfs(p, 'COM', 0, set()))
    
if __name__ == '__main__':
    main()
