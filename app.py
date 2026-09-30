import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="LegalEase", layout="centered")
st.title("LegalEase: AI Legal Document Generator")
st.write("Generate Employment Contracts, NDAs, Lease Agreements with Gemini 1.5 Pro")

doc_type = st.selectbox("Document Type", ["Employment Contract", "NDA", "Lease Agreement", "Service Agreement"])
parties = st.text_input("Parties Involved", placeholder="e.g., John Doe (Freelancer), ABC Corp (Client)")
terms = st.text_area("Terms (semicolon separated)", placeholder="e.g., Confidentiality; Payment 30 days; Term 12 months")
dates = st.date_input("Effective Date")

if st.button("Generate Document", type="primary"):
    prompt = f"Generate {doc_type} for {parties} terms {terms} date {dates}. Formal legal language."
    st.session_state['doc'] = prompt + "\n\n[Connect Gemini API Key for AI generation - gemini-1.5-pro]"

if 'doc' in st.session_state:
    edited = st.text_area("Preview & Edit", value=st.session_state['doc'], height=400)
    st.download_button("Download as TXT", edited, file_name="LegalEase.txt")
