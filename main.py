print("loading imports")
from bertopic import BERTopic
import numpy as np
import pandas as pd
import os
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from sklearn.datasets import fetch_20newsgroups
print("finished loading")

# --------------------------------------------------------
# Constants
# --------------------------------------------------------
PROGRAM_PATH = os.path.dirname(__file__)
PATH_TO_MODEL_VANILLA = "/models/VanillaModel"
PATH_TO_MODEL_MULTILINGUAL = "/models/MultilingualModel"


def main():
    list_of_models = ["VanillaModel", "MultilingualModel", "CustomModel"]
    dict_of_models = {"VanillaModel": PATH_TO_MODEL_VANILLA,
                      "MultilingualModel": PATH_TO_MODEL_MULTILINGUAL,
                      "CustomModel": None}
    list_of_programs = ["ShowTopics", "VisualizeModel", "Both"]

    index_of_model = get_options_index(list_of_models, "Which dataset should be used?")
    name_of_model = list_of_models[index_of_model]
    transformed_model = load_model(dict_of_models[name_of_model])
    
    index_of_program = get_options_index(list_of_programs, "Which program do you want to execute?")
    execute_chosen_program(index_of_program, transformed_model)

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
def execute_chosen_program(index_of_program, transformed_model):
    if index_of_program == 0:
        show_topics(transformed_model)
    elif index_of_program == 1:
        visualize_model(transformed_model)
    elif index_of_program == 2:
        show_topics(transformed_model)
        visualize_model(transformed_model)


def build_question(my_list, question):
    question_string = question + "\n"
    for index in range(len(my_list)):
        question_string += str(index) + ": " + str(my_list[index]) + "\n"

    return question_string


def get_options_index(my_list, question):
    index = -1
    while index > len(my_list) - 1 or index < 0:
        question_string = build_question(my_list, question)
        index = input(question_string)

        try:
            index = int(index)
        except:
            print("Please only enter the numbers from above!")
    return index


def load_model(model_name):
    if model_name is not None:
        path_to_model = os.path.join(PROGRAM_PATH + model_name)
    else:
        path_to_model = get_custom_model()
        path_to_model = os.path.normpath(path_to_model)

    try:
        transformed_model = BERTopic.load(path_to_model)
    except:
        print("No model was selected.\nProgram is shutting down.")
        quit()

    print("model was loaded")
    return transformed_model


def get_custom_model():
    root = Tk()
    root.focus_set()
    path_to_model = askopenfilename(parent=root)
    root.destroy()
    return path_to_model


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
    path_to_model = os.path.join(PROGRAM_PATH + "/", "Trainingsdaten" + "/", "data.csv")

    data_frame_complete = pd.read_csv(path_to_model, dtype=str)
    data_frame_list = data_frame_complete['body'].tolist()

    # converting all list entries to type string
    for x in range(0, len(data_frame_list)):
        data_frame_list[x] = str(data_frame_list[x])
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
