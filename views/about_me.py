import streamlit as st

from forms.contact import contact_form



## --- Contact Form ---
@st.dialog("📩 Get in Touch")
def show_contact_form():
    contact_form()

# --- Hero Section ---
col1, col2 = st.columns([1, 2], gap="small", )
with col1:
    st.image("./assets/about.jpg", width=330)

with col2:
    st.title("✨ Faryal Junaid", anchor=False)
    st.markdown(
        """
        **Frontend Developer** | Passionate about AI & Web3  
        Currently learning **Agentic AI** from Governor Sindh Initiative 🚀  
        """,
        unsafe_allow_html=True,
    )

    if st.button("📬 Contact Me!"):
        show_contact_form()

# --- Experience & Qualifications ---
st.markdown("---")
st.subheader("💼 Experience & Qualifications", anchor=False)
st.write(
    """
    🔹  **1+ years** of experience extracting insights from data  
    🔹  Strong hands-on experience in **TypeScript** & **Next.js**  
    🔹  Good understanding of **statistical principles** & applications  
    🔹  Excellent **team-player** with a strong sense of initiative  
    """
)

# --- Hard Skills ---
st.markdown("---")
st.subheader("🚀 Hard Skills", anchor=False)
st.write(
    """
    🔹  **Programming:** Python (Scikit-learn, Pandas), SQL, VBA  
    🔹  **Data Visualization:** PowerBi, MS Excel, Plotly  
    🔹  **Modeling:** Logistic regression, linear regression, decision trees  
    🔹  **Databases:** Stripe, MongoDB, Sanity  
    """
)

# --- Footer ---
st.markdown("---")
st.markdown("<center>✨ Made with ❤️ by Faryal Junaid ✨</center>", unsafe_allow_html=True)
