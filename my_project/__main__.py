import sys
import math
import random


def monte_carlo_call_price_stats(
    s0: float, k: float, t: float, r: float, sigma: float, n_sim: int
) -> tuple[float, float, float, float]:
    discounted_payoffs = []

    for _ in range(n_sim):
        z = random.gauss(0, 1)
        s_t = s0 * math.exp((r - 0.5 * sigma ** 2) * t + sigma * math.sqrt(t) * z)
        payoff = max(s_t - k, 0.0)
        discounted_payoff = math.exp(-r * t) * payoff
        discounted_payoffs.append(discounted_payoff)

    mc_price = sum(discounted_payoffs) / n_sim

    variance = sum((x - mc_price) ** 2 for x in discounted_payoffs) / (n_sim - 1)
    standard_error = math.sqrt(variance / n_sim)

    ci_lower = mc_price - 1.96 * standard_error
    ci_upper = mc_price + 1.96 * standard_error

    return mc_price, standard_error, ci_lower, ci_upper


def normal_cdf(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def black_scholes_call_price(s0: float, k: float, t: float, r: float, sigma: float) -> float:
    d1 = (math.log(s0 / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)

    price = s0 * normal_cdf(d1) - k * math.exp(-r * t) * normal_cdf(d2)
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

    mc_price, standard_error, ci_lower, ci_upper = monte_carlo_call_price_stats(
        s0, k, t, r, sigma, n_sim
    )
    bs_price = black_scholes_call_price(s0, k, t, r, sigma)
    abs_error = abs(mc_price - bs_price)

    print("=== European Call Option Pricing ===")
    print(f"S0     = {s0}")
    print(f"K      = {k}")
    print(f"T      = {t}")
    print(f"r      = {r}")
    print(f"sigma  = {sigma}")
    print(f"n_sim  = {n_sim}")

    print("\n--- Results ---")
    print(f"Monte Carlo Price = {mc_price:.6f}")
    print(f"Black-Scholes     = {bs_price:.6f}")
    print(f"Absolute Error    = {abs_error:.6f}")
    print(f"Standard Error    = {standard_error:.6f}")
    print(f"95% CI            = [{ci_lower:.6f}, {ci_upper:.6f}]")


if __name__ == "__main__":
    main()