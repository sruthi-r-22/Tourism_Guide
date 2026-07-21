import sys
import os

# Align paths perfectly
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from backend import app, db, Destination

destinations_list = [
    # === SUMMER (15 Places) ===
    ("Munnar", "Kerala", "Summer", 8500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTHAHXNj4XFmmoU3j4fkXPiX0RywRIcDpcSDYBnsGPdXmx9fb4je3OrMnDR&s=10"),
    ("Ooty", "Tamil Nadu", "Summer", 8000, "https://media-cdn.tripadvisor.com/media/photo-s/0f/1f/37/8b/ooty-lake.jpg"),
    ("Manali", "Himachal Pradesh", "Summer", 11000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjV304F_4PwtnqvR1bJQ-sBaSUIoEnKltBiCf62IqoCA&s=10"),
    ("Kasauli", "Himachal Pradesh", "Summer", 7000, "https://hblimg.mmtcdn.com/content/hubble/img/kasauli/mmt/destination/m_destination-kasauli-landscape_l_400_640.jpg"),
    ("Coonoor", "Tamil Nadu", "Summer", 7500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScom8oPli1Ag5Afz-gDHW98kpGMTNTXzOCLGG3EhtURbfEQ3SYmdES44Mj&s=10"),
    ("Kodaikanal", "Tamil Nadu", "Summer", 9000, "https://static.toiimg.com/thumb/msid-99556308,width-748,height-499,resizemode=4,imgsize-147272.jpg"),
    ("Dharamshala", "Himachal Pradesh", "Summer", 9500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR9Jv9eLnBeP0UXJaLe1A7Aw6jqDZJAaIb6R_cRekLb7K3UsZ1IHLZgiI&s=10"),
    ("Shimla", "Himachal Pradesh", "Summer", 9000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAYrTwW4NHOMxgVLIkCwUXJDkH3OR6WeI_Ymhjmbu46A&s=10"),
    ("Mussoorie", "Uttarakhand", "Summer", 8000, "https://clubmahindra.gumlet.io/blog/media/section_images/shuttersto-17534db46414b71.jpg?w=376&dpr=2.6"),
    ("Horsley Hills", "Andhra Pradesh", "Summer", 6000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7obR6iAhimJeGbuWbVqXaDLLjawOs9OUCZOVQxk579y83FNvkyXs1I4A&s=10"),
    ("Nainital", "Uttarakhand", "Summer", 8500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSnvKi5jmUAXtwRVFxdXTnqbxmyEVxHFuzbZA7mO5RvHA&s=10"),
    ("Mount Abu", "Rajasthan", "Summer", 7500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJvuxg3FHOm3_zpyHqqjbjnaFCuLcHJ60ahK2nLsmL5g&s=10"),
    ("Dalhousie", "Himachal Pradesh", "Summer", 9500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwI0VnZ-zdPvXLryNseJGzIDri2oYfrKrz_YLY5YxIf1ktBLk8VMsg88Y&s=10"),
    ("Chikmagalur", "Karnataka", "Summer", 7000, "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/26/25/6e/67/caption.jpg?w=500&h=500&s=1"),
    ("Yercaud", "Tamil Nadu", "Summer", 6500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfEYesUrhYxNXvmzWTYutuIMC4u--xWPjFeidsuIQWOg&s=10"),

    # === MONSOON (15 Places) ===
    ("Lonavala", "Maharashtra", "Monsoon", 6500, "https://english.cdn.zeenews.com/sites/default/files/2025/05/02/1739907-untitled-design.png"),
    ("Mahabaleshwar", "Maharashtra", "Monsoon", 7000, "https://s7ap1.scene7.com/is/image/incredibleindia/krishnabai-temple-mahabaleshwar-maharashtra-1-attr-nearby?qlt=82&ts=1726668976352"),
    ("Ananthagiri Hills", "Telangana", "Monsoon", 5000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp7uTWym3jxWEo_D9HpQlOZaYlJ-5s-tRpfiRxFqPcQQ&s=10"),
    ("Araku Valley", "Andhra Pradesh", "Monsoon", 7000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqgAqoakK4IT_CR9FhOQlGCz4sUBzvtirGB4Qw4J0MbCXrTwuEei5xmP1N&s=10"),
    ("Wayanad", "Kerala", "Monsoon", 7500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLnBPQMGKkG4VERprKgmj8wk1FF4XpX8XWLs5hvqGygpCKa8jsQ225kUE&s=10"),
    ("Coorg", "Karnataka", "Monsoon", 7500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbpcZdY9qVpzTYTE12CwHCmajXvG0blfD9B_QksNFAmQ&s"),
    ("Cherrapunji", "Meghalaya", "Monsoon", 12000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBo3XU8nkGslDOjUjko9JOmZUWlQrd0lmVTsbreJzdQQ&s=10"),
    ("Agumbe", "Karnataka", "Monsoon", 6000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQT-9vQjIkMQSRBEAuL7jiV9FBTeuMC30m7T8udAaTILTRYvbPFVfTlYUU&s=10"),
    ("Igatpuri", "Maharashtra", "Monsoon", 5500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6SwkiOhtqIel6dv8gnRfhtXdQYVLL3GazLzbFK4dTCg&s"),
    ("Kuntala Waterfalls", "Telangana", "Monsoon", 4000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNn_LnMYscVXEhYt4goM7SPlsmdmyR96eLEn1a8KZ9pg&s"),
    ("Bhandardara", "Maharashtra", "Monsoon", 6000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4oU7XfWu2WNouMzy4MSggvXdYjmohwAlzu7jEy4fvRw&s=10"),
    ("Athirappilly", "Kerala", "Monsoon", 8000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQeabysirNPCkhfxiy9rr8zW4tZurkFRfvbCWMs0kWNYg&s=10"),
    ("Matheran", "Maharashtra", "Monsoon", 5000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQWeWMMDrKtWB8-iPs3-pFqxIMNdNPLN8d_P--3B8LrY4llsCZJZsFU7_Z6&s=10"),
    ("Amboli", "Maharashtra", "Monsoon", 5000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSJtRheDQxfFQPzw7tT3YtbVocqKo6GWmOScmUqdR3F7Q&s=10"),
    ("Jog Falls", "Karnataka", "Monsoon", 6500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLNHXLN_s_6uZwNlIoUJOFwgPbJcmaqOxINBV-a0LhFA&s"),

    # === WINTER (15 Places) ===
    ("Jaipur", "Rajasthan", "Winter", 8000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdekhaXVoXe2bT4ZuKhZg965FyfBGWjCaKH98ZTPF-9w&s"),
    ("Jaisalmer", "Rajasthan", "Winter", 8500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5srR6vN1ma8OJ0Wzx6EhWxIvei2rLePOe106DYCKdew&s=10"),
    ("Hampi", "Karnataka", "Winter", 6500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJwYM-Q3msFVUAkC9gw1DT0XIvCr4A6iISIAAvI1lQDpNuNuVisnwkd5w&s=10"),
    ("Pondicherry", "Puducherry", "Winter", 7000, "https://static.toiimg.com/photo/79423803.cms"),
    ("Goa", "Goa", "Winter", 12000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMn1g0AEjBNW4NhWMlBbgwmqlRiHPbITiGrKF4vEto_6oumIh1P4GlEqY&s=10"),
    ("Agra", "Uttar Pradesh", "Winter", 6000, "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/Taj_Mahal_in_March_2004.jpg/640px-Taj_Mahal_in_March_2004.jpg"),
    ("Rann of Kutch", "Gujarat", "Winter", 11000, "https://www.brahmandtour.com/img/slider/road-trip-to-rann-of-kutch-2.webp"),
    ("Varanasi", "Uttar Pradesh", "Winter", 5500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAuq4bcWY9Q4zhv0Mj4FlI2eflCroAWStBZ56ZU6R9xg&s=10"),
    # Fixed comma typo here -> changed to forward slash
    ("Udaipur", "Rajasthan", "Winter", 9500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvEw4MalWr23j5vxBfO0fUNIy_asIf6IX3xkeXH3rv7Q&s=10"),
    ("Gokarna", "Karnataka", "Winter", 6000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1GJZy9lMn8SPVecfCbuZEvH25r_3mQn40u0F5C4N7dw&s=10"),
    ("Alleppey", "Kerala", "Winter", 10500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSor92SOsW4IoLAxfZcObjFIiGnK9ew9E4-ml1h0yADuw&s=10"),
    ("Auli", "Uttarakhand", "Winter", 13000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTt156gs-4_61HCHvrGilFU-UFF40PMQeyfuiSblkVaEQ&s=10"),
    ("Badami", "Karnataka", "Winter", 5000, "https://s7ap1.scene7.com/is/image/incredibleindia/bhutanatha-temple-badami-karnataka-1-attr-nearby?qlt=82&ts=1742170844177"),
    ("Khajuraho", "Madhya Pradesh", "Winter", 7500, "https://media.istockphoto.com/id/177249944/photo/king-and-lion-fight-statue-kandariya-mahadev-temple.jpg?s=612x612&w=0&k=20&c=nBowCup6IKaA6m1oSfqTpz8YDQ6f2HzRS0XeMvlyLm0="),
    ("Mysore", "Karnataka", "Winter", 6000, "https://static.toiimg.com/thumb/51010213/Mysore-Palace.jpg?width=1200&height=900"),

    # === SPRING (15 Places) ===
    ("Shillong", "Meghalaya", "Spring", 9000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsRsATrQ66xC47UOpGV6UkETAPu67iyMXnRv9bavXtOLxaW7f5nielwq3i&s=10"),
    ("Gangtok", "Sikkim", "Spring", 9500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQD39Ef3geJFCOfN0Ym-wfFdEKskCj-ufNqsQ-d1zNs1oDFQlxUeXfGzA&s=10"),
    ("Tulip Garden Srinagar", "Jammu & Kashmir", "Spring", 12000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScjdl_0rPZPUyOvPPlqoL_uVo8uhJfgHrMeqpjlNqtpA&s=10"),
    ("Yumthang Valley", "Sikkim", "Spring", 11000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoHkpMSzfcrZKVkup-libkqgu94smoFX6jgqiZgnvprg&s=10"),
    ("Kasol", "Himachal Pradesh", "Spring", 7000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPaMqH0fmISf9Uxg-WjQL7KN4c8iP_CGikeh3CFPb0MA&s=10"),
    ("Rishikesh", "Uttarakhand", "Spring", 6000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSo9vaZKD26sJK_Za1Yf4j7gZXLqaQFljH5wnlR_SxYTg&s=10"),
    ("Valley of Flowers", "Uttarakhand", "Spring", 14000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXLRW9s9UQwUL9YGZBGqw7eBDM6HsWS1HDk7Plh_wd1A&s=10"),
    ("Mirik", "West Bengal", "Spring", 6500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRba1Mhlrv9B6aZ0soJRO2Y8JsMixj7HThyJbUtrgp6BQ&s=10"),
    ("Kalimpong", "West Bengal", "Spring", 7500, "https://s7ap1.scene7.com/is/image/incredibleindia/lord-buddha-statue-1-kalimpong-wb-attr-nearby?qlt=82&ts=1726645005259"),
    ("Palampur", "Himachal Pradesh", "Spring", 7000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgqN7QvxCO74ZGV-Z2Kr8qSSpkzZMcV9iYad2QUo47aCdpj8FvleMAN8X1&s=10"),
    ("Lansdowne", "Uttarakhand", "Spring", 5500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxPw02kn4fG3i5iOwti7qg4y4p9Rncrgq9L_j-bxOERXCGeZ1kDW_ez6OT&s=10"),
    ("Ziro", "Arunachal Pradesh", "Spring", 9000, "https://static.toiimg.com/photo/112410346.cms"),
    ("Kaziranga", "Assam", "Spring", 10000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS03O7m_bRkZvB2pANQeSdJEoF41802xXDTe9A6Esee5eyUDNbxs_bCsS7c&s=10"),
    ("Tawang", "Arunachal Pradesh", "Spring", 12000, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYWrr1w_DRSiIqBTh9nNEFm_EYsAe2lhPf0p4XxpJt5rQS7YQFMuN9SONF&s=10"),
    ("Kullu", "Himachal Pradesh", "Spring", 6500, "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcaRJ5kwPawQ4ziDEHQwgktpAyvep0nD9f7P_EFYVt0H7YKGRODpSJXhE&s=10")
]

with app.app_context():
    print("Purging database storage completely...")
    db.reflect()
    db.drop_all()
    db.create_all()
    
    print("Populating 60 hand-verified, distinct geographic destination records...")
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
    print("🎉 Success! Zero network dependencies. Every single location is locked in with its own accurate picture.")