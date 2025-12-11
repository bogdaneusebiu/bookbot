from stats import get_num_words
from stats import make_output
from stats import get_letter_freq
import sys

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    number_of_words = get_num_words(book)
    letter_freq = get_letter_freq(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")

    characters = make_output(letter_freq)

    for char in characters:
        if char["name"].isalpha():
            print(f"{char["name"]}: {char["num"]}")

    print("============= END ===============")
main()
