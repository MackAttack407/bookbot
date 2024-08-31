def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_dict = get_num_characters(text)
    
    print(f"--- Begin report of books/frankenstein.txt --- \n{num_words} words found in the document\n")
    print_char_counts(characters_dict)
    print("--- End report ---")
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_characters(text):
    characters = {}
    lowered_string = text.lower()
    for i in lowered_string:
        current_count = characters.get(i, 0)
        current_count += 1
        characters[i] = current_count
    return characters

def print_char_counts(char_dict):
    # Sort the dictionary by value (count) in descending order
    sorted_chars = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_chars:
        if char.isalpha():  # Only print alphabetic characters
            print(f"The '{char}' character was found {count} times")
   

main()



