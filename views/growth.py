import streamlit as st

# 🎯 Title for the Streamlit page
st.title("🌱 Growth Mindset Challenge 🚀")

# 🔍 Description of the Growth Mindset
st.header("🤔 What is Growth Mindset?")
st.write("""
    A **Growth Mindset** is the belief that abilities and intelligence can be developed through dedication, hard work, and learning.  
    People with a growth mindset are more likely to **embrace challenges 💪, learn from criticism 🎯, and find motivation in others' success 🌟.**
""")

# ⚖️ Growth Mindset vs Fixed Mindset
st.header("⚖️ Growth Mindset vs Fixed Mindset")

st.write("""
- **🌱 Growth Mindset**: Believes that intelligence and abilities can grow with effort and learning.
- **🚧 Fixed Mindset**: Believes that intelligence and abilities are static and cannot be changed.

### 🔑 Key Differences:
- **💡 Challenges**:  
  - 🌱 *Growth Mindset*: Embraces challenges, sees them as opportunities to learn.  
  - 🚧 *Fixed Mindset*: Avoids challenges, feels threatened by them.
  
- **🔥 Effort**:  
  - 🌱 *Growth Mindset*: Believes effort leads to mastery.  
  - 🚧 *Fixed Mindset*: Believes effort is a sign of inability.

- **📝 Feedback**:  
  - 🌱 *Growth Mindset*: Accepts feedback as a tool for improvement.  
  - 🚧 *Fixed Mindset*: Rejects feedback, sees it as criticism.
  
- **🏆 Success of Others**:  
  - 🌱 *Growth Mindset*: Finds inspiration in others’ success.  
  - 🚧 *Fixed Mindset*: Feels threatened by others’ success.
""")

# 📝 Self-Assessment (simple quiz)
st.header("📝 Self-Assessment: Growth or Fixed Mindset?")
st.write("""
🔍 **Answer the following questions to see where you stand on the growth mindset spectrum.**  
*(Check the boxes that apply to you)*  
""")

questions = [
    "💭 Do you believe intelligence is something you can improve with effort?",
    "📉 When you fail, do you see it as an opportunity to learn?",
    "🗣️ Do you seek feedback to improve your performance?",
    "🏋️‍♂️ Do you enjoy taking on challenges?"
]

responses = []

# Create checkboxes for self-assessment
for question in questions:
    response = st.checkbox(question)
    responses.append(response)

# 📊 Show Results
if st.button("🔍 Check My Mindset"):
    growth_score = sum(responses)
    
    st.write(f"🎯 **Your Growth Mindset Score: {growth_score}/{len(questions)}**")
    
    if growth_score == len(questions):
        st.write("🌟 **Great job! You're fully embracing a growth mindset.** Keep pushing forward! 🚀")
    elif growth_score > len(questions) // 2:
        st.write("👍 **You're on the right track.** Keep working on your growth mindset! 💡")
    else:
        st.write("🔄 **It looks like you lean towards a fixed mindset.** Consider working on embracing challenges and learning from feedback. 💪")

# 🌟 How to Cultivate a Growth Mindset
st.header("🌟 How to Cultivate a Growth Mindset")
st.write("""
Here are a few steps to help you **develop and nurture a growth mindset**:

1. **💪 Embrace challenges** – Don't shy away from difficulties. See them as opportunities for growth.  
2. **📝 Learn from criticism** – Constructive feedback is a valuable tool for improvement. Use it to better yourself.  
3. **🎯 Celebrate effort** – Hard work and persistence lead to success. Keep going!  
4. **🔄 Reflect on your progress** – Celebrate small wins and continuously look for areas to improve.  
5. **🚀 Stay inspired** – Find motivation in others’ success and let it fuel your journey.  

### 📚 Resources to Learn More:
- 📖 [**Book: Mindset by Carol Dweck**](https://www.amazon.com/Mindset-Psychology-Carol-Dweck-Ph-D/dp/0345472322)  
- 🎤 [**TED Talk: The Power of Yet by Carol Dweck**](https://www.ted.com/talks/carol_dweck_the_power_of_yet)
""")

# 💖 Closing Note
st.write("""
💡 **Remember, adopting a growth mindset takes time and practice.**  
🌱 Celebrate **each step of progress** you make, no matter how small! 🚀  
""")
