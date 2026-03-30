# Monte Carlo European Call Option Pricing

This project implements a Monte Carlo simulation to estimate the price of a European call option.

## Description

The stock price is simulated using a stochastic process (Geometric Brownian Motion). The option payoff is computed and discounted to obtain the present value.

## Usage

Run the program via:

python my_project S0 K T r sigma n_sim

Example:

python my_project 100 110 1 0.05 0.2 10000

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

## Notes

The accuracy improves with larger simulation size (n_sim).