def get_number_words(book):
    return len(book.split())


def get_characters_occurence(book):
    characters = {}
    for char in book:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1
    return characters


def sort_on(dict):
    return dict["num"]


def sort_characters(characters):
    new_characters = []
    for key in characters:
        if key.isalpha():
            new_characters.append({"char": key, "num": characters[key]})
    new_characters.sort(reverse=True, key=sort_on)
    return new_characters
