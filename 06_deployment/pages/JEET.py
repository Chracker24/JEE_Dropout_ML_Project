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

if "messages" not in st.session_state:
    st.session_state.messages = []

if "answers" not in st.session_state:
  st.session_state.answers = []
st.write(st.session_state.answers)
model = genai.GenerativeModel('gemini-1.5-flash')

generation_config = GenerationConfig(
  max_output_tokens=200,  
  temperature=0.7,       
  top_p=0.7,
  top_k=40
)

st.title("Gemini Chat with Max Output Control")

try:
  response = model.generate_content(
    f"You are a chatbot for a model (RandomForestClassifier) that predicts the probability that the student will dropout from JEE or NEET. The student's name is {st.session_state.name} Please remind the student that the model can be wrong and is only a way for the student to have a second thought in order to prevent and too much work into a field they might ultimately not go to. Be Friendly, Calm, Understanding and offer ways and introspective points to the student to understand. The responses of the student is as follows in the list {(st.session_state.answers)} in the list format [score,school_board,class12,attempts,coaching_institute,daily_study_hours,family_income,family_education,location_type,peer_pressure_level,mental_health_issues,peer_focused_mh,parental_support] (Do not specify this list in your answer). The School Board is : 0 for State, 1 for CBSE, 2 for ICSE. coaching institute is 0 for Branded, 1 for local and 2 for Self-study students. family_income is 0 for Low, 1 for Medium and 2 for High. family_education is 0 for 10th pass, 1 for 12th pass, 2 for Graduate, 3 for Post-Graduate. location_type is 0 for Rural, 1 for Semi-Urban and 2 for Urban. peer_pressure_level is 0 for Low, 1 for Medium and 2 for High. mental_health_issues is 0 for No and 1 for Yes. peer_focused_mh is 2*peer_pressure_level + mental_health_issues and parental_support is a mix between family_education, location_type. Find if you can find any really standing out feature in the list, and the student has a {(prediction[0]*100):.2f}% of dropping out. Remind the student that he has 2 chances to interact with you and then the chat will be stopped.Please answer within 200 words",
    generation_config=generation_config, 
    stream=False 
  )
  response_text = ""
  if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
    response_text = response.candidates[0].content.parts[0].text
  else:
    if response.prompt_feedback and response.prompt_feedback.block_reason:
        response_text = f"Response blocked due to: {response.prompt_feedback.block_reason.name}"
    else:
        response_text = "No response generated or unexpected response structure."

  st.session_state.messages.append({"role": "assistant", "content": response_text})
  with st.chat_message("assistant"):
    st.markdown(response_text)

except Exception as e:
  st.error(f"An error occurred: {e}")
  st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})
  with st.chat_message("assistant"):
    st.markdown(f"Error: {e}")


if user_input := st.chat_input("Chat with JEET"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    for i in range(2):
      chat_history_for_model = []
      for msg in st.session_state.messages:
        role = "user" if msg["role"] == "user" else "model"
        chat_history_for_model.append({"role": role, "parts": [{"text": msg["content"]}]})


      try:
        response = model.generate_content(
          chat_history_for_model,
          generation_config=generation_config, 
          stream=False 
        )

        with st.spinner("JEET is writing his JEE exam"):
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

                st.session_state.messages.append({"role": "assistant", "content": response_text})
                with st.chat_message("assistant"):
                  st.markdown(response_text)

      except Exception as e:
        st.error(f"An error occurred: {e}")
        st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})
        with st.chat_message("assistant"):
          st.markdown(f"Error: {e}")

        
        
