import streamlit as st

#layout
st.set_page_config(layout="wide")

# header
st.title("Forensic :blue[Analytics]:green[.] FEC Reading Guide")

# introduction
st.markdown("""
    You can use the this reading guide to reference relevant literature on AML and CTF topics.
    The documents are groupd into the following categories:
    - **Fundamentals:** the basics to our domain.
        - Guideline on the WWFT and SW
        - From recovery to balance
    - **Baselines and Q&A:** additions to the basics based on newer publications.
        - DNB Wwft Q&As and Good Practices
        - NVB Industry Baseline Client Data Actualisation
    - **Advanced reading:** more in-depth publications on specific topics.
        - Anit-Money Laudering Regulation (AMLR)
            
    Navigate to these sections via the buttons at the top of this page. 

    While it's a good idea to familiarize yourself with at least the fundamentals, these documents
    can be quite lengthy. To get a quick answer to a pressing question, you can consult these documents
    with the help of [Headstart](https://headstart.deloitte.nl). Use the prompt template below to get 
    the answers you're looking for:
    ```
    ***** Context *****
    I am a consultant in the FEC domain who has received a guideline from the regulator and I need assistance
    in analysing the document.
            
    ***** Task *****
    Your task is to analyse the provided document and answer the question below based on its content.
            
    ***** Input format *****
    The document is a PDF with with varying structure.
            
    ***** Instructions *****
    1. Carefully read and understand the document.
    2. Extract relevant information that directly addresses the question.
    3. Provide a clear and concise answer based on the document's content.
    4. Provide references to specific sections or pages in the document to support your answer.
    5. If the document does not contain sufficient information to answer the question, respond accordingly.
    6. Do not make up information that is not present in the document.
            
    ***** Output format *****
    Provide answer with a maximun length of 200 words. If applicable, include references to specific 
    sections or pages in the document.
    ```    
    """)

st.divider()

st.markdown("""
    #### Contact
    Send a message to Daan Wiedenhof (dwiedenhof@deloitte.nl) for questions or additions.
""")