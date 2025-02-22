import streamlit as st
from forms.contact import contact_form

# --- Contact Form ---
@st.dialog("📩 Get in Touch")
def show_contact_form():
    contact_form()

# --- Hero Section ---
col1, col2 = st.columns([1, 2], gap='medium', vertical_alignment="center")

with col1:
    st.image(
        "./assets/about.jpg",
        use_container_width=True,  # Use the new recommended parameter
    )
    st.markdown(
        """
        <style>
            img {
                
                border-radius: 50px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                height:220px
            }
        </style>
        """,
        unsafe_allow_html=True,
    )




with col2:
    st.title("✨ Faryal Junaid", anchor=False)
    st.markdown(
        """
        **Frontend Developer** | Passionate about AI & Web3  
        Currently learning **Agentic AI** from Governor Sindh Initiative 🚀  
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
    """
    <p style="font-size:18px; font-weight:bold;  padding:10px; border-radius:10px;">
        ✨ I am an expert in pixel-perfect, SEO-friendly, and responsive web applications.
    </p>
    """,
    unsafe_allow_html=True,
    )
      # Create two columns
col1, col2 = st.columns(2)

with col1:
    st.link_button("💖 Visit Profile", "https://portfolio-next-js-eight-sooty.vercel.app/")

with col2:
    st.button("📬 Contact Me!", on_click=show_contact_form)
    
# --- Experience & Qualifications ---
st.markdown("---")
st.subheader("💼 Experience & Qualifications", anchor=False)
st.write(
    """
    🔹  **1+ years** of experience extracting insights from data  
    🔹  Strong hands-on experience in **TypeScript** & **Next.js**  
    🔹  Senior student in the **GIAIC program**, continuously enhancing skills  
    🔹  Good understanding of **responsive and optimized** web applications  
    🔹  Excellent **team-player** with a strong sense of initiative  
    """
)

# --- Hard Skills ---
st.markdown("---")
st.subheader("🚀 Hard Skills", anchor=False)
st.write(
    """
    🔹  **Languages & Frameworks:** Python, HTML, CSS, JavaScript, TypeScript, Next.js  
    🔹  **Front-End Development:** Responsive design, UI/UX optimization, animations  
    🔹  **Performance Optimization:** SEO best practices, lazy loading, code splitting  
    🔹  **Tools & Libraries:** Git, Tailwind CSS, Bootstrap, Figma, Inquirer.js  
    """
)

# --- Footer ---
st.markdown("---")
st.markdown("<center>✨ Made with ❤️ by Faryal Junaid ✨</center>", unsafe_allow_html=True)
