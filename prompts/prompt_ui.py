import streamlit as st
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key="YOUR_API_KEY"
)
 
st.title("Prompt UI")
prompt = st.text_input("Enter your prompt")

if prompt:
    response = llm.predict(prompt)
    st.write(response)

#template 
from langchain_core.prompts import PromptTemplate
prompt=PromptTemplate()
template=
input_variable=['Paper_input','style_input','lenght_input']

if st.button('summarise'):
    chain= template | model
    chain.invoke({
    'Paper_input':paper_input,
    'style_input':style_input,
    'lenght_input':lenght_input
    })

    st.write(result.content)