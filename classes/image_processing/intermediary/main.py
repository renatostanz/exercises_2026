from line_classifier import LineClassifier

if __name__ == "__main__":
    classifier = LineClassifier(None)
    print(f" | The image has a {classifier.get_line_classification(None)} line.")
