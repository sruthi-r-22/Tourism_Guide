import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from backend import app, db, Destination

# Exactly 15 unique destinations per season as requested
destinations_list = [
    # === SUMMER (15 Places) ===
    ("Munnar", "Kerala", "Summer", 8500),
    ("Ooty", "Tamil Nadu", "Summer", 8000),
    ("Manali", "Himachal Pradesh", "Summer", 11000),
    ("Kasauli", "Himachal Pradesh", "Summer", 7000),
    ("Coonoor", "Tamil Nadu", "Summer", 7500),
    ("Kodaikanal", "Tamil Nadu", "Summer", 9000),
    ("Dharamshala", "Himachal Pradesh", "Summer", 9500),
    ("Shimla", "Himachal Pradesh", "Summer", 9000),
    ("Mussoorie", "Uttarakhand", "Summer", 8000),
    ("Horsley Hills", "Andhra Pradesh", "Summer", 6000),
    ("Nainital", "Uttarakhand", "Summer", 8500),
    ("Mount Abu", "Rajasthan", "Summer", 7500),
    ("Dalhousie", "Himachal Pradesh", "Summer", 9500),
    ("Chikmagalur", "Karnataka", "Summer", 7000),
    ("Yercaud", "Tamil Nadu", "Summer", 6500),
    
    # === MONSOON (15 Places) ===
    ("Lonavala", "Maharashtra", "Monsoon", 6500),
    ("Mahabaleshwar", "Maharashtra", "Monsoon", 7000),
    ("Ananthagiri Hills", "Telangana", "Monsoon", 5000),
    ("Araku Valley", "Andhra Pradesh", "Monsoon", 7000),
    ("Wayanad", "Kerala", "Monsoon", 7500),
    ("Coorg", "Karnataka", "Monsoon", 7500),
    ("Cherrapunji", "Meghalaya", "Monsoon", 12000),
    ("Agumbe", "Karnataka", "Monsoon", 6000),
    ("Igatpuri", "Maharashtra", "Monsoon", 5500),
    ("Kuntala Waterfalls", "Telangana", "Monsoon", 4000),
    ("Bhandardara", "Maharashtra", "Monsoon", 6000),
    ("Athirappilly", "Kerala", "Monsoon", 8000),
    ("Matheran", "Maharashtra", "Monsoon", 5000),
    ("Udawalawe", "Monsoon Haven", "Monsoon", 15000),
    ("Jog Falls", "Karnataka", "Monsoon", 6500),

    # === WINTER (15 Places) ===
    ("Jaipur", "Rajasthan", "Winter", 8000),
    ("Jaisalmer", "Rajasthan", "Winter", 8500),
    ("Hampi", "Karnataka", "Winter", 6500),
    ("Pondicherry", "Puducherry", "Winter", 7000),
    ("Goa", "Goa", "Winter", 12000),
    ("Agra", "Uttar Pradesh", "Winter", 6000),
    ("Rann of Kutch", "Gujarat", "Winter", 11000),
    ("Varanasi", "Uttar Pradesh", "Winter", 5500),
    ("Udaipur", "Rajasthan", "Winter", 9500),
    ("Gokarna", "Karnataka", "Winter", 6000),
    ("Alleppey", "Kerala", "Winter", 10500),
    ("Auli", "Uttarakhand", "Winter", 13000),
    ("Badami", "Karnataka", "Winter", 5000),
    ("Khajuraho", "Madhya Pradesh", "Winter", 7500),
    ("Mysore", "Karnataka", "Winter", 6000),

    # === SPRING (15 Places) ===
    ("Shillong", "Meghalaya", "Spring", 9000),
    ("Gangtok", "Sikkim", "Spring", 9500),
    ("Tulip Garden Srinagar", "Jammu & Kashmir", "Spring", 12000),
    ("Yumthang Valley", "Sikkim", "Spring", 11000),
    ("Kasol", "Himachal Pradesh", "Spring", 7000),
    ("Rishikesh", "Uttarakhand", "Spring", 6000),
    ("Valley of Flowers", "Uttarakhand", "Spring", 14000),
    ("Mirik", "West Bengal", "Spring", 6500),
    ("Kalimpong", "West Bengal", "Spring", 7500),
    ("Palampur", "Himachal Pradesh", "Spring", 7000),
    ("Lansdowne", "Uttarakhand", "Spring", 5500),
    ("Ziro", "Arunachal Pradesh", "Spring", 9000),
    ("Kaziranga", "Assam", "Spring", 10000),
    ("Tawang", "Arunachal Pradesh", "Spring", 12000),
    ("Kullu", "Himachal Pradesh", "Spring", 6500)
]

with app.app_context():
    print("Dropping old tables to guarantee clean data swap...")
    db.drop_all()
    db.create_all()
    
    for name, state, season, budget in destinations_list:
        db.session.add(Destination(
            name=name,
            state=state,
            season=season,
            budget=budget,
            image_url="https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=600&q=80",
            description=f"A spectacular 1-2 day getaway spot located in {state}, perfect for a refreshing seasonal trip."
        ))
        
    db.session.commit()
    print("🎉 Success! All 60 unique destinations loaded into SQLite database storage.")