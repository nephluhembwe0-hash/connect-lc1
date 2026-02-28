from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmer le mot de passe', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('S\'inscrire')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mot de passe', validators=[DataRequired()])
    submit = SubmitField('Se connecter')

class PostForm(FlaskForm):
    content = TextAreaField('Contenu', validators=[DataRequired()])
    gdrive_link = StringField('Lien Google Drive (optionnel)')
    submit = SubmitField('Publier')

class ModeForm(FlaskForm):
    mode = SelectField('Choisissez votre mode', choices=[('online', 'Online'), ('offline', 'Offline')])
    submit = SubmitField('Changer de mode')