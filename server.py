from flask import Flask, render_template, redirect, url_for

from forms import TeamForm, ProjectForm
from model import User, Team, Project, connect_to_db

app = Flask(__name__)

app.secret_key = "secret key 69" #creates the secret key used by the token.

user_id = 1

@app.route("/") #route for home page
def home():
    team_form = TeamForm() #assigns the TeamForm to the team_form variable. 
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)
    return render_template("home.html", team_form = team_form, project_form = project_form) #renders the html template, and inserts the TeamForm and ProjectForm forms.

@app.route("/add-team", methods=["POST"]) #creates the add_team endpoint, as a post method.
def add_team():
    team_form = TeamForm() #assigns TeamForm to a variable.

    if team_form.validate_on_submit(): #checks that all form validators are met.
        print(team_form.team_name.data) #prints data from new team.
        return redirect(url_for("home")) #redirects to home page
    else:
        return redirect(url_for("home"))

@app.route("/add-project", methods=["POST"])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)

    if project_form.validate_on_submit():
        print(project_form.project_name.data)
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug = True, port = 8000, host = "localhost")