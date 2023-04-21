import streamlit as st
import itertools
import time
import string 
def AinB(A, B):
    for char in A:
        if char not in B:
            return False

    return True

def deviner_mot_de_passe(chaine_a_tester,selected_option):
    """

    Fonction brute de force pour trouver une chaine de caractére
    
    """
    compteur = 0 # ini compteur
    compteur_widget = st.empty() # definit un contenaire
    # Liste des options possibles
    if selected_option == "Chiffres": 
        caracteres_possibles = string.digits # define digits (012345566789)
    elif selected_option == "Chiffres & Lettres":
        caracteres_possibles = string.digits+string.ascii_letters # define ( lettre Lower et Upper + degits)
    else:
        caracteres_possibles = string.printable # sinon tout les caractéres

    if AinB(chaine_a_tester, caracteres_possibles):
        # verifie la chaine des possibles contient au moins une fois la chaine a tester
        
        for longueur in range(1, len(chaine_a_tester) + 1): # longueur sur itérable chaine à tester
            for tentative in itertools.product(caracteres_possibles, repeat=longueur):
                # produit des tuples contenant toutes les combinaisons possibles d'un ensemble de valeurs donné
                compteur += 1 # addition compteur

                if len(chaine_a_tester) > 3 and (compteur % 1000) == 0:
                    # si la chaise a tester et supérieur à 3 on module sur 1000 
                    time.sleep(0.001)
                    compteur_widget.text(f"Nombre de tentatives : {compteur}")

                elif len(chaine_a_tester) <= 3 and (compteur % 100) == 0:
                    # si la chaise a tester est inf ou egale a 3 on module sur 100
                    time.sleep(0.001)
                    compteur_widget.text(f"Nombre de tentatives : {compteur}")

                mot_tentatif = "".join(tentative)
                if mot_tentatif == chaine_a_tester: # si le try egale la chaine a tester
                    st.write("<span style='color:green;font-size:50px'>"+mot_tentatif+"</span>", unsafe_allow_html=True) # affiche le mot trouvé
                    compteur_widget.text(f"Nombre de tentatives : {compteur}") # on affiche le compteur avec le reste en plus ( modulo)
                    break
    else:
        st.write('Il faut tester sur la bonne chaine')

##########################################################################


st.header('Brute de Force') # titre de app
st.divider() # séparateur

col1, col2 = st.columns(2)

with col1:
    
    txt = "Les attaques par brute-force consistent à trouver un mot de passe ou une clé à travers des tentatives successives. Il s'agit donc de casser le mot de passe en tentant des combinaisons successives jusqu'à trouver la bonne."
    st.write(txt) # explication de la brute force
    st.markdown("***Comment ca marche ?***") # markdown comment select / options
    st.write("Evaluez le nombre d'essais possible en fonction du mot de passe et de la chaine des caractéres des possible pour briser votre mot de passe")

with col2:

    options = ["Chiffres", "Chiffres & Lettres", "Full Printable"] # option des valeurs a comparer
    selected_option = st.selectbox("Choisissez une option", options) # selection des valeurs

    mdp = st.text_input("Entrez le mot à deviner :") # mot de passe

    # Créer un bouton pour démarrer la devinette
    if st.button("Tester son Mot de Passe en Brute de Force"):
        # Vérifier que l'utilisateur a entré un mot de passe à deviner
        if mdp and selected_option:
            deviner_mot_de_passe(mdp,selected_option)
        else:
            st.write("Veuillez entrer un mot de passe à deviner")
st.divider()
st.subheader("temps d'obtention d'une chaine par Brute Froce en 2022")
st.image("img/tab.png")
st.divider()
st.write("Les attaques par force brute évoluent et se basent désormais sur des dictionnaires de mots de passe")
st.write("Ce qui réduit considérablement le temps de crack de la chaine")

