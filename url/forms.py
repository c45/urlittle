from flask_wtf import FlaskForm
from wtforms import validators, StringField


class urlForm(FlaskForm):
    original_url = StringField('Title', [
        validators.InputRequired()])

    def save_url(self, url):
        self.populate_obj(url)
        if not "http" in url.original_url:
            url.original_url = "https://" + url.original_url
        if not "." in url.original_url:
            url.original_url = url.original_url + ".com/"
        return url