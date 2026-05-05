from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from datetime import datetime, timezone

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    languages = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Candidate {self.id}>'


@app.route('/', methods=["GET", "POST"])
def index():

    candidates = Candidate.query.order_by(Candidate.date_created).all()

    filtered_candidates = []
    show_filter = False
    active_div = "lac"

    if request.method == "POST":

        # ================= CREATE =================
        if 'cnc-c-name-input' in request.form:
            name = request.form['cnc-c-name-input'].strip()
            languages = request.form['cnc-c-language-input'].strip()
            age = request.form['cnc-c-age-input']

            if not name or not languages or not age:
                return redirect('/')

            try:
                age = int(age)
            except:
                return "Invalid age"

            new_candidate = Candidate(name=name, age=age, languages=languages)

            db.session.add(new_candidate)
            db.session.commit()
            return redirect('/')

        # ================= FILTER =================
        elif 'filter_type' in request.form:
            filter_type = request.form['filter_type']
            value = request.form['value'].strip()

            show_filter = True
            active_div = "fc"

            if filter_type == "id":
                try:
                    filtered_candidates = Candidate.query.filter_by(id=int(value)).all()
                except:
                    filtered_candidates = []

            elif filter_type == "age":
                try:
                    filtered_candidates = Candidate.query.filter_by(age=int(value)).all()
                except:
                    filtered_candidates = []

            elif filter_type == "language":
                filtered_candidates = Candidate.query.filter(
                    Candidate.languages.contains(value)
                ).all()

    return render_template(
        'index.html',
        candidates=candidates,
        filtered_candidates=filtered_candidates,
        show_filter=show_filter,
        active_div=active_div
    )


@app.route('/delete/<int:id>', methods=['POST'])
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


@app.route('/edit', methods=['POST'])
def edit_candidate():
    candidate_id = request.form['id']
    candidate = Candidate.query.get_or_404(candidate_id)

    name = request.form.get('name')
    age = request.form.get('age')
    languages = request.form.get('languages')

    # Only update if value is provided
    if name and name.strip():
        candidate.name = name.strip()

    if age and age.strip():
        try:
            candidate.age = int(age)
        except:
            return "Invalid age"

    if languages and languages.strip():
        candidate.languages = languages.strip()

    try:
        db.session.commit()
        return redirect('/')
    except:
        return "Failed to update candidate"
    
    

if __name__ == "__main__":

    app.run(debug=True, port=3000)
