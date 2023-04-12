from flask import Flask, render_template
from forms import TeamForm

app = Flask(__name__)

app.secret_key = "secret key 69" #creates the secret key used to validate tokens later on.

@app.route("/") #route for home page
def home():
    team_form = TeamForm() #assigns the TeamForm to the team_form variable. 
    
    return render_template("home.html", team_form = team_form) #renders the html template, and inserts the TeamForm form.







if __name__ == "__main__":
    app.run(debug = True)