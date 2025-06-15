from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Contact

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

@bp.route('/add', methods=['POST'])
def add_contact():
    name = request.form['name']
    email = request.form['email']
    notes = request.form.get('notes', '')
    contact = Contact(name=name, email=email, notes=notes)
    db.session.add(contact)
    db.session.commit()
    return redirect(url_for('main.index'))
