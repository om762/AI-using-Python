import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

model = Perceptron()
# model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=1)
# model = GaussianNB()

# Read Data
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)
    
    data =  []
    for row in reader:
        data.append({
            'evidence': [float(cell) for cell in row[:4]],
            "label":"Authentic" if row[4] == "0" else "Counterfeit"
        })

# Holdout Data Cross-Validation: Seperating data in two parts
# Training group and testing group
holdout = int(0.40 * len(data))
random.shuffle(data)
testing = data[:holdout]
training = data[holdout:]

# Train model on traning group
X_training = [row['evidence'] for row in training]
y_training = [row['label'] for row in training]
model.fit(X_training, y_training)

# Make prediction on testing group
X_testing = [row["evidence"] for row in testing]
y_testing = [row["label"] for row in testing]
predictions = model.predict(X_testing)

# Compute how well we performed
correct = 0
incorrect = 0
total = 0

for actual, predicted in zip(y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
    else:
        incorrect += 1

# Result
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")