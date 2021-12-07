
def lbtt(Value):
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
    
    
    if Value < 0:
        raise ValueError(
            "Property Value cannot be negative!"
        )
    
    # Tax rate is 0% up to £145,000
    if Value <= 145000:
        return 0

    # 2% from £145,001 to £250,000
    if Value <= 250000:
        return int(0.02 * (Value - 145000))

    # 5% from £250,001 to £325,000
    if Value <= 325000:
        return int(2100 + 0.05 * (Value - 250000))

    # 10% from £325,001 to £750,000
    if Value <= 750000:
        return int(2100 + 3750 + 0.10 * (Value - 325000))

    # 12% for > £750,000
    if Value > 750000:
        return int(2100 + 3750 + 42500 + 0.12 * (Value - 750000))