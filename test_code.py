from bertopic import BERTopic
import pandas as pd

#CSV einlesen in ein Dataframe
df = pd.read_csv('Trainingsdaten/data.csv', dtype=str)

#Spalte Body in eine Liste einfügen
docs = df['body'].tolist()
print("List is ready")

#Liste ausgeben
print(docs)

#Model erstellen
model = BERTopic(language="german")
print("Transform")

#Liste ins Model geben
topics, probs = model.fit_transform(docs)
print("Transform success")

#Topics ausgeben lassen
print(model.get_topic_freq())
