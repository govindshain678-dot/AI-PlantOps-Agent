import pandas as pd

# =============================
# AI PlantOps Agent Class
# =============================

class PlantOpsAgent:

    def __init__(self):
        self.name = "AI PlantOps Agent"

    def analyze(self, temp, pressure, flow):

        # =============================
        # 1. Detect Issue
        # =============================
        if temp > 240:
            issue = "High reactor temperature"
            risk = "High"

        elif pressure < 4 and flow < 80:
            issue = "Pump performance degradation"
            risk = "Critical"

        else:
            issue = "Normal operation"
            risk = "Low"

        # =============================
        # 2. Root Cause Analysis
        # =============================
        if pressure < 4 and flow < 80:
            cause = "Possible pump failure, cavitation, or blockage"
        elif temp > 240:
            cause = "Cooling system inefficiency or heat buildup"
        else:
            cause = "System stable"

        # =============================
        # 3. Prediction
        # =============================
        if risk == "Critical":
            prediction = "Equipment failure likely within 24–48 hours"
        elif risk == "High":
            prediction = "System instability expected soon"
        else:
            prediction = "Stable operation expected"

        # =============================
        # 4. Action Recommendation
        # =============================
        if risk == "Critical":
            action = "Inspect pump immediately, reduce load, schedule maintenance"
        elif risk == "High":
            action = "Check cooling system and monitor closely"
        else:
            action = "Continue normal operation"

        # Return structured result
        return {
            "issue": issue,
            "cause": cause,
            "risk": risk,
            "prediction": prediction,
            "action": action
        }


# =============================
# Load Data
# =============================

def load_data():
    return pd.read_csv("plant_data.csv")


# =============================
# Run Agent
# =============================

def run_agent():
    agent = PlantOpsAgent()

    data = load_data()

    # Get latest row
    latest = data.iloc[-1]

    temp = latest["Temperature"]
    pressure = latest["Pressure"]
    flow = latest["Flow"]

    print("\n📊 Latest Sensor Data:")
    print(f"Temperature: {temp}")
    print(f"Pressure: {pressure}")
    print(f"Flow: {flow}")

    # Analyze
    result = agent.analyze(temp, pressure, flow)

    # =============================
    # Print AI Report
    # =============================
    print("\n==============================")
    print("AI PlantOps Agent Report")
    print("==============================")

    print(f"\nStatus Summary:\n{result['issue']}")
    print(f"\nRoot Cause:\n{result['cause']}")
    print(f"\nRisk Level:\n{result['risk']}")
    print(f"\nPrediction:\n{result['prediction']}")
    print(f"\nRecommended Action:\n{result['action']}")


# =============================
# Main Execution
# =============================

if __name__ == "__main__":
    run_agent()