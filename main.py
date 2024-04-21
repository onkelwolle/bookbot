def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(text)} words in {book_path}")
    
    print_counted_chars(text)
    
    print(f"--- End report of {book_path} ---")

def print_counted_chars(text):
    letter_list = convert_dict_to_list(count_letters_in_text(text))
    letter_list.sort(key=sort_on, reverse=True)
    for letter in letter_list:
        print(f"{letter['letter']}: {letter['num']}")

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(dict):
    return [{"letter": key, "num": dict[key]} for key in dict]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters_in_text(text):
    letter_dict = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

main()