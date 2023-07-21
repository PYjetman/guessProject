print("HI! Welcome to the Guess Your Age program.")
more = 100#max
less = 0#minimal
choice = input("Would you like to give me a chance to guess your age? ")#user input
#condition loop with conditional statements
while choice.lower() == "yes":
    for i in range(1, 7):
        guessed_age = (more + less) // 2
        print("Attempt", i)
        print("Is your age more or less than " + str(guessed_age) + ": ")
        answer = input("Type 'more', 'less', or 'correct': ")

        if answer.lower() == "more":
            less = guessed_age + 1
        elif answer.lower() == "less":
            more = guessed_age - 1
        elif answer.lower() == "correct":
            print("Im smarter than your average bear! Your age is", guessed_age)
            break
        else:
            print("Please respond with 'more', 'less', or 'correct'.")
            continue

        if more < less:
            print("You are not providing consistent answers! Let's start again.")
            more = 100
            less = 0
            break

    if more >= less:
        print("I'm done guessing! Your age is probably", guessed_age)
        break

    choice = input("Would you like to give me another chance to guess your age? ")

print("Thank you for playing the Guess Your Age program!")

