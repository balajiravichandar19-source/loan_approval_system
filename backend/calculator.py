def calculate_emi(loan_amount, loan_term, annual_rate=10):
    r = annual_rate / 1200
    emi = (loan_amount * r) / (1 - (1 + r) ** -loan_term)
    return round(emi, 2)
