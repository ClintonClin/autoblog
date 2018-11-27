from flask import render_template  # importation of the render-template
from . import main

@main.errorhandler(404)  # decorator that passes in the error recieved
def for_oh_for(error):
    """
    function that renders the 404 error page
    """
    return render_template('forOhfor.html'), 404  