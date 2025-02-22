import streamlit as st
import random

def get_random_challenge():
    challenges = [
        "Implement a function to check if a number is prime!",
        "Write a Python program to reverse a string without using slicing.",
        "Find the largest element in a given list.",
        "Write a function to check if a string is a palindrome.",
        "Implement a basic calculator that supports addition, subtraction, multiplication, and division.",
        "Generate Fibonacci numbers up to a given limit.",
        "Create a program that counts the number of vowels in a string.",
        "Write a function to check if two strings are anagrams.",
        "Implement a simple to-do list using Python lists.",
        "Create a program that finds the factorial of a number using recursion."
    ]
    return random.choice(challenges)

def daily_coding_challenge():
    st.header("⚓ Embrace Challenges")
    st.markdown("#### 💡 Daily Coding 💻 Challenge!")
    st.write("Sharpen your coding skills with a new challenge every day!")
    if st.button("Start Challenge 🚀"):
        st.success(f"Today's Challenge: {get_random_challenge()}")

def python_quiz():
    st.header("📜 Learn from Mistakes ")
    st.markdown("#### 📝 Quick Python🐍 Quiz")
    st.write("Test your Python knowledge with a quick quiz!")
    
    questions = [
        {"question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "4", "16"], "answer": "8"},
        {"question": "Which keyword is used to define a function in Python?", "options": ["func", "def", "define", "lambda"], "answer": "def"},
        {"question": "What data type is the result of: type(5)?", "options": ["int", "str", "float", "type"], "answer": "int"},
        {"question": "Which of these is a mutable data type?", "options": ["tuple", "string", "list", "set"], "answer": "list"},
        {"question": "What does the 'len()' function do?", "options": ["Returns length of an object", "Returns a random number", "Creates a new object", "Removes an item"], "answer": "Returns length of an object"},
        {"question": "Which operator is used for floor division?", "options": ["/", "//", "%", "**"], "answer": "//"},
        {"question": "Which of these methods is used to add an item to a list?", "options": ["insert()", "add()", "push()", "append()"], "answer": "append"},
        {"question": "How do you create a dictionary in Python?", "options": ["[]", "()", "{}", "<>"] , "answer": "{}"},
        {"question": "What does 'is' keyword check?", "options": ["Equality", "Identity", "Membership", "None of the above"], "answer": "Identity"},
        {"question": "Which of these is used to handle exceptions?", "options": ["catch", "try-except", "error-handling", "handle"], "answer": "try-except"}
    ]
    
    if 'quiz_index' not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.correct_answers = 0
        st.session_state.wrong_answers = 0
        st.session_state.answers = []
    
    if st.session_state.quiz_index < len(questions):
        q = questions[st.session_state.quiz_index]
        st.write(f"Q{st.session_state.quiz_index+1}: {q['question']}")
        user_answer = st.radio("Choose an answer:", q["options"], key=f"q{st.session_state.quiz_index}")
        
        if st.button("Submit Answer"):
            st.session_state.answers.append({"question": q["question"], "user_answer": user_answer, "correct_answer": q["answer"]})
            
            if user_answer == q["answer"]:
                st.session_state.correct_answers += 1
                st.success("Correct! ✅")
            else:
                st.session_state.wrong_answers += 1
                st.error(f"Wrong! ❌ The correct answer is {q['answer']}")
            
            st.session_state.quiz_index += 1
            st.rerun()
    else:
        st.info(f"Quiz Completed! 🎉\nCorrect: {st.session_state.correct_answers} | Wrong: {st.session_state.wrong_answers}")
        st.write("### Review Your Answers:")
        for ans in st.session_state.answers:
            st.write(f"**Q:** {ans['question']}")
            st.write(f"**Your Answer:** {ans['user_answer']} | **Correct Answer:** {ans['correct_answer']}")
            st.markdown("---")


# 🎮 Number Guessing Game
def number_guessing_game():
    st.header("🎀 Stay Positive")
    st.markdown("#### 🎮 Guess the Number!")
    st.write("Guess a number between 1 and 10!")

    if 'target_number' not in st.session_state:
        st.session_state.target_number = random.randint(1, 10)
        st.session_state.guess_attempts = 0

    guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

    if st.button("Submit Guess"):
        st.session_state.guess_attempts += 1
        if guess == st.session_state.target_number:
            st.success(f"Correct! 🎉 You guessed it in {st.session_state.guess_attempts} attempts!")
            st.session_state.challenge_streak += 1
            del st.session_state.target_number
            del st.session_state.guess_attempts
        else:
            st.warning("Wrong guess, try again! ❌")


# 🧠 Math Challenge Game
def math_challenge():
    st.subheader("🧮 Solve the Math Challenge!")
    st.write("Answer simple math problems to test your skills.")

    if 'num1' not in st.session_state:
        st.session_state.num1 = random.randint(1, 20)
        st.session_state.num2 = random.randint(1, 20)
        st.session_state.operator = random.choice(["+", "-", "*"])

    problem = f"{st.session_state.num1} {st.session_state.operator} {st.session_state.num2}"
    correct_answer = eval(problem)

    st.write(f"📌 Solve: {problem}")
    user_answer = st.number_input("Your Answer:", step=1, key="math_input")

    if st.button("Submit Answer", key="submit_math"):
        if user_answer == correct_answer:
            st.success("Correct! ✅ Well done!")
            st.session_state.challenge_streak += 1
            del st.session_state.num1
            del st.session_state.num2
            del st.session_state.operator
        else:
            st.error(f"Incorrect! ❌ The correct answer was {correct_answer}.")
    

# 🏆 Challenge Streak Tracker
def challenge_streak():
    st.subheader("🏆💪 Your Challenge Streak")
    st.write("Track how many challenges you've completed so far!")
    if 'challenge_streak' not in st.session_state:
        st.session_state.challenge_streak = 0
    if st.button("Check My Streak 🔥"):
        st.success(f"You've completed {st.session_state.challenge_streak} challenges! Keep going!")

def share_progress():
    st.header("🎆 Celebrate Effort ")
    st.markdown("#### 📣📊 Share Your Progress")
    st.write("Let your friends know about your achievements!")
    if st.button("Share Now 📢"):
        st.balloons()
        st.success("🎉 Shared successfully! Keep up the great work!")

def main():
    st.title("🚀 MindGrowth Challenge Hub")
    st.write("A growth mindset is the belief that abilities can be developed through effort, learning, and perseverance.")
    st.markdown("---")
    
    daily_coding_challenge()
    st.markdown("---")
    python_quiz()
    st.markdown("---")
    number_guessing_game()
    st.markdown("---")
    math_challenge()
    st.markdown("---")
    challenge_streak()
    st.markdown("---")
    share_progress()
    

main()
