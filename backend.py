from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure local SQLite instances path variables
db_path = os.path.join(os.path.dirname(__file__), 'tourism.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Relational mapping schema structural model
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

# Automatically initialize structures and drop core seed records if table is blank
with app.app_context():
    db.create_all()
    
    if not Destination.query.first():
        seed_places = [
            Destination(
                name="Ooty", state="Tamil Nadu", season="Summer", budget=8000,
                image_url="https://blog.rideally.com/wp-content/uploads/2022/05/Ooty.jpg",
                description="Ooty is one of India's most famous hill stations. Known for tea plantations, Botanical Gardens, Doddabetta Peak, and Ooty Lake boating rides."
            ),
            Destination(
                name="Goa", state="Goa", season="Winter", budget=12000,
                image_url="https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=900&q=80",
                description="Goa is India's most popular coastal destination. Features beautiful sandy Baga beaches, historic Fort Aguada lines, and vibrant nightlife options."
            ),
            Destination(
                name="Munnar", state="Kerala", season="Monsoon", budget=8500,
                image_url="https://i.pinimg.com/736x/f6/66/b5/f666b51c07f0ac06594f60050e9a068e.jpg",
                description="Munnar is a majestic green hill station escape. Celebrated for sprawling Tea Museums, mist-covered Eravikulam valleys, and roaring waterfalls."
            )
        ]
        db.session.add_all(seed_places)
        db.session.commit()

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
    name = request.form.get('name')
    state = request.form.get('state')
    season = request.form.get('season')
    budget = request.form.get('budget')
    image_url = request.form.get('image_url')
    description = request.form.get('description')

    if name and state and season and budget:
        # Create record instance tracking layout arguments
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
        except Exception as e:
            db.session.rollback()
            print(f"Error handling transactional database commit: {e}")
            
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)