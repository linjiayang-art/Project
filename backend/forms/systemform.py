from flask_wtf import FlaskForm
from wtforms import StringField, DateField, FileField,DateTimeField, SelectMultipleField, SubmitField, FieldList, IntegerField, validators
from wtforms.validators import DataRequired, length, NumberRange,ValidationError
from flask_wtf.file import FileRequired, FileAllowed

class MenuFrom(FlaskForm):
    id = IntegerField('id')
    parent_id = IntegerField('parent_id')
    menu_name = StringField('menu_name', validators=[DataRequired()])
    menu_type = StringField('menu_type', validators=[DataRequired()])
    menu_path = StringField('menu_path', validators=[DataRequired()])
    component = StringField('component', validators=[DataRequired()])
    # menu_perm=StringField('menu_perm',validators=[DataRequired()])
    menu_visible = StringField('menu_visible',)
    menu_icon = StringField('menu_icon', validators=[DataRequired()])
    redirect_url = StringField('redirect_url')
    
    def validate_parent_id(form,field):
        if field.data is None:
            raise ValidationError(' must parent_id ')
        
class UplaodForm(FlaskForm):
    file=FileField('file',validators=[FileRequired(),FileAllowed(['jpg','png','gif','jpeg','txt','xlsx','xls'])])