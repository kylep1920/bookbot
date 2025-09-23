import sys
from stats import count_words
from stats import count_characters
from stats import sort_on

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return (file_contents)

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]} ....")
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in count_characters(book_text):
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
main()