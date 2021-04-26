from bertopic import BERTopic
import numpy as np
import pandas as pd
import os
# from sklearn.datasets import fetch_20newsgroups
print("import success")
#--------------------------------------------------------
#Import End
#--------------------------------------------------------


def main():
    # Old way to create document from 20newsgroups
    # docs = fetch_20newsgroups(subset='test',  remove=('headers', 'footers', 'quotes'))['data']
    # print(len(docs))

    document = CreateDocFromCSV()
    bertModel = BERTopic()
    print("going to transform")
    topics, _ = bertModel.fit_transform(document)
    print("transform success")
    ShowTopics(bertModel)


#--------------------------------------------------------
#Helper Functions
#--------------------------------------------------------
def CreateDocFromCSV():
    # reading from csv file
    dirname = os.path.dirname(__file__)
    pathToFile = os.path.join(dirname + "/", "Trainingsdaten" + "/", "data.csv")
    # print(pathToFile)

    dataFrame = pd.read_csv(pathToFile)
    docs = dataFrame['body'].tolist()
    # docs = list(df.loc["url"].values)
    # docs = list(df.loc['url', 'title', 'pub_date', 'lead', 'body', 'crawl_date', 'language', 'images', 'tags', 'source', 'elastic_id', 'authors', 'number_of_comments', 'sections', 'edition', 'pub_date_short', 'year_month'].values)
    print("document created")
    return docs

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
