if __name__ == "__main__":
    one = int(input())
    two = int(input())
    three = int(input())

    if one == 60 and two == 60 and three == 60:
        print("Equilateral")
    elif sum([one, two, three]) == 180 and (one == two or one == three or two == three):
        print("Isosceles")
    elif sum([one, two, three]) == 180 and (one != two or one != three or two != three):
        print("Scalene")
    elif sum([one, two, three]) != 180:
        print("Error")