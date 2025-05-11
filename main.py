from sys import argv, exit
from stats import (
    get_number_words,
    get_characters_occurence,
    sort_characters
)


def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        try:
            book_path = argv[1]
            frankenstein_txt = get_book_text(book_path)
            words_count = get_number_words(frankenstein_txt)
            characters = get_characters_occurence(frankenstein_txt)
            sorted_characters = sort_characters(characters)
            print_report(book_path, words_count, sorted_characters)
        except FileNotFoundError:
            print("Book not found")
        except Exception as e:
            print(e)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

    return None


def print_report(path, words_count, sorted_characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


main()
