putmessage.py

Nachrichten �ber IBM MQ an ein IBM i System senden. Der Code l�uft nicht auf IBM i, dazu w�rde eine MQ Client Installation notwendig sein,
leider ist mir das noch nicht gelungen. IBM MQ als Lizenzprogramm auf IBM i reicht allerdings, um zu kommunizieren.

getmessage.py

Nachrichten �ber IBM MQ von einem IBM i System holen.

F�r beide Programme ist es notwendig, dass IBM MQ als Clientinstallation lokal existiert.

PYMQI setzt auf der Clientinstallation auf.