print("Welcome to zavalas POLS Test 2 study guide")

playing = input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()

print("Okay! Let's play :)") 
score = 0 

answer = input("Whats an example of a member of Congress that leaves their job and becomes a lobbyist? ")    
if answer.lower() == "revolving door":
    print('Correct!')
    score += 1 
else:
    print("Incorrect!")

answer = input("True or false: An interest group is defined as an organization whose goal is to get their members elected to office: ")    
if answer.lower() == "false":
    print('Correct!')
    score += 1 
else:
    print("Incorrect!")


answer = input("If someone only voted for candidates of the Democratic Party in the 2020 elections, they engaged in: ")    
if answer.lower() == "straight ticket voting":
    print('Correct!')
    score += 1 
else:
    print("Incorrect!")

answer = input("A common critcism of pluralism is that it: ")    
if answer.lower() == "emphasizes the interests of the wealthy":
    print('Correct!')
    score += 1 
else:
    print("Incorrect!")

answer = input("True or false: The free rider problem refers to the situation that occurs when some individuals receive benefits(get a free ride) without helping to bear the cost: ")    
if answer.lower() == "true":
    print('Correct!')
    score += 1 
else:
    print("Incorrect!")

answer = input("Which of the following is seen as more desirable when conducting a poll? Having a low margin of error/Having a high margin of error? ")    
if answer.lower() == "having a low margin of error":
    print('Correct!')
    score += 1 
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 6) * 100) + "% ")
