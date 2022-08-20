import random
q1 = "What year did the U.S. declare independence? "
a1 = "1776"
q2 = "How many bones are in the adult human body? "
a2 = "206"
q3 = "Are cows ruminants? Yes or No: "
a3 = "yes"
q4 = "Who was the 16th President of the United States? "
a4 = "abraham lincoln"
q5 = "How many feet are in a mile? Give just the number:  "
a5 = "5280"
q6 = "How many meters are in a mile? Give just the number: "
a6 = "1609"
q7 = "What is the biggest state in the U.S.? "
a7 = "alaska"
q8 = "How many centimeters in an inch? Give just the number: "
a8 = "2.54"
q9 = "What year did the Louisiana Purchase occur? "
a9 = "1803"
q10 = "What is World War I also known as? "
a10 = "the great war"
q11 = "What is Las Vegas also known as? "
a11 = "sin city"
q12 = "How many States are in the United States? "
a12 = "50"
q13 = "What city is the capital of Nevada? "
a13 = "carson city"

qa1 = [q1, a1]
qa2 = [q2, a2]
qa3 = [q3, a3]
qa4 = [q4, a4]
qa5 = [q5, a5]
qa6 = [q6, a6]
qa7 = [q7, a7]
qa8 = [q8, a8]
qa9 = [q9, a9]
qa10 = [q10, a10]
qa11 = [q11, a11]
qa12 = [q12, a12]
qa13 = [q13, a13]

qa = [qa1, qa2, qa3, qa4, qa5, qa6, qa7, qa8, qa9, qa10, qa11, qa12, qa13]

answer = input("Welcome to my quiz!! Do you want to play? ")
if answer != "yes":
    print("Ok, maybe next time. Bye!")
    quit()
print("Let's continue then!")

number_correct = 0
#1

Q1 = (random.choice(qa))
Answer = input(Q1[0])
Number_of_Questions = 1
if Answer == Q1[1]:
    print("Correct!")
    number_correct = number_correct + 1
else:
    print("Incorrect")

qa.remove(Q1)

#2
Q2 = (random.choice(qa))
Answer = input(Q2[0])
Number_of_Questions = Number_of_Questions + 1
if Answer == Q2[1]:
    print("Correct!")
    number_correct = number_correct +1
else:
    print("Incorrect")
qa.remove(Q2)

#3
Q3 = (random.choice(qa))
Answer = input(Q3[0])
Number_of_Questions = Number_of_Questions + 1
if Answer == Q3[1]:
    print("Correct!")
    number_correct = number_correct + 1
else:
    print("Incorrect")
qa.remove(Q3)

#4
Q4 = (random.choice(qa))
Answer = input(Q4[0])
Number_of_Questions = Number_of_Questions + 1
if Answer == Q4[1]:
    print("Correct!")
    number_correct = number_correct + 1
else:
    print("Incorrect")
qa.remove(Q4)

#5
Q5 = (random.choice(qa))
Answer = input(Q5[0])
Number_of_Questions = Number_of_Questions + 1
if Answer == Q5[1]:
    print("Correct!")
    number_correct = number_correct + 1
else:
    print("Incorrect")
qa.remove(Q5)

print("You got " + str(number_correct) + " out of " + str(Number_of_Questions) + " correct.")
print("Thanks for playing!")
Input = input("Press Enter to quit: ")
if Input == "":
    quit()


