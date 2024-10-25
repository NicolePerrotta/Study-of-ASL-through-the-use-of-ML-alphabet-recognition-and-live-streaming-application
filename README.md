# Study-of-ASL-through-the-use-of-ML-alphabet-recognition-and-live-streaming-application

Repository del progetto Live ASL Classification creato per il laboratorio di AI a.a 2021/22 fatto da Nicole Perrotta.
Consiste nella classificazione delle 26 lettere dell'alfabeto dei segni americano (ASL) e di 3 parole ('space', 'delete' and 'nothing') attraverso l'uso di reti pre-addestrate
per allenare un nuovo modello sul seguente set di dati: https://www.kaggle.com/datasets/grassknoted/asl-alphabet Il riconoscimento delle immagini avviene attraverso un video live.

Il progetto si divide in due parti, la prima su Colab per la creazione del modello e la seconda in locale per la realizzazione dell'architettura dello streaming video.

Per la creazione del modello ho provato diverse reti neurali convoluzionali pre-addestrate come MobileNet, MobileNetV2, EfficientNetB0 e InceptionV3, queste ultime due si sono
rivelate le più performanti nel test set.

Per il problema del riconoscimento del linguaggio dei segni in live attraverso l'utilizzo di una videocamera ho effettuato diversi paragoni tra i modelli precedentemente creati
e ho studiato il loro comportamento sui frame estrapolati dal video, giungendo alla conclusione che il modello con prestazioni migliori fosse quello con IncpetionV3.

Per caricare i vari modelli, data la dimensione, ho deciso di condividere una cartella drive: https://drive.google.com/drive/folders/1rhTVhObyH4VRnVhtbmFARdpGG2B2rS2J?usp=sharing

La cartella è organizzata nel seguente modo:
-ASL_Classification.ipynb
-B&W_ASL_Classification.ipynb
-Live_ASL_Classification.py
-B&W_Live_ASL_Classification.py
-Dataset.zip -Dataset_B&W.zip
-Demo.mp4 che contiene una breve dimostrazione del comportamento del modello
-Evaluations.xlsx che contiene la valutazione dei vari modelli
-Letters.xlxs che contiene il comportamento del mondello scelto nel riconoscere i vari segni
-Saved_models dove sono salvati i pesi di tutti i modelli usati
