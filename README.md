# DHBW_BERTopic
#Einleitung

#Einrichtung mit Anaconda auf Windows

Vorraussetzung: Microsoft C++ Build Tools sollte installiert sein, Python Komplett deinstallieren
1. Anaconda herunterladen //Python 3.9 ist Nötig!!
2. mit Anaconda ein Environment aufsetzen - conda create --name myenv
3. Environment aktivieren - conda activate myenv
4. pip installieren - conda install pip
5. PATH Variablen einfügen (zur Sicherheit) - siehe Anhang
6. Packages und BERT installieren - pip install pytorch-transformers,
pip install pytorch-nlp, pip install bertopic
7. weiteres Package ist protobuf - sonst Traceback und Importerror - pip install protobuf


#Einrichtung ohne Anaconda auf Mac/Linux
Version Python 3.7.1 oder höher benötigt.

$ brew install bertopic

#Verwendung und Ausführung des Beispiel-Codes
$ from bertopic import BERTopic

$ import pandas as pd

$ df = pd.read_csv('Trainingsdaten/data.csv', dtype=str)

$ docs = df['body'].tolist()

$ model = BERTopic(language="german")

$ topics, probs = model.fit_transform(docs)

#Sammlung der Models
Vanilla Model
https://drive.google.com/drive/u/0/folders/1yLuXdentikQGQ0KJ_iNTOmShsxomchJI

#Bert Model einbinden
model = BERTopic.load("models/MODEL")
