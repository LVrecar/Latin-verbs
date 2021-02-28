#!/usr/bin/env python
# -*- coding: utf-8 -*-

glagoli_deklinacije = {"accipio":"3v", "aedifico":"1", "aestimo":"1", "ago":"3k", "alo":"3k", "ambulo":"1", "amitto":"3k", "amo":"1", "appareo":"2", "appello":"1", "ardeo":"2", "aspicio":"3v","audio":"4",
					   "bibo":"3k",
					   "cado":"3k", "cano":"3k", "carpo":"3k", "celebro":"1", "claudo":"3k", "cogito":"1", "cognosco":"3k", "comparo":"1", "compleo":"2", "condo":"3k", "contendo":"3k", "convenio":"4", "credo":"3k", "creo":"1", "cupio":"3v", "curo":"1", "curro":"3k",
					   "debeo":"2", "delecto":"1", "deleo":"2", "descendo":"3k", "desino":"3k", "dico":"3k", "discedo":"3k", "disco":"3k", "divido":"3k", "doceo":"2", "dono":"1", "dormio":"4", "duco":"3k",
					   "emo":"3k", "eripio":"3v", "erro":"1", "excito":"1", "exerceo":"2", "expugno":"1",
					   "facio":"3v", "faveo":"2", "finio":"4", "firmo":"1", "flecto":"3k", "floreo":"2", "fugo":"1",
					   "gigno":"3k",
					   "habeo":"2",
					   "iacio":"3v", "impero":"1", "impleo":"2", "incendo":"3k", "incido":"3k", "intellego":"3k", "invado":"3k", "invenio":"4", "iubeo":"2", "iudico":"1", "iuvo":"1",
					   "laboro":"1", "laudo":"1", "lego":"3k",
					   "maneo":"2", "misceo":"2", "moneo":"2", "monstro":"1", "moveo":"2", "munio":"4",
					   "narro":"1", "neglego":"3k", "noceo":"2", "nosco":"3k",
					   "obsideo":"2", "occido":"3k", "opprimo":"3k", "oppugno":"1", "orno":"1",
					   "parco":"3k", "pareo":"2", "paro":"1", "pendeo":"2", "perficio":"3v", "pervenio":"4", "peto":"3k", "placeo":"2", "porto":"1", "possideo":"2", "postulo":"1", "praebeo":"2", "premo":"3", "probo":"1", "prohibeo":"2", "promitto":"3k", "propero":"1", "pugno":"1", "punio":"4",
					   "quaero":"3k",
					   "rapio":"3v", "reddo":"3k", "reduco":"3k", "regno":"1", "relinquo":"3k", "repello":"3k", "repeto":"3k", "respondeo":"2", "revoco":"1", "rideo":"2", "rumpo":"3k",
					   "scio":"4", "scribo":"3v", "sentio":"4", "servo":"1", "solvo":"3k", "specto":"1", "spero":"1", "supero":"1",
					   "taceo":"2", "tempto":"1", "teneo":"2", "terreo":"2", "timeo":"2", "tracto":"1", "tribuo":"3v", "turbo":"1",
					   "uro":"3k",
					   "valeo":"2", "venio":"4", "verto":"3k", "video":"2", "vinco":"3k", "vivo":"3k", "voco":"1", "volo":"1", "vulnero":"1"}
glagoli_perfekt = {"accipio":"accepi", "aedifico":"aedeficavi", "aestimo":"aestimavi", "ago":"egi", "alo":"alui", "ambulo":"ambulavi", "amitto":"amisi", "amo":"amavi", "appareo":"apparui", "appello":"appellavi", "ardeo":"arsi", "aspicio":"aspexi", "audio":"audivi",
				   "bibo":"bibi",
				   "cado":"cecidi", "cano":"cecini", "carpo":"carpsi", "celebro":"celebravi", "claudo":"clausi", "cogito":"cogitavi", "cognosco":"cognovi", "comparo":"comparavi", "compleo":"complevi", "condo":"condidi", "contendo":"contendi", "convenio":"conveni", "credo":"credidi", "creo":"creavi", "cupio":"cupivi", "curo":"curavi", "curro":"cucurri",
				   "debeo":"debui", "delecto":"delectavi", "deleo":"delevi", "descendo":"descendi", "desino":"desii", "dico":"dico", "discedo":"discessi", "disco":"didici", "divido":"divisi", "doceo":"docui", "dono":"donavi", "dormio":"dormivi", "duco":"duxi",
				   "emo":"emi", "eripio":"eripui", "erro":"erravi", "excito":"excitavi", "exerceo":"exercui", "expugno":"expugnavi ",
				   "facio":"feci", "faveo":"favi", "finio":"finivi", "firmo":"firmavi", "flecto":"flexi", "floreo":"florui", "fugo":"fugavi",
				   "gigno":"genui",
				   "habeo":"habui",
				   "iacio":"ieci", "impero":"imperavi", "impleo":"implevi", "incendo":"incendi", "incido":"incidi", "intellego":"intellexi", "invado":"invasi", "invenio":"inveni", "iubeo":"iussi", "iudico":"iudicavi", "iuvo":"iuvi",
				   "laboro":"laboravi", "laudo":"laudavi", "lego":"legi",
				   "maneo":"mansi", "misceo":"miscui", "moneo":"monui", "monstro":"monstravi", "moveo":"movi", "munio":"munivi",
				   "narro":"narravi", "neglego":"neglexi", "noceo":"nocui", "nosco":"novi",
				   "obsideo":"obsedi", "occido":"occidi", "opprimo":"oppressi", "oppugno":"opugnavi", "orno":"ornavi",
				   "parco":"peperci", "pareo":"parui", "paro":"paravi", "pendeo":"pependi", "perficio":"perfeci", "pervenio":"perveni", "peto":"petivi", "placeo":"placui", "porto":"portavi", "possideo":"possedi", "postulo":"postulavi", "praebeo":"praebui", "premo":"pressi", "probo":"probavi", "prohibeo":"prohibui", "promitto":"promisi", "propero":"properavi", "pugno":"pugnavi", "punio":"punivi",
				   "quaero":"quaesivi",
				   "rapio":"rapui", "reddo":"redidi", "reduco":"reduxi", "regno":"regnavi", "relinquo":"reliqui", "repello":"reppuli", "repeto":"repetivi", "respondeo":"respondi", "revoco":"revocavi", "rideo":"risi", "rumpo":"rupi",
				   "scio":"scivi", "scribo":"scripsi", "sentio":"sensi", "servo":"servavi", "solvo":"solvi", "specto":"spectavi", "spero":"speravi", "supero":"superavi",
				   "taceo":"tacui", "tempto":"temptavi", "teneo":"tenui", "terreo":"terrui", "timeo":"timui", "tracto":"tractavi", "tribuo":"tribui", "turbo":"turbavi",
				   "uro":"ussi",
				   "valeo":"valui", "venio":"veni", "verto":"verti", "video":"vidi", "vinco":"vici", "vivo":"vixi", "voco":"vocavi", "volo":"volavi", "vulnero":"vulneravi"}
koncnice = {"prezenta" : "o,s,t,mus,tis,nt", "prezentp" : "or,ris,tur,mur,mini,ntur",
			"imperfekta" : "m,s,t,mus,tis,nt", "imperfektp" : "r,ris,tur,mur,mini,ntur",
			"futurIa" : "", "futurIp" : "r,ris,tur,mur,mini,ntur",
			"perfekta" : "i,isti,it,imus,istis,erunt", "perfektp" : "",
			"pluskvamperfekta" : "eram,eras,erat,eramus,eratis,erant", "pluskvamperfektp" : "", 
			"futurIIa" : "ero,eris,erit,erimus,eritis,erint", "futurIIp" : ""}

def aktiv(osnova, koncnice, glagoli_perfekt):

	prezenta = koncnice["prezenta"]
	kon = prezenta.split(",")
	prezentA(kon, osnova, konjugacija)

	imperfekta = koncnice["imperfekta"]
	kon = imperfekta.split(",")
	imperfektA(kon, osnova, konjugacija)

	futurIa = koncnice["futurIa"]
	futurIA(osnova, konjugacija)	

	perfekta = koncnice["perfekta"]
	kon = perfekta.split(",")
	perfektA(kon, osnova, konjugacija, glagoli_perfekt)

	plperfekta = koncnice["pluskvamperfekta"]
	kon = plperfekta.split(",")
	plperfektA(kon, osnova, konjugacija, glagoli_perfekt)

	futurIIa = koncnice["futurIIa"]
	kon = futurIIa.split(",")
	futurIIA(kon, osnova, konjugacija, glagoli_perfekt)
def pasiv(osnova, koncnice):
	prezentp = koncnice["prezentp"]
	kon = prezentp.split(",")
	prezentP(kon, osnova, konjugacija)

	imperfektp = koncnice["imperfektp"]
	kon = imperfektp.split(",")
	imperfektP(kon, osnova, konjugacija)

	futurIp = koncnice["futurIp"]
	kon = futurIp.split(",")
	futurIP(kon, osnova, konjugacija)
			
def prezentP(kon, osnova, konjugacija):
	original = osnova
	prezentPspregan = [osnova + "or"]
	kapavem = ""
	count = 0
	for i in kon:
		if count == 5:
			break
		osnova = original
		count += 1
		if konjugacija == "1" and count >= 1:
			osnova += "a"
		elif konjugacija =="3k":
			if count == 1:
				osnova += "e"
			elif count >= 2 and count < 5:
				osnova += "i"
			elif count == 5:
				osnova += "u"
		elif konjugacija in ("3v", "4"):
			if count == 5:
				osnova += "u"
			elif count == 1 and konjugacija == "3v":
				osnova = osnova.replace(" ", "")[:-1]
				osnova += "e"

		kapavem = osnova + kon[count]
		prezentPspregan.append(kapavem)
	print("--------")
	print("PREZENT P")
	print("--------")
	for a in prezentPspregan:
		print(a)	
def imperfektP(kon, osnova, konjugacija):
	original = osnova
	imperfektPspregan = []
	kapavem = ""
	count = 0
	for i in kon:
		if count <= 5:
			osnova = original
			if konjugacija == "1":
				osnova += "a"
			elif konjugacija in ("3k", "3v", "4"):
				osnova += "e"
			osnova += "ba"
			kapavem = osnova + kon[count]
			imperfektPspregan.append(kapavem)
			count += 1
		else:
			break
	print("--------")
	print("IMPERFEKT P")
	print("--------")
	for a in imperfektPspregan:
		print(a)
def futurIP(kon, osnova, konjugacija):
	original = osnova
	futurIPspregan = []
	kapavem = ""
	count = 0
	for i in kon:
		if count <= 5:
			osnova = original
			if konjugacija == "1":
				osnova += "a"
			if konjugacija in ("1", "2"):
				osnova += "b"
				if count == 0:
					osnova += "o"
				elif count == 1:
					osnova += "e"
				elif count in range(2, 5):
					osnova += "i"
				elif count == 5:
					osnova += "u"
			else:
				if count == 0:
					osnova += "a"
				else:
					osnova += "e"
			
			kapavem = osnova + kon[count]
			futurIPspregan.append(kapavem)
			count += 1
		else:
			break
		
	print("--------")
	print("FUTUR I P")
	print("--------")
	for a in futurIPspregan:
		print(a)
def prezentA(kon, osnova, konjugacija):
	original = osnova
	prezentAspregan = []
	kapavem = ""
	count = 0

	for i in kon:
		if count == 6:
			break
		osnova = original
		if konjugacija == "1" and count >=1:
			osnova += "a"
		elif konjugacija == "4":
			kon = ["o","s","t","mus","tis","unt"]
		elif konjugacija in ("3k"):
			kon = ["o","is","it","imus","itis","unt"]
		kapavem = osnova + kon[count]
		prezentAspregan.append(kapavem)
		count += 1
	print("--------")
	print("PREZENT A")
	print("--------")
	for a in prezentAspregan:
		print(a)		
def imperfektA(kon, osnova, konjugacija):
	original = osnova
	imperfektAspregan = []
	kapavem = ""
	count = 0
	for i in kon:
		if count == 6:
			break
		osnova = original
		if konjugacija == "1":
			osnova += "a"
		elif konjugacija in ("3k", "3v", "4"):
			osnova += "e"
		else:
			pass
		osnova += "ba"
		kapavem = osnova + kon[count]
		imperfektAspregan.append(kapavem)
		count += 1
	print("--------")
	print("IMPERFEKT A")
	print("--------")
	for a in imperfektAspregan:
		print(a)		
def futurIA(osnova, konjugacija):
	count = 0
	futurIAspregan = []
	delosnova = ""
	if konjugacija in ("1", "2"):
		if konjugacija == "1":
			osnova += "a"
		kon = ["o", "is", "it", "imus", "itis", "unt"]
		osnova += "b"
	else:
		kon = ["am", "es", "et", "emus", "etis", "ent"]
	delosnova = osnova
	for i in kon:
		osnova = delosnova
		osnova += kon[count]
		count += 1
		futurIAspregan.append(osnova)
	print("--------")
	print("FUTUR I A")
	print("--------")
	for a in futurIAspregan:
		print(a)
def perfektA(kon, osnova, konjugacija, glagoli_perfekt):
	lista = []
	perfektAspregan = []
	osnovna = ""
	for i in glagoli_perfekt:
		if i == verb:
			osnova = glagoli_perfekt[i]
	for x in osnova:
		lista.append(x)
	del lista[-1]
	for y in lista:
		osnovna += y
	for koncnica in kon:
		kapavem = osnovna
		kapavem += koncnica
		perfektAspregan.append(kapavem)	
	print("--------")
	print("PERFEKT A")
	print("--------")
	for a in perfektAspregan:
		print(a)
def plperfektA(kon, osnova, konjugacija, glagoli_perfekt):
	lista = []
	plperfektAspregan = []
	osnovna = ""
	for i in glagoli_perfekt:
		if i == verb:
			osnova = glagoli_perfekt[i]
	for x in osnova:
		lista.append(x)
	lista = lista[:-1]
	for y in lista:
		osnovna += y
	for koncnica in kon:
		kapavem = osnovna
		kapavem += koncnica
		plperfektAspregan.append(kapavem)	
	print("--------")
	print("PLUSKVAMPERFEKT A")
	print("--------")
	for a in plperfektAspregan:
		print(a)
def futurIIA(kon, osnova, konjugacija, glagoli_perfekt):
	lista = []
	futurIIAspregan = []
	osnovna = ""
	for i in glagoli_perfekt:
		if i == verb:
			osnova = glagoli_perfekt[i]
	for x in osnova:
		lista.append(x)
	lista = lista[:-1]
	for y in lista:
		osnovna += y
	for koncnica in kon:
		kapavem = osnovna
		kapavem += koncnica
		futurIIAspregan.append(kapavem)	
	print("--------")
	print("FUTUR II A")
	print("--------")
	for a in futurIIAspregan:
		print(a)

def spregator(glagoli_deklinacije, glagoli_perfekt, koncnice):
	global konjugacija
	global verb
	verb = ""
	verb = input("Glagol v 1. osebi ednine prezenta aktiva: ")
	for i in glagoli_deklinacije:
		if i == verb:
			konjugacija = str(glagoli_deklinacije[i])
			break
		else:
			konjugacija = "0"
	
	if konjugacija == "0":
		print("Ta glagol žal še ni na voljo v Spregatorju. Prosimo, kontakrirajte urednika.")
		spregator(glagoli_deklinacije, glagoli_perfekt, koncnice)
		return

	osnova = verb[:-1]
	aktiv(osnova, koncnice, glagoli_perfekt)
	pasiv(osnova, koncnice)

spregator(glagoli_deklinacije, glagoli_perfekt, koncnice)
