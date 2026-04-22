print("Welcome To Quize Game")
questions = [
    {
        "question":"What is 2+2?",
        "options":["A)3","B)4","C)5","D)6"],
        "answer":"B"
    },
    {
        "question":"what is 5+5?",
        "options":["A)7","B)8","C)9","D)10"],
        "answer":"D"
    }
]

score = 0

for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_input = input("Select Option: ").upper()
    
    if user_input == q["answer"]:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print("Correct Answer:",q["answer"]) 

print("Total score:",score)           