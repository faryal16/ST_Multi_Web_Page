import streamlit as st

# ______Page Seup
about_page = st.Page(
    page="views/about_me.py",
    title="About Me!!",
    icon=":material/account_circle:",
    default=True
)

project_1_page=st.Page(
    page="views/growth.py",
    title="Artical",
    icon=":material/thumb_up:"
    
)
project_2_page=st.Page(
    page="views/challenges.py",
    title="Challenges",
    icon=":material/trophy:"
    
)
project_3_page = st.Page(
    page="views/data_sweeper.py",
    title="Data Sweeper",
    icon=":material/delete_sweep:"
)
project_4_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)


project_5_page=st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)

# ___ Navigation Setup [Without Sections]
# pg =st.navigation(pages=[about_page, project_1_page, project_2_page])

## ___ Navigation Setup [With Sections]
pg=st.navigation(
    {
        
        "info": [about_page],
        "Projects":[project_1_page, project_2_page, project_3_page,project_4_page,project_5_page]
    }
)

# sidebar_logo = st.selectbox("Code With Fairy🍃")
# ___ Shared on Alll pages

# Custom logo styling at the top
st.logo("assets/logo.jpeg"
    
)
st.sidebar.text("Made With ❤ by Fairy")

# Run Navigations
pg.run()
