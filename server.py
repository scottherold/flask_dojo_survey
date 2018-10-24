from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['inputName']
    dojo = request.form['inputDojo']
    language = request.form['inputLanguage']
    comment = request.form['inputComment']
    return render_template("submitted.html", name=name, dojo=dojo, language=language, comment=comment)

if __name__=="__main__":
    app.run(debug=True)