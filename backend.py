from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure local SQLite database path
db_path = os.path.join(os.path.dirname(__file__), 'tourism.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database structural model
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    state = db.Column(db.String(100), nullable=False)
    season = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "state": self.state,
            "season": self.season,
            "budget": self.budget,
            "image_url": self.image_url,
            "description": self.description
        }

# Automatically initialize structures
with app.app_context():
    db.create_all()

# --- WEB AND API APP ROUTES ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/destinations', methods=['GET'])
def get_destinations():
    places = Destination.query.all()
    return jsonify([place.to_dict() for place in places])

@app.route('/add-destination', methods=['POST'])
def add_destination():
    # Accept standardized JSON payloads natively
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing application/json request body."}), 400

    name = data.get('name')
    state = data.get('state')
    season = data.get('season')
    budget = data.get('budget')
    image_url = data.get('image_url')
    description = data.get('description')

    if name and state and season and budget and description:
        new_place = Destination(
            name=name.strip(),
            state=state.strip(),
            season=season,
            budget=int(budget),
            image_url=image_url.strip() if image_url else None,
            description=description.strip()
        )
        try:
            db.session.add(new_place)
            db.session.commit()
            return jsonify({"success": True, "message": "Record committed successfully!"}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Database write conflict: {str(e)}"}), 400
            
    return jsonify({"error": "Missing one or more required destination fields."}), 400

if __name__ == '__main__':
    app.run(debug=True)