import streamlit as st
import random

# Définir le menu
burger_names = [
    "Classic Burger", "Cheese Burger", "Bacon Burger", "Vegan Burger",
    "Chicken Burger", "Fish Burger", "Spicy Burger", "BBQ Burger"
]
sizes = ["Simple", "Double", "Triple"]
doneness_levels = ["Rare", "Medium Rare", "Medium", "Medium Well", "Well Done"]
drinks = [
    "Coca Cola", "Pepsi", "Sprite", "Fanta", "Water", 
    "Orange Juice", "Apple Juice", "Lemonade"
]

st.title("Sélecteur de Commande de Burger Aléatoire")

if st.button('Générer une Commande Aléatoire'):
    selected_burger = random.choice(burger_names)
    selected_size = random.choice(sizes)
    selected_doneness = random.choice(doneness_levels)
    selected_drink = random.choice(drinks)

    st.subheader("Votre Commande de Burger Aléatoire")
    st.write(f"**Burger:** {selected_burger} - {selected_size}")
    st.write(f"**Cuisson:** {selected_doneness}")
    st.write(f"**Boisson:** {selected_drink}")

# Instructions
st.write("""
### Instructions :
- Cliquez sur le bouton 'Générer une Commande Aléatoire' pour obtenir une commande de burger aléatoire.
- L'application sélectionnera aléatoirement un nom de burger, une taille, une cuisson et une boisson pour vous.
""")
