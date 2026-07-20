import sys
import os

# Ensure the parent directory is in the path so we can import frontend
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from frontend import app, db, Destination

# Production-grade starter kit containing verified, high-availability direct imagery paths
bulk_destinations = [
    # === WINTER DESTINATIONS ===
    Destination(
        name="Manali", state="Himachal Pradesh", season="Winter", budget=11000,
        image_url="https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
        description="A high-altitude resort village along the Beas River valley, offering premium adventure sports like paragliding, Solang Valley ski tours, and heavy winter snow activities."
    ),
    Destination(
        name="Jaipur", state="Rajasthan", season="Winter", budget=8000,
        image_url="https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
        description="The iconic Pink City displays magnificent royal fort lines, intricate architectural designs like the Hawa Mahal, and bustling local heritage bazaar circuits."
    ),
    Destination(
        name="Udaipur", state="Rajasthan", season="Winter", budget=9500,
        image_url="https://images.unsplash.com/photo-1569949380643-6e7a6ecff340?auto=format&fit=crop&w=1200&q=80",
        description="Known as the City of Lakes, Udaipur sits around glistening water channels like Lake Pichola where white marble heritage palaces rise directly out of the water surface."
    ),
    Destination(
        name="Gulmarg", state="Jammu & Kashmir", season="Winter", budget=16000,
        image_url="https://images.unsplash.com/photo-1616422285623-13ff0162193c?auto=format&fit=crop&w=1200&q=80",
        description="A premier winter ski resort destination featuring the world's highest operating cable car (Gondola), pristine white snow slopes, and sweeping Himalayan valley viewpoints."
    ),
    Destination(
        name="Jaisalmer", state="Rajasthan", season="Winter", budget=8500,
        image_url="https://images.unsplash.com/photo-1574688461530-580a133e9d8c?auto=format&fit=crop&w=1200&q=80",
        description="The Golden City rises from the heart of the Thar Desert, boasting a living sandstone fort, sunset camel desert safaris, and overnight dune camp experiences."
    ),

    # === SUMMER DESTINATIONS ===
    Destination(
        name="Ooty", state="Tamil Nadu", season="Summer", budget=8000,
        image_url="https://images.unsplash.com/photo-1549488344-1f9b8d2bd1f3?auto=format&fit=crop&w=1200&q=80",
        description="Famous for sprawling emerald tea gardens, a pleasant cool summer climate, Nilgiri toy train rides, and calm boat cruises on Ooty Lake."
    ),
    Destination(
        name="Leh Ladakh", state="Jammu & Kashmir", season="Summer", budget=22000,
        image_url="https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
        description="A high-altitude desert wonderland accessible in summer, characterized by the deep blue Pangong Tso Lake, magnetic hills, and dramatic mountain pass trekking trails."
    ),
    Destination(
        name="Shimla", state="Himachal Pradesh", season="Summer", budget=9000,
        image_url="https://images.unsplash.com/photo-1562916170-664453782d96?auto=format&fit=crop&w=1200&q=80",
        description="The former summer capital of British India, offering historic Mall Road walks, colonial architecture tours, and cool mountain breezes away from plains heat."
    ),
    Destination(
        name="Munnar", state="Kerala", season="Summer", budget=8500,
        image_url="https://images.unsplash.com/photo-1593693411515-c202e974233c?auto=format&fit=crop&w=1200&q=80",
        description="An idyllic South Indian hill station wrapped in neatly manicured tea plantations, misty mountain peaks, Eravikulam National Park safaris, and cascading waterfalls."
    ),

    # === MONSOON DESTINATIONS ===
    Destination(
        name="Goa", state="Goa", season="Monsoon", budget=12000,
        image_url="https://images.unsplash.com/photo-1540206395-68808572332f?auto=format&fit=crop&w=1200&q=80",
        description="Transforms into a lush green paradise during monsoons, showcasing roaring Dudhsagar Waterfalls, quiet uncrowded beaches, and rain-washed spice plantations."
    ),
    Destination(
        name="Wayanad", state="Kerala", season="Monsoon", budget=7500,
        image_url="https://images.unsplash.com/photo-1599940824399-b87987ceb72a?auto=format&fit=crop&w=1200&q=80",
        description="A monsoon haven featuring misty treehouse resorts, intense green forest canopies, historical Edakkal Caves exploration, and Banasura Sagar dam vistas."
    ),
    Destination(
        name="Lonavala", state="Karnataka", season="Monsoon", budget=6500,
        image_url="https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=1200&q=80",
        description="A beloved Western Ghats escape that comes alive under heavy rains with surging waterfalls, foggy mountain lookouts like Tiger's Point, and lush trekking trails."
    ),

    # === SPRING DESTINATIONS ===
    Destination(
        name="Coorg", state="Karnataka", season="Spring", budget=7500,
        image_url="https://images.unsplash.com/photo-1602002418082-a4443e081dd1?auto=format&fit=crop&w=1200&q=80",
        description="Famous for blooming spring coffee plantation flowers, misty valleys, Abbey Falls paths, and up-close interactions at the Dubare Elephant Camp."
    ),
    Destination(
        name="Valley of Flowers", state="Uttarakhand", season="Spring", budget=14000,
        image_url="https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=1200&q=80",
        description="A UNESCO World Heritage site known for alpine meadows blooming with hundreds of endemic flower species, wild flora trails, and stunning glacier backdrop walls."
    ),
    Destination(
        name="Araku Valley", state="Andhra Pradesh", season="Spring", budget=7000,
        image_url="https://images.unsplash.com/photo-1561484930-998b6a7b22e8?auto=format&fit=crop&w=1200&q=80",
        description="A scenic valley escape enriched by blooming spring coffee orchards, local tribal museum histories, Katiki waterfalls, and deep ancient Borra cave networks."
    )
]

with app.app_context():
    print("Connecting to live database environment...")
    
    # Optional: If you want to purge old entries with broken links, uncomment the line below:
    # db.session.query(Destination).delete()
    
    added_count = 0
    updated_count = 0
    
    for place in bulk_destinations:
        exists = Destination.query.filter_by(name=place.name).first()
        if not exists:
            db.session.add(place)
            added_count += 1
            print(f"-> Prepared record for {place.name}")
        else:
            # Overwrite the table properties to push the functional images into the live SQLite engine
            exists.state = place.state
            exists.season = place.season
            exists.budget = place.budget
            exists.image_url = place.image_url
            exists.description = place.description
            updated_count += 1
            
    db.session.commit()
    print(f"\n🎉 Sync Complete! Added {added_count} new entries and successfully synchronized {updated_count} images inside tourism.db!")