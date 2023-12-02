# ECG Signal Analysis Application

## Overview

Welcome to the ECG Signal Analysis Application repository! This Python desktop application is designed to load and analyze ECG signals. The application utilizes PyQt5 for the graphical user interface, pyqtgraph for dynamic plotting, and pandas for data manipulation. It enables users to load an ECG signal, dynamically visualize the waveform, count the total peaks, and display the average heartbeat rate.

## Features

- **ECG Signal Loading:** Load ECG signals in various formats for analysis.
- **Dynamic Plotting:** Real-time plotting of the ECG signal for visual analysis.
- **Peak Counting:** Automatically count the total number of peaks in the ECG signal.
- **Heartbeat Rate Calculation:** Display the average heartbeat rate based on the peak count.

## Requirements

- Python 3.x
- PyQt5
- pyqtgraph
- pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/YoussefHassanien/Heart-Rate-Measurement.git
    cd Heart-Rate-Measurement
    ```

2. Install the required libraries:

    ```bash
    pip install pandas, pyqt5, pyqtgraph
    ```

## Usage

1. Run the application:

    ```bash
    python Heart_Rate_Counter.py
    ```

2. Load an ECG signal using the "Browse Signal" button.

3. The ECG signal will be dynamically plotted in the main window.

4. The application will automatically count the total peaks and display the average heartbeat rate.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.


## Acknowledgments

- Special thanks to the developers of PyQt5, pyqtgraph, and pandas for creating the tools that make this application possible.

Feel free to explore, use, and enhance the application. Happy coding!
