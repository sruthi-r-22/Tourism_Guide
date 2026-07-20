import sys
import os

# Appending system path mapping configurations to resolve parent model imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from backend import app, db, Destination

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
    Destination(
        name="Agra", state="Uttar Pradesh", season="Winter", budget=6000,
        image_url="https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
        description="Home to the world-famous Taj Mahal, the magnificent Agra Fort, and historic Mughal architecture, offering a perfect heritage trip during pleasant winter months."
    ),
    Destination(
        name="Varanasi", state="Uttar Pradesh", season="Winter", budget=5500,
        image_url="https://images.unsplash.com/photo-1561361531-9952a8e3df6a?auto=format&fit=crop&w=1200&q=80",
        description="One of the world's oldest living cities. Famous for spiritual Ganga Aarti ceremonies, vibrant river ghats, labyrinth street alleys, and grand silk weaving heritages."
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
    Destination(
        name="Darjeeling", state="West Bengal", season="Summer", budget=9500,
        image_url="https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        description="Framed by the majestic Kanchenjunga peaks, this scenic hill station is universally prized for premium black tea processing estates and historic UNESCO toy train tracks."
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
        name="Lonavala", state="Maharashtra", season="Monsoon", budget=6500,
        # FIXED: Updated fried chicken image path loop to scenic Western Ghats imagery stream 
        image_url="https://images.unsplash.com/photo-1584810359583-96fc3448beaa?auto=format&fit=crop&w=1200&q=80",
        description="A beloved Western Ghats escape that comes alive under heavy rains with surging waterfalls, foggy mountain lookouts like Tiger's Point, and lush trekking trails."
    ),
    Destination(
        name="Alleppey", state="Kerala", season="Monsoon", budget=10500,
        image_url="https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=1200&q=80",
        description="Famous for majestic backwater networks, luxury overnight houseboat cruises, swaying palm-fringed channels, and picturesque traditional green paddy field vistas."
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
    ),
    Destination(
        name="Hampi", state="Karnataka", season="Spring", budget=6500,
        image_url="https://images.unsplash.com/photo-1600100397608-f010e423b971?auto=format&fit=crop&w=1200&q=80",
        description="A dramatic open-air museum landscape of ancient ruins from the historic Vijayanagara Empire, showcasing giant boulder horizons, monolithic shrines, and intricately carved temples."
    )
]

with app.app_context():
    print("Purging storage cache and setting up a clean layout...")
    db.session.query(Destination).delete()
    
    db.session.add_all(bulk_destinations)
    db.session.commit()
    print(f"🎉 Database Synced Successfully! Added {len(bulk_destinations)} destinations.")