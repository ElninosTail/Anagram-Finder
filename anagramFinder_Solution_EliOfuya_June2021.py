def anagramFinder(file):

    with open(f"{file}.txt", "r") as f:
        reader = f.read()
        basket = list(reader.split())  # converts the text of words into a comma - separated list of words
    print(basket)

    flip = ["".join(sorted(word)) for word in basket]  # flip each word for letters to follow alphabetical order
    # print(flip, "\n")
    print("\n", "-" * 125)

    dict = {}  # empty hash table as placeholder

    for indexPosition, anagrams in enumerate(flip):  # This would provide indexes of position on list
        dict.setdefault(anagrams, []).append(indexPosition)

    print(f"This gives the index of alphabetically arranged letters in single word, and their respective anagram index as: \n{dict} \n")

    print("-" * 125, "\n")

    # print(dict)
    print("This is the order in which anagrams were found from file: \n")
    for index in dict.values():
        if len(index) != 1:
            print([basket[i] for i in index])
        elif len(index) == 1:
            print(f"{[basket[i] for i in index]} ==> no anagrams found ")


file = "anagram"
anagramFinder(file)
