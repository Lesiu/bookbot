def get_num_word(text):
    book_word_list = text.split()
    return len(book_word_list)


def count_letters(text):
    characters = {}
    for character in text:
        character = character.lower()
        if character not in characters.keys():
            characters[character] = 1
        else:
            characters[character] += 1
    return characters


def split_dict(dictionary):
    letter_list = []
    for key, value in dictionary.items():
        letter_list.append({"char": key, "num": value})
    return letter_list


def sort_on(items):
    return items["num"]


def raport(
    path,
    number_of_words,
    sorted_list,
):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for element in sorted_list:
        if element["char"].isalpha():
            print(element["char"] + ":", element["num"])
