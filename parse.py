import os
import re

def isFormatedUUID(texte):
    pattern = re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$', re.IGNORECASE)
    return bool(pattern.match(texte))

def parcours_recursif(point_entree, mot_recherche):
    # Vérifie si le point d'entrée est un fichier dont le nom contient le mot recherché
    if os.path.isfile(point_entree) and mot_recherche in point_entree:
        print("Fichier trouvé:", point_entree)
    
    # Parcourt les dossiers et fichiers dans le point d'entrée
    if os.path.isdir(point_entree):
        for element in os.listdir(point_entree):
            chemin_complet = os.path.join(point_entree, element)
            if isFormatedUUID(element):
                print("Trouvé:", chemin_complet)
            #if os.path.isdir(chemin_complet) and mot_recherche in element:
            #    print("Dossier trouvé:", chemin_complet)

            # Si c'est un dossier, effectue un parcours récursif
            if os.path.isdir(chemin_complet):
                parcours_recursif(chemin_complet, mot_recherche)
            # Si c'est un fichier et que son nom contient le mot recherché, l'affiche
            elif os.path.isfile(chemin_complet) and mot_recherche in element:
                    print("Fichier trouvé:", chemin_complet)

# Point d'entrée et mot à rechercher
point_entree = "d:\\dev"
mot_recherche = "manifest.xml"

# Appel initial à la fonction
parcours_recursif(point_entree, mot_recherche)
