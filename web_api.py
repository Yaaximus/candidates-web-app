from flask import Flask, request, redirect, url_for, render_template
# from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
# from candidate import Candidate

app = Flask(__name__)

# Telling app where the databasae is located, /// for relative path, //// for absolute path, test.db is the database name, everything will be stored in it
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# Initialize database
db = SQLAlchemy(app)

# Create a model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    languages = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # Every time we make a new element, this will return the task and its unique id
    def __repr__(self):
        return '<Candidate %r>' % self.id


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        name = request.form['cnc-c-name-input'].strip()
        languages = request.form['cnc-c-language-input'].strip()
        age = int(request.form['cnc-c-age-input'].strip())

        # ✅ prevent empty or whitespace-only tasks
        if not name.strip():
            return redirect('/')
        
        # ✅ prevent empty or whitespace-only tasks
        if not languages.strip():
            return redirect('/')
        
        new_candidate = Candidate(name=name, age=age, languages=languages)

        try:
            db.session.add(new_candidate)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return str(e)        

    else:
        candidates = Candidate.query.order_by(Candidate.date_created).all()
        return render_template('index.html', candidates=candidates)
    

@app.route('/delete/<int:id>')
def delete(id):
    candidate_to_delete = Candidate.query.get_or_404(id)

    try:
        db.session.delete(candidate_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting the candidate"
    

@app.route('/delete', methods=['POST'])
def delete_by_id():
    candidate_id = request.form['id']

    candidate = Candidate.query.get(candidate_id)

    if not candidate:
        return "Candidate not found"

    try:
        db.session.delete(candidate)
        db.session.commit()
        return redirect('/')
    except:
        return "Error deleting candidate"


if __name__ == "__main__":

    app.run(debug=True, port=3000)
