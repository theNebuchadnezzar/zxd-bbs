from flask import (
    render_template,
    Blueprint,
)


main = Blueprint('resume', __name__)




@main.route('/')
def index():

    t = render_template(
        'resume/index.html',
    )
    return t

