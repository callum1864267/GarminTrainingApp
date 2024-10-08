import pandas as pd

def get_training_data():
    zones_HR = []
    maxHR = 0
    restHR = 0
    print("Enter ")

    for zone in zones:
        while True:
            try:
                time = float(input(f"{zone}: "))
                times.append(time)
                break
            except ValueError:
                print("Please enter a valid number.")

    return zones, times

def get_training_data():
    zones = ["UT3", "UT2", "UT1", "AT", "TR", "AC", "AP"]
    times = []

    print("Enter the time spent in each training zone in minutes:")

    for zone in zones:
        while True:
            try:
                time = float(input(f"{zone}: "))
                times.append(time)
                break
            except ValueError:
                print("Please enter a valid number.")

    return zones, times

def save_to_excel(zones, times):
    training_data = {"Zone": zones, "Time (minutes)": times}
    df = pd.DataFrame(training_data)
    excel_file = 'training_zones.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"Data successfully saved to {excel_file}")

def main():
    zones, times = get_training_data()
    save_to_excel(zones, times)

if __name__ == "__main__":
    main()

