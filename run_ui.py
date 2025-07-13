import streamlit as st
import requests

st.set_page_config(page_title="Financial QueryBot", layout="wide")
st.title("💼 Financial Report Analyzer + QueryBot")
st.markdown("Ask any question related to your uploaded 10-K, tax return, balance sheet, or contract.")

question = st.text_input("❓ What do you want to know?")
if st.button("🔍 Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        try:
            response = requests.post("http://localhost:8000/ask", json={"question": question})
            answer = response.json().get("answer", "No answer returned.")
            st.success(answer)
        except Exception as e:
            st.error(f"Failed to contact backend: {e}")
