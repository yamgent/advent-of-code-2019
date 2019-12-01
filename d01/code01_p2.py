import math
import sys

def main():
    total_fuel = 0

    for line in sys.stdin:
        mass = int(line)

        while True:
            fuel = math.floor(mass / 3) - 2
            if fuel <= 0:
                break

            total_fuel += fuel
            mass = fuel
    
    print(str(total_fuel))


if __name__ == '__main__':
    main()
