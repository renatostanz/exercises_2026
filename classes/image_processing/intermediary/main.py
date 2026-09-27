from line_classifier import LineClassifier
from object_counter import ObjectCounter
from stitching import Stitcher

if __name__ == "__main__":
    intro = f'''

New Iteration:
    Type 1 to select the line classifier script demo
    Type 2 to select the object counter script demo
    Type 3 to select the stitch pipeline script demo
    Type Anything else to quit
{10*"-"}
Your choice: '''

    while True:
        option = input(intro)
        print("\n")
        if option == '1':
            classifier = LineClassifier(None)
            print(f" | The image has a {classifier.get_line_classification(None)} line.")
        elif option == '2':
            counter = ObjectCounter(None)
            print(f" + The image has {counter.count_objects(None)} object(s).")
        elif option == '3':
            stitcher = Stitcher(None)
            stitcher.stitch(None)
            #stitcher.stitch("data/rectangle.png")
            #stitcher.stitch("data/elipse.png")
        else:
            break

    print("Terminating")
