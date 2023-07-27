# https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application
from flask import Flask, render_template
from datetime import datetime
from mocks import Post


# Créez une instance de l'application Flask
app = Flask(__name__)

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
    app.run(debug =True, port =3000)
    