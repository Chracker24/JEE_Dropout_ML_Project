import streamlit as st
import joblib
import time
import pandas as pd
import numpy as np
st.set_page_config(
  layout="centered"
)
if "page" not in st.session_state:
  st.session_state.page = 0
if "answers" not in st.session_state:
  st.session_state.answers = []
if "name" not in st.session_state:
  st.session_state.name = ""  
if "prediction" not in st.session_state:
  st.session_state.prediction = None
boo=False
st.title("Questionaire")
st.caption("the models have been woken from deep slumber, and are ready to predict your future.")

name = st.text_input("What is your name")
st.session_state.name = name
score = st.number_input("What was your JEE/NEET score?")
school= st.selectbox("What board was your school affiliated to?", ["State","CBSE","ICSE"])
lf = lambda x : 0 if x == "State" else (1 if x == "CBSE" else 2)
school_board = lf(school)
class12 = st.number_input("What was your Class 12 percentage overall?")
attempts = st.number_input("How many times have you attemped JEE/NEET?", min_value=0, max_value=10)
coaching = st.selectbox("Are you enrolled in any coaching classes", ["Yes", "No"])
if coaching == "Yes":
  coaching_name = st.text_input("What is the name of your coaching institute?")
cf = lambda x : 2 if coaching=="No" else (0 if x in [
    "Allen",
    "Aakash",
    "Aakash Byju's",
    "Aakash BYJU'S",
    "Byju's",
    "BYJU'S",
    "FIITJEE",
    "Resonance",
    "Motion Education",
    "PACE IIT & Medical",
    "T.I.M.E.",
    "Xylem",
    "XYLEM"
  ] else 1)
coaching_institute = cf(coaching_name)
daily_study_hours = st.number_input("How many hours do you study daily?", min_value=0, max_value=24)
income = st.slider("What is your family's monthly income?", max_value=1000000, step=10000)
ff = lambda x : 0 if x < 80000 else(1 if x <250000 else 2)
family_income = ff(income)
edu = st.selectbox("What is the highest level of education your parents have completed?", ["10th", "12th", "Graduation", "Post Graduation (Masters, PhD)"])
ef = lambda x : 0 if x=="10th" else(1 if x=="12th" else (2 if x=="Graduation" else 3))
family_education = ef(edu)
location = st.selectbox("How would you describe where you live?", ["Rural","Semi-Urban","Urban"])
locationf = lambda x : 0 if x=="Rural" else(1 if x=="Semi-Urban" else 2)
location_type = locationf(location)
compare = st.selectbox("How often do you compare yourself with others?", ["Never", "Sometimes", "Often"])
comparef = lambda x : 0 if x=="Never" else(1 if x=="Sometimes" else 2)
comparison = comparef(compare)
mimic = st.selectbox("How hard do you find youself trying to replicate other's study patterns?", ["Never", "Sometimes", "Often"])
mimicf = lambda x : 0 if x=="Never" else(1 if x=="Sometimes" else 2)
mimic_pattern = mimicf(mimic)
stressed = st.selectbox("How much stressed do you feel when your friends perform better than you", ["None", "a Bit stressed","A lot"])
stressf = lambda x : 0 if x=="None" else(1 if x=="A Bit stressed" else 2) 
stress_comparison = stressf(stressed)
peer_pressure_level = round((comparison + mimic_pattern + stress_comparison)/3) 
over = st.selectbox("Over the past 2 months, How overwhelmed or overloaded by academic pressure or studies have you felt?", ["None","A bit overwhelmed", "Often"])
overf = lambda x:0 if x=="None" else (1 if x=="a bit overwhelmbed" else 2)
overwhelmed = overf(over)
conc = st.selectbox("How often do you find it difficult to concentrate on your studies?", ["Never", "Sometimes", "Often"])
conf = lambda x : 0 if x=="Never" else(1 if x=="Sometimes" else 2)
concentration = conf(conc)
drain = st.selectbox("How often do you feel anxious or emotionally and mentally drained", ["Never", "Sometimes", "Often"])
drainf = lambda x : 0 if x=="Never" else(1 if x=="Sometimes" else 2)
drained = drainf(drain)
mental_health_issues = round((overwhelmed + concentration + drained)/3)
parental_support = 0.30*daily_study_hours + 0.20*family_education + 0.05*coaching_institute
peer_focused_mh = 2*peer_pressure_level + mental_health_issues 
choice = st.checkbox("Ready to predict?")
if choice:
  boo =True
  with st.spinner("Thanks for entering the data, Waking up the models (again...)"):
    model1 = joblib.load("../05_models/Model_JEET.pkl") 
    pred=model1.predict_proba(np.array([score,school_board,class12,attempts,coaching_institute,daily_study_hours,family_income,family_education,location_type,peer_pressure_level,mental_health_issues,peer_focused_mh,parental_support]).reshape(1,-1))
    st.session_state.prediction = pred[:,1]
    st.session_state.answers = [score,school_board,class12,attempts,coaching_institute,daily_study_hours,family_income,family_education,location_type,peer_pressure_level,mental_health_issues,peer_focused_mh,parental_support]
    st.write(st.session_state.answers)
    time.sleep(3)
    if boo:
      
      if pred[:,1] < 0.66 :
        if score!=0 or class12!=0:
          st.markdown("<p style='font-size:2vw; text-align:center'>The Model God has predicted that you will...</p>", unsafe_allow_html=True)
          time.sleep(3)
          st.markdown("<p style='font-size:4vw; text-align:center; color:green'><b>NOT DROPOUT</b></p>", unsafe_allow_html=True)
          time.sleep(1)
          st.markdown("<p style='font-size:1vw; text-align:center'>Dropout? You? Never. Now go submit that assignment you forgot",unsafe_allow_html=True)
        else:
          st.markdown("<p style='font-size:2vw; text-align:center'>The Model God has predicted that you will...</p>", unsafe_allow_html=True) 
          time.sleep(3)
          st.markdown("<p style='font-size:4vw; text-align:center; color:red'><b>DROPOUT</b></p>", unsafe_allow_html=True)
          time.sleep(1)
          st.markdown("<p style='font-size:2vw; text-align:center'>The Model God has forsaken you. Dropout is imminent. May your side hustle prosper</p>", unsafe_allow_html=True)
          time.sleep(1)
          st.markdown(f"<p style='font-size:3vw; text-align:center'>You have a <b style='color:red'>{float(pred[:,1]*100):.2f}%</b> chance of dropping out</p>", unsafe_allow_html=True)
      else:
          st.markdown("<p style='font-size:2vw; text-align:center'>The Model God has predicted that you will...</p>", unsafe_allow_html=True) 
          time.sleep(3)
          st.markdown("<p style='font-size:4vw; text-align:center; color:red'><b>DROPOUT</b></p>", unsafe_allow_html=True)
          time.sleep(1)
          st.markdown("<p style='font-size:2vw; text-align:center'>The Model God has forsaken you. Dropout is imminent. May your side hustle prosper</p>", unsafe_allow_html=True)
          time.sleep(1)
          st.markdown(f"<p style='font-size:3vw; text-align:center'>You have a <b style='color:red'>{float(pred[:,1]*100):.2f}%</b> chance of dropping out</p>", unsafe_allow_html=True)
st.write(st.session_state.answers)