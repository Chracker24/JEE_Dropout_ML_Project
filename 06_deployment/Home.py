import streamlit as st


if 'page' not in st.session_state:
  st.session_state.page = 'home'
st.set_page_config(
  page_title='JEE Dropout Predictor',
  page_icon="🎓",
  layout="wide",
  initial_sidebar_state="collapsed"
)
st.markdown("<h1 style='text-align: center;font-size:70px'>🚀MEET JEET🧠<br>A JEE & NEET Dropout Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;font-size:35px'> Predicts the likelihood of students dropping out of JEE or NEET based on academic and socio-economic factors <br></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;font-size:20px'> Welcome to a place where we listen but we dont judge! <br>This ML model has been trained on data from real students - their marks, mindsets and meltdowns. Whether you're cruising through Class 12 or barely crawling past mock tests, we're here to give you a reality check - <b><i>gently</i></b> (well, mostly 😅). <br><br> 👉 Feed in your facts. <br>🧠 Let the model think.  <br>🔮 Get your future... predicted.<br><br><b>No pressure. No judgment.<br> Just probabilities</b></p>", unsafe_allow_html=True)
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #e63946;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([1, 1, 1,1,1])
with col3:
    if st.button("🔥 Predict Now"):
        st.success("Please open the Data Page from the sidebar")
                
        