import pandas as pd
import streamlit as st

# layout
st.set_page_config(layout="wide")

st.write(
    "### This page contains documents related to AML/CTF industry baselines and QA sessions."
)

st.header("DNB Q&As and Good Practices Q&A:question:")
st.markdown(
    """
    The [Q&A and good practices](https://www.dnb.nl/media/z0upf3bv/dnb-wwft-qas-and-good-practices.pdf) \
    sets out De Nederlandsche Bank’s proposed good practices to help obliged entities implement the Netherlands’ WWFT \
            (AML/CFT) requirements by clarifying supervisory expectations and offering practical measures to prevent, \
            detect and report money‑laundering and terrorist financing. It covers the full AML/CFT control cycle and \
            emphasises a risk‑based approach, the effective use of data and technology, robust governance and cooperation \
            with the FIU and supervisors.

    Key topics covered include:

    - Enterprise‑wide risk assessment and risk‑based CDD: customer acceptance, onboarding, beneficial‑ownership checks, \
    enhanced due diligence and ongoing monitoring.
    - Detection and monitoring: transaction monitoring, alert generation and tuning, use of data, analytics and automation, \
    and model validation.
    - Governance and quality assurance: policies, roles and board oversight, independent testing, record‑keeping, training \
    and culture.
    - Reporting and external cooperation: suspicious transaction reporting to the FIU, information sharing, outsourcing \
    controls and engagement with supervisors.
"""
)

with st.expander("DNB Wwft Q&As and Good Practices"):
    st.pdf(
        "pdfs/dnb-wwft-qas-and-good-practices.pdf",
        height=620,
    )

st.divider()

st.header("NVB Industry Baseline Client Data Actualisation :guitar:")
st.markdown(
    """
    The [NVB standards](https://www.nvb.nl/media/5706/nvb-standaarden_5_client-data-actualisation_30-5.pdf)
    set out recommended practices for banks to keep client data
    current and accurate, supporting compliance with AML/CFT obligations and sound
    client relationship management. They establish a risk‑based framework for the
    timing and triggers for data updates, verification methods, governance and the
    treatment of non‑responsive or changed clients.

    Key topics covered include:

    - **Risk‑based actualisation:** Principles for periodic reviews, event‑driven
    triggers (e.g. material transactions, changes in ownership or circumstance)
    and heightened procedures for higher‑risk clients.
    - **Processes and verification:** Accepted data sources and documentary or
    electronic verification methods, use of third‑party data and digital channels,
    and rules for recording confirmed changes.
    - **Roles, escalation and decision‑making:** Responsibilities across front office,
    compliance/KYC teams and senior management, plus escalation paths for
    ambiguous or high‑risk findings.
    - **Controls and auditability:** Documentation, retention, quality assurance,
    follow‑up for unresponsive clients (account restrictions or closure) and
    oversight to ensure consistent application.
"""
)

with st.expander("NVB Industry Baseline Client Data Actualisation"):
    st.pdf(
        "pdfs/nvb-standaarden_5_client-data-actualisation_30-5.pdf",
        height=620,
    )

st.divider()

st.header("NVB Industry Baseline Client Data Actualisation :abacus:")
st.markdown(
    """
    The [NVB Industry Baseline on Models in alert and event generation](https://www.nvb.nl/media/ophlutr2/nvb-baseline-models-in-alert-and-event-generation-en.pdf)
    offers practical guidance for banks to use models (rule‑based and advanced) in AML/CFT alert
    and event generation. It promotes a risk‑based approach to detect ML/TF, supports transition
    from simple rules to advanced models, and stresses the need for ongoing validation, data
    governance and proportionate oversight to ensure reliable, explainable and fair use.

    Key topics covered include:

    - **Risk‑based application:** Principles for tuning model sensitivity, bucketing outputs
    (e.g. low/medium/high) and linking buckets to differentiated operational responses
    (automated handling, risk‑differentiated review, comprehensive review).
    - **Data and performance:** Expectations for sourcing, cleansing and regularly actualising
    client and transaction data; quantitative performance metrics (precision/recall), pre‑implementation
    testing and continuous monitoring/back‑testing.
    - **Governance and explainability:** Clear roles and responsibilities across model owners,
    first‑line users, AML/CFT compliance and model‑risk functions; requirements for transparency,
    explainability and safeguards against biased outcomes.
    - **Controls, validation and auditability:** Independent validation, change control,
    documentation standards, reproducible decision records and evidential trails to demonstrate controlled,
    responsible deployment and regulatory compliance.
"""
)

with st.expander("NVB Industry Baseline Model In Alert and Event Generation"):
    st.pdf(
        "pdfs/nvb-baseline-models-in-alert-and-event-generation-en.pdf",
        height=620,
    )

st.divider()
