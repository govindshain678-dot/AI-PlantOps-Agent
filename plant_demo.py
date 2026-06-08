import time
import random

class HeatExchangerSimulation:
    def __init__(self):
        # Initial conditions (Normal Operation)
        self.product_inlet_temp = 150.0  # Celsius
        self.cooling_water_flow = 50.0   # kg/s
        self.fouling_factor = 0.01       # Initial fouling
        self.elapsed_hours = 0

    def get_sensor_data(self):
        """Simulates raw sensor data from the plant."""
        # As fouling increases, heat transfer efficiency drops
        # Product outlet temp rises as a result
        efficiency_loss = self.fouling_factor * 200 
        product_outlet_temp = 80.0 + efficiency_loss + random.uniform(-0.5, 0.5)
        
        # Pressure drop increases with fouling
        pressure_drop = 1.2 + (self.fouling_factor * 50) + random.uniform(-0.02, 0.02)
        
        return {
            "timestamp": f"T+{self.elapsed_hours}h",
            "product_inlet_temp": round(self.product_inlet_temp, 2),
            "product_outlet_temp": round(product_outlet_temp, 2),
            "cooling_water_flow": round(self.cooling_water_flow, 2),
            "pressure_drop_bar": round(pressure_drop, 2)
        }

    def step(self):
        """Advance time and increase fouling."""
        self.elapsed_hours += 4
        self.fouling_factor += 0.05  # Increased fouling rate for demo visibility

class AIPlantOpsAgent:
    def __init__(self):
        self.threshold_temp = 110.0  # Alert if product outlet > 110C
        self.history = []

    def analyze(self, data):
        """Analyzes sensor data using engineering reasoning."""
        print(f"\n--- [AGENT ANALYSIS] {data['timestamp']} ---")
        print(f"Current Product Outlet: {data['product_outlet_temp']}°C")
        print(f"Current Pressure Drop: {data['pressure_drop_bar']} bar")

        # Reasoning Engine
        if data['product_outlet_temp'] > 95.0:
            print("REASONING:")
            print("- Observed: Rising outlet temperature despite constant cooling flow.")
            print("- Observed: Corresponding increase in pressure drop across the shell.")
            print("- Conclusion: High probability of Heat Exchanger Fouling (Deposition).")
            
            # Predictive Insight
            if data['product_outlet_temp'] > self.threshold_temp:
                print("CRITICAL ALERT: Efficiency below safety limits!")
                print("RECOMMENDATION: Initiate bypass for mechanical cleaning immediately.")
            else:
                hours_to_limit = (self.threshold_temp - data['product_outlet_temp']) / 1.5
                print(f"PREDICTION: Safety limit ({self.threshold_temp}°C) will be reached in approx {round(hours_to_limit, 1)} hours.")
                print("RECOMMENDATION: Schedule maintenance for the next 12-hour window.")
        else:
            print("STATUS: Operation within normal efficiency parameters.")

def run_demo():
    sim = HeatExchangerSimulation()
    agent = AIPlantOpsAgent()

    print("=== AI PlantOps Agent: Heat Exchanger Monitoring Demo ===")
    
    # Run simulation for 5 steps (20 hours)
    for _ in range(6):
        data = sim.get_sensor_data()
        agent.analyze(data)
        sim.step()

if __name__ == "__main__":
    run_demo()
