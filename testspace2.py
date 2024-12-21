from ExtraFunctions import get_key

def move_input():
    print("-WASD to move-")
    while True:
        key = get_key()
        print(f"You pressed: {key}")
        if key == 'q':  # Exit condition
            print("Exiting...")
            break
