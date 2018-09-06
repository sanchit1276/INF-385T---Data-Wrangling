
#Question 1
correctAnswer = "8"
user_guess = input("What is your guess? ")

if (user_guess == correctAnswer):
    print("You are correct")
else:
    print("You are incorrect")

#Question2
correctAnswer = "8"
user_guess = input("What is your guess? ")

if (user_guess > correctAnswer):
    print("Your guess is too high")
else:
    print("Your guess is too low")

#Question3
correctAnswer = "8"
user_guess = input("What is your guess? ")

while(user_guess != correctAnswer):
    user_guess = input("Guess again! ")

print("You are correct!")

#Question4
