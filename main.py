import sys

if len(sys.argv) != 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_book_text, char_count, sort_it


def main():
    get_book_text(sys.argv[1])
    char_count(sys.argv[1])
    sort_it(char_count(sys.argv[1]))

main()
