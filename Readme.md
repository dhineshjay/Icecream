Ice Cream Parlor API (Streamlit Version)
Overview
This is a Streamlit-based web app for managing ice cream flavors, ingredients, allergens, customer suggestions, and cart items. The app uses SQLite for data storage and provides an interactive UI for performing CRUD operations.

Features
Add, view, and search ice cream flavors (including seasonal options)
Manage ingredients inventory
Add and view allergens
Submit and view customer suggestions
Add and view items in the cart
Interactive interface with Streamlit

Setup Instructions
1. Install Dependencies
Ensure you have Python 3.8+ installed. Then install the required packages:

pip install -r requirements.txt

2. Initialize the Database
Run the init_db.py script to create the SQLite database (icecream.db) and its tables:
python init_db.py

3. Run the Application
Start the Streamlit app:

streamlit run app.py
How to Use
Open the app in your browser (it will launch automatically) at http://localhost:8501.
Use the Sidebar to navigate between features:
Add a New Flavor: Enter flavor details.
View All Flavors: View stored flavors.
Search for Flavors: Search flavors by name.
Manage Ingredients: Add and view ingredients.
Manage Allergens: Add and view allergens.
Customer Suggestions: Submit and view flavor suggestions.
Cart Management: Add and view items in the cart.
File Structure
bash
Copy code
Icecream/
│
├── app.py             
├── init_db.py          
├── requirements.txt    
├── icecream.db         

Troubleshooting
App doesn't run: Ensure all dependencies are installed via requirements.txt.
Database errors: Re-run init_db.py to reset the database.
Port issues: If 8501 is occupied, Streamlit will suggest an alternative port.
