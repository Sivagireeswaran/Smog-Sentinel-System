from sklearn.metrics import accuracy_score, confusion_matrix, cohen_kappa_score
import seaborn as sns
import matplotlib.pyplot as plt

def evaluate_model(Y_test, y_pred):
    """Evaluate model accuracy and Kappa score."""
    accuracy = accuracy_score(Y_test, y_pred)
    kappa = cohen_kappa_score(Y_test, y_pred)
    return accuracy, kappa

def plot_confusion_matrix(Y_test, y_pred, labels):
    """Plot confusion matrix."""
    cm = confusion_matrix(Y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='g', xticklabels=labels, yticklabels=labels, cmap="Blues")
    plt.ylabel('Prediction')
    plt.xlabel('Actual')
    plt.title('Confusion Matrix')
    plt.show()
