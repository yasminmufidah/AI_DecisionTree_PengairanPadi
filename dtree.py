import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('RICE-DATASET.csv')
data.head(10)

enc = LabelEncoder()
data['Status'] = enc.fit_transform(data['Status'].values)
atr_data = data.drop(columns='Status')
cls_data = data['Status']

xtrain, xtest, ytrain, ytest = train_test_split(atr_data, cls_data, test_size=0.2, random_state=50)
tree_data = DecisionTreeClassifier(random_state=50)
tree_data.fit(xtrain, ytrain)

print("Nilai akurasi pada data testing: ", tree_data.score(xtest, ytest))
prediksi = tree_data.predict([[50,38,23,92]])

print(prediksi)

if prediksi == 1:
    print("Siram")
else: 
    print("Tidak Siram")
