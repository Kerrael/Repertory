# Maël QUERRÉ
# Vincent DE MENEZES
# Antoine VINCIGUERRA


from datetime import date

aujourdhui = date.today()
moisCourant = aujourdhui.month

_repertory = "contacts.txt"  # variable privée

OK = 0
WRONG_INPUT = 1
NOTHING_WERE_GIVEN = 2
NO_MATCH_FOUND = 3
NO_BIRTHDAY = 4
ERR_FILE_NAME = 5
ERR_DAY_VALUE = 6
ERR_MONTH_VALUE = 7
ERR_YEAR_VALUE = 8
ERR_BIRTHDATE_FORMAT = 9
ERR_MOBILE_FORMAT = 10


def main():
    global _repertory
    correction_ligne(_repertory)
    saisieChoix = saisie()
    testChoix = test_choix(saisieChoix)
    result(testChoix)


def correction_ligne(fichier):
    try:
        file = open(fichier, "r")
        lines = file.readlines()
        file.close()
    except IOError:
        return ERR_FILE_NAME
    else:
        newFile = open(fichier, "w")
        for line in lines:
            if line[-1] != '\n':
                newFile.write(line + '\n')
            else:
                newFile.write(line)
        newFile.close()


def creer_liste(chain):
    i = 0
    lst = [chain]
    while i < len(chain):
        lst.append(chain[i])
        i += 1
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
    while test_format_choix(choix) != OK:
        print(message_erreur(test_format_choix(choix)))
        choix = saisie()
        test_format_choix(choix)
    return choix


def test_format_choix(choix):
    if choix == "":
        return NOTHING_WERE_GIVEN
    if choix != "p" and choix != "t" and choix != "an" and choix != "aj" and choix != "m" and choix != "sup":
        return WRONG_INPUT
    return OK


def result(choix):
    global _repertory
    global moisCourant
    if choix == "p":
        nameInput = name_input()
        testNom = name_test(nameInput[0], nameInput[1])
        if testNom != OK:
            print(message_erreur(testNom))
        else:
            affiche_contact(nameInput[0], nameInput[1], _repertory)
    if choix == "t":
        affiche_contacts_telephone(_repertory)
    if choix == "an":
        testAnniv = test_anniv(_repertory, moisCourant)
        if testAnniv != OK:
            print(message_erreur(testAnniv))
        else:
            affiche_contacts_anniv(_repertory, moisCourant)
    if choix == "aj":
        contactInput = contact_input()
        ajout_contact(contactInput, _repertory)
    if choix == "m":
        choix_contact(_repertory)


def choix_contact(fichier):
    try:
        file = open(fichier, "r")
        lines = file.readlines()
        file.close()
    except IOError:
        return ERR_FILE_NAME
    else:
        print("Voici les contacts auxquels vous pouvez appliquer des modifications :")
        i = 1
        for line in lines:
            x = line.split(";")
            print(i, x[0], x[1])
            i += 1
        choix = input("Numéro du contact à modifier : ")
        while test_choix_contact(choix) != OK:
            print(message_erreur(test_choix_contact(choix)))
            choix = input("Numéro du contact à modifier : ")
        donnee = input("Saisissez la donnée à modifier : ")


# def test_choix_donnee(donnee):



def test_choix_contact(choix):
    if choix == "":
        return NOTHING_WERE_GIVEN
    if not choix.isdigit():
        return WRONG_INPUT
    return OK


def contact_input():
    prenom = input("Ajouter un prénom : ")
    nom = input("Ajouter un nom : ")
    mobile = input("Ajouter un numéro de mobile : ")
    mobileFormat = mobile_format(mobile)
    while mobileFormat != OK:
        print(message_erreur(mobileFormat))
        mobile = input("Ajouter un numéro de mobile : ")
        mobileFormat = mobile_format(mobile)
    ville = input("Ajouter une ville : ")
    anniv = input("Ajouter une date de naissance (JJ/MM/AAAA) : ")
    annivFormat = anniv_format(anniv)
    while annivFormat != OK:
        print(message_erreur(annivFormat))
        anniv = input("Ajouter une date de naissance (JJ/MM/AAAA) : ")
        annivFormat = anniv_format(anniv)
    return [prenom, nom, mobile, ville, anniv]


def mobile_format(mobile):
    if mobile[0] == "-" or mobile[-1] == "-":
        return ERR_MOBILE_FORMAT
    if not mobile.isdigit():
        for x in mobile:
            if x != "-" and not x.isdigit():
                return ERR_MOBILE_FORMAT
    return OK


def anniv_format(anniv):
    if len(anniv) < 7:
        return ERR_BIRTHDATE_FORMAT
    if anniv[2] != "/" and anniv[5] != "/":
        return ERR_BIRTHDATE_FORMAT
    day, month, year = anniv[:2], anniv[3:5], anniv[6:]
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        return ERR_BIRTHDATE_FORMAT
    if int(day) not in range(1, 32):
        return ERR_DAY_VALUE
    if int(month) not in range(1, 13):
        return ERR_MONTH_VALUE
    if int(year) < 1:
        return ERR_YEAR_VALUE
    return OK


def ajout_contact(contact, fichier):
    t = 0
    prenom, nom = contact[0], contact[1]
    anniv = contact[4]
    try:
        file = open(fichier, "r")
        lines = file.readlines()
        file.close()
    except IOError:
        return ERR_FILE_NAME
    else:
        writableFile = open(fichier, "w")
        for line in lines:
            x = line.split(";")
            if x[0] == prenom and x[1] == nom and x[4][:-1] == anniv:
                t = 1
                g = input("Ce contact existe déjà. Souhaitez-vous ajouter ces informations quand même ? (y/n) [y] : ")
                if g == "y" or g == "":
                    i = 0
                    while i < len(contact):
                        writableFile.write(contact[i] + ";")
                        i += 1
                    writableFile.write('\n')
                else:
                    writableFile.write(line)
            else:
                writableFile.write(line)
        if t == 0:
            i = 0
            while i < len(contact):
                writableFile.write(contact[i] + ";")
                i += 1
            writableFile.write('\n')
        writableFile.close()


def modification_contact(index, contact, fichier):
    try:
        file = open(fichier, "r")
        lines = file.readlines()
        file.close()
    except IOError:
        return ERR_FILE_NAME
    else:
        writableFile = open(fichier, "w")
        i = 0
        for line in lines:
            if i == index:
                writableFile.write(contact)
            else:
                writableFile.write(line)
            i += 1
        writableFile.close()


def name_input():
    prenom = input("Prénom de la personne à rechercher : ")
    nom = input("Nom de la personne à rechercher : ")
    return prenom, nom


def name_test(prenom, nom):
    pos = detect_contact(prenom, nom, _repertory)
    if pos == ():
        return NO_MATCH_FOUND
    return OK


def test_anniv(fichier, mois):
    file = open(fichier, "r")
    lines = file.readlines()
    t = 0
    for line in lines:
        x = line.split(";")
        if line != "" and line != '\n' and x[4] != "" and x[4] != '\n':
            if int(x[4][3:5]) == mois:
                t = 1
    if not t:
        return NO_BIRTHDAY
    return OK


def detect_anniversaire(month, fichier):
    file = open(fichier, "r")
    lines = file.readlines()
    pos = ()
    i = 0
    for line in lines:
        x = line.split(";")
        if int(x[4][3:5]) == month:
            pos += (i,)
        i += 1
    file.close()
    return pos


def affiche_contact(prenom, nom, fichier):
    file = open(fichier, "r")
    lines = file.readlines()
    res = ""
    i = 0
    for line in lines:
        x = line.split(";")
        if x[0] == prenom and x[1] == nom:
            res += line
        i += 1
    print(res)
    file.close()


def affiche_contacts_telephone(fichier):
    pos = detect_telephone(fichier)
    file = open(fichier, "r")
    lines = file.readlines()
    res = ""
    i = 0
    for line in lines:
        if i in pos:
            res += line
        i += 1
    print(res)
    file.close()


def detect_telephone(fichier):
    """Détecte les contacts ayant un numéro de téléphone donné dans un fichier.

    La fonction parcourt le fichier et renvoie les positions des lignes de contacts
    possédant un numéro de téléphone.
    :param fichier: Le nom d'un fichier.
    :return: Les positions des lignes de contacts possédant un numéro de téléphone.
    """
    file = open(fichier, "r")
    lines = file.readlines()
    pos = ()
    i = 0
    for line in lines:
        x = line.split(";")
        if x[2] != "":
            pos += (i,)
        i += 1
    file.close()
    return pos


def affiche_contacts_anniv(fichier, month):
    file = open(fichier, "r")
    lines = file.readlines()
    res = ""
    for line in lines:
        x = line.split(";")
        if line != "" and line != '\n' and x[4] != "" and x[4] != '\n':
            if int(x[4][3:5]) == month:
                res += line
    print(res)
    file.close()


def detect_contact(prenom, nom, fichier):
    file = open(fichier, "r")
    lines = file.readlines()
    pos = ()
    i = 0
    for line in lines:
        x = line.split(";")
        if x[0] == prenom and x[1] == nom:
            pos += (i,)
        i += 1
    file.close()
    return pos


def message_erreur(n):
    tabErreurs = ["OK",
                  "Mauvaise saisie",
                  "Aucun choix n'a été donné",
                  "Pas de résultat trouvé",
                  "Aucun contact ne fête son anniversaire pendant le mois courant",
                  "Fichier introuvable",
                  "Quantième invalide",
                  "Mois invalide",
                  "Année invalide",
                  "Format de date incorrect",
                  "Format de numéro invalide"]
    return tabErreurs[n]


main()
