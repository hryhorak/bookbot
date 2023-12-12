def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    # counting_words(text)

    # counting_letters(text)

    aggragate(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def counting_words(text):
    words = text.split()
    print(len(words))

def aggragate(text):
    print("--- Begin report of books/frankenstein.txt ---")
    count = counting_words(text)

    print(f"{count} words found in the document")


    counting_letters(text)

def counting_letters(text):
    dict = {}
    text = text.lower()

    for letter in text:
        if letter.isalpha():
            if letter.lower() not in dict:
                dict[letter] = 1
            dict[letter] += 1
   

    for i, j in dict.items():
        print(f"The '{i}' character was found {j} times")
        

main()