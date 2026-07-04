from predictor import predict_game
import streamlit as st
st.set_page_config(
    page_title="Colby's MLB AI",
    page_icon="⚾",
    layout="centered"
)

st.title("⚾ Colby's MLB AI")
st.subheader("Sportsbook Style Predictor")

home_team = st.selectbox(
    "Home Team",
    [
        "Arizona Diamondbacks",
        "Atlanta Braves",
        "Baltimore Orioles",
        "Boston Red Sox",
        "Chicago Cubs",
        "Chicago White Sox",
        "Cincinnati Reds",
        "Cleveland Guardians",
        "Colorado Rockies",
        "Detroit Tigers",
        "Houston Astros",
        "Kansas City Royals",
        "Los Angeles Angels",
        "Los Angeles Dodgers",
        "Miami Marlins",
        "Milwaukee Brewers",
        "Minnesota Twins",
        "New York Mets",
        "New York Yankees",
        "Athletics",
        "Philadelphia Phillies",
        "Pittsburgh Pirates",
        "San Diego Padres",
        "San Francisco Giants",
        "Seattle Mariners",
        "St. Louis Cardinals",
        "Tampa Bay Rays",
        "Texas Rangers",
        "Toronto Blue Jays",
        "Washington Nationals"
    ]
)

away_team = st.selectbox(
    "Away Team",
    [
        "Arizona Diamondbacks",
        "Atlanta Braves",
        "Baltimore Orioles",
        "Boston Red Sox",
        "Chicago Cubs",
        "Chicago White Sox",
        "Cincinnati Reds",
        "Cleveland Guardians",
        "Colorado Rockies",
        "Detroit Tigers",
        "Houston Astros",
        "Kansas City Royals",
        "Los Angeles Angels",
        "Los Angeles Dodgers",
        "Miami Marlins",
        "Milwaukee Brewers",
        "Minnesota Twins",
        "New York Mets",
        "New York Yankees",
        "Athletics",
        "Philadelphia Phillies",
        "Pittsburgh Pirates",
        "San Diego Padres",
        "San Francisco Giants",
        "Seattle Mariners",
        "St. Louis Cardinals",
        "Tampa Bay Rays",
        "Texas Rangers",
        "Toronto Blue Jays",
        "Washington Nationals"
    ]
)

if st.button("Predict Game"):

    if home_team == away_team:
        st.error("Please select two different teams.")
    else:
        result = predict_game(home_team, away_team)

st.success("Prediction Complete!")

st.markdown("## 🏆 Winner")
st.write(result["winner"])

st.markdown("## 📊 Win Probability")
st.progress(int(result["home_pct"]))
st.write(f"**{home_team}: {result['home_pct']}%**")
st.write(f"**{away_team}: {result['away_pct']}%**")

st.markdown("## ⭐ Confidence")
st.write(f"{result['confidence']} / 10")

st.markdown("## 📈 Why")

for reason in result["reasons"]:
    st.write(f"• {reason}")
