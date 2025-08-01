import streamlit as st
import google.generativeai as genai
from google.generativeai.types import GenerationConfig
import time

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
if "prediction" not in st.session_state:
    st.error("Prediction not set. Go back to the previous page.")
    st.stop()
else:
    prediction = st.session_state.prediction
system_prompt=f"""
You are JEET, a friendly, calm, introspective chatbot who helps students reflect on their likelihood of dropping out of JEE/NEET. You base your support on model predictions and user responses.

Guidelines:
- Speak kindly and clearly.
- Encourage self-reflection.
- Offer emotional and practical support.
- Highlight any risk factors **without stating numbers except the dropout probability**.
- Keep responses concise but specific (~900 tokens).
- Do NOT mention tokens or model limitations.
- Ask really straightforward questions that prompts the student's answer to be indicative of problems faced
- You only have 4 more messages to help the student.
"""
student_details = f"""
Student Info:
- Name: {st.session_state.name}
- Dropout probability: {(prediction[0]*100):.2f}%
- Student answers (inferred context, do NOT show raw numbers): {st.session_state.answers} in the list format [score,school_board,class12,attempts,coaching_institute,daily_study_hours,family_income,family_education,location_type,peer_pressure_level,mental_health_issues,peer_focused_mh,parental_support] (Do not specify this list in your answer).
-The School Board is : 0 for State, 1 for CBSE, 2 for ICSE.
-coaching institute is 0 for Branded, 1 for local and 2 for Self-study students.
-family_income is 0 for Low, 1 for Medium and 2 for High.
-family_education is 0 for 10th pass, 1 for 12th pass, 2 for Graduate, 3 for Post-Graduate.
-location_type is 0 for Rural, 1 for Semi-Urban and 2 for Urban.
-peer_pressure_level is 0 for Low, 1 for Medium and 2 for High.
-mental_health_issues is 0 for No and 1 for Yes.
-peer_focused_mh is 2*peer_pressure_level + mental_health_issues
-parental_support is a mix between family_education, location_type.
"""
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_count" not in st.session_state:
  st.session_state.chat_count = 1
if "answers" not in st.session_state:
  st.session_state.answers = []
st.write(st.session_state.answers)
model = genai.GenerativeModel('gemini-2.5-flash-lite',
        generation_config = GenerationConfig(
        max_output_tokens=1000,  
        temperature=0.8,       
        top_p=0.5,
        top_k=40
))

st.title("Gemini Chat with Max Output Control")
constraint = ". Please answer within 700 tokens. Do not mention this in your response. Keep the responses concise yet really informative and simple. Do not use excessie bullet points to convey answers"

if "chat_history_for_model" not in st.session_state:
  st.session_state.chat_history_for_model = []
if "first_response" not in st.session_state:
  st.session_state.first_response = False
st.write(st.session_state.first_response)
if st.session_state.first_response == True:
  st.write("lol")
  for msg in st.session_state.chat_history_for_model:
    with st.chat_message(msg["role"]):
      if msg["role"]!="System":
        st.markdown(msg["content"])
elif st.session_state.first_response==False:
  try:
    st.write("its here")
    if "chat" not in st.session_state:
      st.session_state.chat = model.start_chat(history=[{"role":"user", "parts":[system_prompt]}])
    st.session_state.chat_history_for_model.append({"role":"System","content":system_prompt})
    response = st.session_state.chat.send_message(student_details)
    response_text = ""
    if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
      response_text = response.candidates[0].content.parts[0].text
    else:
      if response.prompt_feedback and response.prompt_feedback.block_reason:
          response_text = f"Response blocked due to: {response.prompt_feedback.block_reason.name}"
      else:
          response_text = "No response generated or unexpected response structure."

    st.session_state.chat_history_for_model.append({"role": 'assistant', "content": response_text})
    st.session_state.first_response = True
    with st.chat_message("assistant"):
      st.markdown(response_text)

  except Exception as e:
    st.error(f"An error occurred: {e}")
    st.session_state.chat_history_for_model.append({"role": "assistant", "content": f"Error: {e}"})
    with st.chat_message("assistant"):
      st.markdown(f"Error: {e}")
      
if user_input := st.chat_input("Chat with JEET"):
  st.session_state.chat_count+=1
  st.write(st.session_state.chat_count)
  if st.session_state.chat_count>5:
    st.write("You have exhausted your talking chances")
    st.write("I hope you had a Fun Time Talking to me")
    st.stop()
  up_user_input = user_input + constraint
  st.session_state.chat_history_for_model.append({"role": "user", "content": user_input})
  with st.chat_message("user"):
      st.markdown(user_input)


  response = st.session_state.chat.send_message(up_user_input)
    
  with st.spinner("JEET is coming from his prep"):
    time.sleep(2)
    with st.spinner("JEET is thinking"):
      time.sleep(3)
      with st.spinner("Finding optimum response"):
        time.sleep(3)
        with st.spinner("Finding a 'proper' way to say it"):
          time.sleep(4)
          response_text = ""
          if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
            response_text = response.candidates[0].content.parts[0].text
          else:
              if response.prompt_feedback and response.prompt_feedback.block_reason:
                response_text = f"Response blocked due to: {response.prompt_feedback.block_reason.name}"
              else:
                response_text = "No response generated or unexpected response structure."

          with st.chat_message("assistant"):
              st.session_state.chat_history_for_model.append({"role": 'assistant', "content": response_text}) 
              st.markdown(response_text)  
              


