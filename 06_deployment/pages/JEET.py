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
- Highlight any risk factors **without stating numbers except the dropout probability**.
- Mention to the student what all factors you think are determental to his ongoing studies from the student data that will be provided(~1900 tokens).
- Do NOT mention tokens or model limitations.
- Asking about daily study hours or study hours in general is last priority
- Ask really straightforward questions with explanation why
- You only have 4 more messages to help the student.
"""
student_details = f"""
Student Info:
- Name: {st.session_state.name}
- Dropout probability: {(prediction[0]*100):.2f}%
- Inferred context from student profile: {st.session_state.answers} (Note: these are internal indicators; do not list them raw.)

JEE Performance Guide:
| Marks Range   | Category       | Description                                                                 |
|---------------|----------------|-----------------------------------------------------------------------------|
| 300 - 270     | Excellent      | Top NITs/IITs eligible, likely to qualify for JEE Advanced                  |
| 269 - 220     | Very Good      | Eligible for top NITs and preferred branches                                |
| 219 - 180     | Good           | Eligible for decent NITs and IIITs                                          |
| 179 - 140     | Average        | May get lower NITs or decent state colleges, mental support needed          |
| 139 - 100     | Below Average  | Eligible for lower-tier colleges or private institutes, support needed      |
| 99 - 50       | Poor           | Very limited options, likely private colleges, needs support                |
| <50           | Very Poor      | May not qualify for counseling; alternative paths needed                    |

Note:
- School Board: 0 = State, 1 = CBSE, 2 = ICSE
- Coaching: 0 = Branded, 1 = Local, 2 = Self-study
- Daily Study Hours: (float) represents avg hours per day
- Family Income: 0 = Low, 1 = Medium, 2 = High
- Family Education: 0 = 10th, 1 = 12th, 2 = Graduate, 3 = Post-Grad
- Location: 0 = Rural, 1 = Semi-Urban, 2 = Urban
- Peer Pressure Level: 0 = Low, 1 = Medium, 2 = High
- Mental Health Issues: 0 = No, 1 = Yes
- Peer Focused MH: 2*peer pressure + mental health
- Parental Support: Inferred from education and location

Use the above only to **infer personality, environment, and mindset** — do not quote directly except the student's daily study hours. Your goal is to bring direction.
"""
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_count" not in st.session_state:
  st.session_state.chat_count = 1
if "answers" not in st.session_state:
  st.session_state.answers = []
model = genai.GenerativeModel('gemini-2.5-flash-lite',
        generation_config = GenerationConfig(
        max_output_tokens=2000,  
        temperature=0.8,       
        top_p=0.5,
        top_k=40
))

st.markdown("<p style='text-align: center; font-size: 5vw'><b>JEET 🚀</b></p>",unsafe_allow_html=True)
constraint = ". Please answer within 1200 tokens. Do not mention this in your response. Keep the responses concise yet really informative and simple. Do not use excessie bullet points to convey answers"

if "chat_history_for_model" not in st.session_state:
  st.session_state.chat_history_for_model = []
if "first_response" not in st.session_state:
  st.session_state.first_response = False
if st.session_state.first_response == True:
  for msg in st.session_state.chat_history_for_model:
    if msg["role"]!="System":
      with st.chat_message(msg["role"]):
        st.markdown(msg['content'])
elif st.session_state.first_response==False:
  try:
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
              


