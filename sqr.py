import math

def calc_dist(a1, b1, a2, b2):
    return math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

def get_square_area(a1, b1, a2, b2, a3, b3, a4, b4):
    side_length = min(
        calc_dist(a1, b1, a2, b2),
        calc_dist(a2, b2, a3, b3),
        calc_dist(a3, b3, a4, b4),
        calc_dist(a4, b4, a1, b1)
    )
    return int(side_length**2)

def main():
    t = int(input())
    for i in range(t):
        a1, b1 = map(int, input().split())
        a2, b2 = map(int, input().split())
        a3, b3 = map(int, input().split())
        a4, b4 = map(int, input().split())

        area = get_square_area(a1, b1, a2, b2, a3, b3, a4, b4)
        print(area)

if __name__ == "__main__":
    main()
