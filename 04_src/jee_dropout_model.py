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

X = jee_final.drop(["dropout","admission_taken"], axis=1)
Y = jee_final["dropout"]
X_n = jee_final.drop(["dropout","Income vs Admission","PSxIA","admission_taken"], axis=1)
Y_n = jee_final["dropout"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)
X_train_n, X_test_n, y_train_n, y_test_n = train_test_split(X_n, Y_n, test_size=0.2, random_state=42, stratify=Y_n)

pipeline_A = Pipeline([
  ('scaler', StandardScaler()),
  ('smote', SMOTE(random_state=42)),
  ('rfc', RandomForestClassifier(random_state=42, class_weight='balanced', min_samples_leaf=1, min_samples_split=2, n_estimators=100))
])

pipeline_B = Pipeline([
  ('smote', SMOTE(random_state=42)),
  ('rfc', RandomForestClassifier(random_state=42, class_weight='balanced', min_samples_leaf=1, min_samples_split=5, n_estimators=100, max_depth=10))
])

pipeline_A.fit(X_train, y_train)
pipeline_B.fit(X_train_n, y_train_n)

print("Saving models....")
joblib.dump(pipeline_A, "Model A.pkl")
joblib.dump(pipeline_B, "Model_B.pkl")
print("Models saved successfully")