import streamlit as st
from llm_helper import get_ai_responses

# setting browser title
st.set_page_config(page_title="Talent Scout AI Hiring Assistant",page_icon="🤖")

# app title
st.title("🤖 Talent Scout AI Hiring Assistant")

# specifying instructions for gemini model
system_prompt="""
You are the Hiring Assistant for 'TalentScout', a tech recruitment agency.
Your goal is to screen candidates efficiently.

STRICT PROCESS:
1. GREETING: Briefly greet the user and explain you are here to screen them.
2. INFO GATHERING: Ask for these details ONE BY ONE. Wait for the user to answer before asking the next:
   - Full Name
   - Email Address
   - Years of Experience
   - Desired Position
   - Tech Stack (Languages/Frameworks)
3. TECHNICAL SCREENING: Once you have the Tech Stack, generate 3 relevant technical questions. Ask them ONE BY ONE.
4. CLOSING: Thank them and say a recruiter will be in touch.

BEHAVIOR:
- Be professional but friendly.
- If the user asks off-topic questions (like "What is the weather?"), politely refuse and return to the interview.
- Keep responses short (under 50 words) unless asking a technical question.
"""
# Sidebar reset button
with st.sidebar:
    if st.button("Reset Interview"):
        st.session_state.messages = [{"role": "system", "content": system_prompt}]
        st.rerun()

# Intialize server memory for messages 
# Ensuring streamlit remebers messages despite reruns
if "messages" not in st.session_state:
    st.session_state.messages=[
        {"role":"system", "content":system_prompt}
    ]
    # triggering intial greeting from AI
    with st.spinner("Intialising recruiter..."):
        first_greeting=get_ai_responses(st.session_state.messages)
    st.session_state.messages.append({"role":"model","content":first_greeting})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    if message["role"]!="system":
        with st.chat_message(message["role"]):
            st.write(message['content'])

# Accepting user input
user_input=st.chat_input("Type your response here...")

if user_input:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.write(user_input)
    # Append user message to session state
    st.session_state.messages.append({"role":"user","content":user_input})

    with st.spinner("Recruiter is typing..."):
        # getting AI response
        ai_reply = get_ai_responses(st.session_state.messages)
    
    # Display AI response on chat message container
    with st.chat_message("model"):
        st.write(ai_reply)
    # Append AI response to session state
    st.session_state.messages.append({"role":"model","content":ai_reply})