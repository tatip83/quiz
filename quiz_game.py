
def run_quiz():
    print("Welcome to the Quiz!")
    
    if input("Do you want to play? (yes/no): ").strip().lower() != "yes":
        print("Goodbye!")
        return


    questions = {
        "Which planet is known as the 'Red Planet'?": "Mars",
        "What is the largest mammal?": "Blue Whale",
        "Which video game has sold the most copies ever?": "Minecraft",
        "Which city is known as the 'Big Apple'?": "New York City"
    }

    score = 0

    for question, correct_answer in questions.items():
        user_answer = input(f"\n{question} ").strip()
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct! ✅")
            score += 1
        else:
            print(f"Incorrect! ❌ (Correct would be: {correct_answer})")

    print(f"\n--- Done! Your score is {score}/{len(questions)} ---")

if __name__ == "__main__":
    run_quiz()