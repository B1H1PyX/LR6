def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
def main():
    input_list = input("Enter the elements of the list separated by space: ").split()
    input_list = [int(item) for item in input_list]
    if not input_list:
        print("Error: The list is empty. Enter at least one element.")
        return
    bubble_sort(input_list)
    print("Sorted list (using bubble sort):", input_list)
if __name__ == "__main__":
    main()