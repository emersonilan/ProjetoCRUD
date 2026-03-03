# pages/contacts.py
# Blueprint modelo

from flask import Blueprint, render_template

contacts_bp = Blueprint("contacts", __name__)

@contacts_bp.route("/contacts")
def contacts_page(): 
    page_title = "Faça contato"
    return render_template("contacts.html", page_title=page_title)

@contacts_bp.route("/privacy")
def privacy_page():
    page_title = "Políticas de Privacidade"
    return render_template("privacy.html", page_title=page_title)