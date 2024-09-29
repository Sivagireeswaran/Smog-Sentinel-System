from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

def split_data(X, Y, test_size=0.3):
    """Split the dataset into train and test."""
    return train_test_split(X, Y, test_size=test_size)

def train_knn(X_train, Y_train, k):
    """Train KNN model."""
    knn = KNeighborsClassifier(n_neighbors=k).fit(X_train, Y_train)
    return knn

def train_random_forest(X_train, Y_train):
    """Train Random Forest model."""
    rf = RandomForestClassifier(n_estimators=100, max_depth=4, random_state=100).fit(X_train, Y_train)
    return rf

def train_logistic_regression(X_train, Y_train):
    """Train Logistic Regression model."""
    lr = LogisticRegression(C=0.01, solver='liblinear').fit(X_train, Y_train)
    return lr

def train_decision_tree(X_train, Y_train):
    """Train Decision Tree model."""
    dt = DecisionTreeClassifier(max_depth=5, min_samples_leaf=6, max_leaf_nodes=10).fit(X_train, Y_train)
    return dt
