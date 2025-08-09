from langchain_groq import ChatGroq
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
st.set_page_config(page_title='Email Generator',layout='centered',page_icon=':MAIL:')
st.title("Email Generator based on the given skills to employer")

# os.environ['GROQ_API_KEY']=os.getenv('GROQ_API_KEY')
os.environ['GROQ_API_KEY'] = st.secrets['GROQ_API_KEY']
st.text('Enter your skill and name(optional) we will cerate your MAIL for the same')

st.text('Skill:')
skills=st.text_input(label='Your skills',label_visibility='collapsed')
st.text('Name:')
name=st.text_input('Your Name(optional)',label_visibility='collapsed')
if not skills.strip():
    st.stop()
submit_button = st.button('Submit')
llm = ChatGroq(model='llama-3.1-8b-instant')
if submit_button:
    prompt = ("""
                your are best chatbot avaiable for the generation of the email just give the
              email text only like subject and main body not the the preamble
              and use the name {name} if given else give the general and use
              the best way to find the given skills importance and give specific
              thing which is required for the employer to consider the mail as first and best impression
              according to the skills given : {skills}
              generate the email in email format like the employee who want to showcase his talent to the employer
              with best regards 
              Do not provide a preamble.
             make creative as you can so that it doesnt look like the coded message
            """)
    final_prompt = PromptTemplate(
        input_variables=['skills'],
        template=prompt
    )
    import re

    chain = LLMChain(llm=llm,prompt=final_prompt)
    response = chain.invoke({'skills':skills,'name':name})
    st.success(response['text'])