# DHBW_BERTopic
1. Einleitung
TODO: Projektvorstellung

2. Einrichtung der Anaconda Environment
2.1 Einrichtung mit Anaconda auf Windows
2.1.1 Manuelles Erstellen der Environment:
  !!!Vorraussetzung: Microsoft C++ Build Tools sollte installiert sein, Python Komplett deinstallieren!!!
  1. Anaconda herunterladen
  2. mit Anaconda ein Environment aufsetzen - conda create --name myenv
  3. Environment aktivieren - conda activate myenv
  4. pip installieren - conda install pip
  5. PATH Variablen einfügen (zur Sicherheit) - siehe Anhang
  6. Packages und BERT installieren - pip install pytorch-transformers pytorch-nlp protobuf bertopic

2.1.2 Erstellen der Environment mit dem .yml File:
  1. Conda Prompt öffen
  2. Zur .yml Datei navigieren
  3. Environment erstellen - conda env create -f bert39nonvisual.yml

2.2 Einrichtung ohne Anaconda auf Mac/Linux

3. Verwendung und Ausführung des Beispiel-Codes
  Pfad zur python.exe eines Environemts in der Conda Prompt:
  activate myenv
  where python
  In der IDE den Interpreter ändern und die von conda angezeigte python.exe auswählen.
