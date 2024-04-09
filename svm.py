import pandas as pd
import csv
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

originalDataPath = 'Data/duplicated_data.csv'

def preprocess_and_train():
    df = pd.read_csv(originalDataPath, encoding='latin-1')

    

    Numerics = LabelEncoder()

    inputs = df.drop('results',axis='columns')
    target = df['results']

    

    #creating new dataframe

    inputs['q1']=Numerics.fit_transform(inputs['Q1'])
    inputs['q2']=Numerics.fit_transform(inputs['Q2'])
    inputs['q3']=Numerics.fit_transform(inputs['Q3'])
    inputs['q4']=Numerics.fit_transform(inputs['Q4'])
    inputs['q5']=Numerics.fit_transform(inputs['Q5'])
    inputs['q6']=Numerics.fit_transform(inputs['Q6'])
    inputs['q7']=Numerics.fit_transform(inputs['Q7'])
    inputs['q8']=Numerics.fit_transform(inputs['Q8'])
    inputs['q9']=Numerics.fit_transform(inputs['Q9'])
    inputs['q10']=Numerics.fit_transform(inputs['Q10'])
    inputs['q11']=Numerics.fit_transform(inputs['Q11'])
    inputs['q12']=Numerics.fit_transform(inputs['Q12'])
    inputs['q13']=Numerics.fit_transform(inputs['Q13'])
    inputs['q14']=Numerics.fit_transform(inputs['Q14'])
    inputs['q15']=Numerics.fit_transform(inputs['Q15'])
    inputs['q16']=Numerics.fit_transform(inputs['Q16'])
    inputs['q17']=Numerics.fit_transform(inputs['Q17'])
    inputs['q18']=Numerics.fit_transform(inputs['Q18'])
    inputs['q19']=Numerics.fit_transform(inputs['Q19'])
    inputs['q20']=Numerics.fit_transform(inputs['Q20'])
    inputs['q21']=Numerics.fit_transform(inputs['Q21'])
    inputs['q22']=Numerics.fit_transform(inputs['Q22'])
    inputs['q23']=Numerics.fit_transform(inputs['Q23'])
    inputs['q24']=Numerics.fit_transform(inputs['Q24'])
    inputs['q25']=Numerics.fit_transform(inputs['Q25'])
    inputs['q26']=Numerics.fit_transform(inputs['Q26'])
    inputs['q27']=Numerics.fit_transform(inputs['Q27'])
    inputs['q28']=Numerics.fit_transform(inputs['Q28'])
    inputs['q29']=Numerics.fit_transform(inputs['Q29'])
    inputs['q30']=Numerics.fit_transform(inputs['Q30'])
    inputs['q31']=Numerics.fit_transform(inputs['Q31'])
    inputs['q32']=Numerics.fit_transform(inputs['Q32'])

    inputs_n=inputs.drop(['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','Q27','Q28','Q29','Q30','Q31','Q32'],axis='columns')

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(inputs_n, target, test_size=0.3, random_state=42)

    # Initialize and train the classifier
    Classifier = SVC()
    Classifier.fit(X_train, y_train)

    # Accuracy
    Classifier.score(inputs_n,target)

    return Classifier


# Function to predict new data
def predict(new_data, Classifier):

    # Append new data to csv file
    with open(originalDataPath, 'a', newline='', encoding='ISO-8859-1') as originalData:
        writer = csv.writer(originalData)
        writer.writerow(new_data)

    newDF = pd.read_csv(originalDataPath, encoding='latin-1')

    numerics = LabelEncoder()

    X = newDF.drop('results', axis='columns')
    y = newDF['results']

    #creating new dataframe

    X['q1']=numerics.fit_transform(X['Q1'])
    X['q2']=numerics.fit_transform(X['Q2'])
    X['q3']=numerics.fit_transform(X['Q3'])
    X['q4']=numerics.fit_transform(X['Q4'])
    X['q5']=numerics.fit_transform(X['Q5'])
    X['q6']=numerics.fit_transform(X['Q6'])
    X['q7']=numerics.fit_transform(X['Q7'])
    X['q8']=numerics.fit_transform(X['Q8'])
    X['q9']=numerics.fit_transform(X['Q9'])
    X['q10']=numerics.fit_transform(X['Q10'])
    X['q11']=numerics.fit_transform(X['Q11'])
    X['q12']=numerics.fit_transform(X['Q12'])
    X['q13']=numerics.fit_transform(X['Q13'])
    X['q14']=numerics.fit_transform(X['Q14'])
    X['q15']=numerics.fit_transform(X['Q15'])
    X['q16']=numerics.fit_transform(X['Q16'])
    X['q17']=numerics.fit_transform(X['Q17'])
    X['q18']=numerics.fit_transform(X['Q18'])
    X['q19']=numerics.fit_transform(X['Q19'])
    X['q20']=numerics.fit_transform(X['Q20'])
    X['q21']=numerics.fit_transform(X['Q21'])
    X['q22']=numerics.fit_transform(X['Q22'])
    X['q23']=numerics.fit_transform(X['Q23'])
    X['q24']=numerics.fit_transform(X['Q24'])
    X['q25']=numerics.fit_transform(X['Q25'])
    X['q26']=numerics.fit_transform(X['Q26'])
    X['q27']=numerics.fit_transform(X['Q27'])
    X['q28']=numerics.fit_transform(X['Q28'])
    X['q29']=numerics.fit_transform(X['Q29'])
    X['q30']=numerics.fit_transform(X['Q30'])
    X['q31']=numerics.fit_transform(X['Q31'])
    X['q32']=numerics.fit_transform(X['Q32'])

    


    X_New = X.drop(['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','Q27','Q28','Q29','Q30','Q31','Q32'], axis='columns')

    newData = X_New.iloc[-1].tolist()
    print(newData)

    output = Classifier.predict([newData])
    prediction = output[0]

    with open(originalDataPath, 'r', newline='', encoding='ISO-8859-1') as file:
        rows = list(csv.reader(file))

    rows.pop()

    with open(originalDataPath, 'w', newline='', encoding='ISO-8859-1') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    
    return prediction