from bertopic import BERTopic
import numpy as np
import pandas as pd
import os
import time
from sklearn.datasets import fetch_20newsgroups

#--------------------------------------------------------
# Constants
#--------------------------------------------------------
PROGRAM_PATH = os.path.dirname(__file__)
PATH_TO_MODEL_VANILLA = "/models/VanillaModel"
PATH_TO_MODEL_MULTILINGUAL = "/models/MultilingualModel"

def main():

    listOfDatasets = ["VanillaModel", "MultilingualModel"]
    listOfPrograms = ["ShowTopics", "VizualizeModel", "All"]
    datasetToUse = -1
    programToExecute = -1

    while (datasetToUse > 2 or datasetToUse < 1):
        datasetToUse = input("Welcher Datensatz soll verwendet werden?\n1: VanillaModel\n2: MultilingualModel\n")
        try:
            datasetToUse = int(datasetToUse)
        except:
            print("Bitte nur die genannten Zahlen eingeben!")

    while (programToExecute > 3 or programToExecute < 1):
        programToExecute = input(f"Was soll mit dem Datensatz {listOfDatasets[datasetToUse-1]} gemacht werden?\n1: ShowTopics\n2: VizualizeModel\n3: Both\n")
        try:
            programToExecute = int(programToExecute)
        except:
            print("Bitte nur die genannten Zahlen eingeben!")

    if listOfDatasets[datasetToUse-1] == "VanillaModel":
        pathToModel = os.path.join(PROGRAM_PATH + PATH_TO_MODEL_VANILLA)
    elif listOfDatasets[datasetToUse-1] == "MultilingualModel":
        pathToModel = os.path.join(PROGRAM_PATH + PATH_TO_MODEL_MULTILINGUAL)

    transformedModel = BERTopic.load(pathToModel)

    if listOfPrograms[programToExecute-1] == "ShowTopics":
        ShowTopics(transformedModel)
    elif listOfPrograms[programToExecute-1] == "VizualizeModel":
        VisualizeModel(transformedModel)
    elif listOfPrograms[programToExecute-1] == "All":
        ShowTopics(transformedModel)
        VisualizeModel(transformedModel)

    # Old way to create document from 20newsgroups
    # docs = fetch_20newsgroups(subset='test',  remove=('headers', 'footers', 'quotes'))['data']

    # create a new model from scratch and save it
    # csvDocument = CreateDocFromCSV()
    # transformedModel = TransformModel(csvDocument)
    # try:
    #     transformedModel.save(PROGRAM_PATH + "\\models\\MultilingualModel")
    #     print("Model saved")
    # except Exception:
    #     print(Exception)


#--------------------------------------------------------
#Helper Functions
#--------------------------------------------------------
def TransformModel(document):
    bertModel = BERTopic(language="multilingual")
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
    print(f"1st topics: {myModel.get_topic(0)}") 
    print(f"3rd topics: {myModel.get_topic(2)}")
    print(f"42nd topics: {myModel.get_topic(42)}")


def VisualizeModel(myModel):
    pt = myModel.visualize_topics()
    pt.show()

if __name__ == '__main__':
    main()
