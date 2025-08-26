#  EB Lifetime Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

Analysis pipeline for studying Ellerman Bomb lifetime distributions with intensity thresholding.

## Features

- **Multi-dataset processing** of EB sources
- **Lifetime calculation** from timeframe data
- **Intensity thresholding** analysis
- **Statistical comparison** of detection methods
- **Publication-ready visualizations**

##  Quick Start

### Installation

```bash
git clone https://github.com/yourusername/eb-lifetime-analysis.git
cd eb-lifetime-analysis
pip install -r requirements.txt
```

### Basic Usage

```bash
python scripts/lifetime_analysis.py
```

### Jupyter Notebook

```bash
jupyter notebook notebooks/exploratory_analysis.ipynb
```

## Data Structure

Place your EB source files in the `data/` directory:

```
data/
├── YYYYMMDD/
│   ├── sources_S2P0T10.5d3t5.npy
│   ├── wings.fits
│   └── qs.txt
```

Expected NPY file structure:
- `id`: EB event identifiers
- `timeframe`: Observation timeframes
- `peak`: Peak intensity values
- `filled`: Filler indicators (-1 for fillers)

##  Outputs

- `results/lifetime_comparison.pdf`: Lifetime distribution plot
- Console output: Detailed statistics summary
- Numerical results: Saved as numpy arrays

## 🎯 Threshold Methodology

EB detection uses intensity thresholding to distinguish real events from noise:

```python
threshold = 1.5 × quiet_sun_mean_intensity
```

**Criteria:** EB peak intensity must exceed this threshold to be considered valid.

**Default:** 1.5× quiet sun level (50% brighter than background)

**Customization:** Modify `THRESHOLD_FACTORS` in `config.py`

For detailed methodology, see [threshold documentation](docs/threshold_methodology.md)


##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
