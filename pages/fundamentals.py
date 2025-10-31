import streamlit as st
import pandas as pd

# layout
st.set_page_config(layout="wide")

st.write("### Hi there colleague, welcome to the Forensic Analytics reading guide.")

# col1, col2 = st.columns(2, border=True)


st.header("The WWFT bible :open_book:")
st.markdown(
    """
    The [DNB guideline on the Wwft and the Sanctions Act](https://www.dnb.nl/media/chqnfjjh/leidraad-wwft-sw-eng.pdf) requires \
    firms to adopt a risk‑based approach with strong KYC at onboarding and continuous monitoring throughout the client \
    relationship to prevent money laundering, terrorist financing and sanctions breaches. Controls must be proportionate, \
    documented and supported by governance and training.

    - **KYC and enhanced due diligence:** Conduct thorough customer due diligence at onboarding (identity, beneficial ownership, \
    purpose and intended activity), apply enhanced measures for PEPs, complex ownership structures and higher‑risk clients, and \
    ensure documentation and escalation paths for uncertain cases.
    - **Continuous monitoring and response:** Maintain transaction and behaviour monitoring to detect anomalies, update risk \
    profiles over time, file STRs with FIU‑Netherlands when warranted, and ensure systems, staff training and oversight keep \
    monitoring effective (outsourcing does not remove the firm’s responsibility).
"""
)

with st.expander("Guideline on the WWFT and SW"):
    st.pdf(
        "pdfs\leidraad-wwft-sw-eng.pdf",
        height=850,
    )

st.divider()

st.header("DNB updated guidelines :ok_hand:")
st.markdown(
    """
    From [Recovery to Balance](https://www.dnb.nl/media/mdgafi3a/from-recovery-to-balance.pdf) \
    outlines how organisations should move from crisis‑driven recovery to a sustainable, balanced \
    operating model that supports resilience, growth and stakeholder expectations. It emphasises strategic risk management \
    and digital transformation as the twin enablers of stability and adaptive capability.

    - **Risk‑based approach:** Identify, assess and prioritise risks across strategy, operations and supply chains, allocate \
    resources proportionately, and embed risk assessment into decision‑making, planning and stress‑testing to \
    ensure resilience and capital efficiency.
    - **Use of technology:** Leverage data analytics, automation and integrated dashboards for continuous monitoring \
    and early‑warning, adopt cloud and digital platforms for scalability, and ensure strong model governance, \
    data quality and cyber‑controls to make tech‑driven insights reliable and actionable.
"""
)

with st.expander("From recovery to balance"):
    st.pdf(
        "C:/Users/dwiedenhof/Documents/streamlit_template/Streamlit template/pdfs/from-recovery-to-balance.pdf",
        height=580,
    )

st.divider()
