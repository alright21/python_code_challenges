# sort a word list alphabetically
def sort_words(phrase):

    phrase = phrase[0].split()
    phrase.sort()
    
    return " ".join(phrase)
    
# take the input
user_input = input("Enter a sentence: ")

# get the result
to_check = []
to_check.append(user_input)
print(sort_words(to_check))