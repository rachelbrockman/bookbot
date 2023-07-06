def count_words(words):
    word = words.split()
    number_words = len(word)
    print(f"Number of words in book: {number_words}")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)


main()
