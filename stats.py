def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def book_text_string():
    book_text = get_book_text("books/frankenstein.txt")
    return(book_text)

def each_character(book_text_string):
    each_character_dict = {}
    lower_case_text = book_text_string.lower()
    for character in lower_case_text:
        each_character_dict[character] = 1



    print(each_character_dict)

each_character(book_text_string())
