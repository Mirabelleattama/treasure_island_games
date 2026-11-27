
import streamlit as st

# Page settings
st.set_page_config(
    page_title="Treasure Island Adventure",
    page_icon="🏝️",
    layout="centered"
)

# Your original Treasure Island illustration
treasure_map = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
*******************************************************************************
'''

# Store the player's progress
if "stage" not in st.session_state:
    st.session_state.stage = "start"

# Website heading
st.title("🏝️ TREASURE ISLAND")
st.caption("An interactive adventure")

st.code(treasure_map, language=None)

# Starting point
if st.session_state.stage == "start":

    st.write("Welcome to Mirabelle's Treasure Island.")
    st.write("Your mission is to find the treasure.")

    st.subheader("You are on your way to the village.")
    st.write("There are two roads. Which road will you choose?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅️ LEFT", use_container_width=True):
            st.session_state.stage = "lake"
            st.rerun()

    with col2:
        if st.button("RIGHT ➡️", use_container_width=True):
            st.session_state.stage = "lose"
            st.rerun()

# Lake stage
elif st.session_state.stage == "lake":

    st.subheader("🌊 The Lake")
    st.write(
        "You have come to a lake and there is an island "
        "in the middle of the lake."
    )
    st.write("Will you wait for the boat or swim across?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⛵ WAIT", use_container_width=True):
            st.session_state.stage = "doors"
            st.rerun()

    with col2:
        if st.button("🏊 SWIM", use_container_width=True):
            st.session_state.stage = "crocodile"
            st.rerun()

# Three doors stage
elif st.session_state.stage == "doors":

    st.subheader("🚪 The Village House")
    st.write("You arrive at the village unharmed.")
    st.write("There is a house with three doors.")
    st.write("One red, one yellow and one blue.")
    st.write("Which colour do you choose?")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🔴 RED", use_container_width=True):
            st.session_state.stage = "fire"
            st.rerun()

    with col2:
        if st.button("🟡 YELLOW", use_container_width=True):
            st.session_state.stage = "win"
            st.rerun()

    with col3:
        if st.button("🔵 BLUE", use_container_width=True):
            st.session_state.stage = "monsters"
            st.rerun()

# Game outcomes
elif st.session_state.stage == "fire":

    st.error("🔥 It is a room full of fire. Game over!")

elif st.session_state.stage == "monsters":

    st.error("👹 You entered a room full of monsters. Game over!")

elif st.session_state.stage == "crocodile":

    st.error("🐊 You got attacked by a crocodile. Game over!")

elif st.session_state.stage == "lose":

    st.error("You lose!")

elif st.session_state.stage == "win":

    st.success("🏆 You found the treasure. You Win!")

    st.balloons()

# Play again button
if st.session_state.stage != "start":

    st.divider()

    if st.button("🔄 PLAY AGAIN", use_container_width=True):
        st.session_state.stage = "start"
        st.rerun()
