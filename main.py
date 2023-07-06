def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = count_letters(text)
    print(chars_dict)
    report = print_report(chars_dict)
    print(f"{report}")


def count_words(words):
    word = words.split()
    number_words = len(word)
    print(f"Number of words in book: {number_words}")


def count_letters(text):
    char_count = {}  # empty dictionary
    for character in text:
        lower_case = character.lower()
        if lower_case.isalpha():
            if lower_case in char_count:
                char_count[lower_case] += 1
            else:
                char_count[lower_case] = 1
    return char_count


def print_report(char_count):
    report = []
    for character, count in char_count.items():
        report.append((f"The {character}", f" character was found {count} times"))
    report.sort()
    return report


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
