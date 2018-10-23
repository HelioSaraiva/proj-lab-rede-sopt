import json
import pandas as pd
import matplotlib.pyplot as plt

def createGraph(json):
    data  = json
    count = [i['count'] for i in data["items"]]
    name  = [i['name'] for i in data["items"]]

    df = pd.DataFrame({'count': count, 'name': name})
    print(df)

    plt.bar(name,count)
    plt.show(block=True)

def main():
    with open('tags.json') as f:
        createGraph(json.load(f))
if __name__ == '__main__':
    main()