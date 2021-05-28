import matplotlib
import pandas as pd
import re
import requests
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.tokens import Span
import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm
import os


#--------------------------------------------------------
# Constants
#--------------------------------------------------------
PROGRAM_PATH = os.path.dirname(__file__)

nlp = spacy.load('de_core_news_lg')

pd.set_option('display.max_colwidth', 200)

# reading from csv file
pathToFile = os.path.join(PROGRAM_PATH + "/", "Trainingsdaten" + "/", "data.csv")

dataFrameComplete = pd.read_csv(pathToFile, dtype=str)[:1000]
dataFrameList = dataFrameComplete['body'].tolist()

# converting all list entries to type string
for x in range(0, len(dataFrameList)):
    dataFrameList[x] = str(dataFrameList[x])
# docs = list(df.loc['url', 'title', 'pub_date', 'lead', 'body', 'crawl_date', 'language', 'images', 'tags', 'source', 'elastic_id', 'authors', 'number_of_comments', 'sections', 'edition', 'pub_date_short', 'year_month'].values)
print("document created")

def get_entities(sent):
    ## chunk 1
    ent1 = ""
    ent2 = ""

    prv_tok_dep = ""  # dependency tag of previous token in the sentence
    prv_tok_text = ""  # previous token in the sentence

    prefix = ""
    modifier = ""

    #############################################################

    for tok in nlp(sent):
        ## chunk 2

        # if token is a punctuation mark then move on to the next token
        if tok.dep_ != "punct":
            # check: token is a compound word or not
            if tok.dep_ == "cp":
                prefix = tok.text
                # if the previous word was also a 'compound' then add the current word to it
                if prv_tok_dep == "cp":
                    prefix = prv_tok_text + " " + tok.text

            # check: token is a modifier or not
            if tok.dep_.endswith("mo"):
                modifier = tok.text
                # if the previous word was also a 'compound' then add the current word to it
                if prv_tok_dep == "cp":
                    modifier = prv_tok_text + " " + tok.text

            ## chunk 3
            if tok.pos_.find("NOUN") == False and tok.dep_.find("sb") == False:
                ent1 = modifier + " " + prefix + " " + tok.text
                prefix = ""
                modifier = ""
                prv_tok_dep = ""
                prv_tok_text = ""

            ## chunk 4
            if tok.pos_.find("NOUN") == False and tok.dep_.find("oa") == False:
                ent2 = modifier + " " + prefix + " " + tok.text
                prefix = ""
                modifier = ""
                prv_tok_dep = ""
                prv_tok_text = ""

            ## chunk 5
            # update variables
            prv_tok_dep = tok.dep_
            prv_tok_text = tok.text
    #############################################################

    return [ent1.strip(), ent2.strip()]


def get_relation(sent):
    doc = nlp(sent)

    matcher = Matcher(nlp.vocab)

    pattern = [{'DEP': 'ROOT'},
               {'DEP': 'prep', 'OP':"?"},
               {'DEP': 'agent', 'OP': "?"},
               {'POS': 'ADJ', 'OP': "?"}]
    matcher.add("matching_1", [pattern])
    matches = matcher(doc)
    k = len(matches) - 1
    span = doc[matches[k][1]:matches[k][2]]
    return span.text


#create entity pairs from our dataFrameList
entity_pairs = []

for i in tqdm(dataFrameList):
    entity_pairs.append(get_entities(i))

#get the verbs from each sentences in dataFrameList
relations = [get_relation(i) for i in tqdm(dataFrameList)]

#takes the Subject
source = [i[0] for i in entity_pairs]
#takes the object
target = [i[1] for i in entity_pairs]

#create realtion for each sb and obj 
kd_df = pd.DataFrame({'source': source, 'target': target, 'edge': relations})

#edge wurde gefiltert mit "ist"
G = nx.from_pandas_edgelist(kd_df[kd_df['edge']=="ist"], "source", "target",
                            edge_attr=True, create_using=nx.MultiDiGraph())

plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k = 0.5)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos=pos)
plt.show()
# print(get_entities("Der Film hat 200 Patente"))
