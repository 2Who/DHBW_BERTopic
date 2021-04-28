from bertopic import BERTopic
import numpy as np
import pandas as pd
import os
import time
# from sklearn.datasets import fetch_20newsgroups
print("import success")

#--------------------------------------------------------
# Constants
#--------------------------------------------------------
PROGRAM_PATH = os.path.dirname(__file__)

def main():
    # Old way to create document from 20newsgroups
    # docs = fetch_20newsgroups(subset='test',  remove=('headers', 'footers', 'quotes'))['data']

    # create a new model from scratch
    # csvDocument = CreateDocFromCSV()
    # transformedModel = TransformModel(csvDocument)

    # import an existing model
    transformedModel = BERTopic.load(PROGRAM_PATH + "/models/vanilla_deutsch")
    ShowTopics(transformedModel)

    # ShowTopics(transformedModel)
    # VisualizeModel(transformedModel)


#--------------------------------------------------------
#Helper Functions
#--------------------------------------------------------
def TransformModel(document):
    bertModel = BERTopic()
    print("going to transform")
    transformTime = time.perf_counter()
    try:
        topics, _ = bertModel.fit_transform(document)
        transformTime = time.perf_counter() - transformTime
        transformTime = transformTime / 60
        print(f"Transformation success! Duration:{transformTime:0.4f} minutes")
    except Exception:
        print(Exception)
        transformTime = time.perf_counter() - transformTime
        transformTime = transformTime / 60
        print(f"Transformation failed! Duration:{transformTime:0.4f} minutes")
    return bertModel

def CreateDocFromCSV():
    # reading from csv file
    pathToFile = os.path.join(PROGRAM_PATH + "/", "Trainingsdaten" + "/", "data.csv")

    dataFrameComplete = pd.read_csv(pathToFile, dtype=str)
    dataFrameList = dataFrameComplete['body'].tolist()
    # converting all list entries to type string
    for x in range(0, len(dataFrameList)):
        dataFrameList[x] = str(dataFrameList[x])
    # docs = list(df.loc['url', 'title', 'pub_date', 'lead', 'body', 'crawl_date', 'language', 'images', 'tags', 'source', 'elastic_id', 'authors', 'number_of_comments', 'sections', 'edition', 'pub_date_short', 'year_month'].values)
    print("document created")
    return dataFrameList

def ShowTopics(myModel):
    print(myModel.get_topic_freq().head())
    print(myModel.get_topic_freq())
    print("1st topics: " + myModel.get_topic(0)) 
    print("3rd topics: " + myModel.get_topic(2))
    print("42nd topics: " + myModel.get_topic(42))

def VisualizeModel(myModel):
    myModel.visualize_topics()

if __name__ == '__main__':
    main()
