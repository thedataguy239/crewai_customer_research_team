import os, streamlit as st

# Boot the local LLM server first
from local_llm import launch_server, get_base_url
os.environ["OPENAI_API_BASE"] = get_base_url()
os.environ["OPENAI_API_KEY"] = "sk-local"  # dummy
launch_server()

from crew_setup import build_crew

st.set_page_config(page_title="Customer Intel Agent", page_icon="👔")
st.title("👔 Customer Intel Agent (CrewAI + Local LLM)")
st.toast("Running FREE local LLM via llama.cpp (CPU) — first query may be slow.")

st.markdown(
    """
Type a company **name or domain**.  
The app will:
1) Look up your CRM (local Excel),  
2) Analyze mock account data if found, and  
3) Research the public web for recent intel.  
    """
)

company = st.text_input("Company name or domain", "Acme Corp")
if st.button("Run analysis", type="primary"):
    with st.spinner("Running agents..."):
        crew = build_crew(company)
        result = crew.kickoff()
    st.subheader("Output")
    if hasattr(result, "raw"):
        st.markdown(result.raw if isinstance(result.raw, str) else str(result.raw))
    else:
        st.markdown(str(result))

st.divider()
st.caption("Powered by CrewAI • Streamlit • llama.cpp • Pandas • DuckDuckGo/Tavily")
