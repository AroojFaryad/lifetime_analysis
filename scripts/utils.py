def calculate_thresholds():
    """
    Calculate intensity thresholds for each dataset.
    
    Returns:
        thresholds (list): Calculated thresholds for each dataset
    """
    thresholds = []
    for thresh_factor, qs_mean in zip(Config.THRESHOLD_FACTORS, Config.QS_MEANS):
        threshold = thresh_factor * qs_mean
        thresholds.append(threshold)
        print(f"Threshold: {thresh_factor} × {qs_mean} = {threshold:.2f}")
    
    return thresholds
