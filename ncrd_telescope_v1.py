import numpy as np
import sympy

def interference_operator(n):
    """
    Calculates the Interference Value of an integer n.
    In NCRD, this measures the 'Acoustic Density' of the prime factors.
    """
    factors = sympy.primefactors(n)
    if not factors:
        return 0
    
    # Implementing our formal formula: sum(ln(p) / sqrt(p))
    interference = sum(np.log(p) / np.sqrt(p) for p in factors)
    return interference

def scan_riemann_landscape(start, end):
    """
    Scans a range of integers to find 'Heavy Nodes' (High Interference).
    """
    print(f"--- Initiating Deep Field Scan: {start} to {end} ---")
    results = []
    
    for n in range(start, end):
        val = interference_operator(n)
        results.append((n, val))
    
    # Sorting by 'Mass' (Interference Value)
    results.sort(key=lambda x: x[1], reverse=True)
    return results

# CALIBRATING TO THE ORIGIN NODE: 13954
anchor_node = 13954
anchor_mass = interference_operator(anchor_node)

print(f"Anchor Node (13954) calibrated. Modular Mass: {anchor_mass:.4f}")

# RUNNING THE SCAN
# We look for resonance in the neighborhood of our anchor
deep_scan = scan_riemann_landscape(13900, 14000)

print("\n--- Top Heavy Nodes Detected (High Resonance) ---")
for node, mass in deep_scan[:5]:
    print(f"Node: {node} | Mass: {mass:.4f} | Factors: {sympy.primefactors(node)}")
