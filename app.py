from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    nom_complet = None
    if request.method == 'POST':
        # On récupère les données du formulaire
        prenom = request.form.get('prenom')
        nom = request.form.get('nom')
        nom_complet = f"{prenom} {nom}"
    
    return render_template('index.html', resultat=nom_complet)

if __name__ == '__main__':
    app.run(debug=True)