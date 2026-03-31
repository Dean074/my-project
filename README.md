# Monte Carlo European Call Option Pricing

This project implements a Monte Carlo simulation to estimate the price of a European call option.

## Description

The stock price is simulated using a stochastic process (Geometric Brownian Motion). The option payoff is computed and discounted to obtain the present value.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Dean074/my-project.git
cd my-project
pip install -e .
```

## Usage

Run the program via:

```bash
python -m my_project S0 K T r sigma n_sim
```

Example:

```bash
python -m my_project 100 110 1 0.05 0.2 10000
```

## Parameters

- S0: initial stock price
- K: strike price
- T: time to maturity
- r: risk-free interest rate
- sigma: volatility
- n_sim: number of simulations

## Output

The program prints the estimated option price.

## Validation

The Monte Carlo price is compared with the Black-Scholes analytical solution.

The program outputs:
- Monte Carlo estimated price
- Black-Scholes price
- Absolute error between both methods
- Standard error of the Monte Carlo estimator
- 95% confidence interval

## Convergence Analysis

The convergence plot demonstrates that the Monte Carlo estimate approaches the analytical Black-Scholes price as the number of simulations increases.

The confidence interval narrows as the number of simulations grows, indicating reduced estimation uncertainty.

## Example Output

Monte Carlo Price: 5.9368  
Black-Scholes Price: 6.0401  
Absolute Error: 0.1033  
Standard Error: 0.1157  
95% CI: [5.7101, 6.1636]

## Project Structure

my_project/
├── my_project/
│   ├── __init__.py
│   ├── __main__.py
├── pyproject.toml
├── README.md
├── example_usage.ipynb

## Requirements

- Python 3.11
- matplotlib
- numpy

## Notes

The accuracy improves with larger simulation size (n_sim).