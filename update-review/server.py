from flask import Flask, render_template

from model import Dinosaur, connect_to_db, db

from forms import DinosaurForm

app = Flask(__name__)
app.secret_key = "super secret"

@app.route("/<name>")
def home(name):
    new_dino = Dinosaur(name=name, herbivore=False)
    db.session.add(new_dino)
    db.session.commit()
    return "welcome home"

@app.route("/update-dino/<dino_id>", methods=["GET", "POST"])
def update_dino(dino_id):
    dino = Dinosaur.query.get(dino_id)
    form = DinosaurForm(obj=dino)

    if form.validate_on_submit():
        name = form.name.data
        herbivore = form.herbivore.data
        dino.name = name
        dino.herbivore = herbivore
        db.session.add(dino)
        db.session.commit()
        return "nice"
    else:
        return render_template("update-dino.html", form=form, dino=dino)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True)