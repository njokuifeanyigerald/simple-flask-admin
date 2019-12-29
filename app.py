from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost/flask_admin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
admin = Admin(app)

class Data(db.Model):
    __tablename__ = 'admin_data'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))

admin.add_view(ModelView(Data, db.session))

@app.route('/')
def home():
    form = Data.query.all()
    return render_template('home.html', form=form)


if __name__ == "__main__":
    app.run()
