# WeitenMessenEDM
&copy; Sven Möller

Mit dem Programm "WeitenMessenEDM" können Wurfweiten für die Disziplinen Kugel, Diskus, Speer und Hammer mittels einer Leica-Totalstation gemessen werden.

### _Hinweise_
* Das GSI-Format (GSI 8 oder GSI16) wird automatisch erkannt.
* Das Programm ist nicht für UHD-Anzeigen geeignet.

## Zwingende Einstellungen an der Totalstation
* Über die GSI-Ausgabe sind kartesische Koordinaten auszugeben.
* Port: _- wird in der UI angegeben -_
* Baudrate: 19200
* Parität: keine
* Stopbits: 1
* Datenbits: 8

## Folgende Module müssen in Python vorhanden sein
* PyQt5
* serial
* math
* time
* logging
