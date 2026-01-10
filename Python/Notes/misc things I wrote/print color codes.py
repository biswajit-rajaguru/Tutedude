for i in range(256):
    color_code = f"\033[38;5;{i}m"
    reset = f"\033[0m"
    print(f"{color_code} {i:<3} {reset}", end = " ")
    if (i+1) % 16 == 0:
        print()

