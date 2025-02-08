
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

    print(word_count)

main()