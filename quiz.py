question = ["Who painted the Moana Lisa?", "Who is the godess of wisdom in greek Mythology?", "How many people are on the basketball court at one time in one team?"]
answer = ["Leonardo da Vinci", "Athena", "5"]

score = 0
print("Welcome to this quiz game")
print("You will have 3 questions to answer")
print("This is your first question")

print (question[0])
answer2 = input()

if answer2 == answer[0]:
    print("You got it correct")
    score = score + 1
else:
    print("You got it wrong")

print (question[1])
answer3 = input()

if answer3 == answer[1]:
    print("You got it correct")
    score = score + 1
else:
    print("You got it wrong")

print (question[2])
answer4 = input()
if answer4 == answer[2]:
    print("You got it correct")
    score = score + 1
else:
    print("You got it wrong")


if score < 2:
    print("Better luck next time")
else:
    print("Good job you got "score" out of 5")