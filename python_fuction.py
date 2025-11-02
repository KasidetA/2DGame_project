def calculate_weight_ratio(mp, rp):
    me = 5.97e24
    re = 6371
    massRatio = mp / me
    radiusRatio = re / rp
    return massRatio * radiusRatio * radiusRatio
