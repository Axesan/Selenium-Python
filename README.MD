

# Prise en main de selenium 
Docs : https://selenium-python.readthedocs.io/ 


Executer cette commande pour installer sélénium : 
- **$ pip install selenium**

# A propos : 

Selenium est un outil d’automatisation de test pour le web. Il permet de créer des « robots » qui naviguent dans des pages webs comme le ferait un vrai utilisateur. Bien que le premier rôle de Selenium soit le testing de pages webs (développement web), cet outil est beaucoup utilisé pour l’extraction de données . 


# Installation de driver : 

- **Firefox :** https://github.com/mozilla/geckodriver/releases (*Utilisé dans notre exemple*)
- **Google :** https://sites.google.com/chromium.org/driver/
- **Edge :** https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
- **Safary :** https://webkit.org/blog/6900/webdriver-support-in-safari-10/ 

Une fois le driver installé mettez le dans la racine du projet *( Libre à vous d'organiser sa comme vous le souhaiter )*

# **Projet-Axesan** :

## Fonctionnalités  : 
  - Ouverture du navigateur avec la page souhaiter à partir de l'url . 
  - Détecter le click sur une balise *<button>* . 
  - Récupérer les informations d'une balise <h4> *(Dans notre exemple on selectionne le nom du produit ainsi que sont prix et ça catégorie)*
  - Affichage du résultats . 
