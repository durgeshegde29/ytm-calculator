from scipy.optimize import root_scalar

def bond_price(cash_flows, times, ytm):
    return sum(cf / (1 + ytm) ** t for cf,t in zip(cash_flows, times))

def solve_ytm(cash_flows, times, price):
    if price <= 0:
        return "Error: Bond price must be greater than 0."

    def f(ytm):
        return bond_price(cash_flows, times, ytm) - price

    try:
        result = root_scalar(f, bracket=[0.0001, 10], method="bisect")
        return round(result.root * 100, 4) if result.converged else "Error: YTM calculation did not converge."
    except ValueError as e:
        return f"Error: {str(e)}"