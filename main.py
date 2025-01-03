def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        text = f.read()
        
    word_count = count_words(text)
    char_count = count_characters(text)
    
    print_report(book_path, word_count, char_count)
        
def count_words(text):
    return len(text.split())

def count_characters(text):
    char_count = {}
    for char in text:
        if char.lower() not in char_count:
            char_count[char.lower()] = 0
        char_count[char.lower()] += 1
    return char_count

def print_report(book_path, word_count, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    for char in char_count:
        if char.isalpha():
            print(f"The '{char} character was found {char_count[char]} times")
    print("--- End report ---")
    return
    
main()