import random


quiz_data_by_difficulty = {
    "easy": [
        {
            "question": "What is the capital city of France?",
            "options": ["Rome", "Paris", "Berlin", "London"],
            "correct_answer_index": 1
        },
        {
            "question": "Which animal is known as the 'King of the Jungle'?",
            "options": ["Tiger", "Lion", "Elephant", "Bear"],
            "correct_answer_index": 1
        },
        {
            "question": "How many continents are there in the world?",
            "options": ["5", "6", "7", "8"],
            "correct_answer_index": 2
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
            "correct_answer_index": 3
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "O2", "N2"],
            "correct_answer_index": 0
        },
    ],
    "hard": [
        {
            "question": "Which famous physicist developed the theory of relativity?",
            "options": ["Isaac Newton", "Niels Bohr", "Albert Einstein", "Stephen Hawking"],
            "correct_answer_index": 2
        },
        {
            "question": "In what year did the Titanic sink?",
            "options": ["1905", "1912", "1918", "1923"],
            "correct_answer_index": 1
        },
        {
            "question": "Which country is the largest producer of coffee in the world?",
            "options": ["Colombia", "Vietnam", "Brazil", "Ethiopia"],
            "correct_answer_index": 2
        },
        {
            "question": "What is the longest river in the world?",
            "options": ["Amazon River", "Yangtze River", "Mississippi River", "Nile River"],
            "correct_answer_index": 3
        },
        {
            "question": "Who wrote the play 'Hamlet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
            "correct_answer_index": 1
        },
    ],
    "extreme": [
        {
            "question": "What is the capital of Liechtenstein?",
            "options": ["Vaduz", "Bern", "Luxembourg City", "Monaco"],
            "correct_answer_index": 0
        },
        {
            "question": "Which of the following is the largest known living single organism by mass?",
            "options": ["Blue Whale", "General Sherman Tree", "Pando (Aspen Grove)", "Honey Fungus"],
            "correct_answer_index": 3
        },
        {
            "question": "What is the name of the smallest bone in the human body?",
            "options": ["Femur", "Stapes", "Fibula", "Patella"],
            "correct_answer_index": 1
        },
        {
            "question": "Which year marked the end of the War of the Spanish Succession with the Treaty of Utrecht?",
            "options": ["1701", "1713", "1720", "1732"],
            "correct_answer_index": 1
        },
        {
            "question": "In quantum mechanics, what does the 'Heisenberg Uncertainty Principle' state?",
            "options": ["An electron can be in two places at once.", "It's impossible to know both the exact position and momentum of a particle simultaneously.", "Energy cannot be created or destroyed.", "Light travels at a constant speed."],
            "correct_answer_index": 1
        },
    ]
}

def run_quiz_by_difficulty():
    print("--- Welcome to the General Knowledge Quiz! ---")
   
    selected_difficulty = None
    while selected_difficulty not in ["easy", "hard", "extreme"]:
        print("\n--- Choose your Difficulty Level ---")
        print("1. Easy")
        print("2. Hard")
        print("3. Extreme")
       
        choice = input("Enter your choice (1, 2, or 3): ").strip()
       
        if choice == '1':
            selected_difficulty = "easy"
        elif choice == '2':
            selected_difficulty = "hard"
        elif choice == '3':
            selected_difficulty = "extreme"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    quiz_questions = quiz_data_by_difficulty[selected_difficulty]
    random.shuffle(quiz_questions) 
    score = 0
    total_questions = len(quiz_questions)

    print(f"\n--- Starting {selected_difficulty.upper()} Quiz ---")
    print(f"You'll answer {total_questions} questions. Good luck!\n")

    for i, q_data in enumerate(quiz_questions):
        print(f"\n--- Question {i + 1}/{total_questions} ---")
        print(q_data["question"])

        options = q_data["options"].copy() 
       
        for j, option in enumerate(options):
            print(f"{j + 1}. {option}")

        while True:
            try:
                user_input = input("Enter the number of your answer: ").strip()
                choice_index = int(user_input) - 1
               
                if 0 <= choice_index < len(options):
                    break
                else:
                    print("Invalid option. Please enter a number corresponding to an answer.")
            except ValueError:
                print("Invalid input. Please enter a number (e.g., 1, 2, 3).")

        if choice_index == q_data["correct_answer_index"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {q_data['options'][q_data['correct_answer_index']]}")
       
        print("-" * 30) 

    print("\n--- Quiz Finished! ---")
    print(f"You scored {score} out of {total_questions} in the {selected_difficulty.upper()} level!")
   
   
    percentage = (score / total_questions) * 100
    if percentage == 100:
        print("Perfect score! You're a true GK master!")
    elif percentage >= 70:
        print("Excellent job!")
    elif percentage >= 50:
        print("Well done!")
    else:
        print("Good effort! Keep learning and practicing.")

if __name__ == "__main__":
    run_quiz_by_difficulty()
