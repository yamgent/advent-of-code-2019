import math
import sys

def main():
    total_fuel = 0

    for line in sys.stdin:
        mass = int(line)
        fuel = math.floor(mass / 3) - 2
        total_fuel += fuel
    
    print(str(total_fuel))


if __name__ == '__main__':
    main()
