def bubble_sort(input_array):
    # assumes input is list
    for i in range(1, len(input_array)):
        for j in range(len(input_array)-i):
            if input_array[j+1] < input_array[j]:
                temp = input_array[j]
                input_array[j] = input_array[j+1]
                input_array[j+1] = temp
    return input_array


if __name__ == "__main__":
    INPUT_ARRAY = [17, 2, 9, 0, 0, -5, 17, 8, 1]
    print(bubble_sort(INPUT_ARRAY))
