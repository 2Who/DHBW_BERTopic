# DHBW_BERTopic

## Einleitung
Im Zuge des Moduls "Neue Konzepte" an der DHBW Lörrach im Studiengang Informatik (TIF18A) soll das ML-Modell Bertopic optimiert werden.
Hierzu sollen Knowledge-Graphen (KGE) verwendet werden, um das Topic Modelling zu verbessern.

Im ersten Schritt soll ein lauffähiges Bert erarbeitet werden, während im zweiten Schritt verschiedene Knowledge Graphen integriert werden.
Im dritten Schritt soll BERT schließlich mit dem entsprechenden KGE zusammenarbeiten und in einer Verbesserung des Topic Modellings resultieren.
 
## Einrichtung der Anaconda Environment auf Windows  
[Dokumentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) zur Verwendung von Conda Environments von conda.io  
Manuelles Erstellen der Environment:  
  * Vorraussetzung: [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/de/visual-cpp-build-tools/) sollte installiert sein, Python komplett deinstallieren
  * Anaconda herunterladen
  * mit Anaconda ein Environment aufsetzen - conda create --name myenv
  * Environment aktivieren - conda activate myenv
  * pip installieren - conda install pip
  * Packages und BERT installieren - pip install pytorch-transformers pytorch-nlp protobuf bertopic

Erstellen der Environment mit dem .yml File:  
  * bertopic38.yml vom Repository downloaden
  * Conda Prompt öffen
  * Zur .yml Datei navigieren
  * Environment erstellen - conda env create -f bert39nonvisual.yml  

## Einrichtung ohne Anaconda auf Mac/Linux
Version Python 3.7.1 oder höher benötigt.

$ brew install bertopic

## Verwendung und Ausführung des Beispiel-Codes
$ from bertopic import BERTopic

$ import pandas as pd

$ df = pd.read_csv('Trainingsdaten/data.csv', dtype=str)

$ docs = df['body'].tolist()

$ model = BERTopic(language="german")

$ topics, probs = model.fit_transform(docs)

### Sammlung der Models
Vanilla Model
https://drive.google.com/drive/u/0/folders/1yLuXdentikQGQ0KJ_iNTOmShsxomchJI

### Bert Model einbinden
model = BERTopic.load("models/MODEL")

## Verwendung und Ausführung des Beispiel-Codes
  * Pfad zur python.exe eines Environemts in der Conda Prompt:
  * activate myenv
  * where python
  * In der IDE den Interpreter ändern und die von conda angezeigte python.exe auswählen.

