from flask import Flask, render_template, redirect, url_for

from forms import TeamForm, ProjectForm, ProjectUpdateForm, TeamUpdateForm, DeleteForm
from model import db, User, Team, Project, connect_to_db

app = Flask(__name__)

app.secret_key = "secret key 69" #creates the secret key used by the token.

user_id = 1


@app.route("/") #route for home page
def home():
    team_form = TeamForm() #assigns the TeamForm to the team_form variable. 
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)
    return render_template("home.html", team_form = team_form, project_form = project_form) #renders the html template, and inserts the TeamForm and ProjectForm forms.


@app.route("/add-project", methods=["POST"])
def add_project():
    project_form = ProjectForm()
    project_form.update_teams(User.query.get(user_id).teams)

    if project_form.validate_on_submit():
        project_name = project_form.project_name.data
        description = project_form.description.data
        completed = project_form.completed.data
        team_selection = project_form.team_selection.data
        new_project = Project(project_name, description, completed, team_selection)
        with app.app_context():
            db.session.add(new_project)
            db.session.commit()
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))
    
@app.route("/all-projects")
def all_projects():
    project_list = Project.query.all()
    project_update_form = ProjectUpdateForm()
    project_update_form.re_update_teams(User.query.get(user_id).teams)
    project_delete_form = DeleteForm()
    project_delete_form.update_delete(Project.query.all())
    return render_template("all_projects.html", project_list = project_list, project_update_form = project_update_form, project_delete_form = project_delete_form)

@app.route("/update-project", methods=["POST"])
def update_project():
    project_update_form = ProjectUpdateForm()
    project_update_form.re_update_teams(User.query.get(user_id).teams)
    
    if project_update_form.validate_on_submit():
        project_name = project_update_form.project_name.data
        description = project_update_form.description.data
        completed = project_update_form.completed.data
        team_selection = project_update_form.team_selection.data
        updated_project = Project(project_name, description, completed, team_selection)
        with app.app_context():
            db.session.add(updated_project)
            db.session.commit()
        return redirect(url_for("all_projects"))
    else:
        return redirect(url_for("all_projects"))

@app.route("/add-team", methods=["POST"]) #creates the add_team endpoint, as a post method.
def add_team():
    team_form = TeamForm() #assigns TeamForm to a variable.
    
    if team_form.validate_on_submit(): #checks that all form validators are met.
        team_name = team_form.team_name.data
        new_team = Team(team_name, user_id)
        with app.app_context():
            db.session.add(new_team)
            db.session.commit()
        return redirect(url_for("home")) #redirects to home page
    else:
        return redirect(url_for("home"))

@app.route("/all-teams")
def all_teams():
    team_list = Team.query.filter_by(user_id = user_id).all()
    team_update_form = TeamUpdateForm()
    
    return render_template("all_teams.html", team_list = team_list, team_update_form = team_update_form)
    
@app.route("/update-team", methods=["POST"])
def update_team():
    team_update_form = TeamUpdateForm()
    
    if team_update_form.validate_on_submit(): #checks that all form validators are met.
        team_name = team_update_form.team_name.data
        new_team = Team(team_name, user_id)
        with app.app_context():
            db.session.add(new_team)
            db.session.commit()
        return redirect(url_for("all_teams")) 
    else:
        return redirect(url_for("all_teams"))
    
@app.route("/project-delete", methods=["POST"])
def project_delete():
    project_delete_form = DeleteForm()
    project_delete_form.update_delete(Project.query.all())
    
    if project_delete_form.validate_on_submit():
        project_id = project_delete_form.delete_item_select.data 

        new_delete = Project.query.get(project_id)
        db.session.delete(new_delete)
        db.session.commit()
        return redirect(url_for("all_projects"))
    else:
        return redirect(url_for("all_projects"))

# @app.route("/team-delete", methods=("POST"))
# def team_delete():
    



if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug = True, port = 8000, host = "localhost")


