from stats import word_count, get_book_text, book_text_string, each_character, sorted_char_list, sort_on, print_list
import sys

def main():
    book_text = book_text_string()
    character_dict = each_character(book_text)
    sort_list = sorted_char_list(character_dict)
    file_path = sys.argv[1]
    
    print(f"\
============ BOOKBOT ============]\n\
Analyzing book found at {file_path}...\n\
---------- Word Count ----------\n\
Found {word_count(book_text)} total words\n\
--------- Character Count -------")
    print_list(sort_list)
    print("============= END ===============")
    
    

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:    
    main()



    
    
    
    