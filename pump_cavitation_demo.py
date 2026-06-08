import random
import time

class PumpSimulation:
    def __init__(self):
        self.suction_pressure = 2.5  # bar
        self.discharge_pressure = 12.0 # bar
        self.vibration_level = 1.2   # mm/s
        self.suction_valve_opening = 100.0 # percentage
        self.elapsed_minutes = 0

    def get_sensor_data(self):
        """Simulates pump sensor data."""
        # As suction valve closes (clogging), suction pressure drops and vibration rises
        clogging_effect = (100.0 - self.suction_valve_opening) / 10.0
        
        current_suction = self.suction_pressure - (clogging_effect * 0.4) + random.uniform(-0.05, 0.05)
        current_vibration = self.vibration_level + (clogging_effect * 1.5) + random.uniform(-0.1, 0.1)
        current_discharge = self.discharge_pressure - (clogging_effect * 0.2) + random.uniform(-0.1, 0.1)

        return {
            "timestamp": f"T+{self.elapsed_minutes}min",
            "suction_pressure_bar": round(current_suction, 2),
            "discharge_pressure_bar": round(current_discharge, 2),
            "vibration_mms": round(current_vibration, 2),
            "suction_valve_pos": round(self.suction_valve_opening, 1)
        }

    def step(self):
        """Simulate a progressive suction filter clog."""
        self.elapsed_minutes += 10
        self.suction_valve_opening -= 15 # Simulating rapid filter clogging

class AIPlantOpsAgent:
    def __init__(self):
        self.npsh_required = 1.0 # Net Positive Suction Head required
        self.vibration_limit = 4.5 # ISO 10816 limit for this pump class

    def analyze(self, data):
        print(f"\n--- [AGENT ANALYSIS] {data['timestamp']} ---")
        print(f"Suction: {data['suction_pressure_bar']} bar | Vibration: {data['vibration_mms']} mm/s")

        # Reasoning Engine
        if data['vibration_mms'] > 2.5:
            print("REASONING:")
            print(f"- Observed: Vibration increased to {data['vibration_mms']} mm/s.")
            print(f"- Observed: Suction pressure dropped to {data['suction_pressure_bar']} bar.")
            
            if data['suction_pressure_bar'] < self.npsh_required:
                print("- Conclusion: CRITICAL CAVITATION DETECTED.")
                print("- Engineering Fact: Suction pressure is below vapor pressure threshold.")
                print("RECOMMENDATION: SHUT DOWN PUMP IMMEDIATELY to prevent impeller damage.")
            else:
                print("- Conclusion: INCIPIENT CAVITATION / SUCTION STARVATION.")
                print("RECOMMENDATION: Check suction strainers and open suction valves fully.")
        else:
            print("STATUS: Pump operating smoothly within hydraulic limits.")

def run_demo():
    sim = PumpSimulation()
    agent = AIPlantOpsAgent()

    print("=== AI PlantOps Agent: Centrifugal Pump Cavitation Demo ===")
    
    # Run for 6 steps
    for _ in range(6):
        data = sim.get_sensor_data()
        agent.analyze(data)
        if data['vibration_mms'] > 7.0: # Stop if it gets too crazy
            break
        sim.step()

if __name__ == "__main__":
    run_demo()
