from flask import Blueprint, render_template, request, redirect
from flask_login import login_required

from .extensions import db
from .models import User


views = Blueprint('views', __name__)

@views.route('/')
def home():
  return render_template('home.html')

@views.route('/profile/<int:wall_id>', methods=['GET', 'POST'])
def profile(wall_id):
  return render_template('profile.html')