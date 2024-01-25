import math

def black_scholes_call(S, X, T, r, sigma):
    d1 = (math.log(S / X) + (r + (sigma ** 2) / 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)
    N_d1 = norm_cdf(d1)
    N_d2 = norm_cdf(d2)
    call_value = S * N_d1 - X * math.exp(-r * T) * N_d2
    return call_value

def norm_cdf(x):
    """Cumulative distribution function for the standard normal distribution."""
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0