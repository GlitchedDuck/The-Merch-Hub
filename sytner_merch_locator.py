import streamlit as st
import datetime
from typing import Dict, List

st.set_page_config(
    page_title="The Merch Hub",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sytner authentic brand colors
PRIMARY = "#1a1a1a"
SECONDARY = "#333333"
ACCENT = "#666666"
LIGHT_GREY = "#f5f5f5"
BORDER = "#e5e5e5"
SUCCESS = "#22c55e"

# Custom CSS - Sytner minimal aesthetic
st.markdown(f"""
<style>
    .stApp {{
        background-color: {LIGHT_GREY};
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
    }}
    
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Primary action buttons - sleek red */
    .stButton > button[kind="primary"] {{
        background-color: {PRIMARY};
        color: white;
        border: none;
        border-radius: 0;
        font-weight: 500;
        letter-spacing: 1px;
        text-transform: uppercase;
        font-size: 11px;
        padding: 14px 28px;
        transition: all 0.3s ease;
    }}
    
    .stButton > button[kind="primary"]:hover {{
        background-color: {SECONDARY};
        border: none;
        transform: translateY(-1px);
    }}
    
    /* Secondary buttons */
    .stButton > button {{
        background-color: white;
        color: {PRIMARY};
        border: 2px solid {PRIMARY};
        border-radius: 0;
        font-weight: 500;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        font-size: 12px;
        padding: 10px 20px;
        transition: all 0.2s ease;
    }}
    
    .stButton > button:hover {{
        background-color: {PRIMARY};
        color: white;
    }}
    
    .stTabs [data-baseweb="tab-list"] {{
        gap: 0;
        border-bottom: 2px solid {BORDER};
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background-color: transparent;
        border-radius: 0;
        padding: 16px 32px;
        font-weight: 400;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        font-size: 12px;
        color: {ACCENT};
    }}
    
    .stTabs [aria-selected="true"] {{
        background-color: transparent;
        color: {PRIMARY};
        border-bottom: 3px solid {PRIMARY};
    }}
    
    .stTextInput > div > div > input {{
        border-radius: 0;
        border: 1px solid {BORDER};
        font-size: 14px;
    }}
    
    .stSelectbox > div > div {{
        border-radius: 0;
        border: 1px solid {BORDER};
    }}
    
    .stRadio > div {{
        gap: 16px;
    }}
    
    /* Cleaner slider */
    .stSlider {{
        padding-top: 8px;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA: DEALERSHIPS & MERCHANDISE
# ============================================================================

DEALERSHIPS = {
    "Sytner BMW Cardiff": {
        "region": "South Wales",
        "contact": "merchandise@sytnercardiff.co.uk",
        "phone": "029 2046 8000",
        "brands": ["BMW", "MINI"]
    },
    "Sytner BMW Sheffield": {
        "region": "Yorkshire",
        "contact": "merchandise@sytnersheffield.co.uk",
        "phone": "0114 567 8901",
        "brands": ["BMW", "MINI"]
    },
    "Sytner Audi Leicester": {
        "region": "East Midlands",
        "contact": "merchandise@sytnerleicester.co.uk",
        "phone": "0116 234 5678",
        "brands": ["Audi"]
    },
    "Sytner Audi Newport": {
        "region": "South Wales",
        "contact": "merchandise@sytnernewport.co.uk",
        "phone": "01633 456 789",
        "brands": ["Audi"]
    },
    "Sytner Mercedes-Benz Nottingham": {
        "region": "East Midlands",
        "contact": "merchandise@sytnernottingham.co.uk",
        "phone": "0115 789 0123",
        "brands": ["Mercedes-Benz"]
    },
    "Sytner Porsche Solihull": {
        "region": "West Midlands",
        "contact": "merchandise@sytnersolihull.co.uk",
        "phone": "0121 789 4561",
        "brands": ["Porsche"]
    },
    "Sytner Jaguar Land Rover Coventry": {
        "region": "West Midlands",
        "contact": "merchandise@sytnercoventry.co.uk",
        "phone": "024 7655 4321",
        "brands": ["Jaguar", "Land Rover"]
    },
    "Sytner Volkswagen Oldbury": {
        "region": "West Midlands",
        "contact": "merchandise@sytneroldbury.co.uk",
        "phone": "0121 456 7890",
        "brands": ["Volkswagen"]
    },
    "Sytner Ferrari Birmingham": {
        "region": "West Midlands",
        "contact": "merchandise@sytnerferrari.co.uk",
        "phone": "0121 555 0100",
        "brands": ["Ferrari"]
    },
    "Sytner Lamborghini London": {
        "region": "London",
        "contact": "merchandise@sytnerlamborghini.co.uk",
        "phone": "020 7123 4567",
        "brands": ["Lamborghini"]
    },
    "Sytner Bentley Manchester": {
        "region": "North West",
        "contact": "merchandise@sytnerbentley.co.uk",
        "phone": "0161 234 5678",
        "brands": ["Bentley"]
    },
    "Sytner Rolls-Royce London": {
        "region": "London",
        "contact": "merchandise@sytnerrolls.co.uk",
        "phone": "020 7987 6543",
        "brands": ["Rolls-Royce"]
    },
    "Sytner Aston Martin Bristol": {
        "region": "South West",
        "contact": "merchandise@sytneraston.co.uk",
        "phone": "0117 345 6789",
        "brands": ["Aston Martin"]
    },
    "Sytner McLaren Birmingham": {
        "region": "West Midlands",
        "contact": "merchandise@sytnermclaren.co.uk",
        "phone": "0121 888 9999",
        "brands": ["McLaren"]
    },
    "Sytner Maserati Leeds": {
        "region": "Yorkshire",
        "contact": "merchandise@sytnermaserati.co.uk",
        "phone": "0113 567 8901",
        "brands": ["Maserati"]
    }
}

MERCHANDISE_CATALOG = [
    # BMW Merchandise
    {"id":"BMW001","brand":"BMW","name":"BMW M Sport Polo Shirt","category":"Apparel","description":"Premium cotton polo with embroidered M logo, perfect for showroom or casual wear","price":45.00,"sizes":["S","M","L","XL","XXL"],"colors":["Navy","Black","White"],"image":"👕","stock_type":"in_stock","stock_levels":{"Sytner BMW Cardiff":25,"Sytner BMW Sheffield":18},"special_order_fee":0},
    {"id":"BMW002","brand":"BMW","name":"BMW Performance Cap","category":"Apparel","description":"Adjustable cap with BMW Motorsport colors and branding","price":28.00,"sizes":["One Size"],"colors":["Black/Blue","Navy/White"],"image":"🧢","stock_type":"in_stock","stock_levels":{"Sytner BMW Cardiff":40,"Sytner BMW Sheffield":32},"special_order_fee":0},
    {"id":"BMW003","brand":"BMW","name":"BMW Insulated Travel Mug","category":"Drinkware","description":"Stainless steel mug, keeps drinks hot for 6 hours","price":22.00,"sizes":["500ml"],"colors":["Silver","Black"],"image":"☕","stock_type":"in_stock","stock_levels":{"Sytner BMW Cardiff":45,"Sytner BMW Sheffield":38},"special_order_fee":0},
    {"id":"BMW004","brand":"BMW","name":"BMW Model Car (1:43 Scale)","category":"Collectibles","description":"Die-cast model car, various BMW series available","price":75.00,"sizes":["1:43"],"colors":["Various Models"],"image":"🏎️","stock_type":"special_order","stock_levels":{},"special_order_fee":5.00},
    {"id":"BMW005","brand":"BMW","name":"BMW Wireless Charger","category":"Tech","description":"Fast wireless charging pad with BMW logo illumination","price":38.00,"sizes":["Standard"],"colors":["Black"],"image":"📱","stock_type":"in_stock","stock_levels":{"Sytner BMW Sheffield":12},"special_order_fee":0},
    {"id":"BMW006","brand":"BMW","name":"BMW Sport Backpack","category":"Bags","description":"Water-resistant backpack with laptop compartment","price":75.00,"sizes":["One Size"],"colors":["Navy","Black"],"image":"🎒","stock_type":"in_stock","stock_levels":{"Sytner BMW Cardiff":8},"special_order_fee":0},
    
    # Audi Merchandise
    {"id":"AUDI001","brand":"Audi","name":"Audi Sport Jacket","category":"Apparel","description":"Water-resistant jacket with Audi Sport branding","price":85.00,"sizes":["S","M","L","XL","XXL"],"colors":["Grey","Black"],"image":"🧥","stock_type":"in_stock","stock_levels":{"Sytner Audi Leicester":15,"Sytner Audi Newport":12},"special_order_fee":0},
    {"id":"AUDI002","brand":"Audi","name":"Audi Rings Keyring","category":"Accessories","description":"Premium metal keyring with four rings logo","price":18.00,"sizes":["Standard"],"colors":["Silver","Black"],"image":"🔑","stock_type":"in_stock","stock_levels":{"Sytner Audi Leicester":50,"Sytner Audi Newport":45},"special_order_fee":0},
    {"id":"AUDI003","brand":"Audi","name":"Audi Sport Water Bottle","category":"Drinkware","description":"BPA-free sports bottle with Audi Sport design, 750ml","price":16.00,"sizes":["750ml"],"colors":["Red/Black","Grey"],"image":"🧴","stock_type":"in_stock","stock_levels":{"Sytner Audi Leicester":35,"Sytner Audi Newport":28},"special_order_fee":0},
    {"id":"AUDI004","brand":"Audi","name":"Audi Collection Notebook","category":"Stationery","description":"A5 premium notebook with leather-effect cover","price":22.00,"sizes":["A5"],"colors":["Black"],"image":"📓","stock_type":"special_order","stock_levels":{},"special_order_fee":3.00},
    {"id":"AUDI005","brand":"Audi","name":"Audi RS Performance Cap","category":"Apparel","description":"Audi RS line cap with embroidered logo","price":32.00,"sizes":["One Size"],"colors":["Black","Grey"],"image":"🧢","stock_type":"in_stock","stock_levels":{"Sytner Audi Leicester":22},"special_order_fee":0},
    
    # Mercedes-Benz Merchandise
    {"id":"MERC001","brand":"Mercedes-Benz","name":"Mercedes-AMG Polo Shirt","category":"Apparel","description":"Performance polo with AMG branding and breathable fabric","price":52.00,"sizes":["S","M","L","XL","XXL"],"colors":["Black","Silver","Petronas Green"],"image":"👕","stock_type":"in_stock","stock_levels":{"Sytner Mercedes-Benz Nottingham":22},"special_order_fee":0},
    {"id":"MERC002","brand":"Mercedes-Benz","name":"Mercedes-Benz Star Cap","category":"Apparel","description":"Classic cap with three-pointed star embroidery","price":32.00,"sizes":["One Size"],"colors":["Black","Navy"],"image":"🧢","stock_type":"in_stock","stock_levels":{"Sytner Mercedes-Benz Nottingham":38},"special_order_fee":0},
    {"id":"MERC003","brand":"Mercedes-Benz","name":"Mercedes-Benz Travel Mug","category":"Drinkware","description":"Premium insulated mug with star logo, 450ml","price":28.00,"sizes":["450ml"],"colors":["Silver","Black"],"image":"☕","stock_type":"in_stock","stock_levels":{"Sytner Mercedes-Benz Nottingham":30},"special_order_fee":0},
    {"id":"MERC004","brand":"Mercedes-Benz","name":"Mercedes-AMG Model Car","category":"Collectibles","description":"1:43 scale AMG GT model with detailed interior","price":85.00,"sizes":["1:43"],"colors":["Various"],"image":"🏎️","stock_type":"special_order","stock_levels":{},"special_order_fee":8.00},
    {"id":"MERC005","brand":"Mercedes-Benz","name":"Mercedes-Benz Leather Wallet","category":"Accessories","description":"Genuine leather wallet with Mercedes star","price":65.00,"sizes":["Standard"],"colors":["Black","Brown"],"image":"👛","stock_type":"special_order","stock_levels":{},"special_order_fee":5.00},
    
    # Porsche Merchandise
    {"id":"POR001","brand":"Porsche","name":"Porsche Motorsport Jacket","category":"Apparel","description":"Premium jacket with Porsche crest and racing stripes","price":120.00,"sizes":["S","M","L","XL","XXL"],"colors":["Black","Guards Red"],"image":"🧥","stock_type":"special_order","stock_levels":{},"special_order_fee":10.00},
    {"id":"POR002","brand":"Porsche","name":"Porsche Crest Keyring","category":"Accessories","description":"Enamel crest keyring, gift box included","price":35.00,"sizes":["Standard"],"colors":["Classic Crest"],"image":"🔑","stock_type":"in_stock","stock_levels":{"Sytner Porsche Solihull":25},"special_order_fee":0},
    {"id":"POR003","brand":"Porsche","name":"Porsche Espresso Cup Set","category":"Drinkware","description":"Set of 2 porcelain espresso cups with crest","price":42.00,"sizes":["90ml"],"colors":["White/Crest"],"image":"☕","stock_type":"in_stock","stock_levels":{"Sytner Porsche Solihull":18},"special_order_fee":0},
    {"id":"POR004","brand":"Porsche","name":"Porsche 911 Model (1:43)","category":"Collectibles","description":"Detailed 911 replica, various generations available","price":95.00,"sizes":["1:43"],"colors":["Various"],"image":"🏎️","stock_type":"special_order","stock_levels":{},"special_order_fee":8.00},
    {"id":"POR005","brand":"Porsche","name":"Porsche Design Pen","category":"Stationery","description":"Premium ballpoint pen with Porsche Design branding","price":75.00,"sizes":["Standard"],"colors":["Silver","Black"],"image":"🖊️","stock_type":"special_order","stock_levels":{},"special_order_fee":6.00},
    
    # Ferrari Merchandise
    {"id":"FER001","brand":"Ferrari","name":"Scuderia Ferrari Team Shirt","category":"Apparel","description":"Official team polo with Prancing Horse logo","price":95.00,"sizes":["S","M","L","XL","XXL"],"colors":["Rosso Corsa","Black"],"image":"👕","stock_type":"in_stock","stock_levels":{"Sytner Ferrari Birmingham":10},"special_order_fee":0},
    {"id":"FER002","brand":"Ferrari","name":"Ferrari Cavallino Keyring","category":"Accessories","description":"Prancing Horse keyring with carbon fiber effect","price":48.00,"sizes":["Standard"],"colors":["Carbon/Yellow"],"image":"🔑","stock_type":"in_stock","stock_levels":{"Sytner Ferrari Birmingham":20},"special_order_fee":0},
    {"id":"FER003","brand":"Ferrari","name":"Ferrari Racing Cap","category":"Apparel","description":"Official Scuderia Ferrari cap with team branding","price":55.00,"sizes":["One Size"],"colors":["Red","Black"],"image":"🧢","stock_type":"in_stock","stock_levels":{"Sytner Ferrari Birmingham":15},"special_order_fee":0},
    {"id":"FER004","brand":"Ferrari","name":"Ferrari Model Collection","category":"Collectibles","description":"1:43 scale models, various Ferrari models available","price":125.00,"sizes":["1:43"],"colors":["Various"],"image":"🏎️","stock_type":"special_order","stock_levels":{},"special_order_fee":15.00},
    {"id":"FER005","brand":"Ferrari","name":"Ferrari Leather Wallet","category":"Accessories","description":"Premium leather wallet with embossed Prancing Horse","price":85.00,"sizes":["Standard"],"colors":["Black","Red"],"image":"👛","stock_type":"special_order","stock_levels":{},"special_order_fee":7.00},
    
    # Lamborghini Merchandise
    {"id":"LAMB001","brand":"Lamborghini","name":"Lamborghini Team Jacket","category":"Apparel","description":"Premium jacket with Raging Bull logo and racing details","price":145.00,"sizes":["S","M","L","XL"],"colors":["Black/Yellow","Black/Orange"],"image":"🧥","stock_type":"special_order","stock_levels":{},"special_order_fee":12.00},
    {"id":"LAMB002","brand":"Lamborghini","name":"Lamborghini Carbon Keyring","category":"Accessories","description":"Real carbon fiber keyring with shield logo","price":65.00,"sizes":["Standard"],"colors":["Carbon Fiber"],"image":"🔑","stock_type":"in_stock","stock_levels":{"Sytner Lamborghini London":12},"special_order_fee":0},
    {"id":"LAMB003","brand":"Lamborghini","name":"Lamborghini Travel Bag","category":"Bags","description":"Luxury weekend bag with leather details","price":195.00,"sizes":["Large"],"colors":["Black"],"image":"👜","stock_type":"special_order","stock_levels":{},"special_order_fee":15.00},
    {"id":"LAMB004","brand":"Lamborghini","name":"Lamborghini Racing Cap","category":"Apparel","description":"Lamborghini Squadra Corse cap with hexagon pattern","price":58.00,"sizes":["One Size"],"colors":["Black/Yellow","Black/Green"],"image":"🧢","stock_type":"in_stock","stock_levels":{"Sytner Lamborghini London":8},"special_order_fee":0},
    
    # Bentley Merchandise
    {"id":"BENT001","brand":"Bentley","name":"Bentley Leather Wallet","category":"Accessories","description":"Hand-stitched leather wallet with Bentley 'B' emblem","price":95.00,"sizes":["Standard"],"colors":["Black","Tan"],"image":"👛","stock_type":"in_stock","stock_levels":{"Sytner Bentley Manchester":8},"special_order_fee":0},
    {"id":"BENT002","brand":"Bentley","name":"Bentley Crystal Decanter","category":"Gifts","description":"Hand-cut crystal decanter with Bentley logo","price":185.00,"sizes":["750ml"],"colors":["Crystal"],"image":"🍷","stock_type":"special_order","stock_levels":{},"special_order_fee":15.00},
    {"id":"BENT003","brand":"Bentley","name":"Bentley Cufflinks","category":"Accessories","description":"Sterling silver cufflinks with 'B' logo","price":125.00,"sizes":["Standard"],"colors":["Silver"],"image":"👔","stock_type":"special_order","stock_levels":{},"special_order_fee":8.00},
    
    # Rolls-Royce Merchandise
    {"id":"RR001","brand":"Rolls-Royce","name":"Rolls-Royce Spirit Pen","category":"Stationery","description":"Luxury fountain pen with Spirit of Ecstasy detail","price":125.00,"sizes":["Standard"],"colors":["Black/Silver"],"image":"🖊️","stock_type":"in_stock","stock_levels":{"Sytner Rolls-Royce London":6},"special_order_fee":0},
    {"id":"RR002","brand":"Rolls-Royce","name":"Rolls-Royce Leather Journal","category":"Stationery","description":"Hand-bound leather journal with RR monogram","price":85.00,"sizes":["A5"],"colors":["Black","Burgundy"],"image":"📓","stock_type":"special_order","stock_levels":{},"special_order_fee":10.00},
    {"id":"RR003","brand":"Rolls-Royce","name":"Rolls-Royce Cufflinks","category":"Accessories","description":"Silver-plated cufflinks with Spirit of Ecstasy","price":150.00,"sizes":["Standard"],"colors":["Silver"],"image":"👔","stock_type":"special_order","stock_levels":{},"special_order_fee":10.00},
    
    # Aston Martin Merchandise
    {"id":"AM001","brand":"Aston Martin","name":"Aston Martin Wings Keyring","category":"Accessories","description":"Enamel wings keyring in gift box","price":45.00,"sizes":["Standard"],"colors":["Silver/Green"],"image":"🔑","stock_type":"in_stock","stock_levels":{"Sytner Aston Martin Bristol":15},"special_order_fee":0},
    {"id":"AM002","brand":"Aston Martin","name":"Aston Martin Polo Shirt","category":"Apparel","description":"Premium polo with embroidered wings logo","price":75.00,"sizes":["S","M","L","XL","XXL"],"colors":["Racing Green","Black","White"],"image":"👕","stock_type":"in_stock","stock_levels":{"Sytner Aston Martin Bristol":12},"special_order_fee":0},
    {"id":"AM003","brand":"Aston Martin","name":"Aston Martin Racing Jacket","category":"Apparel","description":"Team jacket with heritage racing details","price":135.00,"sizes":["S","M","L","XL","XXL"],"colors":["Racing Green"],"image":"🧥","stock_type":"special_order","stock_levels":{},"special_order_fee":12.00},
    
    # McLaren Merchandise
    {"id":"MCL001","brand":"McLaren","name":"McLaren Racing Cap","category":"Apparel","description":"Official McLaren F1 team cap with papaya branding","price":48.00,"sizes":["One Size"],"colors":["Papaya/Blue","Black"],"image":"🧢","stock_type":"in_stock","stock_levels":{"Sytner McLaren Birmingham":18},"special_order_fee":0},
    {"id":"MCL002","brand":"McLaren","name":"McLaren Carbon Keyring","category":"Accessories","description":"Genuine carbon fiber keyring with McLaren logo","price":55.00,"sizes":["Standard"],"colors":["Carbon Fiber"],"image":"🔑","stock_type":"in_stock","stock_levels":{"Sytner McLaren Birmingham":10},"special_order_fee":0},
    {"id":"MCL003","brand":"McLaren","name":"McLaren Team Polo","category":"Apparel","description":"F1 team polo shirt with sponsor logos","price":68.00,"sizes":["S","M","L","XL","XXL"],"colors":["Papaya","Black"],"image":"👕","stock_type":"in_stock","stock_levels":{"Sytner McLaren Birmingham":14},"special_order_fee":0},
    
    # Maserati Merchandise
    {"id":"MAS001","brand":"Maserati","name":"Maserati Trident Keyring","category":"Accessories","description":"Enamel trident keyring with leather strap","price":42.00,"sizes":["Standard"],"colors":["Blue/Silver"],"image":"🔑","stock_type":"in_stock","stock_levels":{"Sytner Maserati Leeds":14},"special_order_fee":0},
    {"id":"MAS002","brand":"Maserati","name":"Maserati Polo Shirt","category":"Apparel","description":"Premium cotton polo with embroidered trident","price":65.00,"sizes":["S","M","L","XL","XXL"],"colors":["Navy","Black","White"],"image":"👕","stock_type":"in_stock","stock_levels":{"Sytner Maserati Leeds":10},"special_order_fee":0},
    {"id":"MAS003","brand":"Maserati","name":"Maserati Leather Wallet","category":"Accessories","description":"Italian leather wallet with trident embossing","price":78.00,"sizes":["Standard"],"colors":["Black","Brown"],"image":"👛","stock_type":"special_order","stock_levels":{},"special_order_fee":6.00},
    
    # Jaguar Merchandise
    {"id":"JAG001","brand":"Jaguar","name":"Jaguar Heritage Jacket","category":"Apparel","description":"Classic jacket with Jaguar leaper embroidery","price":95.00,"sizes":["S","M","L","XL","XXL"],"colors":["British Racing Green","Black"],"image":"🧥","stock_type":"in_stock","stock_levels":{"Sytner Jaguar Land Rover Coventry":8},"special_order_fee":0},
    {"id":"JAG002","brand":"Jaguar","name":"Jaguar Leaper Keyring","category":"Accessories","description":"Chrome leaper keyring in presentation box","price":32.00,"sizes":["Standard"],"colors":["Chrome"],"image":"🔑","stock_type":"in_stock","stock_levels":{"Sytner Jaguar Land Rover Coventry":25},"special_order_fee":0},
    {"id":"JAG003","brand":"Jaguar","name":"Jaguar Polo Shirt","category":"Apparel","description":"Performance polo with Jaguar branding","price":58.00,"sizes":["S","M","L","XL","XXL"],"colors":["Navy","White","Green"],"image":"👕","stock_type":"in_stock","stock_levels":{"Sytner Jaguar Land Rover Coventry":16},"special_order_fee":0},
    
    # Land Rover Merchandise
    {"id":"LR001","brand":"Land Rover","name":"Land Rover Travel Bag","category":"Bags","description":"Rugged canvas travel bag with leather straps","price":85.00,"sizes":["Large"],"colors":["Olive","Black"],"image":"🎒","stock_type":"in_stock","stock_levels":{"Sytner Jaguar Land Rover Coventry":6},"special_order_fee":0},
    {"id":"LR002","brand":"Land Rover","name":"Land Rover Water Bottle","category":"Drinkware","description":"Insulated steel bottle with Land Rover logo, 750ml","price":22.00,"sizes":["750ml"],"colors":["Green","Black"],"image":"🧴","stock_type":"in_stock","stock_levels":{"Sytner Jaguar Land Rover Coventry":30},"special_order_fee":0},
    {"id":"LR003","brand":"Land Rover","name":"Land Rover Heritage Cap","category":"Apparel","description":"Canvas cap with vintage Land Rover badge","price":28.00,"sizes":["One Size"],"colors":["Khaki","Navy"],"image":"🧢","stock_type":"in_stock","stock_levels":{"Sytner Jaguar Land Rover Coventry":22},"special_order_fee":0},
    
    # Volkswagen Merchandise
    {"id":"VW001","brand":"Volkswagen","name":"VW GTI Polo Shirt","category":"Apparel","description":"GTI performance polo with plaid detailing","price":38.00,"sizes":["S","M","L","XL","XXL"],"colors":["Black","Red"],"image":"👕","stock_type":"in_stock","stock_levels":{"Sytner Volkswagen Oldbury":20},"special_order_fee":0},
    {"id":"VW002","brand":"Volkswagen","name":"VW Logo Cap","category":"Apparel","description":"Classic VW cap with embroidered logo","price":24.00,"sizes":["One Size"],"colors":["Blue","Black"],"image":"🧢","stock_type":"in_stock","stock_levels":{"Sytner Volkswagen Oldbury":35},"special_order_fee":0},
    {"id":"VW003","brand":"Volkswagen","name":"VW Travel Mug","category":"Drinkware","description":"Insulated mug with classic VW logo","price":18.00,"sizes":["400ml"],"colors":["Blue","White"],"image":"☕","stock_type":"in_stock","stock_levels":{"Sytner Volkswagen Oldbury":28},"special_order_fee":0},
    
    # MINI Merchandise
    {"id":"MINI001","brand":"MINI","name":"MINI Cooper Cap","category":"Apparel","description":"Classic MINI cap with Union Jack detail","price":26.00,"sizes":["One Size"],"colors":["Black","Red"],"image":"🧢","stock_type":"in_stock","stock_levels":{"Sytner BMW Cardiff":28,"Sytner BMW Sheffield":22},"special_order_fee":0},
    {"id":"MINI002","brand":"MINI","name":"MINI Keyring","category":"Accessories","description":"Chrome MINI logo keyring","price":16.00,"sizes":["Standard"],"colors":["Chrome"],"image":"🔑","stock_type":"in_stock","stock_levels":{"Sytner BMW Cardiff":40,"Sytner BMW Sheffield":35},"special_order_fee":0},
    {"id":"MINI003","brand":"MINI","name":"MINI Cooper Tote Bag","category":"Bags","description":"Canvas tote with MINI Cooper heritage print","price":32.00,"sizes":["One Size"],"colors":["Black","Navy"],"image":"👜","stock_type":"in_stock","stock_levels":{"Sytner BMW Cardiff":12},"special_order_fee":0}
]

# ============================================================================
# SESSION STATE
# ============================================================================

if 'cart' not in st.session_state:
    st.session_state.cart = []
if 'selected_dealership' not in st.session_state:
    st.session_state.selected_dealership = None
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = "Grid"
if 'show_cart' not in st.session_state:
    st.session_state.show_cart = False

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_total_stock(item):
    """Get total stock across all dealerships"""
    return sum(item['stock_levels'].values())

def get_available_dealerships(item):
    """Get list of dealerships with stock"""
    if item['stock_type'] == 'special_order':
        return list(DEALERSHIPS.keys())  # Special orders available from any dealership
    return list(item['stock_levels'].keys())

def filter_catalog(brand=None, category=None, stock_filter=None, dealership=None, search_term=None, price_range=None):
    """Filter merchandise based on criteria"""
    filtered = MERCHANDISE_CATALOG.copy()
    
    if brand and brand != "All Brands":
        filtered = [i for i in filtered if i['brand'] == brand]
    
    if category and category != "All Categories":
        filtered = [i for i in filtered if i['category'] == category]
    
    if stock_filter == "In Stock Only":
        filtered = [i for i in filtered if i['stock_type'] == 'in_stock' and len(i['stock_levels']) > 0]
    elif stock_filter == "Special Order Only":
        filtered = [i for i in filtered if i['stock_type'] == 'special_order']
    
    if dealership and dealership != "All Dealerships":
        # Show items available at this dealership or special orders
        filtered = [i for i in filtered if dealership in i['stock_levels'] or i['stock_type'] == 'special_order']
    
    if search_term:
        search_lower = search_term.lower()
        filtered = [i for i in filtered if 
                   search_lower in i['name'].lower() or 
                   search_lower in i['description'].lower() or
                   search_lower in i['brand'].lower() or
                   search_lower in i['category'].lower()]
    
    if price_range:
        min_price, max_price = price_range
        filtered = [i for i in filtered if min_price <= i['price'] <= max_price]
    
    return filtered

def add_to_cart(item, dealership, quantity=1):
    """Add item to cart"""
    # Check if already in cart from this dealership
    for cart_item in st.session_state.cart:
        if cart_item['id'] == item['id'] and cart_item['dealership'] == dealership:
            cart_item['quantity'] += quantity
            cart_item['subtotal'] = cart_item['quantity'] * (item['price'] + item['special_order_fee'])
            return True
    
    # Add new item
    st.session_state.cart.append({
        'id': item['id'],
        'name': item['name'],
        'brand': item['brand'],
        'category': item['category'],
        'price': item['price'],
        'special_order': item['stock_type'] == 'special_order',
        'special_order_fee': item['special_order_fee'],
        'dealership': dealership,
        'quantity': quantity,
        'subtotal': quantity * (item['price'] + item['special_order_fee'])
    })
    return True

def get_cart_total():
    """Calculate cart total"""
    return sum(item['subtotal'] for item in st.session_state.cart)

def get_cart_count():
    """Get total items in cart"""
    return sum(item['quantity'] for item in st.session_state.cart)

# ============================================================================
# MAIN APP
# ============================================================================

# Header - ultra minimal
st.markdown(f"""
<div style='background: white; padding: 48px 24px; border-bottom: 1px solid {BORDER};'>
    <div style='max-width: 1200px; margin: 0 auto; text-align: center;'>
        <h1 style='color: {PRIMARY}; margin: 0; font-size: 28px; font-weight: 400; letter-spacing: 3px;'>THE MERCH HUB</h1>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar - ultra minimal
with st.sidebar:
    st.markdown("<div style='margin-bottom: 32px;'></div>", unsafe_allow_html=True)
    
    # Dealership filter only
    selected_dealership = st.selectbox(
        "Location",
        ["All Dealerships"] + sorted(DEALERSHIPS.keys()),
        key="dealership_selector"
    )
    
    if selected_dealership != "All Dealerships":
        st.session_state.selected_dealership = selected_dealership
    else:
        st.session_state.selected_dealership = None
    
    st.markdown("<div style='margin: 32px 0;'></div>", unsafe_allow_html=True)
    
    # Cart summary - minimal
    cart_count = get_cart_count()
    cart_total = get_cart_total()
    
    if cart_count > 0:
        st.markdown(f"""
        <div style='background: {PRIMARY}; color: white; padding: 24px; text-align: center;'>
            <div style='font-size: 13px; opacity: 0.7; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px;'>Order</div>
            <div style='font-size: 32px; font-weight: 300; margin-bottom: 16px;'>£{cart_total:.2f}</div>
            <div style='font-size: 12px; opacity: 0.7;'>{cart_count} item{"s" if cart_count != 1 else ""}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div style='margin: 16px 0;'></div>", unsafe_allow_html=True)
        
        if st.button("View Order", use_container_width=True, type="primary"):
            st.session_state.show_cart = True
            st.rerun()
    
    st.markdown("<div style='margin: 48px 0;'></div>", unsafe_allow_html=True)
    
    # Minimal filters
    with st.expander("Filters", expanded=False):
        brands = ["All Brands"] + sorted(list(set(item['brand'] for item in MERCHANDISE_CATALOG)))
        brand_filter = st.selectbox("Brand", brands)
        
        categories = ["All Categories"] + sorted(list(set(item['category'] for item in MERCHANDISE_CATALOG)))
        category_filter = st.selectbox("Category", categories)
        
        stock_filter = st.radio("Stock", ["All Items", "In Stock Only", "Special Order Only"])
        
        st.markdown("**Price**")
        price_range = st.slider("Price Range", 0, 200, (0, 200), 10, label_visibility="collapsed")
        
        search_term = st.text_input("Search", placeholder="Search...")

# Main content area
if st.session_state.show_cart:
    # CART PAGE
    st.markdown("<div style='margin: 48px 0 32px 0;'></div>", unsafe_allow_html=True)
    
    col_back, col_space = st.columns([1, 4])
    with col_back:
        if st.button("← Back"):
            st.session_state.show_cart = False
            st.rerun()
    
    st.markdown("<div style='margin: 32px 0;'></div>", unsafe_allow_html=True)
    
    if not st.session_state.cart:
        st.info("Your order is empty. Browse the catalog to add items.")
    else:
        # Display cart items
        for idx, cart_item in enumerate(st.session_state.cart):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                special_badge = ""
                if cart_item['special_order']:
                    special_badge = f"<span style='background: #ff9800; color: white; padding: 3px 8px; font-size: 10px; border-radius: 0; margin-left: 12px; text-transform: uppercase; letter-spacing: 0.5px;'>Special Order +£{cart_item['special_order_fee']:.0f}</span>"
                
                st.markdown(f"""
                <div style='background: white; padding: 20px; border: 1px solid {BORDER}; margin-bottom: 16px;'>
                    <div style='display: flex; justify-content: space-between; align-items: start;'>
                        <div style='flex: 1;'>
                            <h4 style='margin: 0 0 8px 0; color: {PRIMARY}; font-size: 16px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px;'>
                                {cart_item['name']}{special_badge}
                            </h4>
                            <div style='font-size: 12px; color: {ACCENT}; margin-bottom: 4px;'>
                                <strong>Brand:</strong> {cart_item['brand']} • <strong>Category:</strong> {cart_item['category']}
                            </div>
                            <div style='font-size: 12px; color: {ACCENT}; margin-top: 8px; padding-top: 8px; border-top: 1px solid {BORDER};'>
                                📍 <strong>Collection from:</strong> {cart_item['dealership']}
                            </div>
                            <div style='font-size: 12px; color: {ACCENT}; margin-top: 4px;'>
                                <strong>Quantity:</strong> {cart_item['quantity']}
                            </div>
                        </div>
                        <div style='text-align: right; margin-left: 24px;'>
                            <div style='font-size: 24px; font-weight: 300; color: {PRIMARY};'>£{cart_item['subtotal']:.2f}</div>
                            <div style='font-size: 11px; color: {ACCENT}; margin-top: 4px;'>£{cart_item['price']:.2f} each</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("<br><br>", unsafe_allow_html=True)
                if st.button("REMOVE", key=f"remove_{idx}", use_container_width=True):
                    st.session_state.cart.pop(idx)
                    st.rerun()
        
        # Order summary
        st.markdown("---")
        
        col_summary, col_total = st.columns([2, 1])
        
        with col_total:
            st.markdown(f"""
            <div style='background: {PRIMARY}; color: white; padding: 24px; border-radius: 0;'>
                <h3 style='margin: 0 0 20px 0; font-weight: 300; letter-spacing: 1px; text-transform: uppercase; font-size: 14px;'>
                    ORDER SUMMARY
                </h3>
                <div style='display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 14px; font-weight: 300;'>
                    <span>Subtotal:</span>
                    <span>£{cart_total:.2f}</span>
                </div>
                <div style='display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 14px; font-weight: 300;'>
                    <span>Collection:</span>
                    <span style='color: {SUCCESS};'>FREE</span>
                </div>
                <hr style='border: 1px solid rgba(255,255,255,0.2); margin: 16px 0;'>
                <div style='display: flex; justify-content: space-between; font-size: 20px; font-weight: 300;'>
                    <span>Total:</span>
                    <span>£{cart_total:.2f}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            if st.button("PLACE ORDER", type="primary", use_container_width=True):
                st.session_state.checkout_mode = True
                st.rerun()
        
        with col_summary:
            if st.button("🗑️ CLEAR ORDER", use_container_width=True):
                st.session_state.cart = []
                st.rerun()
        
        # Checkout form
        if st.session_state.get('checkout_mode'):
            st.markdown("---")
            st.markdown("### 📝 YOUR DETAILS")
            
            with st.form("checkout_form"):
                col_a, col_b = st.columns(2)
                with col_a:
                    name = st.text_input("Full Name *", placeholder="John Smith")
                    email = st.text_input("Email Address *", placeholder="john.smith@sytner.co.uk")
                with col_b:
                    phone = st.text_input("Phone Number *", placeholder="07700 900000")
                    department = st.text_input("Department *", placeholder="e.g. Marketing, Finance")
                
                notes = st.text_area("Special Instructions (optional)", placeholder="Any specific requirements...")
                
                st.markdown(f"""
                <div style='background: {LIGHT_GREY}; padding: 16px; border-left: 3px solid {PRIMARY}; margin: 16px 0;'>
                    <div style='font-size: 12px; color: {ACCENT};'>
                        <strong>Collection Policy:</strong> You'll receive email notifications when each item is ready for collection
                        at the designated dealership. In-stock items: 2-3 working days. Special orders: 5-7 working days.
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                col_submit, col_cancel = st.columns(2)
                with col_submit:
                    submitted = st.form_submit_button("✅ CONFIRM ORDER", type="primary", use_container_width=True)
                with col_cancel:
                    cancelled = st.form_submit_button("❌ CANCEL", use_container_width=True)
                
                if submitted:
                    if name and email and phone and department:
                        order_ref = f"MERCH-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                        
                        # Group items by dealership
                        dealerships_in_order = {}
                        for item in st.session_state.cart:
                            dealer = item['dealership']
                            if dealer not in dealerships_in_order:
                                dealerships_in_order[dealer] = []
                            dealerships_in_order[dealer].append(item['name'])
                        
                        collection_summary = "\n".join([f"**{dealer}:** {', '.join(items)}" 
                                                       for dealer, items in dealerships_in_order.items()])
                        
                        st.success(f"""
                        ✅ **ORDER PLACED SUCCESSFULLY**
                        
                        **Order Reference:** {order_ref}  
                        **Total:** £{cart_total:.2f}  
                        **Items:** {cart_count}  
                        
                        **Collection Points:**  
                        {collection_summary}
                        
                        📧 **Confirmation sent to:** {email}  
                        ⏱️ **Collection Timeline:**  
                        - In-stock items: 2-3 working days  
                        - Special orders: 5-7 working days
                        
                        You'll receive individual collection notifications for each dealership.
                        """)
                        st.balloons()
                        
                        # Clear cart
                        st.session_state.cart = []
                        st.session_state.checkout_mode = False
                        st.session_state.show_cart = False
                    else:
                        st.error("⚠️ Please fill in all required fields")
                
                if cancelled:
                    st.session_state.checkout_mode = False
                    st.rerun()

else:
    # CATALOG PAGE
    
    # Filter catalog
    filtered_catalog = filter_catalog(
        brand=brand_filter if brand_filter != "All Brands" else None,
        category=category_filter if category_filter != "All Categories" else None,
        stock_filter=stock_filter if stock_filter != "All Items" else None,
        dealership=st.session_state.selected_dealership,
        search_term=search_term if search_term else None,
        price_range=price_range if price_range != (0, 200) else None
    )
    
    # Results header - minimal
    st.markdown("<div style='margin: 48px 0 24px 0;'></div>", unsafe_allow_html=True)
    
    st.markdown(f"<p style='color: {ACCENT}; font-size: 13px; margin: 0 0 24px 0; letter-spacing: 0.5px;'>{len(filtered_catalog)} items available</p>", unsafe_allow_html=True)
    
    # Sort results by name for clean display
    filtered_catalog = sorted(filtered_catalog, key=lambda x: x['name'])
    
    if not filtered_catalog:
        st.warning("No products found matching your filters.")
    else:
        # Group products by brand for tabs
        brands_in_catalog = {}
        for item in filtered_catalog:
            brand = item['brand']
            if brand not in brands_in_catalog:
                brands_in_catalog[brand] = []
            brands_in_catalog[brand].append(item)
        
        sorted_brands = sorted(brands_in_catalog.keys())
        
        # Create tabs for each brand
        tabs = st.tabs(sorted_brands)
        
        for idx, brand in enumerate(sorted_brands):
            with tabs[idx]:
                st.markdown("<div style='margin: 32px 0;'></div>", unsafe_allow_html=True)
                brand_items = brands_in_catalog[brand]
                
                # 4-column grid
                cols_per_row = 4
                for i in range(0, len(brand_items), cols_per_row):
                    cols = st.columns(cols_per_row)
                    for j, col in enumerate(cols):
                        if i + j < len(brand_items):
                            item = brand_items[i + j]
                            with col:
                                # Availability
                                if item['stock_type'] == 'special_order':
                                    avail_color = "#ff9800"
                                    avail_icon = "⚠"
                                    avail_text = f"Special Order +£{item['special_order_fee']:.0f}"
                                else:
                                    total_stock = sum(item['stock_levels'].values())
                                    if total_stock > 0:
                                        avail_color = "#4caf50"
                                        avail_icon = "✓"
                                        avail_text = f"{total_stock} in stock"
                                    else:
                                        continue
                                
                                # Product card
                                st.markdown(f"""
                                <div style='background: white; border: 1px solid {BORDER}; margin-bottom: 24px;'>
                                    <div style='background: {LIGHT_GREY}; padding: 48px 20px; text-align: center;'>
                                        <div style='font-size: 56px;'>{item['image']}</div>
                                    </div>
                                    <div style='padding: 24px 20px;'>
                                        <div style='font-size: 15px; font-weight: 500; color: {PRIMARY}; margin-bottom: 12px; min-height: 44px; line-height: 1.5;'>
                                            {item['name']}
                                        </div>
                                        <div style='font-size: 11px; color: {ACCENT}; margin-bottom: 20px; text-transform: uppercase; letter-spacing: 0.8px;'>
                                            {item['category']}
                                        </div>
                                        <div style='padding: 16px 0; margin-bottom: 20px; border-top: 1px solid {BORDER}; border-bottom: 1px solid {BORDER};'>
                                            <div style='font-size: 26px; font-weight: 300; color: {PRIMARY}; text-align: center;'>£{item['price']:.2f}</div>
                                        </div>
                                        <div style='font-size: 11px; font-weight: 500; text-align: center; color: {avail_color}; margin-bottom: 16px;'>
                                            {avail_icon} {avail_text}
                                        </div>
                                    </div>
                                </div>
                                """, unsafe_allow_html=True)
                                
                                # Add button
                                if item['stock_type'] == 'special_order':
                                    available_locs = list(DEALERSHIPS.keys())
                                else:
                                    available_locs = list(item['stock_levels'].keys())
                                
                                if len(available_locs) == 1:
                                    if st.button("Add to Order", key=f"add_{item['id']}", use_container_width=True, type="primary"):
                                        add_to_cart(item, available_locs[0])
                                        st.rerun()
                                else:
                                    selected_loc = st.selectbox("Collection", available_locs, key=f"loc_{item['id']}", label_visibility="collapsed")
                                    if st.button("Add", key=f"add_{item['id']}", use_container_width=True, type="primary"):
                                        add_to_cart(item, selected_loc)
                                        st.rerun()
