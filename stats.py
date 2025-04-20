import sys

def sort_on(dict):
    return dict["count"]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def book_text_string():
    book_text = get_book_text(sys.argv[1])
    return(book_text)

def word_count(book_text_string):
    word_list = book_text_string.split()
    num_words = len(word_list)

    return num_words

def each_character(book_text_string):
    each_character_dict = {}
    lower_case_text = book_text_string.lower()
    for character in lower_case_text:
        if character in each_character_dict:
            each_character_dict[character] += 1
        else:
            each_character_dict[character] = 1

    return each_character_dict

def sorted_char_list(character_dict):
    character_list = []
    for character, count in character_dict.items():
        if character.isalpha():
            character_list.append({"character": character, "count": count})
    character_list.sort(reverse=True,key=sort_on)
    return character_list

def print_list(sort_list):
    for pair in sort_list:
        print(str(pair["character"]) + ": " + str(pair["count"]))

