# DHBW_BERTopic
## Einleitung  
TODO: Projektvorstellung
 
## Einrichtung der Anaconda Environment auf Windows  
Dokumentation zur Verwendung von [Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#) 
Manuelles Erstellen der Environment:  
  * Vorraussetzung: Microsoft C++ Build Tools sollte installiert sein, Python Komplett deinstallieren
  * Anaconda herunterladen
  * mit Anaconda ein Environment aufsetzen - conda create --name myenv
  * Environment aktivieren - conda activate myenv
  * pip installieren - conda install pip
  * PATH Variablen einfügen (zur Sicherheit) - siehe Anhang
  * Packages und BERT installieren - pip install pytorch-transformers pytorch-nlp protobuf bertopic

Erstellen der Environment mit dem .yml File:  
  * Conda Prompt öffen
  * Zur .yml Datei navigieren
  * Environment erstellen - conda env create -f bert39nonvisual.yml

## Verwendung und Ausführung des Beispiel-Codes
  * Pfad zur python.exe eines Environemts in der Conda Prompt:
  * activate myenv
  * where python
  * In der IDE den Interpreter ändern und die von conda angezeigte python.exe auswählen.
