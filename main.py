import sys
from stats import count_words
from stats import count_chars
from stats import report


def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        path = sys.argv[1]
        num_words = count_words(get_book_text(path))
        num_chars = count_chars(get_book_text(path))
        sorted_list = report(num_chars)
        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {path}")
        print ("----------- Word Count ----------")
        print (f"Found {num_words} total words")
        print ("--------- Character Count -------")
        for char_dict in sorted_list:
            char = char_dict["char"]
            count = char_dict["num"]
            if char.isalpha():
                print(f"{char}: {count}")
        print ("============= END ===============")


main()