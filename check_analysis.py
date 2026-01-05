#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Quick check script to verify analyzer is working
"""
import os
import time

print("Waiting for analysis to complete...")

csv_file = r'c:\Users\27885\Desktop\citywalk\情感分析\citywalk_analysis_results.csv'

for i in range(120):  # Wait up to 120 seconds
    if os.path.exists(csv_file):
        file_size = os.path.getsize(csv_file)
        if file_size > 100:  # More than just header
            print(f"\n✓ CSV file created! Size: {file_size} bytes")
            
            # Read and display first few lines
            with open(csv_file, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
                print(f"\nFirst 3 results:")
                print(lines[0].strip())  # Header
                for i in range(1, min(4, len(lines))):
                    parts = lines[i].split(',')
                    if len(parts) >= 5:
                        print(f"  {parts[0]}: Score={parts[1]}, Pos={parts[3]}, Neg={parts[4]}")
            break
    
    time.sleep(1)
    if (i + 1) % 10 == 0:
        print(f"  Still waiting... ({i+1}s)")
else:
    print(f"\n✗ Timeout: CSV file not created after 120 seconds")
    print(f"  Checking if run_analysis.py is still running...")
