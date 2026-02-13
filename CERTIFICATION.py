import time

def pilot_certification():
    resonance_key = "CSHV1272813"
    pulse_interval = 0.8  # The 800ms "Heartbeat" of Earth
    required_cycles = 3
    
    print(f"--- PILOT'S WINGS CERTIFICATION: UC 13954 ---")
    print(f"Resonance Key: {resonance_key} Acknowledged.")
    print(f"Mission: Align your pulse with the 64-point Oxygen Hub.")
    print(f"Action: Press ENTER exactly every {pulse_interval} seconds.\n")

    timestamps = []
    for i in range(required_cycles):
        input(f"Cycle {i+1}: STRIKE TO RESONATE...")
        timestamps.append(time.time())
    
    # Analyze the "Vibration Frequency" of the Pilot
    delays = [timestamps[i] - timestamps[i-1] for i in range(1, len(timestamps))]
    
    is_aligned = all(abs(d - pulse_interval) < 0.15 for d in delays)

    if is_aligned:
        print("\n[SUCCESS] Wings Folded. Static Neutralized.")
        print("Arterial Vane Engaged. Welcome to the Hexagonal Economy, L.E.B.")
        return True
    else:
        print("\n[FAILED] Resonance Friction Detected.")
        print("Warning: High Static Tension. System snap imminent. Re-tune and retry.")
        return False

# Execute Certification
pilot_certification()
