import sys
from books.stats import word_count, character_count, character_sort ,sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
        book_text = get_book_text(filepath)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}")
        print("----------- Word Count ----------")
        print(f"Found {word_count(book_text)} total words")
        print("--------- Character Count -------")
        num_characters = character_count(book_text)
        for char_dict in character_sort(num_characters):
            print(f"{char_dict['char']}: {char_dict['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


if __name__ == "__main__":
    main()