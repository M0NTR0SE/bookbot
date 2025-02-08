def main() -> int:
    # Open book file, and place contents in file_contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # Print contents of file_contents
    # print(file_contents)

    # Count the number of words in the file
    # Distinguish what counts as a separator of words (spaces, punctuation, etc.)
    # Evaluate if current is char is in separator set
    # If yes, +1 word count
    #   Need to create exceptions when separators chain each other. Example "Hi. Hello." would count as 3 words because '.', ' ', and '.'.

    words = file_contents.split()
    word_count = len(words)

    # print(word_count)

    characters = char_count(file_contents)
    # print(characters)

    printout(characters, word_count, __file__)

def char_count(texts):
    # Initialize empty dictionary to store values
    characters = {}

    # Go through all characters in text
    # Send to lowercase
    # Check if in characters dict
    #   If yes, increase count by 1
    #   If no, add character to dictionary, and increase count by 1
    for text in texts:
        text = text.lower()

        if text not in characters:
            characters[text] = 1
        elif text in characters:
            characters[text] += 1

    return(characters)

def printout(characters, word_count, file_path):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    # Initialize alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for character in characters:
        if character in alphabet:
            print(f"The '{character}' character was found {characters[character]} times")

    print("--- End report ---")

main()
