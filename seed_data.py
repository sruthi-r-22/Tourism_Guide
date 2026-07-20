import sys
import os
import json
import urllib.request
import urllib.parse
import urllib.error
import time
import ssl

# Align paths perfectly
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from backend import app, db, Destination

def get_wiki_image(place_name):
    """Fetches image from Wikipedia and handles 429 Too Many Requests errors."""
    query = urllib.parse.quote(place_name)
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={query}&prop=pageimages&format=json&pithumbsize=800"
    
    # Using a unique User-Agent keeps Wikipedia from treating us like a malicious bot
    headers = {'User-Agent': 'LocalTourismApp/1.0 (Learning Project) Python-urllib/3'}
    req = urllib.request.Request(url, headers=headers)
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # Give it up to 3 tries to bypass the 429 error
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})
                
                for page_id, page_data in pages.items():
                    if 'thumbnail' in page_data:
                        return page_data['thumbnail']['source']
                break # If successful but no image found, break the retry loop
                
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait_time = 3  # Wait 3 seconds if Wikipedia says we are going too fast
                print(f" [Slowing down...] ", end="")
                time.sleep(wait_time)
            else:
                break
        except Exception as e:
            break
            
    # Fallback image only if all retries fail
    return "https://images.unsplash.com/photo-1548013146-72479768bada?auto=format&fit=crop&w=600&q=80"

destinations_list = [
    # === SUMMER ===
    ("Munnar", "Kerala", "Summer", 8500, "Munnar"),
    ("Ooty", "Tamil Nadu", "Summer", 8000, "Ooty"),
    ("Manali", "Himachal Pradesh", "Summer", 11000, "Manali, Himachal Pradesh"),
    ("Kasauli", "Himachal Pradesh", "Summer", 7000, "Kasauli"),
    ("Coonoor", "Tamil Nadu", "Summer", 7500, "Coonoor"),
    ("Kodaikanal", "Tamil Nadu", "Summer", 9000, "Kodaikanal"),
    ("Dharamshala", "Himachal Pradesh", "Summer", 9500, "Dharamshala"),
    ("Shimla", "Himachal Pradesh", "Summer", 9000, "Shimla"),
    ("Mussoorie", "Uttarakhand", "Summer", 8000, "Mussoorie"),
    ("Horsley Hills", "Andhra Pradesh", "Summer", 6000, "Horsley Hills"),
    ("Nainital", "Uttarakhand", "Summer", 8500, "Nainital"),
    ("Mount Abu", "Rajasthan", "Summer", 7500, "Mount Abu"),
    ("Dalhousie", "Himachal Pradesh", "Summer", 9500, "Dalhousie, India"),
    ("Chikmagalur", "Karnataka", "Summer", 7000, "Chikmagalur"),
    ("Yercaud", "Tamil Nadu", "Summer", 6500, "Yercaud"),

    # === MONSOON ===
    ("Lonavala", "Maharashtra", "Monsoon", 6500, "Lonavala"),
    ("Mahabaleshwar", "Maharashtra", "Monsoon", 7000, "Mahabaleshwar"),
    ("Ananthagiri Hills", "Telangana", "Monsoon", 5000, "Ananthagiri Hills"),
    ("Araku Valley", "Andhra Pradesh", "Monsoon", 7000, "Araku Valley"),
    ("Wayanad", "Kerala", "Monsoon", 7500, "Wayanad district"),
    ("Coorg", "Karnataka", "Monsoon", 7500, "Kodagu district"),
    ("Cherrapunji", "Meghalaya", "Monsoon", 12000, "Cherrapunji"),
    ("Agumbe", "Karnataka", "Monsoon", 6000, "Agumbe"),
    ("Igatpuri", "Maharashtra", "Monsoon", 5500, "Igatpuri"),
    ("Kuntala Waterfalls", "Telangana", "Monsoon", 4000, "Kuntala Waterfall"),
    ("Bhandardara", "Maharashtra", "Monsoon", 6000, "Bhandardara"),
    ("Athirappilly", "Kerala", "Monsoon", 8000, "Athirappilly Falls"),
    ("Matheran", "Maharashtra", "Monsoon", 5000, "Matheran"),
    ("Amboli", "Maharashtra", "Monsoon", 5000, "Amboli, Sindhudurg"),
    ("Jog Falls", "Karnataka", "Monsoon", 6500, "Jog Falls"),

    # === WINTER ===
    ("Jaipur", "Rajasthan", "Winter", 8000, "Jaipur"),
    ("Jaisalmer", "Rajasthan", "Winter", 8500, "Jaisalmer"),
    ("Hampi", "Karnataka", "Winter", 6500, "Hampi"),
    ("Pondicherry", "Puducherry", "Winter", 7000, "Pondicherry"),
    ("Goa", "Goa", "Winter", 12000, "Goa"),
    ("Agra", "Uttar Pradesh", "Winter", 6000, "Agra"),
    ("Rann of Kutch", "Gujarat", "Winter", 11000, "Rann of Kutch"),
    ("Varanasi", "Uttar Pradesh", "Winter", 5500, "Varanasi"),
    ("Udaipur", "Rajasthan", "Winter", 9500, "Udaipur"),
    ("Gokarna", "Karnataka", "Winter", 6000, "Gokarna, Karnataka"),
    ("Alleppey", "Kerala", "Winter", 10500, "Alappuzha"),
    ("Auli", "Uttarakhand", "Winter", 13000, "Auli, India"),
    ("Badami", "Karnataka", "Winter", 5000, "Badami"),
    ("Khajuraho", "Madhya Pradesh", "Winter", 7500, "Khajuraho Group of Monuments"),
    ("Mysore", "Karnataka", "Winter", 6000, "Mysore"),

    # === SPRING ===
    ("Shillong", "Meghalaya", "Spring", 9000, "Shillong"),
    ("Gangtok", "Sikkim", "Spring", 9500, "Gangtok"),
    ("Tulip Garden Srinagar", "Jammu & Kashmir", "Spring", 12000, "Indira Gandhi Memorial Tulip Garden"),
    ("Yumthang Valley", "Sikkim", "Spring", 11000, "Yumthang Valley of Flowers"),
    ("Kasol", "Himachal Pradesh", "Spring", 7000, "Kasol"),
    ("Rishikesh", "Uttarakhand", "Spring", 6000, "Rishikesh"),
    ("Valley of Flowers", "Uttarakhand", "Spring", 14000, "Valley of Flowers National Park"),
    ("Mirik", "West Bengal", "Spring", 6500, "Mirik"),
    ("Kalimpong", "West Bengal", "Spring", 7500, "Kalimpong"),
    ("Palampur", "Himachal Pradesh", "Spring", 7000, "Palampur"),
    ("Lansdowne", "Uttarakhand", "Spring", 5500, "Lansdowne, India"),
    ("Ziro", "Arunachal Pradesh", "Spring", 9000, "Ziro, Arunachal Pradesh"),
    ("Kaziranga", "Assam", "Spring", 10000, "Kaziranga National Park"),
    ("Tawang", "Arunachal Pradesh", "Spring", 12000, "Tawang"),
    ("Kullu", "Himachal Pradesh", "Spring", 6500, "Kullu")
]

with app.app_context():
    print("Purging database storage completely...")
    db.reflect()
    db.drop_all()
    db.create_all()
    
    print(f"Downloading images at a safe speed for {len(destinations_list)} destinations...")
    
    for name, state, season, budget, wiki_query in destinations_list:
        print(f"-> Fetching {name} ({season})...", end=" ")
        
        img_url = get_wiki_image(wiki_query)
        
        if "unsplash" in img_url:
            print("❌ FAILED (Used Fallback)")
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
        
        # Hard pause of 1.5 seconds between every single request to keep Wikipedia happy
        time.sleep(1.5) 
        
    db.session.commit()
    print("\n🎉 Sync Complete! The database is safely loaded.")