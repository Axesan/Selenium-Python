from re import search
from selenium import webdriver;

# Creer une variable pour déclencher le driver qui ce situe dans la racine du projet au nom 'geckodriver'.
driver = webdriver.Firefox(executable_path="geckodriver.exe"); 
# Dés que le navigateur s'ouvre on et rediriger sur le site
driver.get('http://127.0.0.1:8000/nos-produits');

# on intéragis avec nos elements html par id ou name ou par la class - Ici la barre de recherche de notre site internet E-commerce
search_bar = driver.find_element_by_id('string');
# on envoie l'instruction pour ecrire du texte .
search_bar.send_keys('bonnet');

# On recupere le bouton afin de lancer la recherche sur le site a partir de la class . 
bouton_search = driver.find_element_by_class_name('btn-outline-danger');
# On déclenche le click de notre élément bouton_search 
bouton_search.click();

# On recupere les données des produits pour nous les afficher ne pas oublier le "s" de element qui permet de recuperer toute les class : 
all_title = driver.find_elements_by_class_name('name_product ');
all_price = driver.find_elements_by_class_name('badge.bg-danger');

# RESULT : On parcours cette liste avec une boucle for
print("---------  PRODUITS  --------- \n")
for title in all_title:
    print('****************')
    print(title.text);
    print('***************\n')

print("--------- PRIX -------")
for prix in all_price:
    print(prix.text)
print("----------------------")



