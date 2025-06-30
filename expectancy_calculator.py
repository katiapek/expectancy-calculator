import streamlit as st

st.title("Expectancy Calculator")
import streamlit as st

def calculate_expectancy(win_probability, win_reward):
    return round(win_probability / 100 * win_reward - (1-win_probability/100), 2)

st.title("ClockTrades expectancy calculator")
st.header("Expectancy")
win_probability_pct = st.slider("Select a probability of win (expected win-rate)", min_value=1, max_value=100, value=40)
win_reward_R = st.slider("Select a reward in R", min_value=0.1, max_value=20.0, value=2.0, step=0.1)

expectancy = calculate_expectancy(win_probability_pct, win_reward_R)

st.write("Expectancy is", expectancy, "\$ return on each 1\$ risked")

st.header("Expected Total Return")
no_of_opportunities_per_period = st.slider("How many opportunities there is in a period?", min_value=1, max_value=100, value=10)
no_of_periods = st.slider("How many period would you like to calculate?", min_value=1, max_value=100, value=12)

total_return = round(expectancy * no_of_opportunities_per_period * no_of_periods, 1)
st.write("Total return is", total_return, "R")