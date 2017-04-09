'''
Created on 12 Mar 2017

@author: sam
'''
import random
name = input("What is your name?")
school_class = input("What is your class? 1, 2 or 3.")
while school_class != "1" and school_class != "2" and school_class != "3":
    school_class = input("Your class must be 1, 2 or 3. What class are you in?")
score = 0
for i in range(10):
    num1, num2 = random.randint(1,12), random.randint(1,12)
    operator = random.choice(["*", "+", "-"])
    question = str(num1) + operator + str(num2) if num1 > num2 else str(num2) + operator + str(num1)
    answer = str(eval(question))
    user_answer = input("{}. {}?".format(i + 1, question))
    if user_answer.isdigit() == False:
        user_answer = input("That was not an integer. What is {}?".format(question))
    score += 1 if answer == user_answer else 0
    print("Correct!") if user_answer == answer else print("Incorrect. The correct answer was {}.".format(answer))
print("Well done. You got {}.".format(score)) if score > 5 else print("Unlucky, you got {}".format(score))
try:
    with open("class{}".format(school_class), "a+") as file:
        file.write("{},{}\n".format(name, score))
        print("Your score was written to class{}.\n".format(school_class))
except:
    print("The file failed to write.")
