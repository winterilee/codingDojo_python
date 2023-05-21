from flask import render_template, request, redirect, flash, session, url_for
from flask_app import app
from flask_app.models import recipe
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)