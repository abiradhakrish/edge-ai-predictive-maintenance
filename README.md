# edge-ai-predictive-maintenance
IoT and Edge AI system for real-time equipment monitoring, anomaly detection, and predictive maintenance using machine learning


# Edge AI-Based IoT Predictive Maintenance System

An **IoT and Edge AI predictive maintenance system** designed to monitor equipment health using sensor data and machine learning. The system processes machine data to identify abnormal operating conditions and predict potential equipment failures.

## Overview

Unexpected equipment failures can result in downtime, maintenance costs, and operational losses. Predictive maintenance uses machine data and machine learning to identify early signs of equipment degradation and support proactive maintenance.

This project demonstrates an end-to-end pipeline for collecting sensor data, processing and analyzing machine behavior, developing machine learning models, and performing inference in an edge-oriented environment.

### System Architecture

```text
IoT Sensors
     ↓
Sensor Data Collection
     ↓
MQTT Communication
     ↓
Data Processing & Feature Engineering
     ↓
Machine Learning Model
     ↓
Edge Inference
     ↓
Failure / Anomaly Detection
     ↓
Maintenance Alert
```

## Implemented

* Synthetic IoT sensor data generation
* Machine sensor data preprocessing
* Project environment and dependency setup
* Git-based project version control

## Planned Features

* [ ] Exploratory data analysis and visualization
* [ ] Feature engineering
* [ ] Machine learning-based failure/anomaly detection
* [ ] MQTT-based real-time sensor communication
* [ ] Real-time inference pipeline
* [ ] FastAPI prediction service
* [ ] Model evaluation and performance monitoring
* [ ] Edge-oriented model deployment
* [ ] Integration with real IoT sensors

## Sensors

The system works with machine operating parameters such as:

* **Temperature**
* **Vibration**
* **Current**
* **RPM**

These sensor measurements are used to identify abnormal operating conditions and assess machine health.

## Technology Stack

| Category         | Technologies              |
| ---------------- | ------------------------- |
| Programming      | Python                    |
| Data Processing  | Pandas, NumPy             |
| Machine Learning | Scikit-learn              |
| Communication    | MQTT *(Planned)*          |
| API              | FastAPI *(Planned)*       |
| Database         | SQLite *(Planned)*        |
| Visualization    | Matplotlib                |
| Model Management | Joblib                    |
| Development      | VS Code, Jupyter Notebook |
| Version Control  | Git, GitHub               |

## Machine Learning

The planned machine learning pipeline will include:

1. Data collection
2. Data cleaning and preprocessing
3. Exploratory data analysis
4. Feature engineering
5. Model training
6. Model validation
7. Performance evaluation
8. Model deployment
9. Real-time inference

## Project Structure

```text
edge-ai-predictive-maintenance/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   └── data_generator.py
│
├── models/
├── api/
├── tests/
├── docs/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/abbymike/edge-ai-predictive-maintenance.git
cd edge-ai-predictive-maintenance
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
```

### 3. Activate the environment

On macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Generate sensor data

```bash
python src/data_generator.py
```

The generated dataset is stored in:

```text
data/raw/sensor_data.csv
```

## Planned Machine Learning Evaluation

The machine learning component will be evaluated using appropriate classification or anomaly-detection metrics, depending on the final modeling approach.

Potential metrics include:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* ROC-AUC

For predictive maintenance, particular attention will be given to **recall and false-negative errors**, since failing to identify a potential equipment failure can be costly.

## Edge AI

The project is designed with an edge-oriented architecture where machine learning inference can be performed close to the source of sensor data.

The planned edge implementation will explore:

* Low-latency inference
* Reduced data transmission
* Reduced dependency on cloud processing
* Model optimization for edge environments
* ONNX or other hardware-optimized inference approaches

## Future Enhancements

* Integrate real IoT sensors
* Implement MQTT-based real-time communication
* Use real-world predictive maintenance datasets
* Improve failure prediction and anomaly detection
* Add Remaining Useful Life (RUL) prediction
* Deploy the model on edge hardware
* Optimize the model for low-latency inference
* Add monitoring and automated model evaluation
* Containerize the application using Docker
* Expand the API and monitoring capabilities

## Disclaimer

The initial sensor data used in this project is simulated for development and experimentation. Results obtained from simulated data should not be interpreted as real-world equipment failure predictions.

## Author

**Abinaya Mahendran**

Data Scientist | AI/ML Engineer


