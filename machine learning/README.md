Iris Flower Classification
Kaggle Dataset Used

For this project, I used the Iris Flower Dataset from Kaggle.
This dataset contains measurements of different Iris flowers and their species.

Kaggle Source:
https://www.kaggle.com/datasets/arshid/iris-flower-dataset

I selected rows from this dataset and created my own file named iris.csv, which the program uses for training.

Type of Machine Learning Used
Supervised Learning

This project uses supervised learning, where the model learns from data that already has labels.

Input:
sepal_length, sepal_width, petal_length, petal_width

Label (Output):
Species (Iris-setosa, Iris-versicolor, Iris-virginica)

Supervised learning is used because the model needs to learn which flower measurements belong to which species.

Highlight of iris.csv

Your iris.csv file contains 150 rows and 5 columns:

sepal_length,sepal_width,petal_length,petal_width,Species
5.1,3.5,1.4,0.2,Iris-setosa
4.9,3.0,1.4,0.2,Iris-setosa
4.7,3.2,1.3,0.2,Iris-setosa
...
5.9,3.0,5.1,1.8,Iris-virginica

These values are the training data for the model.

Highlight of ml.py (Core Code)
1. Load Dataset
df = pd.read_csv(r"C:\Users\DC Gaming\Documents\school\coding file\vscode\machine learning\Iris.csv")

2. Split Data
X = df.drop("Species", axis=1)
y = df["Species"]

3. Train the Model (Decision Tree)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

4. Predict Species
sample = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=["sepal_length", "sepal_width", "petal_length", "petal_width"]
)

prediction = model.predict(sample)
species_name = label_encoder.inverse_transform(prediction)

print("Predicted Species:", species_name)

What My ML Program Does

Your machine learning program performs the following:

1. Reads the CSV data
It loads all flower measurements and their species from iris.csv.

2. Trains a Decision Tree model
The model studies the patterns:
How sepal and petal sizes relate to each species.

3. Checks accuracy
It prints how well the model learned based on the training data.

4. Predicts a flower species
When you type or give new flower measurements, the program predicts whether it is:

* Iris-setosa
* Iris-versicolor
* Iris-virginica

In short:
Your ML program learns from real flower data and predicts the species of a new flower based on its measurements.