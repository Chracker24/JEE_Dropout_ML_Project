import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import shap
import joblib
import pickle
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline 
from sklearn.metrics import classification_report
import joblib


jee_final = pd.read_csv("01_Data/03_final/JEE_Dropout_Final.csv", delimiter=',')


X= jee_final.drop(["dropout","Income vs Admission","PSxIA","admission_taken"], axis=1)
Y= jee_final["dropout"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)


pipeline_B = Pipeline([
  ('smote', SMOTE(random_state=42)),
  ('rfc', RandomForestClassifier(random_state=42, class_weight='balanced', min_samples_leaf=1, min_samples_split=5, n_estimators=100, max_depth=10))
])

pipeline_B.fit(X_train, y_train)

print("Saving models....")
joblib.dump(pipeline_B, "Model_JEET.pkl", compress=3)
print("Models saved successfully")