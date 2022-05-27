uploadREPLCHAR.py

Dieses Beispiel lädt ein Excel in eine Datenbankdatei LIBRARY/REPLCHAR (Library muss entsprechend verändert werden)

CREATE TABLE LIBRARY/REPLCHAR (R_FROM CHARACTER ( 100) NOT NULL WITH
DEFAULT, R_TO CHARACTER ( 100) NOT NULL WITH DEFAULT, R_SPACE DEC (
2) NOT NULL WITH DEFAULT, R_ORDER NUMERIC ( 9) NOT NULL WITH DEFAULT)

Die Tabelle muss auch in eine Journal aufgezeichnet werden z. B.

STRJRNPF FILE(LIBRARY/REPLCHAR)   
         JRN(LIBRARY/JRN)         
         IMAGES(*BOTH)            
         OMTJRNE(*OPNCLO)         
         
Anpassungen:

DATASOURCENAME.dsn muss mit User-Id, Passwort und IP-Adresse versehen werden, auf der IBM i kann die /QOpenSys/etc/odbc.ini   
wie folgt aussehen:

### IBM provided DSN - do not remove this line ###   
[*LOCAL]                                             
Description = Default IBM i local database           
Driver      = IBM i Access ODBC Driver               
System      = localhost                              
UserID      = *CURRENT                               
Database    = IASP                                   

uploadREPLCHAR.py muss im Bereich der LIBRARY angepasst werden, damit die SQL Statements funktionieren

die erforderlichen Python-Pakete sind in requirements.txt angeführt