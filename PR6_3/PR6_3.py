def operate_on_set(original_set):
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'y'}
    result_set = original_set.union(vowels_set)
    return result_set
def main():
    given_set = {'c', 'd'}
    result_set = operate_on_set(given_set)
    print("Resulting set:", result_set)
if __name__ == "__main__":
    main()