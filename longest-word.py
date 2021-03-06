if __name__ == "__main__":
    sen = input("Enter a sentence: ")
    longest_word = max(sen.split(), key=len)

    print('Longest word is: ', longest_word)
