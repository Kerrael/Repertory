from datetime import date

aujourdhui = date.today()
moisCourant = aujourdhui.month


# p0 = ["Prénom", "NOM", "Numéro mobile", "Adresse", "Date de naissance"]

# p1 = ["Maël", "QUERRÉ", "0649782912", "Saint-Contest", "09/09/1996"]
# p2 = ["Vincent", "DE MENEZES", "0601010101", "Clamart", ""]
# p3 = ["Gabriel", "FAURÉ", "", "Pamiers", "12/05/1845"]
# p4 = ["Claude", "DEBUSSY", "0602020202", "Saint-Germain-en-laye", "22/08/1862"]
# p5 = ["Frédéric", "CHOPIN", "", "Żelazowa Wola", "01/03/1810" ]
# p6 = ["Jean-Sébastien", "BACH", "", "Eisenach", "31/03/1685"]

# personnes = [p1, p2, p3, p4, p5, p6]

OK = 0
WRONG_INPUT = 1
NOTHING_WERE_GIVEN = 2
NO_MATCH_FOUND = 3
ERROR_BIRTHDAY = 4


def main():
    creer_liste_contacts()
    saisieChoix = saisie()
    testChoix = test_choix(saisieChoix)
    result(testChoix)


def creer_liste_contacts():
    file = open("contacts.txt", "r")
    lines = file.readlines()
    lst = []
    elem = ""
    i = 0
    while i < len(lines):
        j = 0
        while j < len(lines[i]):
            while lines[i][j] != '\n':
                elem = ""
                while lines[i][j] != " ":
                    elem += lines[i][j]
                    j += 1
                lst.append(elem)
                j += 1
        i += 1
    print(lst)

    file.close()


# def creer_liste_contacts():
#     file = open("contacts.txt", "r")
#     res = file.readlines()
#     print(res)
#     print(res[2])
#     chaine = ""
#     lst = []
#     i = 0
#     j = 0
#     while i < len(res):
#         if res[i] == '\n':
#             lst.append(creer_liste(chaine))
#             chaine = ""
#             j = 0
#         elif res[i] != chr(47):
#             chaine += res[i]
#         i += 1
#         j += 1
#     file.close()


def creer_liste(chain):
    i = 0
    lst = []
    lst.append(chain)
    while i < len(chain):
         lst.append(chain[i])
         i += 1
    print("lol", lst)
    return lst


def saisie():
    """Fonction demandant un choix à l'utilisateur.
    Fonction présentant une liste d'actions à réaliser sur le répertoire.
    :return: Le choix de l'utilisateur.
    :rtype: Une chaîne de caractère(s).
    """
    print("Que souhaitez-vous faire ?")
    print("- rechercher une personne par nom et prénom ? (p)")
    print("- rechercher une personne ayant un numéro de téléphone donné ? (t)")
    print("- rechercher une personne dont l'anniversaire tombe pendant le mois courant ? (an)")
    print("- ajouter un contact ? (aj)")
    print("- modifier des informations ? (m)")
    print("- supprimer des informations ? (sup)")
    choix = input("Réponse : ")
    return choix


def test_choix(choix):
    """Vérifie le type du paramètre 'choix'.
    Teste si le choix correspond à ce qui est demandé.
    :param choix: Le choix de l'utilisateur.
    :return: Le choix de l'utilisateur.
    :rtype: Une chaîne de caractères.
    """
    testInput = test_input(choix)
    while testInput != OK:
        print(message_erreur(testInput))
        choix = saisie()
        testInput = test_input(choix)
    return choix


def test_input(choix):
    if choix == "":
        return NOTHING_WERE_GIVEN
    if choix != "p" and choix != "t" and choix != "an" and choix != "aj" and choix != "m" and choix != "sup":
        return WRONG_INPUT
    return OK


def result(choix):
    if choix == "p":
        saisieNom = saisie_nom_prenom()
        testNom = test_nom(saisieNom[0], saisieNom[1])
        while testNom != OK:
            print(message_erreur(testNom))
            saisieNom = saisie_nom_prenom()
            testNom = test_nom(saisieNom[0], saisieNom[1])
        afficher_contact(saisieNom[0], saisieNom[1])
    if choix == "t":
        afficher_contacts_telephone()
    if choix == "an":
        testAnniversaire = test_anniversaire()
        if testAnniversaire != OK:
            print(message_erreur(testAnniversaire))
        else:
            afficher_contacts_anniversaire()
    if choix == "aj":
        saisieContact = saisie_contact()
        ajout_contact(saisieContact)
    # if choix == "m":
    #     choixContact = choix_contact()


def saisie_contact():
    prenom = input("Ajouter un prénom : ")
    nom = input("Ajouter un nom : ")
    mobile = input("Ajouter un numéro de mobile : ")
    adresse = input("Ajouter une adresse : ")
    naissance = input("Ajouter une date de naissance : ")
    return [prenom, nom, mobile, adresse, naissance]


def ajout_contact(contact, fichier):
    file = open
    personnes += [contact]


def saisie_nom_prenom():
    nom = input("Nom de la personne à rechercher : ")
    prenom = input("Prénom de la personne à rechercher : ")
    return nom, prenom


def test_nom(nom, prenom):
    pos = detect_contact(nom, prenom)
    if pos == ():
        return NO_MATCH_FOUND
    return OK


def test_anniversaire():
    pos = detect_anniversaire()
    if pos == ():
        return ERROR_BIRTHDAY
    return OK


def afficher_contact(nom, prenom):
    pos = detect_contact(nom, prenom)
    for p in pos:
        pers = ""
        i = 0
        while i < len(p0):
            if personnes[p][i] != "":
                pers += "  " + personnes[p][i]
            i += 1
        print(pers)


def afficher_contacts_telephone():
    pos = detect_telephone()
    for p in pos:
        pers = ""
        i = 0
        while i < len(p0):
            if personnes[p][i] != "":
                pers += "  " + personnes[p][i]
            i += 1
        print(pers)


def afficher_contacts_anniversaire():
    pos = detect_anniversaire()
    for p in pos:
        pers = ""
        i = 0
        while i < len(p0):
            if personnes[p][i] != "":
                pers += "  " + personnes[p][i]
            i += 1
        print(pers)


def detect_contact(nom, prenom):
    pos = ()
    i = 0
    while i < len(personnes):
        if personnes[i][0] == prenom and personnes[i][1] == nom:
            pos += (i,)
        i += 1
    return pos


def detect_telephone():
    pos = ()
    i = 0
    while i < len(personnes):
        if personnes[i][2] != "":
            pos += (i,)
        i += 1
    return pos


def detect_anniversaire():
    pos = ()
    i = 0
    while i < len(personnes):
        if personnes[i][4][3:5] != "":
            if int(personnes[i][4][3:5]) == moisCourant:
                pos += (i,)
        i += 1
    return pos


def message_erreur(n):
    tabErreurs = ["OK",
                  "Mauvaise saisie",
                  "Aucun choix n'a été donné",
                  "Pas de résultat trouvé",
                  "Aucun contact ne fête son anniversaire pendant le mois courant"]
    return tabErreurs[n]


main()
