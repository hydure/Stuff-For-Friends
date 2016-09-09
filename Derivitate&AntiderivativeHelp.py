#list all the derivatives and antiderivates
#ask user for the answer of a random d/S
#compare the user's responsed to the actual answer, if right then say correct,
#if not give them the another try each random so the user is constantly asked

import random



#creates an array with the identities, and another with their corresponding
#values
arrayQ = ['dsinx', 'dcosx', 'dtanx', 'dcscx', 'dsecx', 'dcotx', 'Ssinxdx', \
          'Scosxdx', 'Ssec^2xdx', 'Scsc^2xdx', 'Ssecxtanxdx',\
        'Scscxcotxdx', 'Stanxdx', 'Scotxdx', 'Ssecxdx', 'Scscxdx']
answerArray = ['cosx', '-sinx', 'sec^2x', '-cscxcotx', 'secxtanx',
               '-csc^2x', '-cosx', 'sinx', 'tanx', '-cotx', 'secx',\
               '-cscx', 'ln|secx|', 'ln|sinx|', 'ln|secx + tanx|',\
               'ln|cscx - cotx|'] 

#randomly selects an index to be used by both arrays so that the identity\
#matches up with its answer
choice = random.randint(0, 15)
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
    choice = random.randint(0, 15)
    print(arrayQ[choice])
    answer_string = input("What does this equal? ")    
print("Goodbye.")