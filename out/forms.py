from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class FormClientes(FlaskForm):
    id_cliente = StringField('Identificador')
    nome_cliente = StringField('Nome', validators=[DataRequired()])
    telefone_cliente = StringField('celular', validators=[DataRequired()])
    email_cliente = StringField('e-mail', validators=[DataRequired(), Email()])
    senha_cliente = PasswordField('Senha', validators=[DataRequired(), Length(6,16)])
    confirma_senha = PasswordField('Confirmação Senha', validators=[DataRequired(), EqualTo('senha_cliente')])
    botao_cadastracliente = SubmitField('Cadastra Cliente')

