import sys
import os

# Add the analysis directory to path
sys.path.insert(0, r"c:\Users\27885\Desktop\citywalk\情感分析")

# Now try to run the main script
print("Starting...")

# Import and run main
try:
    from run_analysis import main
    print("Imported main function")
    main()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
