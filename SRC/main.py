from motors import forward, reverse, left, right, stop


while True:
    command = input("w/a/s/d/x: ")

    if command == "w":
        forward(100)

    elif command == "s":
        reverse(100)
    elif command == "a":
        left(100)
    elif command == "d":
        left(100)
    elif command == "x":
        stop()
    elif command == "q":
        break