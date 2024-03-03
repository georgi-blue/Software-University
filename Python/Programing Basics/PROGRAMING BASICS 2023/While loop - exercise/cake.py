cake_size = int(input()) * int(input())


while True:
    piece_or_stop = input()

    if piece_or_stop == "STOP":
        print(f"{cake_size} pieces are left.")
        break

    cake_pieces = int(piece_or_stop)
    cake_size -= cake_pieces

    if cake_size <= 0:
        print(f"No more cake left! You need {abs(cake_size)} pieces more.")
        break
