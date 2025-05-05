import math
from collections import defaultdict

class NaiveBayesClassifier:
    def __init__(self):
        self.class_priors = defaultdict(float)
        self.feature_likelihoods = defaultdict(lambda: defaultdict(float))
        self.classes = set()
        self.vocab = set()

    def fit(self, X, y):
        n_samples = len(X)
        self.classes = set(y)
        for label in self.classes:
            X_label = [x for x, t in zip(X, y) if t == label]
            self.class_priors[label] = len(X_label) / n_samples
            word_counts = defaultdict(int)
            total_count = 0
            for x in X_label:
                for word in x:
                    word_counts[word] += 1
                    total_count += 1
                    self.vocab.add(word)
            for word in self.vocab:
                self.feature_likelihoods[label][word] = (word_counts[word] + 1) / (total_count + len(self.vocab))

    def predict(self, X):
        preds = []
        for x in X:
            class_scores = {}
            for label in self.classes:
                log_prob = math.log(self.class_priors[label])
                for word in x:
                    log_prob += math.log(self.feature_likelihoods[label].get(word, 1 / (len(self.vocab) + 1)))
                class_scores[label] = log_prob
            preds.append(max(class_scores, key=class_scores.get))
        return preds 
