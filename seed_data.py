import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from backend import app, db, Destination

# Organized list of 60 unique destinations
data = [
    # --- SUMMER ---
    ("Munnar", "Kerala", "Summer", 8500, "https://images.unsplash.com/photo-1593693411515-c202e974233c"),
    ("Ooty", "Tamil Nadu", "Summer", 8000, "https://images.unsplash.com/photo-1549488344-1f9b8d2bd1f3"),
    ("Manali", "Himachal Pradesh", "Summer", 11000, "https://images.unsplash.com/photo-1605649487212-47bdab064df7"),
    ("Kasauli", "Himachal Pradesh", "Summer", 7000, "https://images.unsplash.com/photo-1589483363364-5858e6578794"),
    ("Coonoor", "Tamil Nadu", "Summer", 7500, "https://images.unsplash.com/photo-1616641775685-618841c7b808"),
    ("Kodaikanal", "Tamil Nadu", "Summer", 9000, "https://images.unsplash.com/photo-1612623326173-0498305e940a"),
    ("Dharamshala", "Himachal Pradesh", "Summer", 9500, "https://images.unsplash.com/photo-1591823737606-588426d0e3d2"),
    ("Shimla", "Himachal Pradesh", "Summer", 9000, "https://images.unsplash.com/photo-1562916170-664453782d96"),
    ("Mussoorie", "Uttarakhand", "Summer", 8000, "https://images.unsplash.com/photo-1605540436563-5bca919ae762"),
    ("Horsley Hills", "Andhra Pradesh", "Summer", 6000, "https://images.unsplash.com/photo-1574688461530-580a133e9d8c"),
    ("Nainital", "Uttarakhand", "Summer", 8500, "https://images.unsplash.com/photo-1589483363364-5858e6578794"),
    ("Mount Abu", "Rajasthan", "Summer", 7500, "https://images.unsplash.com/photo-1590490359683-65a33d3d7d85"),
    ("Dalhousie", "Himachal Pradesh", "Summer", 9500, "https://images.unsplash.com/photo-1594964174061-399703657aa7"),
    ("Chikmagalur", "Karnataka", "Summer", 7000, "https://images.unsplash.com/photo-1602002418082-a4443e081dd1"),
    ("Yercaud", "Tamil Nadu", "Summer", 6500, "https://images.unsplash.com/photo-1614088031586-173673b0a701"),
    
    # --- MONSOON ---
    ("Lonavala", "Maharashtra", "Monsoon", 6500, "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec"),
    ("Mahabaleshwar", "Maharashtra", "Monsoon", 7000, "https://images.unsplash.com/photo-1615671520603-4f9e0307f596"),
    ("Ananthagiri Hills", "Telangana", "Monsoon", 5000, "https://images.unsplash.com/photo-1613946069412-38f7f8ff0b6d"),
    ("Araku Valley", "Andhra Pradesh", "Monsoon", 7000, "https://images.unsplash.com/photo-1561484930-998b6a7b22e8"),
    ("Wayanad", "Kerala", "Monsoon", 7500, "https://images.unsplash.com/photo-1599940824399-b87987ceb72a"),
    ("Coorg", "Karnataka", "Monsoon", 7500, "https://images.unsplash.com/photo-1602002418082-a4443e081dd1"),
    ("Cherrapunji", "Meghalaya", "Monsoon", 12000, "https://images.unsplash.com/photo-1544644181-148f3b0dcdc0"),
    ("Agumbe", "Karnataka", "Monsoon", 6000, "https://images.unsplash.com/photo-1506744038136-46273834b3fb"),
    ("Igatpuri", "Maharashtra", "Monsoon", 5500, "https://images.unsplash.com/photo-1615671520603-4f9e0307f596"),
    ("Kuntala Waterfalls", "Telangana", "Monsoon", 4000, "https://images.unsplash.com/photo-1613946069412-38f7f8ff0b6d"),
    ("Bhandardara", "Maharashtra", "Monsoon", 6000, "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec"),
    ("Athirappilly", "Kerala", "Monsoon", 8000, "https://images.unsplash.com/photo-1623193397690-362cb9666fc2"),
    ("Matheran", "Maharashtra", "Monsoon", 5000, "https://images.unsplash.com/photo-1615671520603-4f9e0307f596"),
    ("Udawalawe", "Sri Lanka", "Monsoon", 15000, "https://images.unsplash.com/photo-1590054763901-389f41757134"),
    ("Udaipur", "Rajasthan", "Monsoon", 9500, "https://images.unsplash.com/photo-1569949380643-6e7a6ecff340"),

    # --- WINTER ---
    ("Jaipur", "Rajasthan", "Winter", 8000, "https://images.unsplash.com/photo-1599661046289-e31897846e41"),
    ("Jaisalmer", "Rajasthan", "Winter", 8500, "https://images.unsplash.com/photo-1574688461530-580a133e9d8c"),
    ("Hampi", "Karnataka", "Winter", 6500, "https://images.unsplash.com/photo-1600100397608-f010e423b971"),
    ("Pondicherry", "Puducherry", "Winter", 7000, "https://images.unsplash.com/photo-1589367463456-658b1448b111"),
    ("Goa", "Goa", "Winter", 12000, "https://images.unsplash.com/photo-1540206395-68808572332f"),
    ("Agra", "Uttar Pradesh", "Winter", 6000, "https://images.unsplash.com/photo-1564507592333-c60657eea523"),
    ("Rann of Kutch", "Gujarat", "Winter", 11000, "https://images.unsplash.com/photo-1600100397608-f010e423b971"),
    ("Varanasi", "Uttar Pradesh", "Winter", 5500, "https://images.unsplash.com/photo-1561361531-9952a8e3df6a"),
    ("Gokarna", "Karnataka", "Winter", 6000, "https://images.unsplash.com/photo-1589367463456-658b1448b111"),
    ("Alleppey", "Kerala", "Winter", 10500, "https://images.unsplash.com/photo-1593693397690-362cb9666fc2"),
    ("Auli", "Uttarakhand", "Winter", 13000, "https://images.unsplash.com/photo-1591823737606-588426d0e3d2"),
    ("Badami", "Karnataka", "Winter", 5000, "https://images.unsplash.com/photo-1600100397608-f010e423b971"),
    ("Khajuraho", "Madhya Pradesh", "Winter", 7500, "https://images.unsplash.com/photo-1599661046289-e31897846e41"),
    ("Mysore", "Karnataka", "Winter", 6000, "https://images.unsplash.com/photo-1600100397608-f010e423b971"),
    ("Leh", "Ladakh", "Winter", 20000, "https://images.unsplash.com/photo-1596176530529-78163a4f7af2"),

    # --- SPRING ---
    ("Shillong", "Meghalaya", "Spring", 9000, "https://images.unsplash.com/photo-1544644181-148f3b0dcdc0"),
    ("Gangtok", "Sikkim", "Spring", 9500, "https://images.unsplash.com/photo-1544644181-148f3b0dcdc0"),
    ("Srinagar", "Jammu & Kashmir", "Spring", 12000, "https://images.unsplash.com/photo-1596176530529-78163a4f7af2"),
    ("Yumthang Valley", "Sikkim", "Spring", 11000, "https://images.unsplash.com/photo-1544644181-148f3b0dcdc0"),
    ("Kasol", "Himachal Pradesh", "Spring", 7000, "https://images.unsplash.com/photo-1605649487212-47bdab064df7"),
    ("Rishikesh", "Uttarakhand", "Spring", 6000, "https://images.unsplash.com/photo-1589483363364-5858e6578794"),
    ("Valley of Flowers", "Uttarakhand", "Spring", 14000, "https://images.unsplash.com/photo-1469474968028-56623f02e42e"),
    ("Mirik", "West Bengal", "Spring", 6500, "https://images.unsplash.com/photo-1544735716-392fe2489ffa"),
    ("Kalimpong", "West Bengal", "Spring", 7500, "https://images.unsplash.com/photo-1544735716-392fe2489ffa"),
    ("Palampur", "Himachal Pradesh", "Spring", 7000, "https://images.unsplash.com/photo-1589483363364-5858e6578794"),
    ("Lansdowne", "Uttarakhand", "Spring", 5500, "https://images.unsplash.com/photo-1605540436563-5bca919ae762"),
    ("Ziro", "Arunachal Pradesh", "Spring", 9000, "https://images.unsplash.com/photo-1544644181-148f3b0dcdc0"),
    ("Kaziranga", "Assam", "Spring", 10000, "https://images.unsplash.com/photo-1544644181-148f3b0dcdc0"),
    ("Tawang", "Arunachal Pradesh", "Spring", 12000, "https://images.unsplash.com/photo-1596176530529-78163a4f7af2"),
    ("Kullu", "Himachal Pradesh", "Spring", 6500, "https://images.unsplash.com/photo-1605649487212-47bdab064df7")
]

with app.app_context():
    db.session.query(Destination).delete()
    for name, state, season, budget, img in data:
        db.session.add(Destination(name=name, state=state, season=season, budget=budget, image_url=img, description=f"A beautiful place in {state} perfect for your next trip!"))
    db.session.commit()
    print("Database Synced!")