# Maël QUERRÉ
# Vincent DE MENEZES
# Antoine VINCIGUERRA

from tkinter import *
from datetime import date
from rep import *

_fichierContacts = "contacts.txt"

master = Tk()
master.title("Répertoire de contacts")

aujourdhui = date.today()
moisCourant = aujourdhui.month


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


correction_ligne(_fichierContacts)


def quitter():
    master.quit()
    master.destroy()


# Fonctions des boutons radio avec leur sous-liste
def radio_tout(event):
    cadreListes.grid(row=0)
    lstBoxContacts.grid(row=0)
    yDefilB.grid(row=0, column=1, sticky='ns')
    lstBoxAnniv.grid_forget()
    lstBoxTel.grid_forget()
    lstBoxNom.grid_forget()


def index_tout(event):
    global index
    index = int(lstBoxContacts.curselection()[0])
    inserer_infos(index, lstContacts)


def radio_anniv(event):
    cadreListes.grid(row=0)
    lstBoxAnniv.grid(row=0)
    yDefilB.grid(row=0, column=1, sticky='ns')
    lstBoxContacts.grid_forget()
    lstBoxTel.grid_forget()
    lstBoxNom.grid_forget()


def index_anniv(event):
    global index
    index = int(lstBoxAnniv.curselection()[0])
    if not lstAnniv:
        print("Aucun contact ne fête son anniversaire ce mois ci.")
    else:
        inserer_infos(index, lstAnniv)


def rechercher_bouton():
    global lstTel
    global lstBoxTel
    global lstNom
    global lstBoxNom
    if vR.get() == 3:
        lstTel = liste_telephone(_fichierContacts, numero.get())
        if not lstTel:
            print("Aucun contact possédant ce numéro de téléphone n'a été trouvé")
        lstBoxTel = Listbox(cadreListes, width=40, height=4)
        for element in liste_prenom_nom(lstTel):
            lstBoxTel.insert(END, element)
        radio_telephone(lstBoxTel)
    if vR.get() == 4:
        lstNom = liste_nom(_fichierContacts, recherchePrenom.get(), rechercheNom.get())
        lstBoxNom = Listbox(cadreListes, width=40, height=4)
        for element in liste_prenom_nom(lstNom):
            lstBoxNom.insert(END, element)
        radio_nom(lstBoxNom)


def radio_telephone(lstBox):
    cadreListes.grid(row=0)
    lstBox.grid(row=0)
    yDefilB.grid(row=0, column=1, sticky='ns')
    lstBoxContacts.grid_forget()
    lstBoxAnniv.grid_forget()
    lstBoxNom.grid_forget()
    lstBox.bind('<ButtonRelease-1>', index_telephone)


def index_telephone(event):
    global index
    index = int(lstBoxTel.curselection()[0])
    inserer_infos(index, lstTel)


def radio_nom(lstBox):
    cadreListes.grid(row=0)
    lstBox.grid(row=0)
    yDefilB.grid(row=0, column=1, sticky='ns')
    lstBoxContacts.grid_forget()
    lstBoxAnniv.grid_forget()
    lstBoxTel.grid_forget()
    lstBox.bind('<ButtonRelease-1>', index_nom)


def index_nom(event):
    global index
    index = int(lstBoxNom.curselection()[0])
    inserer_infos(index, lstNom)


def inserer_infos(i, liste):
    contact = liste[i]
    element = contact.split(";")
    saisiePrenom.delete(0, END)
    saisieNom.delete(0, END)
    saisieTel.delete(0, END)
    saisieAdresse.delete(0, END)
    saisieAnniversaire.delete(0, END)
    saisiePrenom.insert(0, element[0])
    saisieNom.insert(0, element[1])
    saisieTel.insert(0, element[2])
    saisieAdresse.insert(0, element[3])
    saisieAnniversaire.insert(0, element[4])


def bouton_modifier_contact():
    prenom = saisiePrenom.get()
    nom = saisieNom.get()
    tel = saisieTel.get()
    adresse = saisieAdresse.get()
    anniv = saisieAnniversaire.get()
    contact = prenom + ";" + nom + ";" + tel + ";" + adresse + ";" + anniv
    return modification_contact(index, contact, _fichierContacts)


def bouton_ajouter_contact():
    prenom = saisiePrenom.get()
    nom = saisieNom.get()
    tel = saisieTel.get()
    adresse = saisieAdresse.get()
    anniv = saisieAnniversaire.get()
    contact = [prenom, nom, tel, adresse, anniv]
    return ajout_contact(contact, _fichierContacts)


def bouton_supprimer_contact():
    prenom = saisiePrenom.get()
    nom = saisieNom.get()
    tel = saisieTel.get()
    adresse = saisieAdresse.get()
    anniv = saisieAnniversaire.get()
    contact = prenom + ";" + nom + ";" + tel + ";" + adresse + ";" + anniv
    return suppression_contact(index, contact, _fichierContacts)


def efface_prenom(event):
    recherchePrenom.delete(0, END)


def efface_nom(event):
    rechercheNom.delete(0, END)


def reboot():
    boutonTout.deselect()
    boutonAnniv.deselect()
    boutonTel.deselect()
    boutonNom.deselect()
    lstBoxAnniv.grid_forget()
    lstBoxTel.grid_forget()
    lstBoxNom.grid_forget()
    yDefilB.grid_forget()


### WIDGETS ###
Label(master, text="Rechercher un contact").grid(row=0)

# Zone de recherche
cadreRecherche = Frame(master)

# Boutons d'options recherche
vR = IntVar()
boutonTout = Radiobutton(cadreRecherche, text="Tout", variable=vR, value=1)
boutonAnniv = Radiobutton(cadreRecherche, text="Anniversaire dans le mois courant", variable=vR, value=2)
boutonTel = Radiobutton(cadreRecherche, text="Numéro de téléphone", variable=vR, value=3)
numero = Entry(cadreRecherche)
boutonNom = Radiobutton(cadreRecherche, text="Prénom et NOM", variable=vR, value=4)
recherchePrenom = Entry(cadreRecherche)
rechercheNom = Entry(cadreRecherche)
recherchePrenom.insert(0, "Prénom")
rechercheNom.insert(0, "NOM")

boutonTout.grid(row=0)
boutonAnniv.grid(row=1)
boutonTel.grid(row=2)
numero.grid(row=2, column=1)
boutonNom.grid(row=3)
recherchePrenom.grid(row=3, column=1)
rechercheNom.grid(row=3, column=2)

boutonTout.select()  # bouton "Tout" sélectionné par défaut

recherchePrenom.bind("<Button-1>", efface_prenom)
rechercheNom.bind("<Button-1>", efface_nom)

boutonRechercher = Button(cadreRecherche, text="Rechercher", command=rechercher_bouton)
boutonRechercher.grid(row=4, columnspan=3)

cadreRecherche.grid(row=1)

# Cadre pour l'affichage des Listboxes
cadreContacts = LabelFrame(master, text="Contacts")
cadreContacts.grid()

# Prévision du cadre où seront affichées les listes déroulantes
cadreListes = Frame(cadreContacts)
cadreListes.grid()

# Liste déroulante pour tous les contacts
lstContacts = liste_contacts(_fichierContacts)
lstBoxContacts = Listbox(cadreListes, width=40, height=4)
for element in liste_prenom_nom(lstContacts):
    lstBoxContacts.insert(END, element)

# Liste déroulante pour la recherche par anniversaires dans le mois courant
lstAnniv = liste_anniversaire(_fichierContacts, moisCourant)
lstBoxAnniv = Listbox(cadreListes, width=40, height=4)
for element in liste_prenom_nom(lstAnniv):
    lstBoxAnniv.insert(END, element)

# Liste déroulante pour la recherche par numéro de télélphone
lstTel = liste_telephone(_fichierContacts, numero.get())
lstBoxTel = Listbox(cadreListes, width=40, height=4)
for element in liste_prenom_nom(lstTel):
    lstBoxTel.insert(END, element)

# Liste déroulante pour la recherche par nom et prénom
lstNom = liste_nom(_fichierContacts, recherchePrenom.get(), rechercheNom.get())
lstBoxNom = Listbox(cadreListes, width=40, height=4)
for element in liste_prenom_nom(lstTel):
    lstBoxNom.insert(END, element)

# Définition de l'ascenseur
yDefilB = Scrollbar(cadreContacts)
yDefilB.config(command=lstBoxContacts.yview)
lstBoxContacts.config(yscrollcommand=yDefilB.set)


# Variable "index" pour récupérer quelle ligne est sélectionnée
index = 0

# Liaisons clic/fonction pour les boutons
lstBoxContacts.bind('<ButtonRelease-1>', index_tout)
lstBoxAnniv.bind('<ButtonRelease-1>', index_anniv)
lstBoxTel.bind('<ButtonRelease-1>', index_telephone)
lstBoxNom.bind('<ButtonRelease-1>', index_nom)

# Liaisons entre les listes déroulantes et une fonction récupérant la ligne du clic
boutonTout.bind('<Button-1>', radio_tout)
boutonAnniv.bind('<Button-1>', radio_anniv)


## Cadre pour les opérations de modification ##
cadreMod = Frame(master)

## Cadre pour les zones d'entrées (saisies)
cadreEntrees = Frame(cadreMod)

## Cadre pour les boutons d'actions
cadreBoutonsActions = Frame(cadreMod)

# Labels de saisie
Label(cadreEntrees, text="Prénom").grid(row=0, sticky='w')
Label(cadreEntrees, text="NOM").grid(row=1, sticky='w')
Label(cadreEntrees, text="Téléphone").grid(row=2, sticky='w')
Label(cadreEntrees, text="Adresse").grid(row=3, sticky='w')
Label(cadreEntrees, text="Anniversaire").grid(row=4, sticky='w')

# Zones de saisie
saisiePrenom = Entry(cadreEntrees)
saisieNom = Entry(cadreEntrees)
saisieTel = Entry(cadreEntrees)
saisieAdresse = Entry(cadreEntrees)
saisieAnniversaire = Entry(cadreEntrees)
saisiePrenom.grid(row=0, column=1)
saisieNom.grid(row=1, column=1)
saisieTel.grid(row=2, column=1)
saisieAdresse.grid(row=3, column=1)
saisieAnniversaire.grid(row=4, column=1)

# Boutons d'actions
boutonModifier = Button(cadreBoutonsActions, text="Modifier", command=bouton_modifier_contact)
boutonAjouter = Button(cadreBoutonsActions, text="Ajouter", command=bouton_ajouter_contact)
boutonSupprimer = Button(cadreBoutonsActions, text="Supprimer", command=bouton_supprimer_contact)
boutonModifier.grid(row=0, column=2)
boutonAjouter.grid(row=1, column=2)
boutonSupprimer.grid(row=2, column=2)

cadreEntrees.grid(row=0)
cadreEntrees.grid(row=0, column=1)
cadreBoutonsActions.grid(row=0, column=2, sticky=S)
cadreMod.grid()

# Bouton quitter
boutonQuitter = Button(master, text="Quitter", command=quitter)
boutonQuitter.grid()

master.mainloop()
