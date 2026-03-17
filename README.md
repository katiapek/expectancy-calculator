# Expectancy & Kelly Criterion Calculator

An interactive trading calculator that computes strategy expectancy, Kelly Criterion position sizing, and projected returns. Built with Streamlit and Plotly.

**[Live Demo](https://expectancy-calculator.marketsmanners.com/)**

## Features

- **Expectancy calculation** — computes expected return per dollar risked based on win probability and reward-to-risk ratio
- **Kelly Criterion** — optimal and Half-Kelly position sizing with risk level classification
- **Projected returns** — forward projection across configurable trading opportunities and time periods
- **Interactive analysis chart** — dual-axis visualization showing alternative parameter combinations that produce the same expectancy (Plotly)
- **Educational sidebar** — formula breakdowns for Expectancy and Kelly Criterion

## How It Works

```
Expectancy = (Win% × R) - (1 - Win%) × 1
Kelly %    = Win% - [(1 - Win%) / R]
```

Where **R** is the Reward-to-Risk ratio and **Win%** is expressed as a decimal.

## Tech Stack

- **Streamlit** — interactive web UI with sliders and metrics
- **Plotly** — dual-axis scatter charts with hover tooltips
- **Docker** — containerized deployment

## Run Locally

```bash
git clone https://github.com/katiapek/expectancy-calculator.git
cd expectancy-calculator
pip install streamlit plotly
streamlit run expectancy_calculator.py
```

## Related Projects

| Project | Description |
|---------|-------------|
| [Compounding Simulator](https://github.com/katiapek/compounding-simulator) | Long-term growth simulation with compounding and risk management |
| [Performance Visualizer](https://github.com/katiapek/performance-visualizer) | Monte Carlo simulation of 100 possible strategy futures |
| [Financial Analysis Terminal](https://github.com/katiapek/financial-analysis-terminal) | Quantitative analytics pipeline for futures markets |

## License

MIT
