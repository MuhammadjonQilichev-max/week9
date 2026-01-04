import requests

URL = "https://api.spacexdata.com/v4/launches"

def get_launches():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            return response.json()
        else:
            print("API error")
            return []
    except:
        print("Internet error")
        return []

def main():
    print("=== SpaceX Launch Viewer ===")

    number = input("How many launches to show? ")

    if not number.isdigit():
        print("Please enter a number.")
        return

    number = int(number)

    launches = get_launches()

    if not launches:
        print("No data found.")
        return

    print("\nLatest Launches:\n")

    for launch in launches[:number]:
        name = launch["name"]
        date = launch["date_utc"]
        success = launch["success"]

        print("Mission:", name)
        print("Date   :", date)
        print("Success:", success)
        print("-" * 30)

if __name__ == "__main__":
    main()
