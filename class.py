import random

def boxes():
    array = []
    while True:
        F = random.randint(0, 6)
        S = random.randint(0, 6)
        T = random.randint(0, 6)
        if F != S and F != T and S != T:
            array.extend([F, S, T])
            break
    return array

def get_coordinates():
    print("Enter three coordinates:")
    scan_array = [int(input()) for _ in range(3)]
    return scan_array

def check(array, scan_array):
    if array == scan_array:
        print("Congratulations! You found all coordinates.")
        exit(0)
    elif array[0] == scan_array[0] and array[1] == scan_array[1]:
        print("Two coordinates are correct.")
    elif array[0] == scan_array[0] and array[2] == scan_array[2]:
        print("Two coordinates are correct.")
    elif array[1] == scan_array[1] and array[2] == scan_array[2]:
        print("Two coordinates are correct.")
    elif array[2] == scan_array[2]:
        print("One coordinate is correct.")
    elif array[0] == scan_array[0]:
        print("One coordinate is correct.")
    elif array[1] == scan_array[1]:
        print("One coordinate is correct.")

def main():
    array = boxes()
    count_try = 0

    while count_try < 5:
        if count_try == 0:
            print("Initial coordinates:", array)
        coordinates = get_coordinates()
        check(array, coordinates)
        count_try += 1

        if count_try == 5:
            print("Maximum tries reached. Generating a new set of random coordinates.")
            array = boxes()
            count_try = 0

if __name__ == "__main__":
    main()