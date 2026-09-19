
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

## Project Status

The project is being developed incrementally, starting with synthetic IoT sensor data generation and progressing toward machine learning-based predictive maintenance and edge inference.

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
| Communication    | MQTT                      |
| API              | FastAPI                   |
| Database         | SQLite                    |
| Visualization    | Matplotlib                |
| Model Management | Joblib                    |
| Development      | VS Code, Jupyter Notebook |
| Version Control  | Git, GitHub               |

## Machine Learning

The machine learning pipeline includes:

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

## Machine Learning Evaluation

The machine learning component will be evaluated using appropriate classification or anomaly-detection metrics depending on the final modeling approach.

Potential metrics include:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* ROC-AUC

For predictive maintenance, particular attention will be given to **recall and false-negative errors**, since failing to identify a potential equipment failure can be costly.

## Edge AI

The project uses an edge-oriented architecture where machine learning inference can be performed close to the source of sensor data.

The system focuses on:

* Low-latency inference
* Reduced data transmission
* Reduced dependency on cloud processing
* Model optimization for edge environments
* Efficient machine learning inference

## Future Enhancements

* Integration with real IoT sensors
* Real-time MQTT communication
* Real-world predictive maintenance datasets
* Remaining Useful Life (RUL) prediction
* Edge hardware deployment
* Model optimization
* Monitoring and automated model evaluation
* Docker-based deployment

## Disclaimer

The initial sensor data used in this project is simulated for development and experimentation. Results obtained from simulated data should not be interpreted as real-world equipment failure predictions.

## Author

**Abinaya Mahendran**

Data Scientist | AI/ML Engineer

GitHub: https://github.com/abiradhakrish


