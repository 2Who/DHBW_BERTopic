from bertopic import BERTopic
import numpy as np
import pandas as pd
import os
import time
from sklearn.datasets import fetch_20newsgroups

# --------------------------------------------------------
# Constants
# --------------------------------------------------------
PROGRAM_PATH = os.path.dirname(__file__)
PATH_TO_MODEL_VANILLA = "/models/VanillaModel"
PATH_TO_MODEL_MULTILINGUAL = "/models/MultilingualModel"


def main():
    list_of_datasets = ["VanillaModel", "MultilingualModel"]
    list_of_programs = ["ShowTopics", "VizualizeModel", "Both"]
    dataset_to_use = -1
    program_to_execute = -1

    while dataset_to_use > len(list_of_datasets) or dataset_to_use < 1:
        dataset_to_use = input(
            f"Welcher Datensatz soll verwendet werden?"
            f"\n1: {list_of_datasets[0]}\n2: {list_of_datasets[1]}\n")
        try:
            dataset_to_use = int(dataset_to_use)
        except:
            print("Bitte nur die genannten Zahlen eingeben!")

    while program_to_execute > len(list_of_programs) or program_to_execute < 1:
        program_to_execute = input(
            f"Was soll mit dem Datensatz {list_of_datasets[dataset_to_use - 1]} gemacht werden?"
            f"\n1: {list_of_programs[0]}\n2: {list_of_programs[1]}\n3: {list_of_programs[2]}\n")
        try:
            program_to_execute = int(program_to_execute)
        except:
            print("Bitte nur die genannten Zahlen eingeben!")

    if list_of_datasets[dataset_to_use - 1] == list_of_datasets[0]:
        path_to_model = os.path.join(PROGRAM_PATH + PATH_TO_MODEL_VANILLA)
    elif list_of_datasets[dataset_to_use - 1] == list_of_datasets[1]:
        path_to_model = os.path.join(PROGRAM_PATH + PATH_TO_MODEL_MULTILINGUAL)

    transformed_model = BERTopic.load(path_to_model)

    if list_of_programs[program_to_execute - 1] == list_of_programs[0]:
        show_topics(transformed_model)
    elif list_of_programs[program_to_execute - 1] == list_of_programs[1]:
        visualize_model(transformed_model)
    elif list_of_programs[program_to_execute - 1] == list_of_datasets[2]:
        show_topics(transformed_model)
        visualize_model(transformed_model)

    # Old way to create document from 20newsgroups
    # docs = fetch_20newsgroups(subset='test',  remove=('headers', 'footers', 'quotes'))['data']

    # create a new model from scratch and save it
    # csvDocument = CreateDocFromCSV()
    # transformed_model = TransformModel(csvDocument)
    # try:
    #     transformed_model.save(PROGRAM_PATH + "\\models\\MultilingualModel")
    #     print("Model saved")
    # except Exception:
    #     print(Exception)


# --------------------------------------------------------
# Helper Functions
# --------------------------------------------------------
def transform_model(document):
    bert_model = BERTopic(language="multilingual")
    print("going to transform")
    transform_time = time.perf_counter()
    try:
        topics, _ = bert_model.fit_transform(document)
        transform_time = time.perf_counter() - transform_time
        transform_time = transform_time / 60
        print(f"Transformation success! Duration:{transform_time:0.4f} minutes")
    except Exception:
        print(Exception)
        transform_time = time.perf_counter() - transform_time
        transform_time = transform_time / 60
        print(f"Transformation failed! Duration:{transform_time:0.4f} minutes")
    return bert_model


def create_coc_from_csv():
    # reading from csv file
    path_to_file = os.path.join(PROGRAM_PATH + "/", "Trainingsdaten" + "/", "data.csv")

    data_frame_complete = pd.read_csv(path_to_file, dtype=str)
    data_frame_list = data_frame_complete['body'].tolist()

    # converting all list entries to type string
    for x in range(0, len(data_frame_list)):
        data_frame_list[x] = str(data_frame_list[x])
    # docs = list(df.loc['url', 'title', 'pub_date', 'lead', 'body', 'crawl_date', 'language', 'images', 'tags', 'source', 'elastic_id', 'authors', 'number_of_comments', 'sections', 'edition', 'pub_date_short', 'year_month'].values)
    print("document created")
    return data_frame_list


def show_topics(my_model):
    print(my_model.get_topic_freq().head())
    print(my_model.get_topic_freq())
    print(f"1st topics: {my_model.get_topic(0)}")
    print(f"3rd topics: {my_model.get_topic(2)}")
    print(f"42nd topics: {my_model.get_topic(42)}")


def visualize_model(my_model):
    pt = my_model.visualize_topics()
    pt.show()


if __name__ == '__main__':
    main()
