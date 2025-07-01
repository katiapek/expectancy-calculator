import streamlit as st

def calculate_expectancy(win_probability, win_reward):
    return round(win_probability / 100 * win_reward - (1-win_probability/100), 2)

st.set_page_config(page_title="Expectancy Calculator", layout="wide")
st.title("ClockTrades expectancy calculator")
st.info("Lorerm sinspudsdsadjpas sdapda")
col1, col2 = st.columns(2)
with col1:
    st.header("Expectancy")
    win_probability_pct = st.slider("Select a probability of win (expected win-rate)", min_value=1, max_value=100, value=40)
    win_reward_R = st.slider("Select a reward in R", min_value=0.1, max_value=20.0, value=2.0, step=0.1)

    expectancy = calculate_expectancy(win_probability_pct, win_reward_R)

    st.metric(label="Expectancy per trade", value=f"{expectancy}R")

with col2:
    st.header("Total Return")
    no_of_opportunities_per_period = st.slider("How many opportunities there is in a period?", min_value=1, max_value=100, value=10)
    no_of_periods = st.slider("How many period would you like to calculate?", min_value=1, max_value=100, value=12)

    total_return = round(expectancy * no_of_opportunities_per_period * no_of_periods, 1)
    st.metric(label="Total return", value=f"{total_return}R")

st.markdown(f"With a probability of **{win_probability_pct}%** of winning a multiple of **{win_reward_R}** "
                f"times the risk taken, the expectancy of return is **{expectancy} of R** per trade."
                f"It means that with the **{no_of_opportunities_per_period} opportunities** in a given period, "
                f"the Total R Return **in {no_of_periods}** periods is **{total_return}** ")

st.markdown("For more Tools visit [ClockTrades.com](https://clocktrades.com)")