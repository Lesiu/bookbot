import sys
from stats import *


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    # path_to_file = "books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path_to_file = sys.argv[1]
        text = get_book_text(path_to_file)
        num_words = get_num_word(text)
        letter_dictionary = count_letters(text)
        sorted_list = split_dict(letter_dictionary)
        sorted_list.sort(key=sort_on, reverse=True)
        raport(path_to_file, num_words, sorted_list)


main()
