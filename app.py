# app.py
import hmac
import os
import streamlit as st
from dotenv import load_dotenv

# Load the .env
load_dotenv()

if "auth" not in st.session_state:
    st.session_state.auth = False


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        # If you use .streamlit/secrets.toml, replace os.environ.get with st.secrets["STREAMLIT_PASSWORD"]
        if hmac.compare_digest(
            st.session_state["password"], os.environ.get("STREAMLIT_PASSWORD", "")
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # st.info(f"Password: {os.environ.get('STREAMLIT_PASSWORD', '')}")
    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False


if not check_password():
    st.stop()


home = st.Page("pages/home.py", title="Home")
fundamentals = st.Page("pages/fundamentals.py", title="Fundamental reading")
baseline_and_qa = st.Page("pages/baseline_and_qa.py", title="Baseline and QA")
advanced = st.Page("pages/advanced.py", title="Advanced reading")

pg = st.navigation([home, fundamentals, baseline_and_qa, advanced], position="top")

pg.run()
