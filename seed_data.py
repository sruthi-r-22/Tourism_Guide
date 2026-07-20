import sys
import os

# Align paths perfectly
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from backend import app, db, Destination

destinations_list = [
    # === SUMMER (15 Unique Places & Images) ===
    ("Munnar", "Kerala", "Summer", 8500, "https://images.unsplash.com/photo-1593693411515-c202e974233c?auto=format&fit=crop&w=600&q=80"),
    ("Ooty", "Tamil Nadu", "Summer", 8000, "https://images.unsplash.com/photo-1549488344-1f9b8d2bd1f3?auto=format&fit=crop&w=600&q=80"),
    ("Manali", "Himachal Pradesh", "Summer", 11000, "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=600&q=80"),
    ("Kasauli", "Himachal Pradesh", "Summer", 7000, "https://images.unsplash.com/photo-1600255821058-c4f89958d700?auto=format&fit=crop&w=600&q=80"),
    ("Coonoor", "Tamil Nadu", "Summer", 7500, "https://images.unsplash.com/photo-1616641775685-618841c7b808?auto=format&fit=crop&w=600&q=80"),
    ("Kodaikanal", "Tamil Nadu", "Summer", 9000, "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=600&q=80"),
    ("Dharamshala", "Himachal Pradesh", "Summer", 9500, "https://images.unsplash.com/photo-1591823737606-588426d0e3d2?auto=format&fit=crop&w=600&q=80"),
    ("Shimla", "Himachal Pradesh", "Summer", 9000, "https://images.unsplash.com/photo-1562916170-664453782d96?auto=format&fit=crop&w=600&q=80"),
    ("Mussoorie", "Uttarakhand", "Summer", 8000, "https://images.unsplash.com/photo-1605540436563-5bca919ae762?auto=format&fit=crop&w=600&q=80"),
    ("Horsley Hills", "Andhra Pradesh", "Summer", 6000, "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=600&q=80"),
    ("Nainital", "Uttarakhand", "Summer", 8500, "https://images.unsplash.com/photo-1610715923992-1dc30c776b7e?auto=format&fit=crop&w=600&q=80"),
    ("Mount Abu", "Rajasthan", "Summer", 7500, "https://images.unsplash.com/photo-1590490359683-65a33d3d7d85?auto=format&fit=crop&w=600&q=80"),
    ("Dalhousie", "Himachal Pradesh", "Summer", 9500, "https://images.unsplash.com/photo-1594964174061-399703657aa7?auto=format&fit=crop&w=600&q=80"),
    ("Chikmagalur", "Karnataka", "Summer", 7000, "https://images.unsplash.com/photo-1602002418082-a4443e081dd1?auto=format&fit=crop&w=600&q=80"),
    ("Yercaud", "Tamil Nadu", "Summer", 6500, "https://images.unsplash.com/photo-1588693951525-66774c86dfcb?auto=format&fit=crop&w=600&q=80"),
    
    # === MONSOON (15 Unique Places & Images) ===
    ("Lonavala", "Maharashtra", "Monsoon", 6500, "https://images.unsplash.com/photo-1584810359583-96fc3448beaa?auto=format&fit=crop&w=600&q=80"),
    ("Mahabaleshwar", "Maharashtra", "Monsoon", 7000, "https://images.unsplash.com/photo-1615671520603-4f9e0307f596?auto=format&fit=crop&w=600&q=80"),
    ("Ananthagiri Hills", "Telangana", "Monsoon", 5000, "https://images.unsplash.com/photo-1500622557534-20d1354ac1de?auto=format&fit=crop&w=600&q=80"),
    ("Araku Valley", "Andhra Pradesh", "Monsoon", 7000, "https://images.unsplash.com/photo-1561484930-998b6a7b22e8?auto=format&fit=crop&w=600&q=80"),
    ("Wayanad", "Kerala", "Monsoon", 7500, "https://images.unsplash.com/photo-1599940824399-b87987ceb72a?auto=format&fit=crop&w=600&q=80"),
    ("Coorg", "Karnataka", "Monsoon", 7500, "https://images.unsplash.com/photo-1618174546416-ca35d46e1654?auto=format&fit=crop&w=600&q=80"),
    ("Cherrapunji", "Meghalaya", "Monsoon", 12000, "https://images.unsplash.com/photo-1544644181-148f3b0dcdc0?auto=format&fit=crop&w=600&q=80"),
    ("Agumbe", "Karnataka", "Monsoon", 6000, "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=600&q=80"),
    ("Igatpuri", "Maharashtra", "Monsoon", 5500, "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=600&q=80"),
    ("Kuntala Waterfalls", "Telangana", "Monsoon", 4000, "https://images.unsplash.com/photo-1432406186174-23278d0af377?auto=format&fit=crop&w=600&q=80"),
    ("Bhandardara", "Maharashtra", "Monsoon", 6000, "https://images.unsplash.com/photo-1533496172125-957774706599?auto=format&fit=crop&w=600&q=80"),
    ("Athirappilly", "Kerala", "Monsoon", 8000, "https://images.unsplash.com/photo-1623193397690-362cb9666fc2?auto=format&fit=crop&w=600&q=80"),
    ("Matheran", "Maharashtra", "Monsoon", 5000, "https://images.unsplash.com/photo-1542273917363-3b1817f69a2d?auto=format&fit=crop&w=600&q=80"),
    ("Udawalawe", "Monsoon Haven", "Monsoon", 15000, "https://images.unsplash.com/photo-1581888227599-779811939961?auto=format&fit=crop&w=600&q=80"),
    ("Jog Falls", "Karnataka", "Monsoon", 6500, "https://images.unsplash.com/photo-1601999109332-542b18dbec57?auto=format&fit=crop&w=600&q=80"),

    # === WINTER (15 Unique Places & Images) ===
    ("Jaipur", "Rajasthan", "Winter", 8000, "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=600&q=80"),
    ("Jaisalmer", "Rajasthan", "Winter", 8500, "https://images.unsplash.com/photo-1574688461530-580a133e9d8c?auto=format&fit=crop&w=600&q=80"),
    ("Hampi", "Karnataka", "Winter", 6500, "https://images.unsplash.com/photo-1600100397608-f010e423b971?auto=format&fit=crop&w=600&q=80"),
    ("Pondicherry", "Puducherry", "Winter", 7000, "https://images.unsplash.com/photo-1589367463456-658b1448b111?auto=format&fit=crop&w=600&q=80"),
    ("Goa", "Goa", "Winter", 12000, "https://images.unsplash.com/photo-1540206395-68808572332f?auto=format&fit=crop&w=600&q=80"),
    ("Agra", "Uttar Pradesh", "Winter", 6000, "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=600&q=80"),
    ("Rann of Kutch", "Gujarat", "Winter", 11000, "https://images.unsplash.com/photo-1603262110263-fb0112e7cc33?auto=format&fit=crop&w=600&q=80"),
    ("Varanasi", "Uttar Pradesh", "Winter", 5500, "https://images.unsplash.com/photo-1561361531-9952a8e3df6a?auto=format&fit=crop&w=600&q=80"),
    ("Udaipur", "Rajasthan", "Winter", 9500, "https://images.unsplash.com/photo-1569949380643-6e7a6ecff340?auto=format&fit=crop&w=600&q=80"),
    ("Gokarna", "Karnataka", "Winter", 6000, "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?auto=format&fit=crop&w=600&q=80"),
    ("Alleppey", "Kerala", "Winter", 10500, "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?auto=format&fit=crop&w=600&q=80"),
    ("Auli", "Uttarakhand", "Winter", 13000, "https://images.unsplash.com/photo-1616422285623-13ff0162193c?auto=format&fit=crop&w=600&q=80"),
    ("Badami", "Karnataka", "Winter", 5000, "https://images.unsplash.com/photo-1627564694465-9831d102e32a?auto=format&fit=crop&w=600&q=80"),
    ("Khajuraho", "Madhya Pradesh", "Winter", 7500, "https://images.unsplash.com/photo-1619546252945-8fbf8e42b292?auto=format&fit=crop&w=600&q=80"),
    ("Mysore", "Karnataka", "Winter", 6000, "https://images.unsplash.com/photo-1590766940554-634a7ed41450?auto=format&fit=crop&w=600&q=80"),

    # === SPRING (15 Unique Places & Images) ===
    ("Shillong", "Meghalaya", "Spring", 9000, "https://images.unsplash.com/photo-1626549219468-b80753086eb2?auto=format&fit=crop&w=600&q=80"),
    ("Gangtok", "Sikkim", "Spring", 9500, "https://images.unsplash.com/photo-1572883777085-bf994be45a9a?auto=format&fit=crop&w=600&q=80"),
    ("Tulip Garden Srinagar", "Jammu & Kashmir", "Spring", 12000, "https://images.unsplash.com/photo-1566838387310-a101714a09c6?auto=format&fit=crop&w=600&q=80"),
    ("Yumthang Valley", "Sikkim", "Spring", 11000, "https://images.unsplash.com/photo-1469474968028-56623f02e42e?auto=format&fit=crop&w=600&q=80"),
    ("Kasol", "Himachal Pradesh", "Spring", 7000, "https://images.unsplash.com/photo-1617469165786-8007eda3caa7?auto=format&fit=crop&w=600&q=80"),
    ("Rishikesh", "Uttarakhand", "Spring", 6000, "https://images.unsplash.com/photo-1598977123418-45f04b616a0e?auto=format&fit=crop&w=600&q=80"),
    ("Valley of Flowers", "Uttarakhand", "Spring", 14000, "https://images.unsplash.com/photo-1447752875215-b2761acb3c5d?auto=format&fit=crop&w=600&q=80"),
    ("Mirik", "West Bengal", "Spring", 6500, "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=600&q=80"),
    ("Kalimpong", "West Bengal", "Spring", 7500, "https://images.unsplash.com/photo-1582298538104-fe2e74c27f59?auto=format&fit=crop&w=600&q=80"),
    ("Palampur", "Himachal Pradesh", "Spring", 7000, "https://images.unsplash.com/photo-1576487248805-cf45f6be679e?auto=format&fit=crop&w=600&q=80"),
    ("Lansdowne", "Uttarakhand", "Spring", 5500, "https://images.unsplash.com/photo-1502082553048-f009c37129b9?auto=format&fit=crop&w=600&q=80"),
    ("Ziro", "Arunachal Pradesh", "Spring", 9000, "https://images.unsplash.com/photo-1622396481328-9b1b78cdd9fd?auto=format&fit=crop&w=600&q=80"),
    ("Kaziranga", "Assam", "Spring", 10000, "https://images.unsplash.com/photo-1561731216-c3a4d99437d5?auto=format&fit=crop&w=600&q=80"),
    ("Tawang", "Arunachal Pradesh", "Spring", 12000, "https://images.unsplash.com/photo-1585128903994-353270bb3f21?auto=format&fit=crop&w=600&q=80"),
    ("Kullu", "Himachal Pradesh", "Spring", 6500, "https://images.unsplash.com/photo-1599307871638-344cb8ba64b6?auto=format&fit=crop&w=600&q=80")
]

with app.app_context():
    print("Purging database storage completely...")
    db.reflect()
    db.drop_all()
    db.create_all()
    
    for name, state, season, budget, img_url in destinations_list:
        db.session.add(Destination(
            name=name,
            state=state,
            season=season,
            budget=budget,
            image_url=img_url,
            description=f"A spectacular 1-2 day getaway spot located in {state}, perfect for an immersive {season.lower()} experience."
        ))
        
    db.session.commit()
    print("🎉 Success! All 60 destinations updated with unique images.")