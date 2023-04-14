from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm): #creates the class of forms for the teams table, inherits properties from FlaskForm.
    team_name = StringField('team_name', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("submit")
    
class ProjectForm(FlaskForm): #creates class of forms for projects table, inherits from FlaskForm.
    project_name = StringField('project name', validators=[DataRequired(), Length(min=4, max=255)]) #add an input for the project name.
    description = TextAreaField('description') #adds an input field for a description.
    completed = BooleanField('completed?') #adds a boolean check to see if completed.
    team_selection = SelectField('team')
    submit = SubmitField('submit')

    def update_teams(self, teams): #takes in the self argument, as well as teams, to update a projects team info.
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams ] #creates the selections for choosing a projects team(s).
    
class ProjectUpdateForm(FlaskForm):
    project_name = StringField('project name', validators=[DataRequired(), Length(min=4, max=255)]) #add an input for the project name.
    description = TextAreaField('description') #adds an input field for a description.
    completed = BooleanField('completed?') #adds a boolean check to see if completed.
    team_selection = SelectField('team')
    submit = SubmitField('submit')
    
    def re_update_teams(self, teams): #takes in the self argument, as well as teams, to update a projects team info.
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams ] #creates the selections for choosing a projects team(s).
        
class TeamUpdateForm(FlaskForm): #creates the class of forms for the teams table, inherits properties from FlaskForm.
    team_name = StringField('team_name', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("submit")      

class DeleteForm(FlaskForm):
    delete_item_select = SelectField('ID', choices = [])
    submit = SubmitField('DELETE')
    
    def update_delete(self, projects):
        self.delete_item_select.choices = [ (project.id, project.project_name) for project in projects ]