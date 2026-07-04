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
        st.success("Prediction engine coming next!")

        st.markdown("## 🏆 Winner")
        st.write(home_team)

        st.markdown("## 📊 Win Probability")
        st.progress(60)
        st.write(f"**{home_team}: 60%**")
        st.write(f"**{away_team}: 40%**")

        st.markdown("## ⭐ Confidence")
        st.write("7.5 / 10")

        st.markdown("## 📈 Why")
        st.write("• Better overall team rating")
        st.write("• Home-field advantage")
        st.write("• Better recent performance")
