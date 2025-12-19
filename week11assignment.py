# The EV Charging Network
# You are managing an Electric Vehicle (EV) charging network.
#  You must calculate the charging cost—applying a discount 
# if the driver is a “Subscriber”—before authorizing the session against their wallet.

# Requirements:

# Helper Function:
def start_charging(drivers_db, stations_db, driver_id, station_id, kwh_amount):
    if driver_id  not in  drivers_db:
        raise KeyError ("Driver not found")
    if station_id not in stations_db:
        raise KeyError ("Station offline")
    if type(kwh_amount)!=int or kwh_amount <= 0:
        raise ValueError ("Invalid kWh amount")
    price_per_kwh = stations_db[station_id]["price"]
    total = kwh_amount * price_per_kwh
    if drivers_db[driver_id]["plan"] == "Subscriber":
        total = total * 0.75
    if drivers_db[driver_id]["wallet"] < total:
        raise ValueError ("Insufficient funds")
    drivers_db[driver_id]["wallet"] -= total
    return float(total)


def batch_charge_requests(drivers_db, stations_db, request_list):
    dictionary={}
    dictionary['revenue']=0
    dictionary['denied_sessions']=0
    for driver_id, station_id,kwh_amount in request_list:
        try:
            revenue=start_charging(drivers_db, stations_db, driver_id, station_id, kwh_amount)
            dictionary["revenue"]+=revenue
        except (KeyError,ValueError) as e:
            dictionary['denied_sessions']+=1
            print(f"Charge Error for {driver_id}: {e}")
    return dictionary

    

# Logic: Iterate through the request_list.
# Error Handling: Catch exceptions. Print "Charge Error for [Driver]: [Message]".
# Return: A dictionary: {'revenue': float, 'denied_sessions': int}.
# Testing Inputs:

# Format: {StationID: {"price": float}}
stations = {
    "S_Fast": {"price": 0.50},
    "S_Slow": {"price": 0.20}
}

# Format: {DriverID: {"wallet": float, "plan": str}}
drivers = {
    "D1": {"wallet": 10.0, "plan": "Guest"},
    "D2": {"wallet": 10.0, "plan": "Subscriber"} # 25% off
}

requests = [
    ("D1", "S_Slow", 20),      # Valid. Cost: 4.0. Rem: 6.0.
    ("D2", "S_Fast", 20),      # Valid. Cost: (10.0 * 0.75) = 7.5. Rem: 2.5.
    ("D1", "S_Fast", 50),      # Error: Cost 25.0 > 6.0.
    ("D1", "S_Hyper", 10),     # Error: Station offline.
    ("D9", "S_Slow", 10),      # Error: Driver not found.
    ("D1", "S_Slow", -5)       # Error: Invalid kWh amount.
]



print(batch_charge_requests(drivers, stations, requests))
# Expected Output:

# Charge Error for D1: Insufficient funds
# Charge Error for D1: 'Station offline'
# Charge Error for D9: 'Driver not found'
# Charge Error for D1: Invalid kWh amount
# {'revenue': 11.5, 'denied_sessions': 4}