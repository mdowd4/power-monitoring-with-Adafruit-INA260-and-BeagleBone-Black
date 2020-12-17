import csv
import time
import board
import adafruit_ina260

# Set up csv file
csvfile = open(r'/var/lib/cloud9/SeniorProject/testing.csv', 'w')
writer = csv.writer(csvfile, dialect='excel')
writer.writerow(["Iout (mA)","Vout (V)","Pout (mW)", "Iin (mA)","Vin (V)","Pin (mW)"]);

# Set up I2C communication
i2c = board.I2C()
ina260_out = adafruit_ina260.INA260(i2c, address=64) # Default address=64
ina260_in = adafruit_ina260.INA260(i2c, address=65) # A0 tied to vs

# Function for taking the average of the values in a list
def npSum(x):
    y = 0
    for i in range(len(x)):
        y = y + x[i]
    return y

# Define some things
m = 30
n = 5*60 # Number of hours times 60 minutes

i_in = []
v_in = []
p_in = []
i_out = []
v_out = []
p_out = []

time.sleep(1)

# Run for n minutes
for j in range(n):
    # Store data in lists every other second for 1 minute
    for k in range(m):

        i_out.insert(k, ina260_out.current)
        v_out.insert(k, ina260_out.voltage)
        p_out.insert(k, ina260_out.power)
        i_in.insert(k, ina260_in.current)
        v_in.insert(k, ina260_in.voltage)
        p_in.insert(k, ina260_in.power)
        time.sleep(1)
        
    # Take average of each and save to csv file
    curr_out = npSum(i_out)/m
    volt_out = npSum(v_out)/m
    powr_out = npSum(p_out)/m
    curr_in = npSum(i_in)/m
    volt_in = npSum(v_in)/m
    powr_in = npSum(p_in)/m
    writer.writerow([curr_out, volt_out, powr_out, curr_in, volt_in, powr_in])
    
    # Clear lists for the next minute
    i_out.clear()
    v_out.clear()
    p_out.clear()
    i_in.clear()
    v_in.clear()
    p_in.clear()
    
csvfile.close()
