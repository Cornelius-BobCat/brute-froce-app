import streamlit as st

code_1 = ''' import streamlit as st
import itertools
import time
import string '''

code_2 = ''' def AinB(A, B):
    for char in A:
        if char not in B:
            return False

    return True'''

code_3 = '''def deviner_mot_de_passe(chaine_a_tester,selected_option):

    compteur = 0
    compteur_widget = st.empty() 
    # Liste des options possibles
    if selected_option == "Chiffres": 
        caracteres_possibles = string.digits 
    elif selected_option == "Chiffres & Lettres":
        caracteres_possibles = string.digits+string.ascii_letters
    else:
        caracteres_possibles = string.printable 

    if AinB(chaine_a_tester, caracteres_possibles):
       
        for longueur in range(1, len(chaine_a_tester) + 1): 
            for tentative in itertools.product(caracteres_possibles, repeat=longueur):
                compteur += 1 # addition compteur
                if len(chaine_a_tester) > 3 and (compteur % 1000) == 0:
                    time.sleep(0.001)
                    compteur_widget.text(f"Nombre de tentatives : {compteur}")

                elif len(chaine_a_tester) <= 3 and (compteur % 100) == 0:
                    # si la chaise a tester est inf ou egale a 3 on module sur 100
                    time.sleep(0.001)
                    compteur_widget.text(f"Nombre de tentatives : {compteur}")

                mot_tentatif = "".join(tentative)
                if mot_tentatif == chaine_a_tester: 
                    st.write("<span style='color:green;font-size:50px'>"+mot_tentatif+"</span>", unsafe_allow_html=True)
                    compteur_widget.text(f"Nombre de tentatives : {compteur}") 
                    break
    else:
        st.write('Il faut tester sur la bonne chaine') '''
code_3_1 = '''
# DETAILS DE LA FONCTION deviner_mot_de_passe():
string.digits  # nombre
string.digits+string.ascii_letters # nombre + lettre Maj et Min
string.printable # l'ensemble des caractéres possible
'''
code_3_2 = '''
# DETAILS DE LA FONCTION deviner_mot_de_passe():
#permet de retourner toutes les combinaisons possibles de tous les éléments des itérables.
for tentative in itertools.product(caracteres_possibles, repeat=longueur):
    '''
code_3_3 = '''
    # DETAILS DE LA FONCTION deviner_mot_de_passe():
    # si chaine à tester sup a 3 caractéres (1000) modulo == 0 alors on affiche les boucles de 1000 en 1000
    if len(chaine_a_tester) > 3 and (compteur % 1000) == 0:
    # si chaine à tester inf ou egal a 3 caractéres (100) modulo == 0 alors on affiche les boucles de 100 en 100
    elif len(chaine_a_tester) <= 3 and (compteur % 100) == 0:
'''
code_3_4='''
# DETAILS DE LA FONCTION deviner_mot_de_passe():
# a chaque boucle on remplit notre contenaire avec la nouvelle valeur de compteur
compteur_widget.text(f"Nombre de tentatives : {compteur}")'''

code_4 = ''' 
    options = ["Chiffres", "Chiffres & Lettres", "Full Printable"]
    selected_option = st.selectbox("Choisissez une option", options) 

    mdp = st.text_input("Entrez le mot à deviner :")'''

code_5 = ''' 
 if st.button("Tester son Mot de Passe en Brute de Force"):
        if mdp and selected_option:
            deviner_mot_de_passe(mdp,selected_option)
        else:
            st.write("Veuillez entrer un mot de passe à deviner")
            '''


st.image("img/vincent.png",width=100)
st.markdown('[Linkedin](https://www.linkedin.com/in/corneliusvincent/)')
st.divider() # separateur

st.code(code_1, language="python")
st.write('Importation des bibliothéque')
st.write("Itertools est un module Python standard qui fournit des fonctions pour créer et manipuler des itérateurs, qui sont des objets qui permettent de parcourir des éléments un par un. Le module itertools contient un grand nombre de fonctions qui peuvent être utilisées pour créer des itérateurs qui produisent des séquences de nombres, de permutations, de combinaisons, de groupes et d'autres structures de données utiles.")
st.divider()

st.code(code_2, language="python")
st.write("permet de verifier en retournant False ou true si toutes les lettres du string A apparaissent au moins 1 fois dans B")
st.divider()

st.code(code_3, language="python")
st.write("Fonction qui permet de tester toutes les possibilités en fonction de l'option choisi.")
st.code(code_3_1, language="python")
st.code(code_3_2, language="python")
st.code(code_3_3, language="python")
st.code(code_3_4, language="python")
st.divider()

st.code(code_4, language="python")
st.write("Création du select et de input à faire remplir par l'utilisateur")
st.divider()

st.code(code_5, language="python")
st.write("Création du button dans le if , si ca renvoit True on lance la fonction")
st.write("Sinon on affiche le contenu de la bouce else:")
st.divider()
