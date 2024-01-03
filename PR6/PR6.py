def split_list(input_list, split_index):
    if split_index >= len(input_list):
        print("Error: The index to split exceeds the size of the list.")
        return None, None
    list1 = input_list[:split_index]
    list2 = input_list[split_index:]
    return list1, list2
def main():
    input_list = input("Enter the list items with a space:").split()
    if not input_list:
        print("The list is empty. Enter at least one item.")
        return
    split_index = int(input("Enter an index to split the list:"))
    list1, list2 = split_list(input_list, split_index)
    if list1 is not None and list2 is not None:
        print("First list:", list1)
        print("Second list:", list2)
if __name__ == "__main__":
    main()