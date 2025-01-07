
def main():
    file_path = 'books/frankenstein.txt'
    content = read_content(file_path)
    word_count = count_words(content)
    char_count = count_characters(content)
    
    print("--- Begin report of books/frankenstein.txt ---")
    
    print(f"{word_count} words found in the document")
    
    sorted_char_count = dict(sorted(char_count.itemsgst(), key=lambda item: item[1], reverse=True))
    
    for char, count in sorted_char_count.items():
        print(f"The {char} character was found {count} times")
    
    print("--- End report  ---")

def read_content(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(content):
    words = content.split()
    return len(words)

def count_characters(content) -> dict:
    characters = {}
    for char in content.lower():
        if not char.isalpha():
            continue
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

if __name__ == '__main__':
    main()