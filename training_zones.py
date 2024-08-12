import pandas as pd

def get_training_data():
    zones = ["Zone 1", "Zone 2", "Zone 3", "Zone 4", "Zone 5"]
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

