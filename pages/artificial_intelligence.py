import streamlit as st

# layout
st.set_page_config(layout="wide")

st.write(
    "### This page contains documents related to (generative) artificial intelligence in a FEC context."
)

st.header("DNB - General principles for the use of AI in the FSI  :six:")

st.markdown(
    """
    ## Summary

    The paper [DNB — General principles for the use of Artificial Intelligence
    in the financial sector](https://www.dnb.nl/media/voffsric/general-principles-for-the-use-of-artificial-intelligence-in-the-financial-sector.pdf)
    explains that Artificial Intelligence (AI), defined as "the theory and
    development of computer systems able to perform tasks that traditionally
    have required human intelligence", is increasingly embedded in the Dutch
    financial sector. It reviews AI's long research history and the marked
    acceleration since about 2010 driven by greater computing power, richer
    data and wider Internet of Things connectivity. The paper surveys current
    applications across front-office and back-office functions, including
    chatbots, identity verification for onboarding, transaction analytics, AML
    surveillance, fraud detection, pricing and underwriting, automated
    document analysis, customer relationship management, risk and portfolio
    management, trading execution and operational automation. It anticipates
    innovations ranging from efficiency gains to new products and services in
    retail and wholesale banking, insurance, payments, asset management and
    market infrastructure. Given finance's public-interest role, potential
    reputational and systemic effects, interconnectivity and sensitive data
    environments, DNB proposes six general principles grouped under
    Soundness, Accountability, Fairness, Ethics, Skills and Transparency. Firms
    should ensure reliable, explainable and resilient AI systems, embed
    governance and accountability, mitigate bias and ethical harms, develop
    skills, and maintain robust data, validation and documentation practices.

    ## Main takeaways

    1. The SAFEST framework sets six pillars of expectation for responsible AI
    use.
    2. AI is already pervasive and can create conduct, operational and systemic
    risk if not well governed.
    3. Firms must strengthen governance, model-risk controls, data quality,
    explainability, vendor oversight and skills.
    """
)

with st.expander("General principles for AI in FSI"):
    st.pdf(
        "pdfs/general-principles-for-the-use-of-artificial-intelligence-in-the-financial-sector.pdf",
        height=860,
    )

st.divider()
