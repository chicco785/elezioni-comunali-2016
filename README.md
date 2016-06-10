# elezioni-comunali-2016
Un web scraper per creare un set di dati dalle pagine del ministero degli interni per le elezioni comunali del 2016.

Lo scraper e' basato su scrapy (http://scrapy.org) un semplice framework python per estrarre dati dai siti web.
Non ha pretesa di essere perfetto (anzi ha ancora qualche baco, e.g., non tutte le pagine sono strutturate uguali,
e quindi ogni tanto fa casino sulle schede bianche e nulle, funzionalita' quindi al momento "commentata" nel codice),
ma volevo solo avere qualche dato da poter usare di prima mano per fare conti, invece che ascoltare chi "manipola" i dati.

Putroppo, dato che Friuli e Sicilia non pubblicano i dati sul sito del ministero, non sono ancora inclusi (anche
se probabilmente il lavoro per estendere lo scraper, non sarebbe cosi' complesso).

Dato che scrapy ha una struttura molto semplice per i dati, durante nell'estrazione non e' facile creare "relazioni",
a questo proposito, ho semplificato molto lo script permettendo due modalita', con la prima modalita' (sindaco) si estraggono
i dati per ogni comune relativi ai voti per i candidati sindaco (sarebbe da aggiungere un campo con la lista delle liste,
per avere piu' chiaro lo schieramento), con la seconda modalita' (lista) si estraggono i voti per le singole liste.

## installazione
### installa python 2.7 (per ubuntu)

$ sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

### installa scrapy

$ pip install scrapy

## uso

$ git clone https://github.com/chicco785/elezioni-comunali-2016.git

$ cd elezioni-comunali-2016

$ scrapy crawl -o lista.csv -s MODE=lista comunali-2016

oppure 

$ scrapy crawl -o sindaco.csv -s MODE=sindaco comunali-2016


## dati estratti

trovate nella cartella dati i due file csv con i dati estratti per sindaci e liste

enjoy federico
