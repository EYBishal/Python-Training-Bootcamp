
def write_quiz(questions):
    with open("quiz.txt", "w") as f:
        num = 1
        for question in questions:
            f.write(f"{num}. {question}\n")
            f.write("\n") 
            num += 1

questions_list = [
    "What is the capital of India?",
    "Who wrote 'Python'?",
    "What is 5 + 7?"
]

write_quiz(questions_list)

