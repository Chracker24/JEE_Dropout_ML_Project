import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
from sklearn.svm import SVC
import joblib
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline 

jee_final = pd.read_csv("01_Data/03_final/JEE_Dropout_Final.csv", delimiter=',')


X= jee_final.drop(["dropout","Income vs Admission","PSxIA","admission_taken"], axis=1)
Y= jee_final["dropout"]

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)


pipeline= Pipeline([
  ('smote', SMOTE(random_state=42)),
  ('scaler', StandardScaler()),
  ('vc', VotingClassifier(estimators=[
      ('rfc', RandomForestClassifier(random_state=42)),
      ('svc', SVC(random_state=42, probability=True))
  ], voting='soft')
  )
])

pipeline.fit(X_train, y_train)

print("Saving models....")
joblib.dump(pipeline, "05_models/Model_JEET.pkl", compress=3)
joblib.dump(pipeline,"06_deployment/model/JEET.pkl")
print("Models saved successfully")