#list all the trig identities
#ask user for the answer of a random trig identity at a certain pi angle
#compare the user's responsed to the actual answer, if right then say correct,
#if not give them another try repeat each random so the user is constantly asked

import random

print("This is to help with trig identities, answer the following questions,\
 pressing 'Q' to quit. \n Ex. 'sqrt(2)/2' equates to the 'square root of 2\
 divided by 2', and 'DNE' means 'Does Not Exist'.")

#creates an array with the identities, and another with their corresponding
#values
arrayQ = ['sin(pi)', 'sin(pi/2)' , 'sin(pi/3)', 'sin(pi/4)', 'sin(pi/6)', \
         'cos(pi)', 'cos(pi/2)', 'cos(pi/3)', 'cos(pi/4)', 'cos(pi/6)', \
         'tan(pi)', 'tan(pi/2)', 'tan(pi/3)', 'tan(pi/4)', 'tan(pi/6)']
answerArray = ['0', '1', 'sqrt(3)/2', 'sqrt(2)/2', '1/2', '1', '0', '1/2', \
               'sqrt(2)/2', 'sqrt(3)/2', '0', 'DNE', 'sqrt(3)', '1',\
               'sqrt(3)/3'] 

#randomly selects an index to be used by both arrays so that the identity\
#matches up with its answer
choice = random.randint(0, 14)
print(arrayQ[choice])
answer_string = input("What does this equal? ")

#repeats random trig identities until user presses 'Q'
while answer_string != 'Q':
    if answer_string == answerArray[choice]:
        print("You are correct!")
    else:
        print("You're incorrect.")
        answer_string = input("Second chance, what does this equal? ")
        if answer_string == answerArray[choice]:
                print("You are correct!")        
    choice = random.randint(0, 14)
    print(arrayQ[choice])
    answer_string = input("What does this equal? ")    
print("Goodbye.")