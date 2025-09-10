import streamlit as st
from crew_setup import build_crew

st.title("Customer Intel Agent (HF Space backend)")

company=st.text_input("Company name","Acme Corp")
if st.button("Run analysis"):
    crew=build_crew(company)
    result=crew.kickoff()
    st.write(result)
