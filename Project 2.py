
def word_counts(text):
    """
    Count number of words in the text.

    Args:
        text: valid text to count words.

    Returns:
        Number of words.
    """
    words=text.split()
    return len(words)

def main():
    while True:
        text =input("Enter a text:")
        if not text.strip():#Check whether an empty string or not.
            print("Oops!! This is a invalid input.")
        else:
            try:
                count=word_counts(text) #Calling the function and providing actual arguments.
                print("\nNumber of words in the text:",count)
                break
            except Exception as e: # Catch any unexpected error.
                print("\nAn error occured:",e)
            
if __name__ == '__main__':
    main()
    