import re
import streamlit as st
import requests  # pip install requests

# Formspree Endpoint
FORMSPREE_URL = "https://formspree.io/f/mqakbkja"  # Replace with your Formspree form ID

# Function to validate email
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

# Function to display contact form
def contact_form():
    st.markdown("<p style='text-align: center; color: gray;'>We'd love to hear from you! Fill out the form below.</p>", unsafe_allow_html=True)

    with st.form("contact_form", border=True):
        name = st.text_input("🧑 First Name", placeholder="Enter your full name")
        email = st.text_input("📨 Email Address", placeholder="Enter your email")
        message = st.text_area("💬 Your Message", placeholder="Write your message here...")
        submit_button = st.form_submit_button("🚀 Submit")

    if submit_button:
        if not name:
            st.error("❌ Please provide your name.", icon="🧑")
            return

        if not email:
            st.error("❌ Please provide your email address.", icon="📨")
            return

        if not is_valid_email(email):
            st.error("⚠️ Please enter a valid email address.", icon="📧")
            return

        if not message:
            st.error("❌ Please provide a message.", icon="💬")
            return

        # Prepare data payload for Formspree
        data = {"name": name, "email": email, "message": message}
        response = requests.post(FORMSPREE_URL, json=data)

        if response.status_code == 200:
            st.success("✅ Your message has been sent successfully! 🎉", icon="🚀")
        else:
            st.error("❌ There was an error sending your message. Please try again later.", icon="😨")

if __name__ == "__main__":
    contact_form()
