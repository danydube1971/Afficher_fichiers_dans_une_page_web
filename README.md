# Afficher_fichiers_dans_une_page_web

Le script utilise Flask pour créer une application Web qui affiche une liste de fichiers dans le répertoire courant ainsi que les sous-dossiers 
avec leur nom, type, taille et date de modification. Les fichiers sont triés par ordre alphabétique et affichés 
dans un tableau d'une page Web. 

Pour utiliser ce script, placer ce script à la racine du dossier des fichiers que vous voulez afficher dans la page web. 
Créer un dossier nommé *templates* dans le même dossier que les fichiers à afficher, puis, placez-y le fichier **liste_fichiers.html** dedans. 
Exécuter le script dans un terminal avec la commande: **python3 "Liste des fichiers.py"**

Testé dans Linux Mint 21

Voici une description détaillée de ce que fait le script :

1. Tout d'abord, le script importe les modules nécessaires : os, datetime et Flask.
2. Le script initialise une instance de l'application Flask en utilisant Flask(__name__).
3. Le décorateur @app.route('/') crée une route pour l'URL racine /. Lorsque l'application reçoit une demande pour cette URL, la fonction list_files() est appelée.
4. La fonction list_files() utilise la fonction os.getcwd() pour obtenir le répertoire courant dans lequel se trouve le script Python.
5. En utilisant la fonction os.listdir(current_dir), la fonction crée une liste de tous les fichiers dans le répertoire courant.
6. La fonction crée une liste de dictionnaires avec des informations sur les fichiers en utilisant une boucle for pour parcourir tous les fichiers dans la liste des fichiers. Les informations stockées dans chaque dictionnaire sont le nom du fichier, le type de fichier, le poids en megs et la date de modification.
7. Les informations stockées dans chaque dictionnaire sont triées par ordre alphabétique par nom de fichier en utilisant la méthode sort().
8. La fonction rend le modèle HTML en utilisant la méthode render_template() de Flask et en passant la liste des fichiers triés dans le modèle.
9. Enfin, le script démarre le serveur de développement Flask en utilisant app.run(debug=True).

