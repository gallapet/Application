import sys

def lbtt2(Value):
    """Calculate the Land and Buildings Transaction Tax (LBTT) due for a property being bought

    Assuming:
    - The buyer does not own any other property
    - The buyer already owns a property (i.e. not a first time buyer)
    - The buyer will sell their current property on the same date as buying the new property
    - The property will only be used for personal use

    Args:
        Value: The value of the property being bought 

    Returns:
        The amount of tax due for a given property value

    Raises:
        ValueError: If Value is negative
    """

    tax_bands = [0.00, 145000.00, 250000.00, 325000.00, 750000.00, sys.float_info.max]
    tax_rates = [0.00, 0.02, 0.05, 0.10, 0.12, 1]
    
    
    if Value < 0:
        raise ValueError(
            "Property Value cannot be negative!"
        )
 
    tax = 0

    for idx in range(0, len(tax_bands) - 1):
        if Value <= tax_bands[idx]:
             tax += 0
        elif Value > tax_bands[idx + 1]:
            tax += tax_rates[idx] * (tax_bands[idx + 1] - tax_bands[idx])
        else:
            tax += tax_rates[idx] * (Value - tax_bands[idx])
        
    return int(tax)
        

"""
    # Tax rate is 0% up to £145,000
    if Value <= tax_bands[1]:
        return 0

    # 2% from £145,001 to £250,000
    if Value <= tax_bands[2]:
        return int(tax_rates[1] * (Value - tax_bands[1]))

    # 5% from £250,001 to £325,000
    if Value <= tax_bands[3]:
        return int(tax_rates[1] * (tax_bands[2] - tax_bands[1]) + tax_rates[2] * (Value - tax_bands[2]))

    # 10% from £325,001 to £750,000
    if Value <= tax_bands[4]:
        return int(tax_rates[1] * (tax_bands[2] - tax_bands[1]) + tax_rates[2] * (tax_bands[3] - tax_bands[2]) + tax_rates[3] * (Value - tax_bands[3]))

    # 12% for > £750,000
    if Value > tax_bands[4]:
        return int(tax_rates[1] * (tax_bands[2] - tax_bands[1]) + tax_rates[2] * (tax_bands[3] - tax_bands[2]) + tax_rates[3] * (tax_bands[4] - tax_bands[3]) + tax_rates[4] * (Value - tax_bands[4]))"""