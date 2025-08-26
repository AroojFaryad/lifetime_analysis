import numpy as np
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

# Import local modules
from config import Config
from utils import load_dataset, calculate_lifetime, analyze_dataset
from plot_utils import create_lifetime_plot, print_summary_statistics

def run_complete_analysis():
    """Run the complete lifetime analysis pipeline."""
    print("EB Lifetime Analysis Pipeline")
    print("=" * 50)
    
    # Initialize results
    all_lifetimes_all = []
    all_lifetimes_filtered = []
    totals = {
        'detections_before': 0, 'detections_after': 0,
        'fillers_before': 0, 'fillers_after': 0,
        'ebs_before': 0, 'ebs_after': 0
    }
    summary_data = []
    
    # Process each dataset with progress bar
    for i, (path, thresh_factor, cadence, qs_mean) in enumerate(
        tqdm(zip(Config.DATASET_PATHS, Config.THRESHOLD_FACTORS, 
                Config.CADENCES, Config.QS_MEANS), 
             total=len(Config.DATASET_PATHS), 
             desc="Processing datasets")):
        
        # Load and analyze dataset
        sources = load_dataset(path)
        if sources is None:
            continue
        
        threshold = thresh_factor * qs_mean
        stats = analyze_dataset(sources, threshold, cadence)
        
        # Aggregate results
        all_lifetimes_all.extend(stats['lifetimes_all'])
        all_lifetimes_filtered.extend(stats['lifetimes_filtered'])
        
        for key in totals:
            totals[key] += stats[key]
        
        summary_data.append({
            'filename': os.path.basename(path),
            **stats
        })
    
    return all_lifetimes_all, all_lifetimes_filtered, totals, summary_data

def main():
    """Main execution function."""
    # Create output directory
    os.makedirs(Config.OUTPUT_PATH, exist_ok=True)
    
    # Run analysis
    results = run_complete_analysis()
    all_lifetimes_all, all_lifetimes_filtered, totals, summary_data = results
    
    # Print summary statistics
    print_summary_statistics(summary_data, totals)
    
    # Create and save plot
    output_path = os.path.join(Config.OUTPUT_PATH, Config.OUTPUT_FILENAME)
    create_lifetime_plot(all_lifetimes_all, all_lifetimes_filtered, output_path)
    
    # Save numerical results
    if all_lifetimes_all:
        np.savez(os.path.join(Config.OUTPUT_PATH, "lifetime_results.npz"),
                all_lifetimes=all_lifetimes_all,
                filtered_lifetimes=all_lifetimes_filtered)
        print(f"Numerical results saved to: {Config.OUTPUT_PATH}/lifetime_results.npz")
    
    print("\n Analysis complete!")

if __name__ == "__main__":
    main()
