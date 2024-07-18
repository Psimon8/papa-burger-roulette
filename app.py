import streamlit as st
import random

# Définir le menu
burger_names = [
    "Le mathis", "Le romeo", "Le louis", "L' oriental", "Le hugo", "Le bollywood", "Le robin",
    "Le savoyard", "Le corentin", "Le classic", "Le big papa", "Le végétarien", "Le nicolas",
    "Le crétois", "Le milano", "L’italien", "Le Bacon", "Le Poivrier", "Le Printannier (poisson)",
    "L’océan (poisson)"
]
sizes = ["Simple"] * 30 + ["Double"] * 10 + ["Triple"]
doneness_levels = ["Bleue", "Saignante", "A point", "Bien Cuit", "Semelle", "Crue"]
drinks = [
    "Coca cola", "Fanta orange", "Fanta citron", "7Up", "Lipton ice tea",
    "Cristalline gazeuse", "Coca zero", "Eau plate Acquarelle", "Schweppes agrumes", "Oasis tropical"
]

if st.button('Go Big or Go Miam !'):
    selected_burger = random.choice(burger_names)
    selected_size = random.choice(sizes)
    selected_doneness = random.choice(doneness_levels)
    selected_drink = random.choice(drinks)

    st.subheader("Votre Commande de Burger Aléatoire")
    st.write(f"**Burger:** {selected_burger} - {selected_size}")
    st.write(f"**Cuisson:** {selected_doneness}")
    st.write(f"**Boisson:** {selected_drink}")

