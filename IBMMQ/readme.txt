putmessage.py

Nachrichten über IBM MQ an ein IBM i System senden. Der Code läuft nicht auf IBM i, dazu würde eine MQ Client Installation notwendig sein,
leider ist mir das noch nicht gelungen. IBM MQ als Lizenzprogramm auf IBM i reicht allerdings, um zu kommunizieren.

getmessage.py

Nachrichten über IBM MQ von einem IBM i System holen.

Für beide Programme ist es notwendig, dass IBM MQ als Clientinstallation lokal existiert.

PYMQI setzt auf der Clientinstallation auf.