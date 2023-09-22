# tout importer depuis tkinter
from tkinter import *

#importer notre boite de message de mb depuis Tkinter
from tkinter import messagebox as mb

#import json pour utiliser le fichier json pour les donnees
import json



#Notre classe pour définir les composants de notre application

class Quiz:

    def __init__(self):

        self.question_no = 0

        self.afficher_titre()
        self.afficher_questions()

        self.choix_selection = IntVar()

        self.option_choix = self.rd_boutons()

        self.afficher_options()

        self.btn()

        self.taille_donne=len(question)

        self.correction = 0


    def affiche_resultat(self):

        #Calculer les mauvaises reponses
        mauvaise_reponse = self.taille_donne - self.correction
        correction = f" Correct : {self.correction} "
        mauvaise = f" Mauvaise reponse : {mauvaise_reponse} "


        #Calculer le pourcentage des bonne reponses
        score  = int (self.correction / self.taille_donne * 100)
        resultat = f"Score : {score} %"

        #Afficher les resultats
        mb.showinfo(" Resutat ", f" {resultat} \n {correction} \n {mauvaise}")



    #Fonction de verification
    def verification(self, question_no):
        if self.choix_selection.get() == reponse[question_no]:
            return True



    #Fonction boutons suivante
    def btn_suivant(self):

        if self.verification(self.question_no):

            self.correction += 1

        self.question_no += 1


        if self.question_no == self.taille_donne:

            self.affiche_resultat()

            fen.destroy()
        else:
            self.afficher_questions()
            self.afficher_options()

    def btn(self):


        # Bouton pour appeler les question suivantes
        btnSuivant = Button(fen, text=" Suivant ", command=self.btn_suivant,
                             width=10, bg="#89CA78", fg="white", font=("ariel", 16, "bold"))


        btnSuivant.place(x=500, y=280)




    #Fonction les reponse aux choix
    def afficher_options(self):
        valeur = 0

        self.choix_selection.set(0)


        for option in choix[self.question_no]:
            self.option_choix[valeur]['text'] = option
            valeur +=1


    #Fonction pour les questions
    def afficher_questions(self):

        lblquestion = Label(fen, text=question[self.question_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w',bg = "#091821", fg="white" )


        lblquestion.place(x=70, y=100)

    # Methode affichage pour le titre de l'application
    def afficher_titre(self):


        lblTitre = Label(fen,bd = 20, relief = RIDGE, text="CONNAISSANCE GENERALE QUIZ", bg="#373e80", fg="white", font=("ariel", 20, "bold"))


        lblTitre.place(x=0, y=0,
                      width=800)


    #Fontion pour nos reponse afficher dans des radio boutons
    def rd_boutons(self):

        # mettre la liste a 0
        question_list = []

        # position y ordonnee
        y_pos = 150

        # ajouter les options a nos question
        while len(question_list) < 4:

            radio_btn = Radiobutton(fen, text=" ", variable=self.choix_selection,
                                    value=len(question_list) + 1, bg = "#091821", fg="#ECFF8B", font=("ariel", 14))

            # ajouter les radio boutons dans la liste
            question_list.append(radio_btn)

            # palcer les radio boutons dans la liste
            radio_btn.place(x=100, y=y_pos)

            # incrementer les radios boutons sur notre axe des y de ...
            y_pos += 40


        return question_list







# creation de ma fenetre
fen = Tk()

# définir la taille de notre fenetre
fen.geometry("800x400+300+200")

#définir le tirtre de notre fenetre
fen.title("Quiz Demo Json")

#si on veut diminuer ou pas notre fenetre
fen.resizable(False, False)
#Couleur
fen.configure(background = "#091821")

# récupère les données du fichier json
with open('donne.json') as f:
    donnee = json.load(f)

# définir la question, les options et la réponse
question = (donnee['question'])
choix = (donnee['choix'])
reponse = (donnee['reponse'])


# crée un objet de notre classe QuizzDemo
Quizz = Quiz()

#demarage de notre application
fen.mainloop()


