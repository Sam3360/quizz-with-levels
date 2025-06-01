General Knowledge (GK) Quiz Application
This is a simple, console-based General Knowledge quiz application built purely with Python. It allows users to test their knowledge by answering multiple-choice questions across different difficulty levels.

Features
Multiple Difficulty Levels: Choose from Easy, Hard, or Extreme questions.

General Knowledge Questions: A set of pre-defined MCQ questions covering various GK topics.

Interactive Console Interface: Play the quiz directly in your terminal or command prompt.

Score Tracking: Your score is calculated and displayed at the end of each quiz session.

Randomized Questions: Questions within the chosen difficulty level are shuffled for variety.

Important Notes
Console-Based: This is a command-line interface (CLI) application. There is no graphical user interface (GUI) or web interface.

No Persistence: The quiz questions are hardcoded within the script. There is no functionality to save user scores or add new questions dynamically. Every time you run the app, it starts fresh.

Requirements
Python 3.x (This script uses standard Python libraries, so no pip install is needed beyond having Python itself).

How to Run the Application
Save the Code:

Copy the entire Python code (the one with quiz_data_by_difficulty) into a file named gk_quiz.py (or any other name ending with .py).

Open Your Terminal/Command Prompt:

Navigate to the directory where you saved gk_quiz.py using the cd command.

Example (Windows): cd C:\Users\YourUser\Documents\my_projects

Example (macOS/Linux): cd ~/Documents/my_projects

Run the Script:

Execute the Python script using the command:

python gk_quiz.py

How to Play
Choose Difficulty:

When the application starts, you will be prompted to select a difficulty level:

1 for Easy

2 for Hard

3 for Extreme

Enter the corresponding number and press Enter.

Answer Questions:

For each question, the question text and numbered options will be displayed.

Enter the number corresponding to your chosen answer and press Enter.

Review Results:

After answering all questions, your final score and a brief performance message will be displayed.

Customization
Add More Questions: You can easily extend the quiz_data_by_difficulty dictionary by adding more question objects to each difficulty list. Ensure each question object has question, options, and correct_answer_index keys.

Adjust Difficulty: Modify the questions or the correct_answer_index to fine-tune the difficulty levels.

Possible Future Enhancements (for advanced learning)
Persistence: Store questions in an external file (e.g., JSON, CSV) so they can be easily modified without changing the code.

User Profiles: Integrate with an authentication system (like the auth_login_system.py we discussed) to track individual user scores.

GUI: Create a graphical user interface using libraries like Tkinter, PyQt, or Kivy for a more visually appealing experience.

Timer: Add a timer for each question or for the entire quiz.

More Question Types: Implement true/false, fill-in-the-blank, or short answer questions.
