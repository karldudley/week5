from random import randrange

# list of joke questions
joke_questions = ["What’s the best thing about Switzerland?", "Did you hear about the mathematician who’s afraid of negative numbers?", "Why do we tell actors to “break a leg?”", "Helvetica and Times New Roman walk into a bar.", "Hear about the new restaurant called Karma?", "Did you hear about the claustrophobic astronaut?", "Why don’t scientists trust atoms?", "How does Moses make tea?", "What kind of exercise do lazy people do?", "What do you call a parade of rabbits hopping backwards?"]

# list of joke answers
joke_answers = ["I don’t know, but the flag is a big plus.", "He’ll stop at nothing to avoid them.", "Because every play has a cast.", "“Get out of here!” shouts the bartender. “We don’t serve your type.”", "There’s no menu: You get what you deserve.", "He just needed a little space.", "Because they make up everything.", "He brews.", "Diddly-squats.", "A receding hare-line."]

print("Welcome to Random Jokes\t\t*** Press enter to see the punchline and get the next joke or type exit to leave :-( ***\n")

# create a loop to contiue serving up random jokes until exit is entered
while(True):
    # get random int from 0-9
    rand_int = randrange(10)

    # print the random joke
    print(f"{joke_questions[rand_int]}\n")
    response = input("-> ").lower()
    print(f"\n\t{joke_answers[rand_int]} :-)\n\n")

    if response == "exit":
        break

print("See you next time!")
