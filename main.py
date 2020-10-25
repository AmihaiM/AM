import csv

def install_python_libraries(package):
    subprocess.call([sys.executable, "-m", "pip", "install", "--proxy", "http://proxy.jer.intel.com:911", package])


# install_python_libraries("pandas")
import pandas as pd
print("hello wrold")

file_path = r"\\jessst01.ger.corp.intel.com\SST\Logs\Windows_Logs\Integration\NPI_Master_CRWFW5101_99.0.58.3_PHBTW_WEEKLY1141_22.20.20422.17241_[Oct_15]\EventsReport_2020-18-10--10-31-29.csv"

ip = "10.12.179.233"
# read csv file to pandas object
df = pd.read_csv(file_path)

del df['Time']  ## delete 'Time' column
# filter by specific IP and code number
print(df[(df['DUT IP'] == ip) & (df["Code"] == 5002.0)])
"""
# read csv file line by line
with open(file_path, "r") as file:
    for i, line in enumerate(file):
        print("[{}]: {}".format(i, line))
"""
print("End")