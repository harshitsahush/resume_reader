import streamlit as st
from io import StringIO
from utils import *

st.title("Resume Reader")
st.header("Built using Streamlit and Groq")
doc = st.file_uploader("Please upload the resume here.", accept_multiple_files=True)
option = st.selectbox("Select the files type", (".pdf", ".docx"))
submit = st.button("Process")

if(submit):
    if(doc):
        if(option == ".pdf"):
            text = get_pdf_text(doc)
        else:
            text = get_docx_text(doc)

        response = query_response(text)
        st.success(response)
        
    else:
        st.error("Please upload a file!!!")