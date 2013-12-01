#!/usr/bin/env python
# coding=utf-8
import random
import smtplib
from email.mime.text import MIMEText
from random import seed
from time import time

#Pruefung der Zufaelligkeit
time_seed = time()
print('benutzter Seed:', time_seed)
seed(time_seed)

#Dictionary von Namen und zugehoerigen Mailadressen; kann unterschiedliche Anzahl von Datensaetzen enthalten
adressbuch={
    "Name1":"Mailadresse1",
    "Name2":"Mailadresse2",
    "Name3":"Mailadresse3"
}

#Funktion für Betreff, Empfaengeradresse und Mailbody Text
def formatmailtext(schenker,beschenkter,schenkermailadresse):
	return '''To: {schenkermailadresse}
Subject: Wichtelmail fuer {schenkerplatzhalter}
MIME-Version: 1.0
Content-type: text/plain; charset=iso-8859-15
Content-Transfer-Encoding: 8bit
Hallo {schenkerplatzhalter},
dein Wichtel ist {beschenkterplatzhalter}! :-)
	'''.format(schenkerplatzhalter=schenker,beschenkterplatzhalter=beschenkter,schenkermailadresse=schenkermailadresse)

#Funktion um Mail zu senden
def sendmail(empfaenger,text):
	session = smtplib.SMTP('Postausangserver')
	session.login('XXXXX', 'XXXXXX')
	session.sendmail('Absenderadresse', [empfaenger], text)
	session.quit()

#Der Variable namen Daten aus Dictionary zuweisen und diese durchmischen
namen=list(adressbuch.keys())
print(namen)
random.shuffle(namen)

#Schenker und Beschrenkte werden festegelegt in der Variante:
#A schenkt B, B schenkt C, usw. und der letzte in der Reihe beschenkt A
for idx, schenker in enumerate(namen):
	nextidx=idx+1
	if nextidx >= len(namen):
		nextidx=0
	beschenkter=namen[nextidx]
	print(schenker, adressbuch[schenker], " -> ", beschenkter, adressbuch[beschenkter])
	mailbody=formatmailtext(schenker, beschenkter, adressbuch[schenker])
	sendmail(adressbuch[schenker], mailbody)
