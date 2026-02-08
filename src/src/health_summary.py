import os
import re
from datetime import datetime

class HealthSummary:
    def __init__(self):
        self.UC_CONSTANT = 13954
        self.handshake_log = "LOGS/CONNECTIVITY_HANDSHAKE.md"

    def get_total_13954_mass(self):
        """Extracts and sums the adapted values from the Ledger."""
        total_mass = 0
        if not os.path.exists(self.handshake_log):
            return 0
            
        with open(self.handshake_log, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # We look for the 4th column in the Markdown table
                parts = line.split('|')
                if len(parts) >= 6:
                    raw_val = parts[4].strip().replace(',', '')
                    # Use regex to find the first sequence of digits
                    match = re.search(r'\d+', raw_val)
                    if match:
                        total_mass += int(match.group())
        return total_mass

    def generate_report(self):
        mass = self.get_total_13954_mass()
        harmonics = mass / self.UC_CONSTANT
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        
        print("\n" + "💠" * 20)
        print(f" SYSTEM HEALTH REPORT | ARCHITECT: L.E.B.")
        print(f" TIMESTAMP: {timestamp}")
        print(" " + "💠" * 20)
        print(f" > Total System Mass:   {mass:,} Units")
        print(f" > Harmonic Frequency:  {harmonics:.4f} x 13954")
        
        # Check for perfect mathematical alignment
        if mass > 0 and mass % self.UC_CONSTANT == 0:
            print(f" > Status:              🟢 HARMONIC SYMMETRY")
        elif mass == 0:
            print(f" > Status:              ⚪️ INERT / INITIALIZING")
        else:
            print(f" > Status:              🟡 ALIGNING (Delta: {self.UC_CONSTANT - (mass % self.UC_CONSTANT)})")
            
        print("-" * 40)
        print(f" [!] Universal Code 13954 is active.")
        print("=" * 40 + "\n")

if __name__ == "__main__":
    reporter = HealthSummary()
    reporter.generate_report()
