# function that prints days of the week on separate lines
def days_of_week():
    print("Monday\nTuesday\nWednesday\nThursday\nFriday\nSaturday\nSunday")#

days_of_week()

print("") # separate outputs

# replace every other word with "Hello"
def replace_words(sentence):
    # put the words into a list
    word_list = sentence.split(" ")
    second = False

    # loop though list and replace every other word
    for counter in range(len(word_list)):
        if second:
            word_list[counter] = "Hello"
        second = not second
    
    # join words back into string
    new_sentence = " ".join(word_list)

    return new_sentence

print(replace_words("No one is useless in this world who lightens the burdens of another"))


