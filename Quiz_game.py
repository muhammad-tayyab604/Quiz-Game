print("Welcome to my computer!")
question=input("Do you want to play a game:\n")

score=0

if question.lower()=='yes' or 'y':
    print("Ok Let's PLay! :)")
elif question.lower()=="no":
    exit()

answer=input("What does CPU stands for:\n")
if answer.lower()=='central processing unit':
    print("CORRECT!")
    score+=1
else:
    print("Incroorect! The Correct is 'central processing unit'")

answer=input("What does PSU stands for:\n")
if answer.lower()=='power supply unit':
    print("CORRECT!")
    score+=1
else:
    print("Incroorect! The Correct is 'Power Supply Unit'")

answer=input("What does RAM stands for:\n")
if answer.lower()=='random access memory':
    print("CORRECT!")
    score+=1
else:
    print("Incorrect! The Correct is 'random access memory'")

answer=input("What does ROM stands for:\n")
if answer.lower()=='read only memory':
    print("CORRECT!")
    score+=1
else:
    print("Incroorect! The Correct is 'Read Only Memory'")

print(f"You got {score} questions corrrect!")
print(f"You got {(score/4)*100}%.")