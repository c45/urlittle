import string
from random import choice
from flask import render_template, request, redirect, abort
from url import app, db
from url.forms import urlForm
from url.models import Url


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        def gen():
            chars = string.ascii_letters + string.digits
            length = 3
            code = ''.join(choice(chars) for x in range(length))
            print("Перевiрка", code)
            exists = db.session.query(
                db.exists().where(Url.short_url == code)).scalar()
            if not exists:
                print(code)
                return code
        code = gen()
        while code is None:
            code = gen()

    if request.method == 'POST' and code is not None:
        form = urlForm(request.form)
        if form.validate_on_submit():
            url = form.save_url(Url(short_url=code))
            db.session.add(url)
            db.session.commit()
            return render_template("success.html", code=code, original_url=url.short_url)
        else:
            print("Error")
    else:
        form = urlForm()
    return render_template("index.html", form=form)


@app.route('/<short_url>')
def redirect_to_old(short_url):
    short_url = Url.query.filter_by(short_url=short_url).first()
    if short_url is None:
        abort(404)
    else:
        db.session.add(short_url)
        db.session.commit()
        return redirect(short_url.original_url)
