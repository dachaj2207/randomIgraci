import streamlit as st
import random
import pickle
def load_players():
    try:
        with open("players.pkl", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

# Function to save the list of players to a file
def save_players(players):
    with open("players.pkl", "wb") as f:
        pickle.dump(players, f)

# Load the list of players at the beginning
igraci = load_players()


st.title("Izbor dve lose ekipe")


dodavanjeIgraca = st.text_input("Dodaj novog igraca")
noviigrac = st.button("Dodaj")
if noviigrac and dodavanjeIgraca.strip()!="":
    igraci.append(dodavanjeIgraca.strip())
    save_players(igraci)


selected_players_placeholder = st.empty()
selected_players = st.multiselect("Izaberi 12 igraca",igraci,max_selections=12)

selected_players_placeholder.write(f"Broj izabranih igraca: {len(selected_players)}")




izaberiDugme =st.button("Izaberi")

if izaberiDugme:
    izabranaLista = [player for player in selected_players]
    randomLista =random.shuffle(izabranaLista)

    tim1 = izabranaLista[:6]
    tim2 = izabranaLista[6:]

    st.write("Tim1:")
    for i, player in enumerate(tim1, start=1):
        st.write(f"{i}. {player}")

    st.write("Tim2:")
    for i, player in enumerate(tim2, start=1):
        st.write(f"{i}. {player}")

