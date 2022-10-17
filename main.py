
book_path = "books/frankenstein.txt"

def main():
    text = open_book(book_path)
    words = get_words(text)
    count = word_count(words)
    char_dic = get_characters(words)
    sorted_characters = sort_characters(char_dic)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    for character in sorted_characters:
        print(f"The {character} character was found {char_dic[character]} times")
    print(f"--- End report ---")
    
def open_book(path):
    with open(path) as f:
        text = f.read()
    f.close()
    return text
    
def get_words(text):
    words = text.split()
    return words

def word_count(words):
    return len(words)

def get_characters(words):
    char_dic = {}
    for word in words:
        word_lowercase = word.lower()
        for character in word_lowercase:
            if character not in char_dic:
                char_dic[character] = 1
            else:
                char_dic[character] += 1
    return char_dic    

def sort_characters(char_dic):
    sorted_list = [] 
    for character in char_dic:
        if character.isalpha():
            sorted_list.append(character)
    sorted_list.sort()
    return sorted_list

main()