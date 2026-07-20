import sys
import os
import json
import urllib.request
import urllib.parse
import ssl
import time

# Align paths perfectly
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from backend import app, db, Destination

def get_commons_image(search_term):
    """Directly searches Wikimedia's image database for real photos of the location."""
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    headers = {'User-Agent': 'TourismGuideApp/2.0 (Python/urllib)'}
    
    # We append 'filetype:bitmap' to guarantee we get a JPG/PNG, not a PDF or video
    query = urllib.parse.quote(f"{search_term} filetype:bitmap")
    search_url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={query}&srnamespace=6&format=json&srlimit=1"
    
    for attempt in range(3):
        try:
            req = urllib.request.Request(search_url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))
                search_results = data.get('query', {}).get('search', [])
                
                if search_results:
                    file_title = search_results[0]['title']
                    
                    # Step 2: Ask Wikimedia for the direct 800px thumbnail of this specific file
                    img_url_req = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&iiurlwidth=800&format=json"
                    req2 = urllib.request.Request(img_url_req, headers=headers)
                    
                    with urllib.request.urlopen(req2, context=ctx, timeout=10) as r2:
                        img_data = json.loads(r2.read().decode('utf-8'))
                        pages = img_data.get('query', {}).get('pages', {})
                        for page_id, page_info in pages.items():
                            if 'imageinfo' in page_info:
                                return page_info['imageinfo'][0]['thumburl']
                                
        except Exception as e:
            time.sleep(2) # If the internet stutters, wait 2 seconds and try again
            
    # Absolute final fallback: A generic lush green landscape (NOT the Taj Mahal)
    return "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/East_Coast_Road_near_Marakkanam.jpg/800px-East_Coast_Road_near_Marakkanam.jpg"

# Hand-curated search terms guaranteed to pull beautiful, accurate photography from Commons
destinations_list = [
    # === SUMMER ===
    ("Munnar", "Kerala", "Summer", 8500, "Munnar tea gardens"),
    ("Ooty", "Tamil Nadu", "Summer", 8000, "Ooty lake landscape"),
    ("Manali", "Himachal Pradesh", "Summer", 11000, "Manali Himachal landscape"),
    ("Kasauli", "Himachal Pradesh", "Summer", 7000, "Kasauli Himachal"),
    ("Coonoor", "Tamil Nadu", "Summer", 7500, "Coonoor Nilgiris"),
    ("Kodaikanal", "Tamil Nadu", "Summer", 9000, "Kodaikanal lake"),
    ("Dharamshala", "Himachal Pradesh", "Summer", 9500, "Dharamshala landscape"),
    ("Shimla", "Himachal Pradesh", "Summer", 9000, "Shimla Ridge"),
    ("Mussoorie", "Uttarakhand", "Summer", 8000, "Mussoorie hills"),
    ("Horsley Hills", "Andhra Pradesh", "Summer", 6000, "Horsley Hills Andhra"),
    ("Nainital", "Uttarakhand", "Summer", 8500, "Nainital lake"),
    ("Mount Abu", "Rajasthan", "Summer", 7500, "Mount Abu Nakki Lake"),
    ("Dalhousie", "Himachal Pradesh", "Summer", 9500, "Dalhousie Himachal"),
    ("Chikmagalur", "Karnataka", "Summer", 7000, "Chikmagalur hills"),
    ("Yercaud", "Tamil Nadu", "Summer", 6500, "Yercaud lake"),

    # === MONSOON ===
    ("Lonavala", "Maharashtra", "Monsoon", 6500, "Lonavala monsoon"),
    ("Mahabaleshwar", "Maharashtra", "Monsoon", 7000, "Mahabaleshwar landscape"),
    ("Ananthagiri Hills", "Telangana", "Monsoon", 5000, "Ananthagiri Hills Vikarabad"),
    ("Araku Valley", "Andhra Pradesh", "Monsoon", 7000, "Araku Valley landscape"),
    ("Wayanad", "Kerala", "Monsoon", 7500, "Wayanad landscape"),
    ("Coorg", "Karnataka", "Monsoon", 7500, "Kodagu landscape"),
    ("Cherrapunji", "Meghalaya", "Monsoon", 12000, "Cherrapunji waterfalls"),
    ("Agumbe", "Karnataka", "Monsoon", 6000, "Agumbe rainforest"),
    ("Igatpuri", "Maharashtra", "Monsoon", 5500, "Igatpuri monsoon"),
    ("Kuntala Waterfalls", "Telangana", "Monsoon", 4000, "Kuntala Waterfall"),
    ("Bhandardara", "Maharashtra", "Monsoon", 6000, "Bhandardara dam"),
    ("Athirappilly", "Kerala", "Monsoon", 8000, "Athirappilly Falls"),
    ("Matheran", "Maharashtra", "Monsoon", 5000, "Matheran landscape"),
    ("Amboli", "Maharashtra", "Monsoon", 5000, "Amboli ghat"),
    ("Jog Falls", "Karnataka", "Monsoon", 6500, "Jog Falls"),

    # === WINTER ===
    ("Jaipur", "Rajasthan", "Winter", 8000, "Hawa Mahal Jaipur"),
    ("Jaisalmer", "Rajasthan", "Winter", 8500, "Jaisalmer Fort"),
    ("Hampi", "Karnataka", "Winter", 6500, "Hampi ruins"),
    ("Pondicherry", "Puducherry", "Winter", 7000, "Pondicherry French Quarter"),
    ("Goa", "Goa", "Winter", 12000, "Goa beach"),
    ("Agra", "Uttar Pradesh", "Winter", 6000, "Taj Mahal"),
    ("Rann of Kutch", "Gujarat", "Winter", 11000, "Rann of Kutch white desert"),
    ("Varanasi", "Uttar Pradesh", "Winter", 5500, "Varanasi ghats"),
    ("Udaipur", "Rajasthan", "Winter", 9500, "Udaipur Lake Palace"),
    ("Gokarna", "Karnataka", "Winter", 6000, "Gokarna beach"),
    ("Alleppey", "Kerala", "Winter", 10500, "Alleppey backwaters"),
    ("Auli", "Uttarakhand", "Winter", 13000, "Auli snow"),
    ("Badami", "Karnataka", "Winter", 5000, "Badami caves"),
    ("Khajuraho", "Madhya Pradesh", "Winter", 7500, "Khajuraho temple"),
    ("Mysore", "Karnataka", "Winter", 6000, "Mysore Palace"),

    # === SPRING ===
    ("Shillong", "Meghalaya", "Spring", 9000, "Shillong landscape"),
    ("Gangtok", "Sikkim", "Spring", 9500, "Gangtok Sikkim"),
    ("Tulip Garden Srinagar", "Jammu & Kashmir", "Spring", 12000, "Tulip Garden Srinagar"),
    ("Yumthang Valley", "Sikkim", "Spring", 11000, "Yumthang Valley"),
    ("Kasol", "Himachal Pradesh", "Spring", 7000, "Kasol Parvati Valley"),
    ("Rishikesh", "Uttarakhand", "Spring", 6000, "Rishikesh Ganga"),
    ("Valley of Flowers", "Uttarakhand", "Spring", 14000, "Valley of Flowers National Park"),
    ("Mirik", "West Bengal", "Spring", 6500, "Mirik lake"),
    ("Kalimpong", "West Bengal", "Spring", 7500, "Kalimpong mountains"),
    ("Palampur", "Himachal Pradesh", "Spring", 7000, "Palampur tea garden"),
    ("Lansdowne", "Uttarakhand", "Spring", 5500, "Lansdowne Uttarakhand"),
    ("Ziro", "Arunachal Pradesh", "Spring", 9000, "Ziro Valley"),
    ("Kaziranga", "Assam", "Spring", 10000, "Kaziranga rhino"),
    ("Tawang", "Arunachal Pradesh", "Spring", 12000, "Tawang Monastery"),
    ("Kullu", "Himachal Pradesh", "Spring", 6500, "Kullu valley")
]

with app.app_context():
    print("Purging old database records...")
    db.reflect()
    db.drop_all()
    db.create_all()
    
    print("Connecting to Wikimedia Commons image database...")
    print("This will take about 90 seconds to safely fetch all 60 unique images. Please wait...\n")
    
    for name, state, season, budget, search_term in destinations_list:
        print(f"[{season}] Extracting photo for {name}...", end=" ")
        
        img_url = get_commons_image(search_term)
        
        if "Marakkanam" in img_url:
            print("⚠️ FAILED (Used Greenery Fallback)")
        else:
            print("✅ SUCCESS")
            
        db.session.add(Destination(
            name=name,
            state=state,
            season=season,
            budget=budget,
            image_url=img_url,
            description=f"A spectacular 1-2 day getaway spot located in {state}, perfect for an immersive {season.lower()} experience."
        ))
        
        # A hard 1.5-second pause ensures Wikimedia NEVER blocks your computer for rate limiting
        time.sleep(1.5) 
        
    db.session.commit()
    print("\n🎉 Database generation complete! You are ready to start the server.")