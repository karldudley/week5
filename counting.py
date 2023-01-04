# function to count the letters in a sample string which is passed as an argument
def count_letters(sample):
    print(f"\nAnalysing: {sample}\n")
    # create empty dict
    letter_dict = {}

    # loop number of times equal to length of sample
    for x in range(len(sample)):
        # check if letter is already a key, if so add 1, if not create it and assign 1
        if sample[x].lower() in letter_dict:
            letter_dict[sample[x].lower()] += 1
        else:
            letter_dict[sample[x].lower()] = 1
    # return the dict of letter values
    return letter_dict

print(count_letters("google.com"))

zen_of_python = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

print(count_letters(zen_of_python))
