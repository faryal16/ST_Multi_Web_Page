import random
import time
import streamlit as st

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            " Hey there! Need help? Check out my LinkedIn **'Faryal Junaid 💖'** 🔗: [Click here](https://www.linkedin.com/in/faryal-junaid-06780b2b4/) 🚀",
            " Hi! What's up? Don't forget to connect with **'Faryal Junaid 💖'** 🤝: [Click here](https://www.linkedin.com/in/faryal-junaid-06780b2b4/) 🌟",
            " Hello! Need assistance? My LinkedIn **'Faryal Junaid 💖'** is full of great tips! 📚 [Visit here](https://www.linkedin.com/in/faryal-junaid-06780b2b4/) 💻",
            " Hey! Got a question? Also, connect to **'Faryal Junaid 💖'** for awesome tutorials 🎓: [Check it out](https://www.linkedin.com/in/faryal-junaid-06780b2b4/)",
            " Hi there! How can I help? BTW, my profile **'Faryal Junaid 💖'** is super cool 🚀: [Click here](https://www.linkedin.com/in/faryal-junaid-06780b2b4/) ",
            " Hello! Looking for help? Check out **'Faryal Junaid 💖'** on LinkedIn 💼: [See profile](https://www.linkedin.com/in/faryal-junaid-06780b2b4/) ",
            " Hey! Need assistance? **'Faryal Junaid 💖'** on LinkedIn has you covered 🏆: [Click here](https://www.linkedin.com/in/faryal-junaid-06780b2b4/)",
            " Hi! Got any coding questions? Don't forget to follow **'Faryal Junaid 💖'** 💻: [Visit here](https://www.linkedin.com/in/faryal-junaid-06780b2b4/)",
            " Hello! Need help? **'Faryal Junaid 💖'** on LinkedIn is a must-see 🧐: [Check out now](https://www.linkedin.com/in/faryal-junaid-06780b2b4/)",
            " Hey there! Any questions? My account **'Faryal Junaid 💖'** rocks 🎉: [See here](https://www.linkedin.com/in/faryal-junaid-06780b2b4/) ",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("💬 Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("💬 What’s up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user", avatar="🧑"):
        st.markdown(f" {prompt}")

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar="💻"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
