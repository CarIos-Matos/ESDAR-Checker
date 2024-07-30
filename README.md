# ESDAR-Checker (Email Security DNS Advanced Records Checker)
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