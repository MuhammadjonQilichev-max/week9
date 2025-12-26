 #  City Traffic Surveyor
text = """MainSt,Downtown,450,100
Broadway,Downtown,300,50
OakAve,Suburbs,100,20
PineRd,Suburbs,50,10
Hwy101,Highway,800,400
Error,Line,Missing,Data
MarketSt,Downtown,500,200"""

with open('traffic_survey.txt','w') as file:
    file.write(text)
total_vehicle_volume = {}
congested_streets = []
def analyze_traffic_flow(filename):
    with open('traffic_survey.txt','r') as filename:
        for line in filename:
            street_name,district,car_count,truck_count=line.strip().split(',')
            try:
                total_volume = int(car_count) + int(truck_count)
                if district in total_vehicle_volume:
                    total_vehicle_volume[district] =+ total_volume
                else:
                    total_vehicle_volume[district] = total_volume
            except (KeyError,ValueError):
                continue
            if total_volume > 500:
                congested_streets.append(f'{street_name} ({total_volume} vehicles)')
    return total_vehicle_volume, congested_streets


def write_traffic_report(district_totals, congested_streets):
    with open('traffic_report.txt', 'w') as file:
        file.write("DISTRICT TRAFFIC VOLUME\n")
        file.write("-----------------------\n")
        for district,totals in district_totals.items():
            file.write(f'{district}: {totals}\n')
        file.write('\n')
        file.write('CONGESTED STREETS (> 500 vehicles)\n')
        file.write("----------------------------------\n")
        for streets in congested_streets:
            file.write(f'{streets}\n')

district_totals,congested_streets = analyze_traffic_flow('traffic_survey.txt')
write_traffic_report(district_totals,congested_streets)


# Expected Output (traffic_report.txt)

# DISTRICT TRAFFIC VOLUME
# -----------------------
# Downtown: 1600
# Suburbs: 180
# Highway: 1200

# CONGESTED STREETS (> 500 vehicles)
# ----------------------------------
# MainSt (550 vehicles)
# Hwy101 (1200 vehicles)
# MarketSt (700 vehicles)