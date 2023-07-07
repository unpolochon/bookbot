def main():
    path = "./books/frankenstein.txt"
    frankenstein_book = get_book_text(path)
    occurences = get_occurences(frankenstein_book)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{get_words_count(frankenstein_book)} words found in the document\n")

    for character in occurences:
        print(f"The {character} was found {occurences[character]} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_words_count(text):
    words = text.split()
    return len(words)

def get_occurences(text):
    occurences = {}
    for character in text:
        lowercase_character = character.lower()
        if not lowercase_character.isalpha():
            continue

        if lowercase_character in occurences:
            occurences[lowercase_character] += 1
        else:
            occurences[lowercase_character] = 1
    return occurences

main()
