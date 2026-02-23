import streamlit as st
from Langgraph_Backend import chatbot   
from langchain_core.messages import HumanMessage
import uuid

#-------------------------------Utility function----------------------------------------------
def generate_thread_id():
    thread_id=uuid.uuid4()
    return thread_id


def reset_chat():
    thread_id=generate_thread_id()
    st.session_state['thread_id']=thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history']=[]

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})

    if state is None:
        return []

    if 'messages' not in state.values:
        return []

    return state.values['messages']



# ============================================================
#                    LangGraph Configuration
# ============================================================
# thread_id uniquely identifies a conversation in LangGraph.
# Same thread_id  -> same conversation context
# Different thread_id -> new chat
# NOTE: This is NOT database persistence (no SQLite yet)

CONFIG = {'configurable': {'thread_id': 1}}


# ============================================================
#                    Session Setup (UI Memory)
# ============================================================
# Streamlit reruns the script after every user action.
# So we store messages in session_state to redraw chat UI.
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = [st.session_state['thread_id']]



        


#------------------------sidebar UI--------------------------------------------
st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.write('My Conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id']=thread_id
        messages = load_conversation(thread_id)

        temp_messages=[]

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            temp_messages.append({
            'role': role,
            'content': msg.content
    })



        st.session_state['message_history']=temp_messages

# ============================================================
#                    Chat History Rendering 
# ============================================================
# Display previous messages stored in UI memory
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])


# ============================================================
#                    User Input Box
# ============================================================
user_input = st.chat_input('Type here')


# ============================================================
#                    Message Processing
# ============================================================
if user_input:

    # ------------------ Store & Display User Message ------------------
    st.session_state['message_history'].append({
        'role': 'user',
        'content': user_input
    })

    with st.chat_message('user'):
        st.text(user_input)


    # ------------------ Run LangGraph (Full Response) ------------------
    # Executes the graph and updates conversation state
    # response = chatbot.invoke(
    #     {'messages': [HumanMessage(content=user_input)]},
    #     config={'configurable': {'thread_id': st.session_state['thread_id']}}
    # )

    # ai_message = response['messages'][-1].content


    # ------------------ Streaming Response (Typing Effect) ------------------
    # Streams tokens one-by-one from the LLM
    with st.chat_message('assistant'):
        ai_message = st.write_stream(
            message_chunk.content
            for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config={'configurable': {'thread_id': st.session_state['thread_id']}},
                stream_mode='messages'
            )
        )


    # ------------------ Save Assistant Message ------------------
    # So it appears again after Streamlit rerun
    st.session_state['message_history'].append({
        'role': 'assistant',
        'content': ai_message
    })
