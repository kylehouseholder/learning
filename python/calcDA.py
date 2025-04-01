import math

def getval(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Try again, but with a number: ")

# Make a list of temperature at altitude from test.txt
altm = getval("Enter altitude (ft): ")
if altm > 40000:
    print("Altitude is too high. Try again.")
    altm = getval("Enter altitude (ft): ")

baro = getval("Enter barometer setting (\"Hg): ")
if baro < 25.5 or baro > 32.0:
    print("Barometer setting out of range, try again.")
    baro = getval("Enter barometer setting (\"Hg): ")

temp = getval("Enter temperature (°C): ")
if temp < -40 or temp > 60:
    print("Temperature exceeds range (-40°C to 60°C), try again.")
    temp = getval("Enter temperature (°C): ")

altoffset = (29.92 - baro) * 1000
altp = altm + altoffset

# !F: Rudimentary ISA calculation - replace
tempISA = 15 + (altm/1000 * -2)
tempoffset = temp - tempISA

# !D: sanity checks
print("Pressure altitude: ")
print(altp)
print("ISA Temp: ")
print(tempISA)

# Calculate density altitude



# Calculate takeoff and landing distances, both calm and with at least two wind depths (user set)

# Calculate climb gradient, climb rate, time to climb to user-driven cruise target

# Calculate estimated HP% and performance in cruise

# Calculate VNAV-style descent profile


# !F: Not a working exit, needs return to menu and exit
exit = getval("Exit? Y/N")
