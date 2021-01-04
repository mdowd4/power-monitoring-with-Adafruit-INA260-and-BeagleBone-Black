import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

# Import data
data1 = pd.read_csv(r'C:\Users\maryc\Desktop\Senior Project\day1.csv')
data2 = pd.read_csv(r'C:\Users\maryc\Desktop\Senior Project\day2.csv')
data3a = pd.read_csv(r'C:\Users\maryc\Desktop\Senior Project\day3_a.csv')
data3b = pd.read_csv(r'C:\Users\maryc\Desktop\Senior Project\day3_b.csv')
data3c = pd.read_csv(r'C:\Users\maryc\Desktop\Senior Project\day3_c.csv')

# Seperate data
# Stationary
Iout_1 = data1['Iout (mA)'].values
Vout_1 = data1['Vout (V)'].values
Pout_1 = data1['Pout (mW)'].values
Iin_1 = data1['Iin (mA)'].values
Vin_1 = data1['Vin (V)'].values
Pin_1 = data1['Pin (mW)'].values
m_1 = len(Iout_1)

# LDR
Iout_2 = data2['Iout (mA)'].values
Vout_2 = data2['Vout (V)'].values
Pout_2 = data2['Pout (mW)'].values
Iin_2 = data2['Iin (mA)'].values
Vin_2 = data2['Vin (V)'].values
Pin_2 = data2['Pin (mW)'].values
m_2 = len(Iout_2)

# GPS A
Iout_3_a = data3a['Iout (mA)'].values
Vout_3_a = data3a['Vout (V)'].values
Pout_3_a = data3a['Pout (W)'].values
Iin_3_a = data3a['Iin (mA)'].values
Vin_3_a = data3a['Vin (V)'].values
Pin_3_a = data3a['Pin (W)'].values
m_3_a = len(Iout_3_a)

# GPS B
Iout_3_b = data3b['Iout (mA)'].values
Vout_3_b = data3b['Vout (V)'].values
Pout_3_b = data3b['Pout (W)'].values
Iin_3_b = data3b['Iin (mA)'].values
Vin_3_b = data3b['Vin (V)'].values
Pin_3_b = data3b['Pin (W)'].values
m_3_b = len(Iout_3_b)

# GPS C
Iout_3_c = data3c['Iout (mA)'].values
Vout_3_c = data3c['Vout (V)'].values
Pout_3_c = data3c['Pout (W)'].values
Iin_3_c = data3c['Iin (mA)'].values
Vin_3_c = data3c['Vin (V)'].values
Pin_3_c = data3c['Pin (W)'].values
m_3_c = len(Iout_3_c)


# Datetime
# Stationary
t_1 = '12:00' # Start time
x_1 = [datetime.datetime.strptime(t_1, "%H:%M") + datetime.timedelta(minutes=i) for i in range(m_1 - 46)]

# LDR
t_2 = '10:52' # Start time
x_2 = [datetime.datetime.strptime(t_2, "%H:%M") + datetime.timedelta(minutes=i) for i in range(m_2)]

# GPS
t_3_a = '12:48'
t_3_b = '14:34'
t_3_c = '15:35'
x_3_a = [datetime.datetime.strptime(t_3_a, "%H:%M") + datetime.timedelta(minutes=i) for i in range(m_3_a)] #30
x_3_b = [datetime.datetime.strptime(t_3_b, "%H:%M") + datetime.timedelta(minutes=i) for i in range(m_3_b)] #60
x_3_c = [datetime.datetime.strptime(t_3_c, "%H:%M") + datetime.timedelta(minutes=i) for i in range(m_3_c)]

# X-axis limits
strt_x = datetime.datetime.strptime('10:40', "%H:%M")
stp_x = datetime.datetime.strptime('16:40', "%H:%M")


# Plot output currents over time 
# Plot figure
plt.figure(figsize=(10,6))
plt.plot(x_1, Iout_1[45:-1], 'orange')
plt.plot(x_2, Iout_2, 'mediumseagreen')
plt.plot(x_3_a, Iout_3_a, 'b')
plt.plot(x_3_b, Iout_3_b, 'b')
plt.plot(x_3_c, Iout_3_c, 'b')

# X-axis data labels
plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%H:%M')
plt.gca().xaxis.set_major_formatter(myFmt)

# Title, legend, labels, save to image file
plt.title('Output Current vs Time')
plt.legend(['Stationary', 'LDR', 'GPS'])
plt.xlabel('Time')
plt.ylabel('Iout (mA)')
plt.ylim(900, 2600)
plt.xlim(strt_x, stp_x)
plt.savefig(r'C:\file_path\Iout.png')
