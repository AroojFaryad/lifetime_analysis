#  Threshold

## Intensity Thresholding for EB Detection

### Overview
This document explains the intensity thresholding method used to distinguish real Ellerman Bombs (EBs) from background noise and filler events.

## Threshold Calculation

The detection threshold is calculated as:

```python
threshold = threshold_factor × quiet_sun_mean_intensity
```

### Formula
```
Threshold = k × I_QS
```

Where:
- `k` = Threshold factor (default: 1.5)
- `I_QS` = Mean quiet sun intensity for the dataset

## Example Calculation

For dataset `20140614`:
- Quiet sun mean intensity: 152.28
- Threshold factor: 1.5

```python
threshold = 1.5 × 152.28 = 228.42
```

## Application Criteria

An EB event is considered valid if:

```python
if np.any(eb_peak_intensity > threshold):
    # Valid EB detection
else:
    # Rejected as noise/filler
```

##  Default Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| `threshold_factor` | 1.5 | 50% above quiet sun level |
| `quiet_sun_mean` | Dataset-specific | Calculated from QS regions |

##  Scientific Rationale

### Why 1.5?
- **Common practice** in solar physics literature
- **Balances sensitivity** and specificity
- **Conservative enough** to minimize false positives
- **Validated** in previous EB studies

### Physical Interpretation
- `>1.5×QS`: Significant chromospheric heating
- `≤1.5×QS`: Likely background variations or noise

## Customization


```python
# For stricter detection (fewer, brighter EBs)
THRESHOLD_FACTORS = [2.0] * len(DATASET_PATHS)

# For more sensitive detection (more, fainter EBs)
THRESHOLD_FACTORS = [1.2] * len(DATASET_PATHS)
```

### Per-Dataset Thresholds
```python
# Different thresholds for each dataset
THRESHOLD_FACTORS = [1.5, 1.6, 1.4, 1.5, 1.7, 1.3, 1.5, 1.6]
```

## Validation Metrics

The threshold effectiveness is evaluated by:
- **Detection statistics** (before/after thresholding)
- **Lifetime distributions**
- **Area and contrast properties**
- **Comparison with visual inspection**


## ❓ Frequently Asked Questions

### Q: Why use a multiplicative threshold?
**A:** Solar intensities vary between datasets and observing conditions. A multiplicative threshold adapts to different background levels.

### Q: Can I use absolute intensity values?
**A:** Yes, but it requires careful calibration and is less robust to changing observing conditions.

### Q: How was the quiet sun mean calculated?
**A:** The mean intensity is computed from predefined quiet sun regions in the `qs.txt` files for each dataset.

### Q: What percentage of events are typically filtered?
**A:** Typically, 20-40% of detections are removed as noise, depending on data quality.
