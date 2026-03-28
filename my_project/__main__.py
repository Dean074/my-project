import sys
import math
import random


def monte_carlo_call_price(s0: float, k: float, t: float, r: float, sigma: float, n_sim: int) -> float:
    payoff_sum = 0.0

    for _ in range(n_sim):
        z = random.gauss(0, 1)
        s_t = s0 * math.exp((r - 0.5 * sigma ** 2) * t + sigma * math.sqrt(t) * z)
        payoff = max(s_t - k, 0.0)
        payoff_sum += payoff

    average_payoff = payoff_sum / n_sim
    price = math.exp(-r * t) * average_payoff
    return price


def main() -> None:
    if len(sys.argv) != 7:
        print("Usage: python -m my_project S0 K T r sigma n_sim")
        print("Example: python -m my_project 100 110 1 0.05 0.2 10000")
        return

    s0 = float(sys.argv[1])
    k = float(sys.argv[2])
    t = float(sys.argv[3])
    r = float(sys.argv[4])
    sigma = float(sys.argv[5])
    n_sim = int(sys.argv[6])

    price = monte_carlo_call_price(s0, k, t, r, sigma, n_sim)

    print("=== Monte Carlo European Call Option Pricing ===")
    print(f"S0     = {s0}")
    print(f"K      = {k}")
    print(f"T      = {t}")
    print(f"r      = {r}")
    print(f"sigma  = {sigma}")
    print(f"n_sim  = {n_sim}")
    print(f"Estimated call price = {price:.6f}")


if __name__ == "__main__":
    main()