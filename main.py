
book_path = "books/frankenstein.txt"

def main():
    text = open_book(book_path)
    words = get_words(text)
    characters = get_characters(words)
    sorted_characters = sort_characters(characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{len(words)} words found in the document")
    for character in sorted_characters:
        print(f"The {character} character was found {characters[character]} times")
    print(f"--- End report ---")
    
def open_book(path):
    with open(path) as f:
        text = f.read()
    f.close()
    return text
    
def get_words(text):
    words = text.split()
    return words

def get_characters(words):
    characters = {}
    for word in words:
        word_lowercase = word.lower()
        for character in word_lowercase:
            if character not in characters:
                characters[character] = 1
            else:
                characters[character] += 1
    return characters    

def sort_characters(characters):
    sorted_list = [] 
    for character in characters:
        if character.isalpha():
            sorted_list.append(character)
    sorted_list.sort()
    return sorted_list

main()