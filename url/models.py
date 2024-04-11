import sqlalchemy as sa
import sqlalchemy.orm as so
from flask import current_app
from url import db

class Url(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    original_url: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)
    short_url: so.Mapped[str] = so.mapped_column(sa.String(16), nullable=False)
    
    def __init__(self, *args, **kwargs):
        super(Url, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<URL %s>' % self.original_url

with current_app.app_context():
  db.create_all()

