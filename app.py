import streamlit as st
import sqlite3
import pandas as pd

# Database connection function
def get_db_connection():
    connection = sqlite3.connect('icecream.db')
    connection.row_factory = sqlite3.Row  # To access columns by name (dict-like)
    return connection

# Set the title of the Streamlit app
st.title('Ice Cream Parlor API')

# Home Page
st.header("Welcome to the Ice Cream Parlor API")

# Option for users to navigate through functionalities
option = st.sidebar.selectbox('Select an option:', [
    'Add a New Flavor',
    'View All Flavors',
    'Search for Flavors',
    'Add Ingredient',
    'View Ingredients',
    'Add Allergen',
    'View Allergen List',
    'Add Customer Suggestion',
    'View Customer Suggestions',
    'View Cart',
    'Add to Cart',
    'Seasonal Flavors'
])

# 1. Add a new flavor
if option == 'Add a New Flavor':
    st.subheader('Add a New Flavor')

    name = st.text_input('Flavor Name')
    is_seasonal = st.selectbox('Is this flavor seasonal?', ['Yes', 'No'])

    if st.button('Add Flavor'):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Flavors (name, is_seasonal) VALUES (?, ?)", (name, 1 if is_seasonal == 'Yes' else 0))
        connection.commit()
        connection.close()
        st.success(f'Flavor "{name}" added successfully!')

# 2. View All Flavors
elif option == 'View All Flavors':
    st.subheader('All Ice Cream Flavors')

    connection = get_db_connection()
    flavors = connection.execute("SELECT * FROM Flavors").fetchall()
    connection.close()

    df = pd.DataFrame(flavors)
    st.write(df)

# 3. Search for a Flavor
elif option == 'Search for Flavors':
    st.subheader('Search for a Flavor')

    query = st.text_input('Search by Flavor Name:')
    if query:
        connection = get_db_connection()
        flavors = connection.execute("SELECT * FROM Flavors WHERE name LIKE ?", ('%' + query + '%',)).fetchall()
        connection.close()

        if flavors:
            df = pd.DataFrame(flavors)
            st.write(df)
        else:
            st.warning('No flavors found.')

# 4. Add Ingredient
elif option == 'Add Ingredient':
    st.subheader('Add a New Ingredient')

    name = st.text_input('Ingredient Name')
    quantity = st.number_input('Quantity', min_value=0, step=1)

    if st.button('Add Ingredient'):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Ingredients (name, quantity) VALUES (?, ?)", (name, quantity))
        connection.commit()
        connection.close()
        st.success(f'Ingredient "{name}" added successfully!')

# 5. View Ingredients
elif option == 'View Ingredients':
    st.subheader('View All Ingredients')

    connection = get_db_connection()
    ingredients = connection.execute("SELECT * FROM Ingredients").fetchall()
    connection.close()

    df = pd.DataFrame(ingredients)
    st.write(df)

# 6. Add Allergen
elif option == 'Add Allergen':
    st.subheader('Add a New Allergen')

    allergen = st.text_input('Allergen Name')

    if st.button('Add Allergen'):
        connection = get_db_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO Allergens (name) VALUES (?)", (allergen,))
            connection.commit()
            st.success(f'Allergen "{allergen}" added successfully!')
        except sqlite3.IntegrityError:
            st.error('Allergen already exists.')
        finally:
            connection.close()

# 7. View Allergen List
elif option == 'View Allergen List':
    st.subheader('View All Allergens')

    connection = get_db_connection()
    allergens = connection.execute("SELECT * FROM Allergens").fetchall()
    connection.close()

    df = pd.DataFrame(allergens)
    st.write(df)

# 8. Add Customer Suggestion
elif option == 'Add Customer Suggestion':
    st.subheader('Submit Flavor Suggestion')

    suggestion = st.text_area('What flavor would you like to suggest?')

    if st.button('Submit Suggestion'):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO CustomerSuggestions (suggestion) VALUES (?)", (suggestion,))
        connection.commit()
        connection.close()
        st.success(f'Suggestion "{suggestion}" submitted successfully!')

# 9. View Customer Suggestions
elif option == 'View Customer Suggestions':
    st.subheader('Customer Flavor Suggestions')

    connection = get_db_connection()
    suggestions = connection.execute("SELECT * FROM CustomerSuggestions").fetchall()
    connection.close()

    df = pd.DataFrame(suggestions)
    st.write(df)

# 10. View Cart
elif option == 'View Cart':
    st.subheader('View Your Cart')

    connection = get_db_connection()
    cart_items = connection.execute('''
        SELECT Cart.id, Flavors.name AS flavor_name
        FROM Cart
        INNER JOIN Flavors ON Cart.flavor_id = Flavors.id
    ''').fetchall()
    connection.close()

    df = pd.DataFrame(cart_items)
    st.write(df)

# 11. Add to Cart
elif option == 'Add to Cart':
    st.subheader('Add a Flavor to Your Cart')

    flavor_id = st.number_input('Flavor ID', min_value=1, step=1)

    if st.button('Add to Cart'):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Cart (flavor_id) VALUES (?)", (flavor_id,))
        connection.commit()
        connection.close()
        st.success(f'Flavor with ID {flavor_id} added to the cart!')

# 12. Seasonal Flavors
elif option == 'Seasonal Flavors':
    st.subheader('Seasonal Ice Cream Flavors')

    connection = get_db_connection()
    seasonal_flavors = connection.execute("SELECT * FROM Flavors WHERE is_seasonal = 1").fetchall()
    connection.close()

    df = pd.DataFrame(seasonal_flavors)
    st.write(df)

# Run the app
if __name__ == "__main__":
    st.write("Streamlit app is running.")
