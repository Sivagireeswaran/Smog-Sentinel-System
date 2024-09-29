import pandas as pd
from scripts.data_processing import load_data, process_missing_data
from scripts.feature_engineering import apply_feature_engineering
from scripts.models import split_data, train_knn, train_random_forest, train_logistic_regression, train_decision_tree
from scripts.evaluation import evaluate_model, plot_confusion_matrix
from scripts.visualization import plot_histogram, plot_bar
from scripts.utils import print_summary

# Load the data
df = load_data('data/data.csv')
print_summary(df)

# Process missing data
df = process_missing_data(df)

# Feature engineering
df = apply_feature_engineering(df)

# Data visualization
plot_histogram(df, 'type', 'Type', 'Frequency')
plot_bar(df, 'state', 'so2', 'State', 'SO2 Levels')

# Prepare data for modeling
X = df[['SOi', 'Noi', 'Rpi', 'SPMi']]
Y = df['AQI_Range']
X_train, X_test, Y_train, Y_test = split_data(X, Y)

# Train KNN
knn_model = train_knn(X_train, Y_train, k=5)
y_pred_knn = knn_model.predict(X_test)

# Evaluate KNN
accuracy_knn, kappa_knn = evaluate_model(Y_test, y_pred_knn)
print(f"KNN Accuracy: {accuracy_knn}, Kappa: {kappa_knn}")
plot_confusion_matrix(Y_test, y_pred_knn, ['Good', 'Moderate', 'Poor', 'Unhealthy', 'Very Unhealthy', 'Hazardous'])

# Similarly, train and evaluate other models like RandomForest, LogisticRegression, DecisionTree...
