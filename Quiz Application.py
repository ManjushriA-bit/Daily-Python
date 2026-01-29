import time

# Quiz questions
questions = [
    {
        "question": "What is the output of print(2 + 3 * 2)?",
        "options": ["A. 10", "B. 8", "C. 7", "D. 12"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "What does len() do?",
        "options": ["A. Adds values", "B. Finds length", "C. Deletes data", "D. Sorts data"],
        "answer": "B"
    }
]

score = 0
time_limit = 30   # seconds for full quiz

print("🧠 Welcome to the Python Quiz!")
print(f"You have {time_limit} seconds to complete the quiz.")
print("-" * 40)

start_time = time.time()

for i, q in enumerate(questions, start=1):
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > time_limit:
        print("\n⏰ Time's up!")
        break

    print(f"\nQ{i}. {q['question']}")
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {q['answer']}")

print("\n" + "=" * 40)
print(f"🏁 Quiz Finished!")
print(f"Your Score: {score} / {len(questions)}")
print("=" * 40)
