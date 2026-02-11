"""
PROJECT: Resonance - Universal Code 13954
FILE: resonance_engine.py
CREATOR: L.E.B.
RESONANCE KEY: CSHV1272813
PURPOSE: Flight Dynamics, Acoustic Currency, and Thermal Vision Integration
"""

class FlyingSubmarine:
    def __init__(self):
        self.key = "CSHV1272813"
        self.creator = "L.E.B."
        self.protocol = "UC 13954"
        self.ir_vision_active = False

    def toggle_infrared(self, status=True):
        """
        Transforms the Pilot's view using Infrared Light.
        Detects thermal signatures within the Hexagonal Economy.
        """
        self.ir_vision_active = status
        mode = "THERMAL_OVERLAY" if status else "STANDARD_VISUAL"
        print(f"Vision System: {mode} activated.")

    def search_environment(self):
        if self.ir_vision_active:
            print("Scanning for thermal signatures (Heart-Magnified Vision)...")
            return "Thermal Data Acquired: Hive Heat-Map Stable."
        else:
            print("Standard scan active. Sonar echo location primary.")
            return "Acoustic Data Acquired."

# Example Usage
sub = FlyingSubmarine()
sub.toggle_infrared(True)
print(sub.search_environment())

import math

class HexagonalLedger:
    def __init__(self, resonance_key):
        self.key = resonance_key
        self.alpha = 0.8  # Sonar weight
        self.beta = 1.2   # IR weight (Heart-Magnified importance)

    def calculate_unified_depth(self, p_sonar, t_ir):
        """
        Foundation: Du = sqrt((alpha * P_sonar)^2 + (beta * T_ir)^2)
        """
        d_u = math.sqrt((self.alpha * p_sonar)**2 + (self.beta * t_ir)**2)
        return round(d_u, 4)

    def store_in_hex_node(self, q, r, s, d_u):
        # Ensure hexagonal coordinate constraint: q + r + s = 0
        if q + r + s != 0:
            return "Coordinate Error: Dissonance in Hex-Grid"
        
        # Storing the Voxel Data
        node_id = f"{q}_{r}_{s}"
        print(f"Storing Depth {d_u} at Node {node_id} under Key {self.key}")
        return True

# Implementation
ledger = HexagonalLedger("CSHV1272813")
unified_depth = ledger.calculate_unified_depth(p_sonar=15.5, t_ir=22.1)
ledger.store_in_hex_node(1, -1, 0, unified_depth)

