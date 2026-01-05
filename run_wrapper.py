import subprocess
import sys

result = subprocess.run(
    [sys.executable, r"c:\Users\27885\Desktop\citywalk\情感分析\run_analysis.py"],
    capture_output=True,
    text=True,
    cwd=r"c:\Users\27885\Desktop\citywalk\情感分析"
)

print("STDOUT:")
print(result.stdout)
print("\nSTDERR:")
print(result.stderr)
print(f"\nReturn code: {result.returncode}")
