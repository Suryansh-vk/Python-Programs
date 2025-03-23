questions = {
    "What is the capital of France?": "Paris",
    "What is 5 + 3?": "8",
    "Who wrote 'Harry Potter'?": "J.K. Rowling",
}

score = 0

for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")

print(f"Final Score: {score}/{len(questions)}")
