def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

questions = [
    {
        "prompt": "If a triangle has sides 3, 4, and 5, what type of triangle is it?",
        "options": ["A. Equilateral", "B. Isosceles", "C. Right", "D. Scalene"],
        "answer": "C"
    },
    {
        "prompt": "What is 12 ÷ 4?",
        "options": ["A. 2", "B. 3", "C. 4", "D. 6"],
        "answer": "B"
    },
    {
        "prompt": "What is 3 cubed (3³)?",
        "options": ["A. 6", "B. 9", "C. 27", "D. 30"],
        "answer": "C"
    },
    {
        "prompt": "What is the sum of the interior angles of a hexagon?",
        "options": ["A. 360°", "B. 540°", "C. 720°", "D. 900°"],
        "answer": "C"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"],
        "answer": "C"
    },
    {
        "prompt": "Which of the following sorting algorithms has the best average-case time complexity?",
        "options": ["A. Bubble Sort", "B. Merge Sort", "C. Insertion Sort", "D. Selection Sort"],
        "answer": "B"
    },
    {
        "prompt": "Which of the following data structures is used in a Breadth-First Search (BFS) algorithm?",
        "options": ["A. Stack", "B. Queue", "C. Priority Queue", "D. Linked List"],
        "answer": "B"
    },
    {
        "prompt": "What is the difference between `is` and `==` in Python?",
        "options": [
            "A. Both compare values",
            "B. `is` compares identity, while `==` compares values",
            "C. `is` compares values, while `==` compares identity",
            "D. They are equivalent in all scenarios"
        ],
        "answer": "B"
    },
    {
        "prompt": "In Java, which keyword is used to prevent a method from being overridden?",
        "options": ["A. final", "B. static", "C. protected", "D. private"],
        "answer": "A"
    }
]

run_quiz(questions)
