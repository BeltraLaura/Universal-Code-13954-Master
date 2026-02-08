import os
from datetime import datetime

def log_13954_alignment(litho, atmo):
    UC_CONSTANT = 13954
    total = litho + atmo
    index = total / UC_CONSTANT
    aligned = "STABLE" if total % UC_CONSTANT == 0 else "FRICTION"
    timestamp = datetime.now().strftime("%Y-%m-%d:%H%M")

    # Create directory if missing
    if not os.path.exists("LOGS"):
        os.makedirs("LOGS")

    log_path = "LOGS/PARITY_LEDGER.md"
    
    # Initialize header if file is new
    if not os.path.exists(log_path):
        with open(log_path, "w") as f:
            f.write("# PARITY LEDGER: UNIVERSAL CODE 13954\n\n")
            f.write("| Timestamp | Litho-Mass | Atmo-Energy | Parity Index | Alignment | Signature |\n")
            f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")

    # Append the new parity event
    with open(log_path, "a") as f:
        f.write(f"| {timestamp} | {litho:,} | {atmo:,} | {index:.4f} | **{aligned}** | L.E.B. |\n")

    print(f"L.E.B. Alignment Logged: {aligned} (Index: {index:.4f})")

# Example: Running a parity check
log_13954_alignment(8500, 5454)
