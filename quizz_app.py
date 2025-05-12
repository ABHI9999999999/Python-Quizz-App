questions = [
    "1.What is the capital of India?",
    "2.Which is the largest planet?",
    "3.Who wrote Harry Potter?"
]

options = [
    ["1.Delhi", "2.Mumbai", "3.Kolkata", "4.Chennai"],
    ["1.Earth", "2.Mars", "3.Jupiter", "4.Venus"],
    ["1.J.K. Rowling", "2.Ruskin Bond", "3.Chetan Bhagat", "4.Sudha Murty"]
]

answers=["1","3","1"]
score=0
for i in range(len(questions)):
    print("\n"+questions[i])
    for opt in options[i]:
        print(opt)
    user_input=input("Enter your damn answer son(1 to 4):")
    
    if user_input==answers[i]:
        print("Correct")
        score+=1
    else:
        print("FUCKING GO TO SCHOOL DUMB RETARD")
        
print("Your fucking Final Score is:",score)