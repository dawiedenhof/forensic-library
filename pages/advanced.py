import streamlit as st

# layout
st.set_page_config(layout="wide")

# header
st.write(
    "### This page contains documents documents with more specific information with regards to AML/CTF, data and other topics."
)

st.header("Anti Money Laundering Regulation (AMLR) :woman_judge:")
st.markdown(
    """

    [Regulation (EU) 2024/1624 (AMLR)](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ:L_202401624) is a directly
    applicable EU law that modernises and harmonises anti‑money‑laundering and counter‑terrorist‑financing (AML/CFT) rules
    across the internal market, converting many previous Directive obligations into uniform requirements for obliged entities.
    It expands the scope of regulated actors (notably crypto‑asset service providers, crowdfunding intermediaries, certain
    real‑estate and high‑value goods actors, investment‑migration operators and parts of the football sector), tightens
    beneficial‑ownership transparency, standardises customer‑due‑diligence and reporting, and grants the Commission and AMLA
    stronger powers on third‑country risk designations and technical standards.

    Main takeaways
    - **Broader scope and harmonisation:** many new categories of firms are captured and must apply directly applicable,
    Union‑wide AML/CFT rules, reducing national divergence and relying on central registers and AMLA/Commission technical
    standards.
    - **Operational obligations and prohibitions:** firms must implement documented group‑wide policies, appoint a compliance
    manager/officer, meet strict outsourcing and BO reporting timelines (typically 28 days), and comply with new prohibitions
    (no anonymous bank/crypto accounts) and thresholds (EUR 10 000 cash limit; deadlines for bearer‑share conversion).
    - **Third‑country and supervisory regime strengthened:** the Commission and AMLA can designate high‑risk/weak third countries
    and require enhanced due diligence or countermeasures; FIUs will use harmonised reporting/transaction templates and stricter
    response deadlines, so substantial process, IT and governance changes are required.
"""
)

with st.expander("Anti Money Laundering Regulation"):
    st.pdf(
        "pdfs/OJ_L_202401624_EN_TXT.pdf",
        height=860,
    )

st.header("Basel Committee on Banking Supervision (BCBS) 239  :classical_building:")
st.markdown(
    """
    The [Basel Committee on Banking Supervision (BCBS) 239)](https://https://www.bis.org/publ/bcbs239.pdf) provides principles for effective risk data aggregation
    and risk reporting to enhance banks' risk management practices. The principles aim to improve banks' ability to aggregate risk data
    accurately and timely, enabling better decision-making and risk oversight.

    Main takeaways
    - **Governance and infrastructure:** banks should establish strong governance frameworks and invest in robust IT infrastructure
    to support effective risk data aggregation and reporting.
    - **Data architecture and quality:** banks need to develop comprehensive data architectures that ensure data accuracy, completeness,
    timeliness, and integrity across the organization.
    - **Risk reporting practices:** banks should implement clear and consistent risk reporting practices that provide relevant,
    accurate, and timely information to senior management and the board.
    - **Supervisory review:** supervisors should assess banks' compliance with the principles and take appropriate actions to address
    deficiencies.
    """
)

with st.expander("BCBS239"):
    st.pdf(
        "pdfs/bcbs239.pdf",
        height=860,
    )
