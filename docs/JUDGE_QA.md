# Judge Q&A — Short Answers

**Q1. What is your innovation?**
A unified software framework combining CNN feature extraction, LSTM temporal learning and GA-based hyperparameter optimization for multi-hazard structural risk monitoring and early warning.

**Q2. Why CNN?**
CNN can learn local patterns and frequency/signature-like features from sensor windows.

**Q3. Why LSTM?**
Structural behavior is time-dependent; LSTM helps model temporal dependencies and evolving damage patterns.

**Q4. Why GA?**
It can automate search over model hyperparameters instead of relying only on manual tuning.

**Q5. What data are you using today?**
The live MVP uses synthetic sensor data generated for demonstration. For final validation, we will use a traceable public/historical structural dataset and document its source.

**Q6. Have you achieved 96.8% accuracy / R² 0.983?**
“No. Those numbers came from reference material in the earlier presentation and are not our experimentally validated results. We removed them from the current SIH presentation and will report our own results only after systematic training and testing.”

**Q7. Do you need physical sensors?**
“No. The SIU software prototype can demonstrate the complete data-to-alert pipeline using CSV or simulated sensor streams. Physical IoT integration is a later deployment stage.”

**Q8. How will you validate it?**
With train/validation/test splits or appropriate cross-validation, class-wise metrics, regression error where applicable, false-alarm rate, latency and robustness across hazard types.

**Q9. What happens after a high-risk prediction?**
The risk engine generates an early-warning state on the dashboard; a future deployment can connect it to SMS/app/API notification services and engineering response workflows.
