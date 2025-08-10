# JEET : AI Powered JEE and NEET Dropout After Class 12 Prediction app

## Overview

**JEET** is a Machine Learning project designed to predict the likelihood of students dropping out after Class 12, focusing on those preparing for or appearing in the Join Entrance Examination (JEE) and/or National Entrance cum Eligibility Test (NEET) in India. BY analysing academic and socio-economic data, JEET helps educators, counselors, and students to identify at-risk indivuiduals for timely intervention.

## Structure
```
JEE_Dropout_ML_Project/
├── .gitignore
├── LICENSE
├── Plan.md
├── README.md
├── 01_Data/
│   ├── 01_raw/
│   │   └── JEE_Dropout_After_Class_12.csv
│   ├── 02_Cleaned and Engineered/
│   │   ├── Feature_Engineered.csv
│   │   └── JEE_Dropout_Cleaned.csv
│   └── 03_final/
│       └── JEE_Dropout_Final.csv
├── 02_Data Analysis/
│   ├── 01_Exploration.ipynb
│   ├── 02_Cleaning.ipynb
│   ├── 03_Feature_Engineering.ipynb
│   └── 04_Merging_Final.ipynb
├── 03_notebooks/
│   └── Prototypes_models.ipynb
├── 04_src/
│   ├── evaluation.py
│   └── jee_dropout_model.py
├── 05_models/
│   └── Model_JEET.pkl
├── 06_deployment/
│   ├── Home.py
│   ├── requirements.txt
│   ├── model/
│   │   └── JEET.pkl
│   └── pages/
│       └── Data.py
│       └── JEET.py
├── gitignore
├── LICENSE
└── README.md
```
## Features
 - Predicts dropout risk using student academic and socio-economic data
 - Handles imbalanced data with SMOTE for better accuracy
 - User-friendly web app built with Streamlit
 - Enables educators and students to take data-driiven actions

## Dataset
includes features such as 
 - Academic scores (Class 10, Class 12, JEE/NEET scores)
 - Attendance records
 - Socio-economic factors (family income, parent's education)
 - Target Labele: dropout status (Yes/No)

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com//Chracker24/JEE_Dropout_ML_Project.git
cd JEE_Dropout_ML_Project
```
### 2. **(Optional)** Create a virtual environment
```bash
python -m venv venv
source venv/Scripts/activate   #MacOS: venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage
1. Navigate to Home.py in 06_deployment
2. Run the Streamlit application using Bash
```bash
streamlit run Home.py
```
3. Input stuudent details via the web interface to get dropout risk predictions
4. Talk with Google Gemini powered JEET chatbot about your shortcomings and help 

## Methodology
 - Data Cleaning, encoding cateogorical variables, and feature scaling and engineering
 - Addressed class imbalance using SMOTE
 - Trained Random Forest Classifier as the main model
 - Evaluated with accuracy, precision, recall, F1-Score and ROC-AUC 
 - used SHAP for model interpretability

## Results
 - Achieved approximately **67%** accuracy
  - This is due to presence of leaky data that got removed and will be fixed in later iterations with better data
 - Nonetheless, Improved recall with data balancing
 - Important predictors : socio-economic status, peer pressure and mental health

## Future work and iterations
 - Incorporate psychological and motivational data
 - Explore advanced models (XGBoost, deep learning)
 - Add personalized intervention suggestions
 - Expand dataset for broader applicability and fix leaky data situation

## Tech Stack
 - Python, scikit-learn
 - imbalanced-learn (SMOTE, Pipeline)
 - pandas, numpy, seaborn, matplotlib
 - SHAP (Interpretabiility)
 - Streamlit (deployment)

## Contributors

Christy Chovalloor - Software Engineering Student, Queen's University Belfast
[Linkedin]("https://www.linkedin.com/in/christy-chovalloor/")
[Github]("https://github.com/Chracker24")

## License
MIT License

## Contact
For questions or collaboration, contact through email : Chr2412@hotmail.com
[Email me](mailto:Chr2412@hotmail.com)