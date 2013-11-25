#!/usr/bin/env python
# coding=utf-8
import random
import smtplib

#Dictionary von Namen und zugehoerigen Mailadressen; kann unterschiedliche Anzahl von Datensaetzen enthalten
adressbuch={
    "Name1":"Mailadresse1",
    "Name2":"Mailadresse2",
    "Name3":"Mailadresse3"
}

#Funktion für Mailbody Text
def formatmailtext(schenker,beschenkter):
	return '''Hallo {schenkerplatzhalter},
dein Wichtel ist {beschenkterplatzhalter}! :-)
	'''.format(schenkerplatzhalter=schenker,beschenkterplatzhalter=beschenkter)

#Funktion um Mail zu senden
def sendmail(empfaenger,text):
	session = smtplib.SMTP('Postausangserver')
	session.login('XXXXX', 'XXXXXX')
	session.sendmail('Absenderadresse', [empfaenger], text)
	session.quit()

#Der Variablen namen Daten aus Dictionary zuweisen und diese durchmischen
namen=list(adressbuch.keys())
random.shuffle(namen)

#Schenker und Beschrenkte werden festegelegt in der Variante A schenkt B, B schenkt C, usw. und der letzte in der Reihe beschenkt A
for idx, schenker in enumerate(namen):
	nextidx=idx+1
	if nextidx >= len(namen):
		nextidx=0
	beschenkter=namen[nextidx]
	print(schenker, adressbuch[schenker], " -> ", beschenkter, adressbuch[beschenkter])
	mailbody=formatmailtext(schenker, beschenkter)
	sendmail(adressbuch[schenker], mailbody)
