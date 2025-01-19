from matplotlib import pyplot as plt
import csv

# Making empty lists to store the data
data = [["Appliance", "Time (Hours)", "Power Consumption (Units)", "Cost (INR)"]]
bill = []
elecp = []
tdata = []

# Function to calculate the bill of the Air Conditioner
def AC():
    global bill, elecp, tdata
    a = int(input("How many stars is your A.C. (higher the stars, lower the bill): "))
    b = int(input("How many hours do you use the A.C. in a day: "))
    
    if a == 1:
        energy = b * 100
        bill_amount = b * 10
    elif a == 2:
        energy = b * 90
        bill_amount = b * 9
    elif a == 3:
        energy = b * 80
        bill_amount = b * 8
    elif a == 4:
        energy = b * 70
        bill_amount = b * 7
    elif a == 5:
        energy = b * 60
        bill_amount = b * 6
    else:
        print("Invalid star rating")
        return

    # For 30 days
    total_energy = energy * 30
    total_bill = bill_amount * 30
    total_time = b * 30
    print(f"Your A.C. consumes {total_energy} units of energy and generates a bill of {total_bill} INR for {b} hours of usage daily.")
    bill.append(total_bill)
    elecp.append(total_energy)
    tdata.append("AIR CONDITIONER")
    data.append(["A.C.", total_time, total_energy, total_bill])

# Function to calculate the bill of a Fan
def fan():
    global bill, elecp, tdata
    b = int(input("How many hours do you use the fan in a day: "))
    energy = b * 5  
    bill_amount = b * 0.5  
    
    # For 30 days
    total_energy = energy * 30
    total_bill = bill_amount * 30
    total_time = b * 30
    print(f"Your fan consumes {total_energy} units of energy and generates a bill of {total_bill} INR for {b} hours of usage daily.")
    bill.append(total_bill)
    elecp.append(total_energy)
    tdata.append("FAN")
    data.append(["Fan", total_time, total_energy, total_bill])

# Function to calculate the bill of a Heater
def heater():
    global bill, elecp, tdata
    b = int(input("How many hours do you use the heater in a day: "))
    energy = b * 150  
    bill_amount = b * 15  
    
    # For 30 days
    total_energy = energy * 30
    total_bill = bill_amount * 30
    total_time = b * 30
    print(f"Your heater consumes {total_energy} units of energy and generates a bill of {total_bill} INR for {b} hours of usage daily.")
    bill.append(total_bill)
    elecp.append(total_energy)
    tdata.append("HEATER")
    data.append(["Heater", total_time, total_energy, total_bill])

# Function to calculate the bill of a Geyser
def geyser():
    global bill, elecp, tdata
    b = int(input("How many hours do you use the geyser in a day: "))
    energy = b * 200  
    bill_amount = b * 20  
    
    # For 30 days
    total_energy = energy * 30
    total_bill = bill_amount * 30
    total_time = b * 30
    print(f"Your geyser consumes {total_energy} units of energy and generates a bill of {total_bill} INR for {b} hours of usage daily.")
    bill.append(total_bill)
    elecp.append(total_energy)
    tdata.append("GEYSER")
    data.append(["Geyser", total_time, total_energy, total_bill])

# Function to read and display data from the CSV file
def read_csv():
    print("\n--- Reading Electricity Consumption Data ---")
    try:
        with open('C:\\Users\\incar\\OneDrive\\Desktop\\electricity bill.txt', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File not found. Please run the program to generate the data.")

# Function to plot a bar graph of appliances and their bills
def plot_graph():
    if not tdata or not bill:
        print("\nNo data available to plot. Please calculate some appliance bills first.")
        return

    # Plotting the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(tdata, bill, color='red', edgecolor='black')
    plt.xlabel("Appliances")
    plt.ylabel("Monthly Bill (INR)")
    plt.title("Electricity Bill per Appliance")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Collect data for appliances
while True:
    print("\n--- Electricity Consumption and Bill Calculation System ---")
    print("\n1. Air Conditioner")
    print("2. Fan")
    print("3. Heater")
    print("4. Geyser")
    print("5. Plot Graph")
    print("6. Read CSV File")
    print("7. Exit and Save Data")
    choice = int(input("Select an option (1-7): "))

    if choice == 1:
        AC()
    elif choice == 2:
        fan()
    elif choice == 3:
        heater()
    elif choice == 4:
        geyser()
    elif choice == 5:
        plot_graph()
    elif choice == 6:
        read_csv()
    elif choice == 7:
        break
    else:
        print("Invalid choice. Please select again.")

# Writing the data to the CSV file
with open('C:\\Users\\incar\\OneDrive\\desktop\\electricity bill.txt', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("\nElectricity consumption data has been saved to 'electricity_bill.csv'.")

