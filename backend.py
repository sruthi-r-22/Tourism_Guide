import os
from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')

# Database Configurations
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tourism.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Data Model
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    state = db.Column(db.String(100), nullable=False)
    season = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    output = []
    for d in destinations:
        output.append({
            'name': d.name,
            'state': d.state,
            'season': d.season,
            'budget': d.budget,
            'image_url': d.image_url,
            'description': d.description
        })
    return jsonify(output)

@app.route('/add-destination', methods=['POST'])
def add_destination():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid payload'}), 400
        
    try:
        new_place = Destination(
            name=data['name'],
            state=data['state'],
            season=data['season'],
            budget=int(data['budget']),
            image_url=data.get('image_url', ''),
            description=data['description']
        )
        db.session.add(new_place)
        db.session.commit()
        return jsonify({'message': 'Success'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)