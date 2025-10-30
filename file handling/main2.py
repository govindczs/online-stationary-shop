stationery_catalog = {
    "Ballpoint Pen": {"price": 0.99, "stock": 500, "ratings": [4.5, 4.0]},
    "Gel Pen": {"price": 1.49, "stock": 300, "ratings": [4.8, 4.2]},
    "Fountain Pen": {"price": 8.99, "stock": 80, "ratings": [4.7, 4.9]},
    "Marker Pen": {"price": 2.49, "stock": 200, "ratings": [4.3]},
    "HB Pencil": {"price": 0.49, "stock": 1000, "ratings": [4.0]},
    "Mechanical Pencil": {"price": 3.99, "stock": 150, "ratings": [4.6]},
    "Colored Pencil": {"price": 1.99, "stock": 400, "ratings": [4.4]},
    "Yellow Highlighter": {"price": 1.29, "stock": 250, "ratings": [4.2]},
    "Pink Highlighter": {"price": 1.29, "stock": 200, "ratings": [4.1]},
    "Spiral Notebook": {"price": 12.99, "stock": 50, "ratings": [4.7, 4.9]},
    "Composition Book": {"price": 8.99, "stock": 75, "ratings": [4.3]},
    "Graph Notebook": {"price": 14.99, "stock": 40, "ratings": [4.8]},
    "A4 Paper (500 sheets)": {"price": 5.99, "stock": 100, "ratings": [4.5]},
    "Legal Paper": {"price": 6.99, "stock": 80, "ratings": [4.4]},
    "Colored Paper Pack": {"price": 9.99, "stock": 60, "ratings": [4.6]},
    "Yellow Post-it": {"price": 2.99, "stock": 120, "ratings": [4.7]},
    "Rainbow Post-it": {"price": 4.99, "stock": 90, "ratings": [4.8]},
    "Standard Stapler": {"price": 7.99, "stock": 60, "ratings": [4.2]},
    "Heavy Duty Stapler": {"price": 19.99, "stock": 25, "ratings": [4.5]},
    "Scotch Tape": {"price": 3.49, "stock": 150, "ratings": [4.3]},
    "Packing Tape": {"price": 4.99, "stock": 100, "ratings": [4.1]},
    "Manila Folder": {"price": 1.99, "stock": 200, "ratings": [4.0]},
    "Plastic Folder": {"price": 2.99, "stock": 180, "ratings": [4.4]},
    "Fine Tip Markers": {"price": 8.99, "stock": 70, "ratings": [4.6]},
    "Brush Markers": {"price": 15.99, "stock": 45, "ratings": [4.9]},
    "24-Pack Crayons": {"price": 4.99, "stock": 120, "ratings": [4.7]},
    "64-Pack Crayons": {"price": 9.99, "stock": 80, "ratings": [4.8]},
    "Watercolor Set": {"price": 12.99, "stock": 50, "ratings": [4.6]},
    "Acrylic Paint Set": {"price": 19.99, "stock": 35, "ratings": [4.7]},
    "Ceramic Pen Holder": {"price": 6.99, "stock": 40, "ratings": [4.3]},
    "Wooden Pen Holder": {"price": 9.99, "stock": 30, "ratings": [4.5]},
    "Basic Calculator": {"price": 8.99, "stock": 60, "ratings": [4.2]},
    "Scientific Calculator": {"price": 24.99, "stock": 40, "ratings": [4.6]}
}

# 5 HOT ITEMS ALREADY IN OFFERZONE! (SIMPLIFIED)
offerzone = {
    "Gel Pen (Offer)": {
        'original_price': 1.49,
        'discount_price': 0.89,  # 40% OFF!
        'discount_percent': 40,
        'stock': 100
    },
    "HB Pencil (Offer)": {
        'original_price': 0.49,
        'discount_price': 0.29,  # 41% OFF!
        'discount_percent': 41,
        'stock': 200
    },
    "Spiral Notebook (Offer)": {
        'original_price': 12.99,
        'discount_price': 8.99,  # 31% OFF!
        'discount_percent': 31,
        'stock': 25
    },
    "Yellow Post-it (Offer)": {
        'original_price': 2.99,
        'discount_price': 1.79,  # 40% OFF!
        'discount_percent': 40,
        'stock': 50
    },
    "24-Pack Crayons (Offer)": {
        'original_price': 4.99,
        'discount_price': 2.99,  # 40% OFF!
        'discount_percent': 40,
        'stock': 60
    }
}

# Updated stock for original items (reduced due to OfferZone)
stationery_catalog["Gel Pen"]["stock"] -= 100
stationery_catalog["HB Pencil"]["stock"] -= 200
stationery_catalog["Spiral Notebook"]["stock"] -= 25
stationery_catalog["Yellow Post-it"]["stock"] -= 50
stationery_catalog["24-Pack Crayons"]["stock"] -= 60

def find_item_insensitive(item_input):
    """Find exact item details with case-insensitive matching."""
    for item_name in stationery_catalog:
        if item_input.lower() == item_name.lower():
            return {
                'item_name': item_name,
                'details': stationery_catalog[item_name]
            }
    return None

def find_offer_item_insensitive(item_input):
    """Find exact offer item details with case-insensitive matching."""
    for item_name in offerzone:
        if item_input.lower() == item_name.lower():
            return {
                'item_name': item_name,
                'details': offerzone[item_name]
            }
    return None

def query_all_items():
    """Query and display all items in the stationery catalog."""
    print("\n📚 All Items in Stationery Catalog:")
    print("-" * 60)
    print(f"{'Item':<30} {'Price':<8} {'Stock':<8} {'Ratings':<12}")
    print("-" * 60)
    for item_name, details in stationery_catalog.items():
        ratings = details['ratings']
        print(f"{item_name:<30} ${details['price']:<7.2f} {details['stock']:<7} {ratings}")
    print("-" * 60)

def display_offerzone():
    """Display all items in OfferZone."""
    if not offerzone:
        print("\n🎉 OfferZone is empty! No discounts available.")
        return
    
    print("\n=== OFFER ZONE - HOT DEALS! ===")
    print("-" * 70)
    print(f"{'Item':<30} {'Original':<8} {'OFF':<5} {'NOW':<6} {'Stock':<6} {'SAVE':<6}")
    print("-" * 70)
    for item_name, details in offerzone.items():
        orig_price = details['original_price']
        disc_price = details['discount_price']
        save = orig_price - disc_price
        print(f"{item_name:<30} ${orig_price:<7.2f} {details['discount_percent']}%{'':<1} ${disc_price:<5.2f} {details['stock']:<5} ${save:<5.2f}")
    print("-" * 70)

def admin_add_to_offerzone():
    """Admin: Add item to OfferZone."""
    print("\n=== ADMIN: Add to OfferZone ===")
    print("Available Items:", ", ".join(list(stationery_catalog.keys())[:5]), "...(type to search)")
    item_input = input("Enter item name: ").strip()
    
    item_info = find_item_insensitive(item_input)
    if not item_info:
        print("❌ Invalid item name!")
        return
    
    item = item_info['details']
    actual_item = item_info['item_name']
    
    if item['stock'] <= 0:
        print("❌ Item is out of stock! Cannot add to OfferZone.")
        return
    
    try:
        discount_percent = float(input(f"Enter discount % (0-90): "))
        if not 0 < discount_percent <= 90:
            print("❌ Discount must be between 1-90%!")
            return
        
        offer_stock = int(input(f"Enter stock for offer (Available: {item['stock']}): "))
        if offer_stock <= 0 or offer_stock > item['stock']:
            print("❌ Invalid stock quantity!")
            return
    except ValueError:
        print("❌ Please enter valid numbers!")
        return
    
    offer_item_name = f"{actual_item} (Offer)"
    original_price = item['price']
    discount_price = original_price * (1 - discount_percent / 100)
    
    offerzone[offer_item_name] = {
        'original_price': original_price,
        'discount_price': discount_price,
        'discount_percent': discount_percent,
        'stock': offer_stock
    }
    
    item['stock'] -= offer_stock
    
    print(f"✅ {offer_stock} x {actual_item} added to OfferZone!")
    print(f"💰 Original: ${original_price:.2f} → Now: ${discount_price:.2f}")
    print(f"🎯 Save: ${original_price - discount_price:.2f} each!")

def admin_remove_from_offerzone():
    """Admin: Remove item from OfferZone."""
    if not offerzone:
        print("\n❌ OfferZone is already empty!")
        return
    
    print("\n=== ADMIN: Remove from OfferZone ===")
    display_offerzone()
    
    item_input = input("Enter offer item name: ").strip()
    
    offer_info = find_offer_item_insensitive(item_input)
    if not offer_info:
        print("❌ Invalid offer item!")
        return
    
    actual_item = offer_info['item_name']
    offer_details = offer_info['details']
    
    original_item_name = actual_item.replace(" (Offer)", "")
    original_item = stationery_catalog[original_item_name]
    original_item['stock'] += offer_details['stock']
    
    del offerzone[actual_item]
    
    print(f"✅ {actual_item} removed from OfferZone!")
    print(f"📦 Stock returned to original: +{offer_details['stock']}")

def user_buy_offer_item():
    """User: Buy item from OfferZone."""
    if not offerzone:
        print("\n❌ No offers available in OfferZone!")
        return
    
    print("\n🛒 === Buy from OfferZone ===")
    display_offerzone()
    
    item_input = input("Enter offer item name: ").strip()
    
    offer_info = find_offer_item_insensitive(item_input)
    if not offer_info:
        print("❌ Invalid offer item!")
        return
    
    item = offer_info['details']
    actual_item = offer_info['item_name']
    
    try:
        quantity = int(input(f"Enter quantity (Available: {item['stock']}): "))
        if quantity <= 0 or quantity > item['stock']:
            print("❌ Invalid quantity or insufficient stock!")
            return
    except ValueError:
        print("❌ Please enter a valid number!")
        return
    
    cart.append({
        "item": actual_item, 
        "quantity": quantity, 
        "price": item['discount_price']
    })
    
    item['stock'] -= quantity
    
    if item['stock'] == 0:
        del offerzone[actual_item]
    
    print(f"✅ Added {quantity} x {actual_item} to cart at ${item['discount_price']:.2f} each!")
    print(f"💰 You save ${(item['original_price'] - item['discount_price']):.2f} per item!")

cart = []

def display_catalog():
    print("\n=== Stationery Shop Catalog ===")
    query_all_items()

def add_to_cart():
    print("\n=== Add Items to Cart ===")
    print("Available Items:", ", ".join(list(stationery_catalog.keys())[:5]), "...(type to search)")
    item_input = input("Enter item name: ").strip()
    item_info = find_item_insensitive(item_input)
    if not item_info:
        print("❌ Invalid item name!")
        return
    item = item_info['details']
    actual_item = item_info['item_name']
    try:
        quantity = int(input(f"Enter quantity (Available: {item['stock']}): "))
        if quantity <= 0 or quantity > item['stock']:
            print("❌ Invalid quantity or insufficient stock!")
            return
    except ValueError:
        print("❌ Please enter a valid number!")
        return
    cart.append({
        "item": actual_item, 
        "quantity": quantity, 
        "price": item['price']
    })
    print(f"✅ Added {quantity} x {actual_item} to cart.")

def view_cart():
    if not cart:
        print("\n🛒 Cart is empty!")
        return
    print("\n=== Your Cart ===")
    total = 0
    for item in cart:
        item_total = item['quantity'] * item['price']
        total += item_total
        print(f"{item['item']} ({item['quantity']} x ${item['price']:.2f}) = ${item_total:.2f}")
    print(f"💰 Total: ${total:.2f}")

def checkout():
    if not cart:
        print("\n🛒 Cart is empty! Nothing to checkout.")
        return
    print("\n=== Checkout ===")
    view_cart()
    confirm = input("Confirm purchase? (yes/no): ").strip().lower()
    if confirm == 'yes':
        for item in cart:
            if "(Offer)" in item['item']:
                offer_info = find_offer_item_insensitive(item['item'])
                if offer_info:
                    offer_details = offer_info['details']
                    offer_details['stock'] -= item['quantity']
            else:
                reg_info = find_item_insensitive(item['item'])
                if reg_info:
                    reg_details = reg_info['details']
                    reg_details['stock'] -= item['quantity']
        print("✅ Purchase successful! Stock updated.")
        cart.clear()
    else:
        print("❌ Purchase cancelled.")

def rate_item():
    print("\n⭐ === Rate an Item ===")
    print("Available Items:", ", ".join(list(stationery_catalog.keys())[:5]), "...(type to search)")
    item_input = input("Enter item name: ").strip()
    item_info = find_item_insensitive(item_input)
    if not item_info:
        print("❌ Invalid item name!")
        return
    actual_item = item_info['item_name']
    try:
        rating = float(input("Enter rating (0-5): "))
        if 0 <= rating <= 5:
            stationery_catalog[actual_item]['ratings'].append(rating)
            print(f"⭐ Rating {rating} added for {actual_item}.")
        else:
            print("❌ Rating must be between 0 and 5!")
    except ValueError:
        print("❌ Please enter a valid number!")

def resell_item():
    print("\n🔄 === Resell an Item ===")
    print("Available Items:", ", ".join(list(stationery_catalog.keys())[:5]), "...(type to search)")
    item_input = input("Enter item name: ").strip()
    item_info = find_item_insensitive(item_input)
    if not item_info:
        print("❌ Invalid item name!")
        return
    item = item_info['details']
    actual_item = item_info['item_name']
    try:
        quantity = int(input(f"Enter quantity to resell (Available: {item['stock']}): "))
        if quantity <= 0 or quantity > item['stock']:
            print("❌ Invalid quantity or insufficient stock!")
            return
        discount = float(input("Enter discount percentage (0-100): "))
        if not 0 <= discount <= 100:
            print("❌ Discount must be between 0 and 100!")
            return
    except ValueError:
        print("❌ Please enter valid numbers!")
        return
    stationery_catalog[actual_item]['stock'] += quantity
    for cart_item in cart[:]:
        if cart_item['item'].lower() == actual_item.lower():
            if cart_item['quantity'] <= quantity:
                quantity -= cart_item['quantity']
                cart.remove(cart_item)
            else:
                cart_item['quantity'] -= quantity
                quantity = 0
            if quantity == 0:
                break
    original_price = item['price']
    resell_price = original_price * (1 - discount / 100)
    resold_item_name = f"{actual_item} (Resold)"
    if resold_item_name not in stationery_catalog:
        stationery_catalog[resold_item_name] = {
            "price": resell_price,
            "stock": quantity,
            "ratings": []
        }
    else:
        stationery_catalog[resold_item_name]['stock'] += quantity
    print(f"✅ Resold {quantity} x {actual_item} at ${resell_price:.2f} each.")

def admin_menu():
    """Admin menu for managing OfferZone."""
    while True:
        print("\n🔐 === ADMIN PANEL - OFFER ZONE ===")
        print("1. View OfferZone")
        print("2. Add Item to OfferZone")
        print("3. Remove Item from OfferZone")
        print("4. Back to Main Menu")
        choice = input("Enter choice (1-4): ").strip()
        if choice == '1':
            display_offerzone()
        elif choice == '2':
            admin_add_to_offerzone()
        elif choice == '3':
            admin_remove_from_offerzone()
        elif choice == '4':
            break
        else:
            print("❌ Invalid choice!")

def user_offerzone_menu():
    """User menu for buying from OfferZone."""
    while True:
        print("\n=== USER OFFER ZONE ===")
        print("1. View Hot Deals")
        print("2. Buy from OfferZone")
        print("3. Back to Main Menu")
        choice = input("Enter choice (1-3): ").strip()
        if choice == '1':
            display_offerzone()
        elif choice == '2':
            user_buy_offer_item()
        elif choice == '3':
            break
        else:
            print("❌ Invalid choice!")

def main():
    while True:
        print("\n🏪 === Stationery Shop - 32 ITEMS! ===")
        print("🔐 ADMIN | 🛒 USER")
        print("1.  User Menu")
        print("2.  Admin Menu (OfferZone)")
        print("3.  Exit")
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            while True:
                print("\n🛒 === USER MENU ===")
                print("1.  View Catalog (32 Items)")
                print("2.  Add to Cart")
                print("3.  OfferZone (5 HOT DEALS!)")
                print("4.  View Cart")
                print("5.  Checkout")
                print("6.  Rate Item")
                print("7.  Back to Main")
                user_choice = input("Enter choice (1-7): ").strip()
                
                if user_choice == '1':
                    display_catalog()
                elif user_choice == '2':
                    add_to_cart()
                elif user_choice == '3':
                    user_offerzone_menu()
                elif user_choice == '4':
                    view_cart()
                elif user_choice == '5':
                    checkout()
                elif user_choice == '6':
                    rate_item()
                elif user_choice == '7':
                    break
                else:
                    print("❌ Invalid choice!")
                    
        elif choice == '2':
            admin_menu()
            
        elif choice == '3':
            print("👋 Thank you for shopping!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()