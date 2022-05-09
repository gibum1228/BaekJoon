if __name__ == "__main__":
    limit = int(input())
    speed = int(input())

    order = speed - limit
    if 1 <= order <= 20:
        print("You are speeding and your fine is $100.")
    elif 21 <= order <= 30:
        print("You are speeding and your fine is $270.")
    elif order >= 31:
        print("You are speeding and your fine is $500.")
    else:
        print("Congratulations, you are within the speed limit!")