httpServer.py

Dieses Beispiel führt definierte Aktionen auf dem System IBM i aus.

http://localhost:8080/nachricht&Nachrichtentext

Damit kann eine Nachricht an den QSYSOPR gesendet werden.

http://localhost:8080/file&lib.table

Damit wird der Inhalt einer Tabelle am Browser unstrukturiert angezeigt.

http://localhost:8080/STOP

Beenden des Servers.
      
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

Als Voraussetzung ist nur pyodbc als Paket erforderlich