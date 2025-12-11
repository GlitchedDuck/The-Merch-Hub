import streamlit as st
import datetime
from typing import Dict, List

# ============================================================================
# CONFIGURATION & STYLING
# ============================================================================

st.set_page_config(
    page_title="Sytner Merchandise Locator",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Brand colors
PRIMARY = "#1e3a8a"  # Sytner blue
ACCENT = "#3b82f6"   # Lighter blue
SUCCESS = "#22c55e"  # Green

# Custom CSS
st.markdown(f"""
<style>
    .stApp {{
        background-color: #f8fafc;
    }}
    
    /* Hide Streamlit branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    
    /* Custom button styling */
    .stButton > button {{
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.3s ease;
    }}
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background-color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
    }}
    
    .stTabs [aria-selected="true"] {{
        background-color: {PRIMARY};
        color: white;
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
        "phone": "029 2046 8000"
    },
    "Sytner BMW Leicester": {
        "region": "East Midlands",
        "contact": "merchandise@sytnerleicester.co.uk",
        "phone": "0116 234 5678"
    },
    "Sytner BMW Nottingham": {
        "region": "East Midlands",
        "contact": "merchandise@sytnernottingham.co.uk",
        "phone": "0115 789 0123"
    },
    "Sytner BMW Solihull": {
        "region": "West Midlands",
        "contact": "merchandise@sytnersolihull.co.uk",
        "phone": "0121 789 4561"
    },
    "Sytner BMW Sheffield": {
        "region": "South Yorkshire",
        "contact": "merchandise@sytnersheffield.co.uk",
        "phone": "0114 567 8901"
    },
    "Sytner BMW Coventry": {
        "region": "West Midlands",
        "contact": "merchandise@sytnercoventry.co.uk",
        "phone": "024 7655 4321"
    },
    "Sytner BMW Newport": {
        "region": "South Wales",
        "contact": "merchandise@sytnernewport.co.uk",
        "phone": "01633 456 789"
    },
    "Sytner BMW Oldbury": {
        "region": "West Midlands",
        "contact": "merchandise@sytneroldbury.co.uk",
        "phone": "0121 456 7890"
    }
}

MERCHANDISE_CATALOG = [
    # Apparel
    {
        "id": "MERCH001",
        "name": "BMW M Sport Polo Shirt",
        "category": "Apparel",
        "description": "Premium cotton polo with embroidered M logo",
        "price": 35.00,
        "sizes": ["S", "M", "L", "XL", "XXL"],
        "colors": ["Navy", "Black", "White"],
        "image": "👕",
        "dealerships": ["Sytner BMW Cardiff", "Sytner BMW Leicester", "Sytner BMW Solihull"],
        "stock_levels": {"Sytner BMW Cardiff": 25, "Sytner BMW Leicester": 18, "Sytner BMW Solihull": 32}
    },
    {
        "id": "MERCH002",
        "name": "Sytner Branded Fleece Jacket",
        "category": "Apparel",
        "description": "Soft fleece with Sytner logo, perfect for showroom",
        "price": 45.00,
        "sizes": ["S", "M", "L", "XL", "XXL"],
        "colors": ["Navy", "Grey"],
        "image": "🧥",
        "dealerships": ["Sytner BMW Nottingham", "Sytner BMW Coventry", "Sytner BMW Sheffield"],
        "stock_levels": {"Sytner BMW Nottingham": 15, "Sytner BMW Coventry": 22, "Sytner BMW Sheffield": 12}
    },
    {
        "id": "MERCH003",
        "name": "BMW Performance Cap",
        "category": "Apparel",
        "description": "Adjustable cap with BMW Motorsport colors",
        "price": 22.00,
        "sizes": ["One Size"],
        "colors": ["Black/Blue", "Navy/White", "Red/White"],
        "image": "🧢",
        "dealerships": ["Sytner BMW Cardiff", "Sytner BMW Newport", "Sytner BMW Oldbury"],
        "stock_levels": {"Sytner BMW Cardiff": 40, "Sytner BMW Newport": 28, "Sytner BMW Oldbury": 35}
    },
    
    # Drinkware
    {
        "id": "MERCH004",
        "name": "BMW Insulated Travel Mug",
        "category": "Drinkware",
        "description": "Stainless steel, keeps drinks hot for 6 hours",
        "price": 18.00,
        "sizes": ["500ml"],
        "colors": ["Silver", "Black"],
        "image": "☕",
        "dealerships": ["Sytner BMW Leicester", "Sytner BMW Solihull", "Sytner BMW Coventry"],
        "stock_levels": {"Sytner BMW Leicester": 45, "Sytner BMW Solihull": 38, "Sytner BMW Coventry": 50}
    },
    {
        "id": "MERCH005",
        "name": "Sytner Water Bottle",
        "category": "Drinkware",
        "description": "BPA-free sports bottle with flip cap",
        "price": 12.00,
        "sizes": ["750ml"],
        "colors": ["Blue", "Black", "White"],
        "image": "🧴",
        "dealerships": ["Sytner BMW Nottingham", "Sytner BMW Sheffield", "Sytner BMW Newport"],
        "stock_levels": {"Sytner BMW Nottingham": 60, "Sytner BMW Sheffield": 42, "Sytner BMW Newport": 55}
    },
    
    # Stationery
    {
        "id": "MERCH006",
        "name": "BMW Branded Notebook Set",
        "category": "Stationery",
        "description": "A5 hardback notebooks, pack of 3",
        "price": 15.00,
        "sizes": ["A5"],
        "colors": ["Mixed"],
        "image": "📓",
        "dealerships": ["Sytner BMW Cardiff", "Sytner BMW Leicester", "Sytner BMW Nottingham"],
        "stock_levels": {"Sytner BMW Cardiff": 35, "Sytner BMW Leicester": 28, "Sytner BMW Nottingham": 40}
    },
    {
        "id": "MERCH007",
        "name": "Premium Pen Set",
        "category": "Stationery",
        "description": "Metal pens with BMW branding, gift box",
        "price": 25.00,
        "sizes": ["Standard"],
        "colors": ["Silver/Blue"],
        "image": "🖊️",
        "dealerships": ["Sytner BMW Solihull", "Sytner BMW Coventry", "Sytner BMW Oldbury"],
        "stock_levels": {"Sytner BMW Solihull": 20, "Sytner BMW Coventry": 18, "Sytner BMW Oldbury": 25}
    },
    
    # Tech Accessories
    {
        "id": "MERCH008",
        "name": "BMW Wireless Charger",
        "category": "Tech",
        "description": "Fast wireless charging pad with BMW logo",
        "price": 35.00,
        "sizes": ["Standard"],
        "colors": ["Black"],
        "image": "📱",
        "dealerships": ["Sytner BMW Leicester", "Sytner BMW Sheffield", "Sytner BMW Cardiff"],
        "stock_levels": {"Sytner BMW Leicester": 15, "Sytner BMW Sheffield": 12, "Sytner BMW Cardiff": 18}
    },
    {
        "id": "MERCH009",
        "name": "USB Memory Stick - 32GB",
        "category": "Tech",
        "description": "Premium metal USB with Sytner branding",
        "price": 20.00,
        "sizes": ["32GB"],
        "colors": ["Silver", "Black"],
        "image": "💾",
        "dealerships": ["Sytner BMW Nottingham", "Sytner BMW Newport", "Sytner BMW Solihull"],
        "stock_levels": {"Sytner BMW Nottingham": 30, "Sytner BMW Newport": 25, "Sytner BMW Solihull": 28}
    },
    
    # Bags
    {
        "id": "MERCH010",
        "name": "BMW Sport Backpack",
        "category": "Bags",
        "description": "Laptop compartment, water resistant",
        "price": 55.00,
        "sizes": ["One Size"],
        "colors": ["Navy", "Black"],
        "image": "🎒",
        "dealerships": ["Sytner BMW Cardiff", "Sytner BMW Coventry", "Sytner BMW Sheffield"],
        "stock_levels": {"Sytner BMW Cardiff": 12, "Sytner BMW Coventry": 15, "Sytner BMW Sheffield": 10}
    },
    {
        "id": "MERCH011",
        "name": "Sytner Tote Bag",
        "category": "Bags",
        "description": "Canvas tote with leather handles",
        "price": 28.00,
        "sizes": ["One Size"],
        "colors": ["Navy", "Beige"],
        "image": "👜",
        "dealerships": ["Sytner BMW Leicester", "Sytner BMW Oldbury", "Sytner BMW Newport"],
        "stock_levels": {"Sytner BMW Leicester": 20, "Sytner BMW Oldbury": 18, "Sytner BMW Newport": 22}
    },
    
    # Desk Items
    {
        "id": "MERCH012",
        "name": "BMW Desktop Clock",
        "category": "Desk Items",
        "description": "Aluminum desk clock with BMW logo",
        "price": 40.00,
        "sizes": ["Standard"],
        "colors": ["Silver"],
        "image": "🕐",
        "dealerships": ["Sytner BMW Solihull", "Sytner BMW Sheffield"],
        "stock_levels": {"Sytner BMW Solihull": 8, "Sytner BMW Sheffield": 6}
    },
    {
        "id": "MERCH013",
        "name": "Leather Desk Mat",
        "category": "Desk Items",
        "description": "Premium leather with Sytner embossing",
        "price": 45.00,
        "sizes": ["Large"],
        "colors": ["Black", "Brown"],
        "image": "📋",
        "dealerships": ["Sytner BMW Cardiff", "Sytner BMW Leicester", "Sytner BMW Nottingham"],
        "stock_levels": {"Sytner BMW Cardiff": 10, "Sytner BMW Leicester": 12, "Sytner BMW Nottingham": 9}
    },
    
    # Gifts
    {
        "id": "MERCH014",
        "name": "BMW Model Car (1:43 Scale)",
        "category": "Gifts",
        "description": "Die-cast model, various models available",
        "price": 65.00,
        "sizes": ["1:43"],
        "colors": ["Various Models"],
        "image": "🏎️",
        "dealerships": ["Sytner BMW Coventry", "Sytner BMW Solihull", "Sytner BMW Cardiff"],
        "stock_levels": {"Sytner BMW Coventry": 15, "Sytner BMW Solihull": 20, "Sytner BMW Cardiff": 18}
    },
    {
        "id": "MERCH015",
        "name": "BMW Keyring Set",
        "category": "Gifts",
        "description": "Metal keyrings, premium gift box",
        "price": 18.00,
        "sizes": ["Standard"],
        "colors": ["Silver", "Black", "Blue"],
        "image": "🔑",
        "dealerships": ["Sytner BMW Leicester", "Sytner BMW Nottingham", "Sytner BMW Sheffield", "Sytner BMW Newport"],
        "stock_levels": {"Sytner BMW Leicester": 45, "Sytner BMW Nottingham": 40, "Sytner BMW Sheffield": 35, "Sytner BMW Newport": 38}
    }
]

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

if 'cart' not in st.session_state:
    st.session_state.cart = []

if 'order_history' not in st.session_state:
    st.session_state.order_history = []

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def add_to_cart(item: Dict, dealership: str, size: str, color: str, quantity: int):
    """Add item to shopping cart"""
    cart_item = {
        "item_id": item["id"],
        "name": item["name"],
        "category": item["category"],
        "price": item["price"],
        "dealership": dealership,
        "size": size,
        "color": color,
        "quantity": quantity,
        "subtotal": item["price"] * quantity,
        "added_at": datetime.datetime.now()
    }
    st.session_state.cart.append(cart_item)
    return True

def remove_from_cart(index: int):
    """Remove item from cart"""
    if 0 <= index < len(st.session_state.cart):
        st.session_state.cart.pop(index)
        return True
    return False

def clear_cart():
    """Clear all items from cart"""
    st.session_state.cart = []

def get_cart_total():
    """Calculate cart total"""
    return sum(item["subtotal"] for item in st.session_state.cart)

def get_cart_count():
    """Get total items in cart"""
    return sum(item["quantity"] for item in st.session_state.cart)

def filter_merchandise(category=None, dealership=None, search_term=None, max_price=None):
    """Filter merchandise based on criteria"""
    results = MERCHANDISE_CATALOG.copy()
    
    if category and category != "All Categories":
        results = [item for item in results if item["category"] == category]
    
    if dealership and dealership != "All Dealerships":
        results = [item for item in results if dealership in item["dealerships"]]
    
    if search_term:
        search_term = search_term.lower()
        results = [item for item in results if 
                   search_term in item["name"].lower() or 
                   search_term in item["description"].lower() or
                   search_term in item["category"].lower()]
    
    if max_price:
        results = [item for item in results if item["price"] <= max_price]
    
    return results

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    # Header
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, {PRIMARY} 0%, {ACCENT} 100%); 
                padding: 32px 24px; border-radius: 16px; margin-bottom: 24px; text-align: center;'>
        <h1 style='color: white; margin: 0 0 12px 0; font-size: 40px; font-weight: 900;'>🛍️ Sytner Merchandise Locator</h1>
        <p style='color: white; font-size: 18px; margin: 0; opacity: 0.95;'>Head Office Exclusive Access</p>
        <p style='color: white; font-size: 14px; margin: 8px 0 0 0; opacity: 0.85;'>Browse and order merchandise from any Sytner dealership</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar - Cart & Filters
    with st.sidebar:
        st.markdown(f"### 🛒 Shopping Cart")
        cart_count = get_cart_count()
        cart_total = get_cart_total()
        
        if cart_count > 0:
            st.markdown(f"""
            <div style='background-color: {SUCCESS}; color: white; padding: 16px; border-radius: 8px; text-align: center; margin-bottom: 16px;'>
                <div style='font-size: 28px; font-weight: 700;'>{cart_count}</div>
                <div style='font-size: 12px; opacity: 0.9;'>Items in Cart</div>
                <div style='font-size: 20px; font-weight: 700; margin-top: 8px;'>£{cart_total:.2f}</div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("🛍️ View Cart & Checkout", use_container_width=True, type="primary"):
                st.session_state.show_cart = True
        else:
            st.info("Your cart is empty")
        
        st.markdown("---")
        st.markdown("### 🔍 Filters")
        
        # Category filter
        categories = ["All Categories"] + sorted(list(set(item["category"] for item in MERCHANDISE_CATALOG)))
        category_filter = st.selectbox("Category", categories, key="category_filter")
        
        # Dealership filter
        dealership_options = ["All Dealerships"] + sorted(list(DEALERSHIPS.keys()))
        dealership_filter = st.selectbox("Dealership", dealership_options, key="dealership_filter")
        
        # Price filter
        max_price = st.slider("Max Price (£)", 0, 100, 100, 5, key="price_filter")
        
        # Search
        search_term = st.text_input("🔎 Search products", placeholder="e.g. polo shirt", key="search_filter")
        
        if st.button("Clear Filters", use_container_width=True):
            st.session_state.category_filter = "All Categories"
            st.session_state.dealership_filter = "All Dealerships"
            st.session_state.price_filter = 100
            st.session_state.search_filter = ""
            st.rerun()
    
    # Main content
    if st.session_state.get('show_cart', False):
        render_cart_page()
    else:
        render_catalog_page(category_filter, dealership_filter, search_term, max_price)

def render_catalog_page(category, dealership, search, max_price):
    """Render the main merchandise catalog"""
    
    # Get filtered results
    filtered_items = filter_merchandise(category, dealership, search, max_price)
    
    # Results summary
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.markdown(f"### 📦 Available Merchandise")
        st.markdown(f"*Showing {len(filtered_items)} of {len(MERCHANDISE_CATALOG)} products*")
    with col2:
        sort_by = st.selectbox("Sort by", ["Name A-Z", "Price Low-High", "Price High-Low", "Category"], label_visibility="collapsed")
    with col3:
        view_mode = st.radio("View", ["Grid", "List"], horizontal=True, label_visibility="collapsed")
    
    # Sort results
    if sort_by == "Price Low-High":
        filtered_items = sorted(filtered_items, key=lambda x: x["price"])
    elif sort_by == "Price High-Low":
        filtered_items = sorted(filtered_items, key=lambda x: x["price"], reverse=True)
    elif sort_by == "Category":
        filtered_items = sorted(filtered_items, key=lambda x: x["category"])
    else:  # Name A-Z
        filtered_items = sorted(filtered_items, key=lambda x: x["name"])
    
    if not filtered_items:
        st.warning("No products found matching your filters. Try adjusting your search criteria.")
        return
    
    # Display items
    if view_mode == "Grid":
        render_grid_view(filtered_items)
    else:
        render_list_view(filtered_items)

def render_grid_view(items):
    """Render products in grid layout"""
    cols_per_row = 3
    
    for i in range(0, len(items), cols_per_row):
        cols = st.columns(cols_per_row)
        for j, col in enumerate(cols):
            if i + j < len(items):
                item = items[i + j]
                with col:
                    render_product_card(item)

def render_product_card(item):
    """Render individual product card"""
    # Available dealerships count
    dealership_count = len(item["dealerships"])
    total_stock = sum(item["stock_levels"].values())
    
    # Card container
    st.markdown(f"""
    <div style='background-color: white; padding: 20px; border-radius: 12px; 
                border: 2px solid #e2e8f0; margin-bottom: 20px; height: 100%;'>
        <div style='font-size: 48px; text-align: center; margin-bottom: 12px;'>{item["image"]}</div>
        <h4 style='color: {PRIMARY}; margin: 0 0 8px 0; font-size: 16px;'>{item["name"]}</h4>
        <p style='color: #64748b; font-size: 13px; margin: 0 0 12px 0; min-height: 40px;'>{item["description"]}</p>
        <div style='background-color: #f8fafc; padding: 8px; border-radius: 6px; margin-bottom: 12px;'>
            <div style='font-size: 24px; font-weight: 700; color: {PRIMARY};'>£{item["price"]:.2f}</div>
            <div style='font-size: 11px; color: #64748b;'>{item["category"]}</div>
        </div>
        <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;'>
            <span style='font-size: 12px; color: #64748b;'>📍 {dealership_count} locations</span>
            <span style='font-size: 12px; color: {"#22c55e" if total_stock > 20 else "#ef4444"};'>
                ● {total_stock} in stock
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Add to cart button
    if st.button(f"🛒 Add to Cart", key=f"add_{item['id']}", use_container_width=True, type="primary"):
        st.session_state.selected_item = item
        st.rerun()
    
    # View details button
    if st.button(f"👁️ View Details", key=f"view_{item['id']}", use_container_width=True):
        show_product_detail_modal(item)

def show_product_detail_modal(item):
    """Show detailed product information in a modal"""
    st.markdown(f"""
    <div style='background-color: white; padding: 24px; border-radius: 12px; border: 2px solid {PRIMARY};'>
        <div style='display: flex; align-items: center; margin-bottom: 20px;'>
            <div style='font-size: 60px; margin-right: 20px;'>{item["image"]}</div>
            <div>
                <h2 style='color: {PRIMARY}; margin: 0 0 8px 0;'>{item["name"]}</h2>
                <p style='color: #64748b; margin: 0; font-size: 16px;'>{item["description"]}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**Price:** £{item['price']:.2f}")
        st.markdown(f"**Category:** {item['category']}")
        st.markdown(f"**Product ID:** {item['id']}")
        
        st.markdown("**Available Sizes:**")
        st.markdown(" • " + " • ".join(item["sizes"]))
        
        st.markdown("**Available Colors:**")
        st.markdown(" • " + " • ".join(item["colors"]))
    
    with col2:
        st.markdown("**📍 Available At:**")
        for dealership in item["dealerships"]:
            stock = item["stock_levels"][dealership]
            stock_color = "#22c55e" if stock > 20 else "#f59e0b" if stock > 10 else "#ef4444"
            st.markdown(f"""
            <div style='background-color: #f8fafc; padding: 8px 12px; border-radius: 6px; margin-bottom: 6px;'>
                <div style='font-weight: 600; color: {PRIMARY};'>{dealership}</div>
                <div style='font-size: 12px; color: {stock_color};'>● {stock} in stock</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add to cart section
    st.markdown("---")
    st.markdown("### 🛒 Add to Cart")
    
    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        selected_dealership = st.selectbox("Dealership", item["dealerships"], key=f"modal_dealership_{item['id']}")
    with col_b:
        selected_size = st.selectbox("Size", item["sizes"], key=f"modal_size_{item['id']}")
    with col_c:
        selected_color = st.selectbox("Color", item["colors"], key=f"modal_color_{item['id']}")
    with col_d:
        quantity = st.number_input("Quantity", 1, 10, 1, key=f"modal_qty_{item['id']}")
    
    if st.button("Add to Cart", type="primary", use_container_width=True, key=f"modal_add_{item['id']}"):
        add_to_cart(item, selected_dealership, selected_size, selected_color, quantity)
        st.success(f"✅ Added {quantity}x {item['name']} to cart!")
        st.balloons()

def render_list_view(items):
    """Render products in list layout"""
    for item in items:
        render_product_list_item(item)

def render_product_list_item(item):
    """Render product as list item"""
    dealership_count = len(item["dealerships"])
    total_stock = sum(item["stock_levels"].values())
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"""
        <div style='background-color: white; padding: 20px; border-radius: 12px; border: 2px solid #e2e8f0; margin-bottom: 16px;'>
            <div style='display: flex; align-items: center;'>
                <div style='font-size: 48px; margin-right: 20px;'>{item["image"]}</div>
                <div style='flex: 1;'>
                    <h4 style='color: {PRIMARY}; margin: 0 0 8px 0;'>{item["name"]}</h4>
                    <p style='color: #64748b; font-size: 14px; margin: 0 0 12px 0;'>{item["description"]}</p>
                    <div style='display: flex; gap: 20px; align-items: center;'>
                        <span style='font-size: 24px; font-weight: 700; color: {PRIMARY};'>£{item["price"]:.2f}</span>
                        <span style='font-size: 12px; color: #64748b;'>Category: {item["category"]}</span>
                        <span style='font-size: 12px; color: #64748b;'>📍 {dealership_count} locations</span>
                        <span style='font-size: 12px; color: {"#22c55e" if total_stock > 20 else "#ef4444"};'>
                            ● {total_stock} in stock
                        </span>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🛒 Add", key=f"list_add_{item['id']}", use_container_width=True, type="primary"):
            st.session_state.selected_item = item
            st.rerun()
        if st.button("👁️ Details", key=f"list_view_{item['id']}", use_container_width=True):
            show_product_detail_modal(item)

def render_cart_page():
    """Render shopping cart and checkout"""
    st.markdown("### 🛒 Your Shopping Cart")
    
    if st.button("← Back to Catalog", type="secondary"):
        st.session_state.show_cart = False
        st.rerun()
    
    st.markdown("---")
    
    if not st.session_state.cart:
        st.info("Your cart is empty. Browse the catalog to add items!")
        return
    
    # Cart items
    for idx, cart_item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([4, 1])
        
        with col1:
            st.markdown(f"""
            <div style='background-color: white; padding: 16px; border-radius: 8px; border: 2px solid #e2e8f0; margin-bottom: 12px;'>
                <div style='display: flex; justify-content: space-between; align-items: center;'>
                    <div>
                        <h4 style='color: {PRIMARY}; margin: 0 0 8px 0;'>{cart_item["name"]}</h4>
                        <p style='color: #64748b; font-size: 13px; margin: 0;'>
                            From: {cart_item["dealership"]}<br>
                            Size: {cart_item["size"]} • Color: {cart_item["color"]} • Qty: {cart_item["quantity"]}
                        </p>
                    </div>
                    <div style='text-align: right;'>
                        <div style='font-size: 20px; font-weight: 700; color: {PRIMARY};'>£{cart_item["subtotal"]:.2f}</div>
                        <div style='font-size: 12px; color: #64748b;'>£{cart_item["price"]:.2f} each</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🗑️ Remove", key=f"remove_{idx}", use_container_width=True):
                remove_from_cart(idx)
                st.rerun()
    
    # Cart summary
    st.markdown("---")
    cart_total = get_cart_total()
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.markdown(f"""
        <div style='background-color: {PRIMARY}; color: white; padding: 20px; border-radius: 12px;'>
            <h3 style='margin: 0 0 16px 0;'>Order Summary</h3>
            <div style='display: flex; justify-content: space-between; margin-bottom: 8px;'>
                <span>Subtotal:</span>
                <span style='font-weight: 700;'>£{cart_total:.2f}</span>
            </div>
            <div style='display: flex; justify-content: space-between; margin-bottom: 8px;'>
                <span>Shipping:</span>
                <span style='font-weight: 700;'>FREE</span>
            </div>
            <hr style='border: 1px solid rgba(255,255,255,0.2); margin: 12px 0;'>
            <div style='display: flex; justify-content: space-between; font-size: 20px; font-weight: 900;'>
                <span>Total:</span>
                <span>£{cart_total:.2f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("✅ Place Order", type="primary", use_container_width=True):
            st.session_state.checkout_mode = True
            st.rerun()
    
    with col1:
        if st.button("🗑️ Clear Cart", use_container_width=True):
            clear_cart()
            st.rerun()
    
    # Checkout form
    if st.session_state.get('checkout_mode', False):
        st.markdown("---")
        st.markdown("### 📝 Delivery Details")
        
        with st.form("checkout_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                name = st.text_input("Full Name *", placeholder="John Smith")
                email = st.text_input("Email *", placeholder="john.smith@sytner.co.uk")
                department = st.text_input("Department *", placeholder="Marketing")
            with col_b:
                phone = st.text_input("Phone Number *", placeholder="07700 900000")
                office_location = st.selectbox("Office Location *", [
                    "Sytner Head Office - Leicester",
                    "Sytner Head Office - Nottingham",
                    "Sytner Regional Office - Birmingham"
                ])
                delivery_preference = st.radio("Delivery", ["Office Delivery", "Collect from Dealership"], horizontal=True)
            
            notes = st.text_area("Special Instructions (optional)", placeholder="Any specific delivery requirements...")
            
            col_submit, col_cancel = st.columns(2)
            with col_submit:
                submitted = st.form_submit_button("🎉 Confirm Order", type="primary", use_container_width=True)
            with col_cancel:
                cancelled = st.form_submit_button("❌ Cancel", use_container_width=True)
            
            if submitted:
                if name and email and department and phone:
                    # Create order
                    order_ref = f"ORD-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
                    order = {
                        "order_ref": order_ref,
                        "items": st.session_state.cart.copy(),
                        "total": cart_total,
                        "customer": {
                            "name": name,
                            "email": email,
                            "department": department,
                            "phone": phone,
                            "office": office_location,
                            "delivery": delivery_preference
                        },
                        "notes": notes,
                        "order_date": datetime.datetime.now(),
                        "status": "Processing"
                    }
                    
                    st.session_state.order_history.append(order)
                    clear_cart()
                    st.session_state.checkout_mode = False
                    st.session_state.show_cart = False
                    
                    st.success(f"""
                    🎉 **Order Placed Successfully!**
                    
                    **Order Reference:** {order_ref}  
                    **Total:** £{cart_total:.2f}  
                    **Delivery To:** {office_location}  
                    
                    📧 Confirmation email sent to: {email}  
                    ⏱️ **Estimated Delivery:** 3-5 working days
                    
                    You can track your order status in the Order History section.
                    """)
                    st.balloons()
                    st.rerun()
                else:
                    st.error("⚠️ Please fill in all required fields")
            
            if cancelled:
                st.session_state.checkout_mode = False
                st.rerun()

# Check if item was selected for adding to cart
if st.session_state.get('selected_item'):
    item = st.session_state.selected_item
    
    st.markdown(f"### 🛒 Add {item['name']} to Cart")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        selected_dealership = st.selectbox("Select Dealership", item["dealerships"], key="add_dealership")
    with col2:
        selected_size = st.selectbox("Select Size", item["sizes"], key="add_size")
    with col3:
        selected_color = st.selectbox("Select Color", item["colors"], key="add_color")
    with col4:
        quantity = st.number_input("Quantity", 1, 10, 1, key="add_quantity")
    
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("✅ Add to Cart", type="primary", use_container_width=True):
            add_to_cart(item, selected_dealership, selected_size, selected_color, quantity)
            st.success(f"✅ Added {quantity}x {item['name']} to cart!")
            del st.session_state.selected_item
            st.balloons()
            st.rerun()
    with col_b:
        if st.button("❌ Cancel", use_container_width=True):
            del st.session_state.selected_item
            st.rerun()
    
    st.markdown("---")

if __name__ == "__main__":
    main()
