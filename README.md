# DHBW_BERTopic
## Einleitung  
TODO: Projektvorstellung
 
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

## Verwendung und Ausführung des Beispiel-Codes
  * Pfad zur python.exe eines Environemts in der Conda Prompt:
  * activate myenv
  * where python
  * In der IDE den Interpreter ändern und die von conda angezeigte python.exe auswählen.
