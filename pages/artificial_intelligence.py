import streamlit as st

# layout
st.set_page_config(layout="wide")

st.write(
    "### This page contains documents related to (generative) artificial intelligence in a FEC context."
)

st.header("DNB - General principles for the use of AI in the FSI  :six:")

st.markdown(
    """
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

st.header("DNB - Technical Model Documentation  :robot:")

st.markdown(
    """
    The NVB Industry Baseline for Technical Model Documentation
    ([20240625-nvb-industry-baseline-tmd-en.pdf](https://www.nvb.nl/media/hs5d30c5/20240625-nvb-industry-baseline-tmd-en.pdf))
    sets out the types of information Dutch banks should record when developing
    and operating advanced analytics, AI and machine‑learning models within the
    AML/CFT framework. Its purpose is to ensure transparency, accountability and
    trustworthiness across the model lifecycle: governance, conceptual and
    technical design, data provenance and processing, development and
    validation, explainability, risk considerations, monitoring, maintenance and
    implementation. The Baseline stresses that models may be used in onboarding,
    ongoing due diligence and transaction monitoring, and describes a practical
    use case combining rule‑based systems with machine learning to reduce false
    positives while retaining coverage of reportable cases. The document
    references the Wwft, GDPR, DNB guidance, Wolfsberg principles and the EU AI
    Act as relevant regulatory context. Key expectations include defined
    governance roles and approvals, detailed data lineage and preprocessing
    records, clear target and feature definitions, performance metrics and
    stability tests, explainability at global and local levels, incident response
    plans, retraining criteria and comprehensive documentation to support
    validation, audits and supervisory engagement.

    1. Model lifecycle coverage: document governance, design, data, validation,
    monitoring, retraining and implementation for each model.

    2. Explainability and validation: require clear target/feature definitions,
    measurable performance metrics, stability tests and interpretable outputs.

    3. Regulatory alignment and accountability: ensure compliance with Wwft,
    GDPR and forthcoming AI Act requirements, with defined roles and audit
    trails.
    """
)

with st.expander("General principles for AI in FSI"):
    st.pdf(
        "pdfs/20240625-nvb-industry-baseline-tmd-en.pdf",
        height=620,
    )
