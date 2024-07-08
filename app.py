import streamlit as st
from utils import *

st.title("Resume Reader")
st.header("Built using Streamlit and Groq")
doc = st.file_uploader("Please upload the resume here.", accept_multiple_files=False)
option = st.selectbox("What is the filetype?", ("pdf", "docx"), placeholder = "Select filetype...")
submit = st.button("Process")

if(submit):
    if(doc):
        if(option == "pdf"):
            text = get_pdf_text(doc)
        else:
            #if docx, need to store in local
            store_in_local(doc)
            path = ""
            text = get_docx_text(path)
        
        #create chat completion
        #get response

    else:
        st.error("Please upload a file!!!")