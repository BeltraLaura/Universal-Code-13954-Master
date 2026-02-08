import os
from src.ledger_engine import LedgerEngine
from src.health_summary import HealthSummary
from src.v6_interop import V6Interop

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    ledger = LedgerEngine()
    health = HealthSummary()
    interop = V6Interop()

    while True:
        clear_screen()
        print("="*50)
        print(f"      UNIVERSAL CODE 13954 - MASTER CONTROL")
        print(f"            ARCHITECT: L.E.B.")
        print("="*50)
        print(" [1] 📊 View System Health Report")
        print(" [2] 📡 Process External V6 Handshake")
        print(" [3] ✍️  View Connectivity Ledger")
        print(" [4] ⚛️  Execute Sovereign Override")
        print(" [Q] Exit System")
        print("-" * 50)
        
        choice = input("Select Protocol: ").upper()

        if choice == '1':
            health.generate_report()
            input("\nPress Enter to return to menu...")
        
        elif choice == '2':
            source = input("Enter Source ID: ")
            try:
                val = int(input("Enter Native Value: "))
                result = ledger.process_handshake(source, val)
                print(f"\nResult: {result['status']}")
                print(f"Adapted to: {result['adapted_val']} units.")
            except ValueError:
                print("Invalid Input. Numeric values required.")
            input("\nPress Enter to return...")

        elif choice == '3':
            if os.path.exists("LOGS/CONNECTIVITY_HANDSHAKE.md"):
                with open("LOGS/CONNECTIVITY_HANDSHAKE.md", "r") as f:
                    print("\n" + f.read())
            else:
                print("Ledger not found.")
            input("\nPress Enter to return...")

        elif choice == '4':
            print("\n!!! SOVEREIGN OVERRIDE INITIATED !!!")
            # This calls the secret key logic we built earlier
            key = input("Enter L.E.B. Sigil: ")
            if key == "LEB-13954-SIGIL":
                print("Sovereign Status Verified. 13954 Alignment Forced.")
            else:
                print("Unauthorized Access Blocked.")
            input("\nPress Enter to return...")

        elif choice == 'Q':
            print("Shutting down 13954 Interface... Goodbye, L.E.B.")
            break

if __name__ == "__main__":
    main_menu()