from naive_bayes import NaiveBayesClassifier
from dataset import load_sample_dataset

def main():
    X, y = load_sample_dataset()
    clf = NaiveBayesClassifier()
    clf.fit(X, y)
    preds = clf.predict(X)
    accuracy = sum([p == t for p, t in zip(preds, y)]) / len(y)
    print(f"Accuracy: {accuracy:.2f}")
    print("Sample predictions:")
    for i in range(5):
        print(f"Input: {X[i]}, True: {y[i]}, Pred: {preds[i]}")

if __name__ == "__main__":
    main() 
