# DHBW_BERTopic
1. Einleitung  
TODO: Projektvorstellung

2. Einrichtung der Anaconda Environment auf Windows  
2.1 Manuelles Erstellen der Environment:  
  1. Vorraussetzung: Microsoft C++ Build Tools sollte installiert sein, Python Komplett deinstallieren
  2. Anaconda herunterladen
  3. mit Anaconda ein Environment aufsetzen - conda create --name myenv
  4. Environment aktivieren - conda activate myenv
  5. pip installieren - conda install pip
  6. PATH Variablen einfügen (zur Sicherheit) - siehe Anhang
  7. Packages und BERT installieren - pip install pytorch-transformers pytorch-nlp protobuf bertopic
  
2.2 Erstellen der Environment mit dem .yml File:  
  1. Conda Prompt öffen
  2. Zur .yml Datei navigieren
  3. Environment erstellen - conda env create -f bert39nonvisual.yml

3. Verwendung und Ausführung des Beispiel-Codes
  Pfad zur python.exe eines Environemts in der Conda Prompt:
  activate myenv
  where python
  In der IDE den Interpreter ändern und die von conda angezeigte python.exe auswählen.
