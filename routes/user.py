import os
import uuid

from flask import (
    render_template,
    Blueprint,
    send_from_directory,
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    abort,
)
from routes import *

from routes import current_user

from models.user import User

from utils import log



main = Blueprint('user', __name__)




@main.route('/recent_replied_topics')
def recent_replied_topics():
    u = current_user()
    recent_replied_topics = User.recent_replied_topics(u.id)
    return render_template("profiles.html", recent_replied_topics=recent_replied_topics)


@main.route('/recent_created_topics')
def recent_created_topics():
    u = current_user()
    recent_created_topics = User.recent_created_topics(u.id)
    return render_template("profiles.html", recent_created_topics=recent_created_topics)

@main.route('/change/info', methods=['POST'])
# @csrf_required

def change_user_info():
    form = request.form
    u = current_user()

    u.update(u.id, **form)
    return redirect(url_for('index.setting'))


@main.route('/change/pass', methods=['POST'])
# @csrf_required

def change_user_password():
    form = request.form
    u = current_user()
    old_pass = form.get('old_pass', '')
    log('old_pass', old_pass)
    new_pass = form.get('new_pass', '')
    log('new_pass', new_pass)
    log('u.id', u.id)

    if u.password == u.salted_password(old_pass):
        u.password = u.salted_password(new_pass)
        log('u.password', u.password)
        form = dict(
            password=u.password,
        )

        u.update(u.id, **form)

        return redirect(url_for('index.index'))

    else:
        return redirect(url_for('index.setting'))



















