from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage , AIMessage
#chat templete
chat_template= ChatPromptTemplate([
    ('system','you are a  helpful customer suppoet agent'),
    MessagesPlaceholder(variable_name='chat_history'), #every history is stored in this
    ('human','{query}')
])
#load chat history

chat_history=[]
with open('chat_history.txt') as f:
    chat_history.append(f.readlines())


print(chat_history)
#create prompt

prompt=chat_template.invoke({'chat_history':chat_history,'query':"Where is my refund"})

print(prompt)