import streamlit as st

def calculate_expectancy(win_probability, win_reward):
    return round(win_probability / 100 * win_reward - (1-win_probability/100), 2)

# Page headers
st.set_page_config(page_title="Expectancy Calculator", layout="wide", page_icon="📈")
st.title("ClockTrades expectancy calculator")
st.markdown("""
**Calculate your trading strategy's expected performance**  
*Expectancy measures the average amount you can expect to win (or lose) per dollar risked*
""")

# Sidebar with information
with st.sidebar:
    st.header("About Expectancy")
    st.markdown("""
    **Expectancy Formula:**
    ```
    (Win% × Avg Win) - (Loss% × Avg Loss)
    ```
    Where:
    - **Win%** = Probability of winning trades
    - **Avg Win** = Profit in multiples of risk (R)
    - **Loss%** = 1 - Win%
    - **Avg Loss** = 1R (by definition)
    """)
    st.markdown("---")
    st.markdown("Made by [ClockTrades](https://clocktrades.com)")
    st.markdown("*For educational purposes only*")


col1, col2 = st.columns(2)
with col1:
    st.header("🧮 Strategy Parameters")
    win_probability_pct = st.slider(
        "**Win Probability (%)**",
        min_value=1,
        max_value=100,
        value=40,
        help="Percentage of trades that are winners"
    )

    win_reward_R = st.slider(
        "**Reward to Risk Ratio**",
        min_value=0.1,
        max_value=20.0,
        value=2.0,
        step=0.1,
        help="Profit potential relative to your risk (e.g., 2.0 = 2:1 ratio)"
    )

    expectancy = calculate_expectancy(win_probability_pct, win_reward_R)

    # Color-coded expectancy display
    if expectancy >= 0:
        exp_color = "green"
        exp_icon = "✅"
    else:
        exp_color = "red"
        exp_icon = "⚠️"

    st.markdown(f"<h3 style='text-align: center; color: {exp_color};'>"
                f"{exp_icon} Expectancy: <b>{expectancy}R</b> per trade </h3>",
                unsafe_allow_html=True)

with col2:
    st.header("📊 Projected Returns")

    no_of_opportunities_per_period = st.slider(
        "**Opportunities per Period**",
        min_value=1,
        max_value=100,
        value=10,
        help="Number of trading opportunities in a given time period"
    )

    no_of_periods = st.slider(
        "**Number of Periods**",
        min_value=1,
        max_value=100,
        value=12,
        help="Number of periods to project forward"
    )

    total_return = round(expectancy * no_of_opportunities_per_period * no_of_periods, 1)

    # Color-coded total return display
    return_color = "green" if total_return >= 0 else "red"
    st.markdown(f"<h3 style='text-align: center; color: {return_color};'>"
                f"Total Return: <b>{total_return}R</b></h3>",
                unsafe_allow_html=True)

# Explanation section
with st.expander("💡 How to interpret these results"):
    st.markdown(f"""
    With a **{win_probability_pct}% win rate** and **{win_reward_R} : 1 reward-to-risk ratio**:

    - Your expectancy is **{expectancy}R** per trade
    - This means you'll average **\${expectancy} per \$1 risked** over many trades
    - With **{no_of_opportunities_per_period} trades per period** over **{no_of_periods} periods**:
        - Total projected return = **{total_return}R**
        - This equals **\${total_return} per \$1 risked** overall
    """)

    st.markdown("""
    **Key Insights:**
    - Positive expectancy (>0) indicates a profitable strategy
    - Expectancy > 0.2 is generally considered good
    - Expectancy > 0.5 is considered excellent
    - Negative expectancy means the strategy loses money over time
    """)

# Footer
st.markdown("---")
st.caption("© 2025 ClockTrades.com • All calculations are theoretical and don't guarantee future results • "
           "Risk management is essential in trading")