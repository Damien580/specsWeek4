from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm): #creates the class of forms for the teams table, inherits properties from FlaskForm.
    team_name = StringField('Team_name', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Submit")
    
class ProjectForm(FlaskForm): #creates class of forms for projects table, inherits from FlaskForm.
    project_name = StringField('Project name', validators=[DataRequired(), Length(min=4, max=255)]) #add an input for the project name.
    description = TextAreaField('Description') #adds an input field for a description.
    completed = BooleanField('Completed?') #adds a boolean check to see if completed.
    team_selection = SelectField('Team')
    submit = SubmitField('Submit')

    def update_teams(self, teams): #takes in the self argument, as well as teams, to update a projects team info.
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams ] #creates the selections for choosing a projects team(s).
    
class ProjectUpdateForm(FlaskForm):
    project_name = StringField('Project Name', validators=[DataRequired(), Length(min=4, max=255)]) #add an input for the project name.
    description = TextAreaField('Description') #adds an input field for a description.
    completed = BooleanField('Completed?') #adds a boolean check to see if completed.
    team_selection = SelectField('Team')
    submit = SubmitField('Submit')
    
    def re_update_teams(self, teams): #takes in the self argument, as well as teams, to update a projects team info.
        self.team_selection.choices = [ (team.id, team.team_name) for team in teams ] #creates the selections for choosing a projects team(s).
        
class TeamUpdateForm(FlaskForm): #creates the class of forms for the teams table, inherits properties from FlaskForm.
    team_name = StringField('Team_name', validators=[DataRequired(), Length(min=4, max=255)])
    submit = SubmitField("Submit")      

class DeleteForm(FlaskForm):
    delete_item_select = SelectField('Name:')
    submit = SubmitField('Delete')
    
    def update_delete(self, projects):
        self.delete_item_select.choices = [ (project.id, project.project_name) for project in projects ]

class TeamDeleteForm(FlaskForm):
    delete_team_select = SelectField('Name')
    submit = SubmitField('Submit')
    
    def update_team_delete(self, teams):
        self.delete_team_select.choices = [ (team.id, team.team_name) for team in teams ]