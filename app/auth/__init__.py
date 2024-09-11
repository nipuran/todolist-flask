from flask import Blueprint

auth_bp = Blueprint("auth_bp", __name__, 
    template_folder="templates", 
    static_folder="static", 
    static_url_path="/auth_static")


from . import routes
