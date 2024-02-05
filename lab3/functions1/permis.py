def all_permutations(string):
    # base case
    if len(string) == 1:
        print(string)
    # recursion case
    else:
        for i in range(len(string)):
            first = string[i]
            rest = string[:i] + string[i + 1:]
            all_permutations(rest)
            print(first + rest)