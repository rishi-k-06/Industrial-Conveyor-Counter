# 🏭 Industrial Conveyor Counter

A robust production tracking system designed for factory environments. It monitors item throughput on a conveyor belt and calculates production efficiency in real-time.

## 🚀 Features
- **High-Speed Detection:** IR beam sensors detect items moving at up to 2m/s.
- **Throughput Analytics:** Calculates "Items Per Minute" (IPM) to identify line slowdowns.
- **Digital Twin Sync:** Real-time synchronization with a Python dashboard via Serial (USB).
- **Batch Management:** Reset and log batch totals automatically.

## ⚙️ Engineering Logic
- **Hardware:** Arduino Nano detects logic state changes on a digital interrupt pin.
- **Software:** Python monitors the Serial buffer and converts timestamps into production rate curves.
