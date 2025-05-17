Anomaly Detection in Option Chain Data — README
===============================================

This project performs anomaly detection on 1-second resampled option chain data using rule-based methods.
It identifies irregularities such as IV spikes, sudden LTP jumps, and volume surges across multiple instruments.

-------------------------
Requirements
-------------------------

Install the required packages using pip:

pip install pandas numpy matplotlib fastparquet

-------------------------
How to Run
-------------------------

1. Place the dataset files (ad1.parquet and ad2.parquet) in the same folder as the notebook.
2. Run the anomaly_detection_script.ipynb using jupyter notebook.
3. The script will:
   - Load and merge the datasets
   - Preprocess the time series data
   - Engineer features: IV z-score, LTP moving average, volume spike score
   - Detect anomalies using rule-based thresholds
   - Save results to results.csv

-------------------------
Output
-------------------------

- results.csv — Detected anomalies with timestamp, instrument, and reason  

-------------------------
Notes
-------------------------

- Keep both parquet files in the same folder as the script
- Output files are generated in the same directory
- The code is general and works with similar structured data from different days
- Please find the summary report added Summary_Report_Divya_220005020

-------------------------
Contact
-------------------------

Divya Singh Maurya - mems220005020@iiti.ac.in
