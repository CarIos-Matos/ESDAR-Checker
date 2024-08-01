# ESDAR-Checker (Email Security DNS Advanced Records Checker)
## How to use ESDAR-Checker
Prerequisites:
- Python3
- you have to be able to run Scripts via Powershell or at least to run the following command in Powershell: ```Set-ExecutionPolicy Unrestricted -Scope Process``` ([Stackoverflow](https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows))


1. Clone Github Repository to your local machine
2. Unpack the Github Repository
3. run Powershell in the ESDAR-Checker Directory
4. Create virtual enviroment according to the following [documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments) (use ```python -m venv .``` to create the virtualenv in the current directory)
5. Activate the virtualenv, if you need help you can look into the following [article](https://realpython.com/python-virtual-environments-a-primer/#activate-it)
6. When you succesfully activatet the virtual enviroment you can install the missing 'checkdmarc' module with the following Command ``` python -m pip install checkdmarc==4.1.1```
7. Open the python file 'config.py' in the ESDAR-Checker directory
8. and enter the FULL path to the ouptut directory which you can find in the resources folder.
9. you have to escape every \ with \ so for example 'C:\\Users\\[USERNAME]\\Downloads\\ESDAR-Checker-1.0.0-beta\\resources\\output'
10. Now your ready to run the ESDAR-Checker!

---

## Use Case
Diese Skript soll dem Benutzer helfen eine beliebige anzahl an Domains respektive URL's auf folgende Punkte zu ueberpruefen
- DMARC
- SPF
- DKIM
- MX Records

Das Skript prüft dabei ob für die oben genannten Punkte ein DNS TXT record vorhanden ist, wenn dem so ist wird dieser fuer die weitere verwendung zwischengespeihcert.
Im Anschluss kann der Record eintrag auf dem Terminal ausgegeben werden oder in ein csv file geschrieben werden.

## Aktueller Status
In Entwicklung. Das Skript funktioniert für einzelne Domains das Error Handling ist jedoch noch nicht ausreichend umgesetzt. 

## Probleme
- csv files geben aktuell noch probleme bei der verarbeitung
- es können nicht mehrere selectoren eingegeben werden
- einzelne Errors führen zu einem ungewollten absturz
- das aktuelle skript benötigt die checkdmarc version 4.4.1 und publicsuffix2. Muss noch geändert werden
