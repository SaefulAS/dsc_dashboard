from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import RoleForm, EmployeeAssignForm, GradeForm
from .. import db
from ..models import Role, Employee, Grade


def check_admin():
    if not current_user.is_admin:
        abort(403)


@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")


@admin.route('/employees')
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()

    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a a paygrade and a role to an employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    # prevent admin from being assigned a role
    if employee.is_admin:
        abort(403)

    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.role = form.role.data
        employee.grade = form.grade.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a, paygrade and a role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')


@admin.route('/employees/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_employee(id):
    """
    Assign a role to an employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    # prevent admin from being assigned role
    if employee.is_admin:
        abort(403)

    db.session.delete(employee)
    db.session.commit()
    flash('You have successfully deleted the account.')

    # redirect to the roles page
    return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Delete Employee')

#--------------------------------------------------#


@admin.route('/grades')
@login_required
def list_grades():
    check_admin()
    """
    List all Pijar Mahir Skills
    """
    grades = Grade.query.all()
    return render_template('admin/grades/grades.html',
                           grades=grades, title='Grades')


@admin.route('/grades/add', methods=['GET', 'POST'])
@login_required
def add_grade():
    """
    Add a Pijar Mahir Skill to the database
    """
    check_admin()

    add_grade = True

    form = GradeForm()
    if form.validate_on_submit():
        grade = Grade(paygrade=form.paygrade.data,
                      amount=form.amount.data)

        try:
            # add role to the database
            db.session.add(grade)
            db.session.commit()
            flash('You have successfully added a new Pijar Mahir Skill.')
        except:
            # in case role name already exists
            flash('Error: Pijar Mahir Skill already exists.')

        # redirect to the Pijar Mahir Skills page
        return redirect(url_for('admin.list_grades'))

    # load role template
    return render_template('admin/grades/grade.html', add_grade=add_grade,
                           form=form, title='Add Pijar Mahir Skill')


@admin.route('/grades/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_grade(id):
    """
    Edit a Pijar Mahir Skill
    """
    check_admin()

    add_grade = False

    grade = Grade.query.get_or_404(id)
    form = GradeForm(obj=grade)
    if form.validate_on_submit():
        grade.paygrade = form.paygrade.data
        grade.amount = form.amount.data
        db.session.add(grade)
        db.session.commit()
        flash('You have successfully edited the Pijar Mahir Skill.')

        # redirect to the roles page
        return redirect(url_for('admin.list_grades'))

    form.amount.data = grade.amount
    form.paygrade.data = grade.paygrade
    return render_template('admin/grades/grade.html', add_grade=add_grade,
                           form=form, title="Edit Pijar Mahir Skill")


@admin.route('/grades/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_grade(id):
    """
    Delete a Pijar Mahir Skill from the database
    """
    check_admin()

    grade = Grade.query.get_or_404(id)
    db.session.delete(grade)
    db.session.commit()
    flash('You have successfully deleted the Pijar Mahir Skill.')

    # redirect to the roles page
    return redirect(url_for('admin.list_grades'))

    return render_template(title="Delete Pijar Mahir Skill")
