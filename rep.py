# Maël QUERRÉ
# Vincent DE MENEZES
# Antoine VINCIGUERRA

ERR_FILE_NAME = 0


def liste_prenom_nom(liste):
    lst = []
    for x in liste:
        contact = x.split(";")
        lst.append(contact[0] + " " + contact[1])
    return lst


def liste_contacts(fichier):
    try:
        file = open(fichier, "r")
        lines = file.readlines()
        file.close()
    except IOError:
        return ERR_FILE_NAME
    else:
        lst = []
        for line in lines:
            lst.append(line)
        return lst


def liste_anniversaire(fichier, mois):
    try:
        file = open(fichier, "r")
        lines = file.readlines()
        file.close()
    except IOError:
        return ERR_FILE_NAME
    else:
        lst = []
        for line in lines:
            x = line.split(";")
            if line != "" and line != '\n' and x[4] != "" and x[4] != '\n':
                if int(x[4][3:5]) == mois:
                    lst.append(line)
        return lst


def liste_telephone(fichier, numero):
    try:
        file = open(fichier, "r")
        lines = file.readlines()
        file.close()
    except IOError:
        return ERR_FILE_NAME
    else:
        lst = []
        for line in lines:
            x = line.split(";")
            if line != "" and line != '\n' and x[2] != "":
                if x[2] == numero:
                    lst.append(line)
        return lst


def liste_nom(fichier, prenom, nom):
    try:
        file = open(fichier, "r")
        lines = file.readlines()
        file.close()
    except IOError:
        return ERR_FILE_NAME
    else:
        lst = []
        for line in lines:
            x = line.split(";")
            if line != "" and line != '\n':
                if x[0] == prenom and x[1] == nom:
                    lst.append(line)
                if prenom == "" and x[1] == nom:
                    lst.append(line)
        return lst



def ajout_contact(contact, fichier):
    t = 1  # variable permettant de tester si l'on veut ajouter le contact
    prenom, nom = contact[0], contact[1]
    anniv = contact[4]
    if anniv[-1] == '\n':
        anniv, contact[4] = anniv[:-1], anniv[:-1]
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
                g = input("Ce contact existe déjà. Souhaitez-vous ajouter ces informations quand même ? (y/n) [y] : ")
                if g != "y" and g != "":
                    t = 0
                writableFile.write(line)
            else:
                writableFile.write(line)
        if t == 1:
            i = 0
            while i < len(contact) - 1:
                writableFile.write(contact[i] + ";")
                i += 1
            writableFile.write(contact[i] + '\n')
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


def suppression_contact(index, contact, fichier):
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
            if i != index:
                writableFile.write(line)
            i += 1
        writableFile.close()