"""Le script utilise Flask pour créer une application Web qui affiche une liste de fichiers dans le répertoire courant 
avec leur nom, type, taille et date de modification. Les fichiers sont triés par ordre alphabétique et affichés dans un 
tableau d'une page Web. 

Pour utiliser ce script, placer ce script à la racine du dossier des fichiers que vous voulez afficher dans la page web. 
Créer un dossier nommé templates dans le même dossier que les fichiers à afficher, puis, placez-y le fichier liste_fichiers.html dedans. 
Exécuter le script dans un terminal avec la commande: python3 Liste des fichiers.py
"""

import os
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def list_files():
    # Obtenir le répertoire courant
    current_dir = os.getcwd()

    # Obtenir une liste de tous les fichiers dans le répertoire courant
    files = os.listdir(current_dir)

    # Créer une liste de dictionnaires avec des informations sur les fichiers
    file_info = []
    for file_name in files:
        file_path = os.path.join(current_dir, file_name)
        file_size = os.path.getsize(file_path) / (1024 * 1024)
        modified_timestamp = os.path.getmtime(file_path)
        modified_datetime = datetime.fromtimestamp(modified_timestamp)
        modified_date = modified_datetime.strftime('%d-%m-%Y')
        file_info.append({
            'name': file_name,
            'type': os.path.splitext(file_name)[1],
            'size': f'{file_size:.2f} MB',
            'modified': modified_date
        })

    # Trier la liste des fichiers par nom
    file_info.sort(key=lambda x: x['name'])

    # Rendre le modèle avec les informations sur les fichiers
    return render_template('liste_fichiers.html', files=file_info)

if __name__ == '__main__':
    app.run(debug=True)

