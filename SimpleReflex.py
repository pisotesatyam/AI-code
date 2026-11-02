def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    elif location == "B":
        return "Move Left"


print("=== Vacuum Cleaner World ===")

location = input("Enter Current Location (A/B): ").upper()
status = input("Enter Room Status (Clean/Dirty): ").capitalize()

action = vacuum_agent(location, status)

print("\nAction Performed :", action)   








