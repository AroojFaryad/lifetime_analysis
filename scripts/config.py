"""
Configuration settings for EB Lifetime Analysis.

Threshold Methodology:
----------------------
threshold = threshold_factor × quiet_sun_mean_intensity

Default: 1.5 × QS_mean (events must be 50% brighter than quiet sun)
"""

class Config:
    # Dataset paths
    DATASET_PATHS = [
        'data/20140614/sources_S2P0T10.5d3t5.npy',
        # ... other paths
    ]
    
    # Threshold parameters
    THRESHOLD_FACTORS = [1.5] * len(DATASET_PATHS)  # 1.5 × QS_mean
    QS_MEANS = [152.28, 108.35, 150.84, 148.91, 111.70, 168.10, 179.41, 172.28]
    
    # Explanation of threshold values:
    # threshold = THRESHOLD_FACTORS[i] × QS_MEANS[i]
    # Example: For dataset 0: threshold = 1.5 × 152.28 = 228.42
