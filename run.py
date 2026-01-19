import streamlit as st
import os
from dotenv import load_dotenv

from src.llm import get_llm
from src.parser import parse_response
from src.zipper import create_zip

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.set_page_config(page_title="Automated Website Maker", page_icon="😋")
st.title("🌐 Automated Website Maker")

prompt = st.text_area("Describe the website you want")

if st.button("Generate Website"):
    if not prompt.strip():
        st.warning("Please enter a description")
        st.stop()

    messages = [
        (
            "system",
            """
Generate ONLY frontend code.

Strict format:
-html-
HTML CODE
-css-
CSS CODE
-js-
JS CODE
"""
        ),
        ("user", prompt)
    ]

    #try:
    
    llm = get_llm()
    response = llm.invoke(messages)
    html, css, js = parse_response(response.content)
    zip_data = create_zip(html, css, js)

    st.download_button(
        "⬇️ Download Website",
        data=zip_data,
        file_name="website.zip",
        mime="application/zip"
        )
    st.success("Website generated successfully!")

    #except Exception:
     #   st.error("Something went wrong. Please try again.")
