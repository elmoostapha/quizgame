def ask_question(question, correct_answer):
    user_answer = input(question).strip().lower()
    return user_answer == correct_answer

def main():
    print("Welcome to the Morocco quiz game!")
    play = input("Do you want to play? (y/n): ").strip().lower()

    if play not in ('y', 'yes'):
        print("Goodbye!")
        quit()

    questions = [
        ("What is the capital of Morocco? ", "rabat"),
        ("What is the most common religion in Morocco? ", "islam"),
        ("In which continent does Morocco lie? ", "africa")
    ]

    score = 0
    for question, answer in questions:
        if ask_question(question, answer):
            score += 1

    if score == 3:
        print("Congratulations! You got all answers correct.")
    elif score == 2:
        print(f"Well done! You got {score} questions correct.")
    elif score == 1:
        print(f"Not bad! You got {score} question correct. Keep it up!")
    else:
        print("Better luck next time! You didn't get any questions correct.")

if __name__ == "__main__":
    main()
