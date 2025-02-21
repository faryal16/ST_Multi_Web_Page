import streamlit as st

# ______Page Seup
about_page = st.Page(
    page="views/about_me.py",
    title="About Me!!",
    icon=":material/account_circle:",
    default=True
)

project_1_page=st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)

project_2_page=st.Page(
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
        "Projects":[project_1_page, project_2_page]
    }
)


# ___ Shared on Alll pages
st.logo("assets/logo.webp")
st.sidebar.text("Made With ❤ by Fairy")

# Run Navigations
pg.run()
