from flask import Blueprint, render_template

main_home_bpp = Blueprint('main_home_bpp', __name__)

@main_home_bpp.route('/')
def index():
    return render_template('index.html')