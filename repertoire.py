from datetime import date

aujourdhui = date.today()
moisCourant = aujourdhui.month


p0 = ["Prénom", "NOM", "Numéro mobile", "Adresse", "Date de naissance"]

p1 = ["Maël", "QUERRÉ", "0649782912", "Saint-Contest", "09/09/1996"]
p2 = ["Vincent", "DE MENEZES", "0601010101", "Clamart", ""]
p3 = ["Gabriel", "FAURÉ", "", "Pamiers", "12/05/1845"]
p4 = ["Claude", "DEBUSSY", "0602020202", "Saint-Germain-en-laye", "22/08/1862"]
p5 = ["Frédéric", "CHOPIN", "", "Żelazowa Wola", "01/03/1810" ]
p6 = ["Jean-Sébastien", "BACH", "", "Eisenach", "31/03/1685"]

personnes = [p1, p2, p3, p4, p5, p6]

OK = 0
WRONG_INPUT = 1
NOTHING_WERE_GIVEN = 2


def test(tuple_saisie):
    if rNom != "":
        result = detect_nom(rNom)
    if rPrenom != "":
        result1 = result
        result1 = detect_prenom(rPrenom)
    if result == result1:
        if rMobile != "":
            result = detect_telephone(rMobile)
        if rAdresse != "":
            result1 = result
            result1 = detect_adresse(rAdresse)
    if result == result1 and result == -1:
        print("Contact inexistant")
    elif result != result1:
        print("Contact inexistant")
    else:
        print(personnes[result])


def saisie():
    rNom = input("Saisissez votre nom : ")
    rPrenom = input("Saisissez votre prénom : ")
    rMobile = input("Saisissez votre numéro de téléphone mobile : ")
    rAdresse = input("Saisissez votre adresse : ")
    return rNom, rPrenom, rMobile, rAdresse


def test_entree(entree):
    res = 0
    i = 0
    while i < 4:
        if entree[i] == "":
            res = NOTHING_WERE_GIVEN
        res = entree
        i += 1
    return res


def detect_nom(nom):
    i = 0
    while i < len(personnes):
        if personnes[i][1] == nom:
            return i
        i += 1
    print("a")
    return -1


def detect_prenom(prenom):
    i = 0
    while i < len(personnes):
        if personnes[i][0] == prenom:
            return i
        i += 1
    print("a")
    return -1


def detect_adresse(adresse):
    i = 0
    while i < len(personnes):
        if personnes[i][3] == adresse:
            return i
        i += 1
    print("a")
    return -1
