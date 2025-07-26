import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import cross_val_score, StratifiedKFold

model2 = joblib.load("05_models/Model_JEET.pkl")

jee = pd.read_csv("01_Data/03_final/JEE_Dropout_Final.csv", delimiter=',')

y = jee.sample(frac=0.4, random_state=50)["dropout"]
X = jee.sample(frac=0.4, random_state=50).drop(["dropout","Income vs Admission","PSxIA","admission_taken"], axis=1)

pred2=model2.predict(X)

print("Evaluation for Model JEET")
print()
print(classification_report(y,pred2))
print("F1_score for Model B:", f1_score(y, pred2, average='weighted'))
scores = cross_val_score(model2, X, y, cv=StratifiedKFold(n_splits=5, shuffle=True, random_state=50), scoring='f1_macro')
print("Cross Val F1 Score:", scores)