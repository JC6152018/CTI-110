# CTI-110
# P4HW1 - Distance Traveled
# Jessica Washington
# July 2nd 2018

# Get the speed.
speed = float(input('What is the speed of the vehicle in mph?'))

# Get the time traveled.
time = float(input('How many hours has it traveled?'))

# Create table header.
print('Hour', '\tDistance Traveled')

# Create divider.
print('-' * 25)

# Find distance
distance = speed * time

#Set accumulator
hour = 0

for hour in range(1, 25):
    if hour <= hour:
        print(hour, '\t', distance / time * hour)
    
