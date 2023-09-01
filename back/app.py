# https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application

# from flask import Flask, render_template
from flask import Flask, render_template, request # Importez 'request' pour gérer les requêtes HTTP
from datetime import datetime
from mocks import Post
from flask_sqlalchemy import SQLAlchemy


# Créez une instance de l'application Flask
app = Flask(__name__)

# db = SQLAlchemy(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///back/database/db.sqlite3"


# Context processor pour injecter la variable 'now' dans les modèles
@app.context_processor
def inject_now():
    return {'now': datetime.now()} # ou on  peut ecrire : return dict(new =datetime.now())

# C.P pour définir la fonction 'pluralize'
@app.context_processor
def utility_processor(): 
    def pluralize(count, singular, plural=None):
        if not isinstance(count, int):
            raise ValueError('"{}" count must be an integer'.format(count))

        if plural is None:
            plural = singular + 's'

        if count == 1:
            string = singular
        else:
            string = plural
        return "{} {}".format(count, string)
    return dict(pluralize=pluralize)

# Définissez les routes (et les fonctions de vue)

# Page d'accueil
@app.route('/')
def home():
    return render_template('pages/home.html')

# Page "À propos"
@app.route('/about')
def about():
    return render_template('pages/about.html')# Ajout de l'extension .html

# Page de contact
@app.route('/contactus')
def contactus():
    return render_template('pages/contactus.html')

# -----------------


# Page de calculate_heart_rate
@app.route('/calculate_heart_rate', methods=['GET', 'POST'])
def calculate_heart_rate():
    if request.method == 'POST':
        age = int(request.form['age'])
        intensite_exercice = request.form['intensite_exercice']
        
        # Effectuez les calculs de fréquence cardiaque ici
        freq_cardiaque_maximale = 220 - age
        if intensite_exercice.lower() == "faible":
            freq_cardiaque_cible = 0.5 * freq_cardiaque_maximale
        elif intensite_exercice.lower() == "moyen":
            freq_cardiaque_cible = 0.7 * freq_cardiaque_maximale
        elif intensite_exercice.lower() == "élevé":
            freq_cardiaque_cible = 0.85 * freq_cardiaque_maximale
        else:
            return "Niveau d'intensité invalide. Veuillez choisir parmi faible, moyen ou élevé."

        # Passez les résultats à afficher dans le modèle HTML de résultat
        return render_template('pages/result.html', age=age, intensite_exercice=intensite_exercice, freq_cardiaque_maximale=freq_cardiaque_maximale, freq_cardiaque_cible=freq_cardiaque_cible)

    # Si la méthode est GET, affichez simplement le formulaire
    return render_template('pages/heart_rate.html')

# ----------------------

# Gestionnaire d'erreur 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

# Liste des articles de blog
@app.route('/blog')
def posts_index():
    posts= Post.all()
    return render_template('posts/index.html', posts=posts)

# Affiche un article de blog spécifique '<int:id>'
@app.route('/index/posts/<int:id>')
def posts_show(id):
    post = Post.find(id)
    return render_template('posts/show.html', post=post)
    

# Point d'entrée pour l'exécution de l'application
if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        app.run(debug =True, port =3000)
    