import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import cross_val_score, StratifiedKFold

model1 = joblib.load("models/Model A.pkl")
model2 = joblib.load("models/Model_B.pkl")
jee = pd.read_csv("Data/03_final/JEE_Dropout_Final.csv", delimiter=',')

X = jee.sample(frac=0.4, random_state=50).drop("dropout", axis=1)
y = jee.sample(frac=0.4, random_state=50)["dropout"]
X_n = jee.sample(frac=0.4, random_state=50).drop(["dropout","Income vs Admission","PSxIA","admission_taken"], axis=1)

pred1=model1.predict(X)
pred2=model2.predict(X_n)

print("Evaluation for Model A")
print()
print(classification_report(y,pred1))
print("F1 Score for Model A:", f1_score(y, pred1, average='weighted'))
scores = cross_val_score(model1, X, y, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=42), scoring='f1_macro')
print("Cross-val F1 scores:", scores)
print("\n \n \n")
print("Evaluation for Model B")
print()
print(classification_report(y,pred2))
print("F1_score for Model B:", f1_score(y, pred2, average='weighted'))
scores = cross_val_score(model2, X_n, y, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=50), scoring='f1_macro')
print("Cross Val F1 Score:", scores)