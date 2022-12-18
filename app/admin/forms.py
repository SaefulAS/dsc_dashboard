from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from ..models import Role, Grade




class RoleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


class GradeForm(FlaskForm):
    paygrade = StringField('Pijar Mahir Skill', validators=[DataRequired()])
    amount = StringField('Role Grades', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EmployeeAssignForm(FlaskForm):
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    grade = QuerySelectField(query_factory=lambda: Grade.query.all(),
                            get_label="paygrade")
    submit = SubmitField('Submit')
