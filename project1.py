class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")
        answer = input("Enter the number of your answer: ")
        
        # Validate user input
        while not answer.isdigit() or not 1 <= int(answer) <= len(question.options):
            answer = input("Invalid input. Please enter a number corresponding to the options: ")
        
        if question.options[int(answer) - 1] == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {question.answer}\n")
    
    print(f"Your final score is: {score}/{len(questions)}")

def main():
    question_prompts = [
        "Who is the founder of Python?",
        "Who is the founder of c++?",
        "Who is the founder of Java?"
    ]
    
    options = [
        ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"],
        ["Bjarne Stroustrup","Dennis Ritchie", "Guido van Rossum", "James Gosling"],
        ["Dennis Ritchie", "Guido van Rossum", "Bjarne Stroustrup", "James Gosling"]
    ]
    
    answers = ["Paris", "4", "Blue"]
    
    questions = [Question(question_prompts[i], options[i], answers[i]) for i in range(len(question_prompts))]
    
    run_quiz(questions)

if __name__ == "__main__":
    main()
