import time
import random

class SolarPanel:
    def __init__(self, efficiency=1):
        self.efficiency = efficiency  # Efficiency of the solar panel (100% by default)
        self.energy_generated = 0     # Total energy generated by the solar panel
        self.max_capacity = 1000      # Maximum energy capacity of the battery
        self.battery_level = 0        # Current battery level
        self.charging_rate = 0.2     # Charging rate of the battery per unit of energy generated

    def generate_energy(self, sunlight_intensity):
        # Calculate the energy generated based on sunlight intensity and panel efficiency
        energy = sunlight_intensity * self.efficiency
        # Charge the battery with the generated energy
        self.battery_level = min(self.battery_level + energy * self.charging_rate, self.max_capacity)
        # Update the total energy generated
        self.energy_generated += energy

    def get_total_energy(self):
        return self.energy_generated

    def get_battery_level(self):
        return self.battery_level

class Sun:
    def __init__(self, intensity=0):
        self.intensity = intensity   # Sunlight intensity (measured in arbitrary units)

    def set_intensity(self, intensity):
        self.intensity = intensity

def simulate_weather_change():
    # Simulate changing weather conditions
    return random.randint(1, 10)

def main():
    solar_panel = SolarPanel()
    sun = Sun()
    count=0
    # Simulation loop
    while True:
        # Simulate changing weather conditions
        weather_change = simulate_weather_change()
        sun.set_intensity(weather_change * 10)  # Adjust sunlight intensity based on weather change

        # Generate energy based on sunlight intensity
        solar_panel.generate_energy(sun.intensity)

        # Print the total energy generated and battery level
        print("Total energy generated:", solar_panel.get_total_energy(), "units")
        print("Battery level:",round(solar_panel.get_battery_level()), "units")
        count+=1
        if solar_panel.get_battery_level()>100:
            break       
        # Wait for some time (simulating real-time)
        time.sleep(1)
    print(count)    

if __name__ == "__main__":
    main()
