![image](https://github.com/MoHazem02/Real-Time-Medical-Data-Monitoring-System/assets/66066832/aacfedb7-28f1-44bc-9a7b-83cc96e19a53)
## Real-Time Medical Data Monitoring System

This project is a real-time medical data monitoring system developed to simulate communication between a medical device and a server application. It utilizes various technologies including Redis database, PyQT5 for the GUI, and TCP socket programming to facilitate the transmission of data from the client to the server.

### Features

- **Data Transmission**: The system facilitates real-time transmission of medical data from the client to the server using TCP socket programming. Data is sent in JSON format.
- **Medical Vital**: The monitored medical vital in this system is Body Temperature. The system simulates a sensor to generate reasonable temperature values.
- **Patient Monitoring**: The system supports monitoring of multiple patients. In this project, 5 patients are monitored simultaneously.
- **Data Visualization**: Pyqtgraph library is utilized for plotting temperature readings against time, providing users with visual representation of the data.
- **Alert System**: An alert is triggered when the temperature reading exceeds 38 degrees Celsius, notifying users of potentially critical conditions.

### Components

- **Server Application**: The server side of the system receives data from the clients, stores it in a Redis database, and provides functionalities for data retrieval.
- **Client Application**: The client side of the system simulates the medical device, generating temperature readings for each patient and sending them to the server.
- **GUI (Graphical User Interface)**: PyQT5 is used to create an intuitive and user-friendly interface for both the client and server applications.
- **Database**: Redis database is employed to store and manage the medical data received from the clients.

### Usage

1. **Installation**:
   - Clone the repository to your local machine.
   - Ensure that Redis database is installed and running on your system.
   - Install the required Python packages.

2. **Running the Server**:
   - Navigate to the server directory.
   - Run the server application using the provided script or command.
   
3. **Running the Client**:
   - Navigate to the client directory.
   - Run the client application using the provided script or command.

4. **Using the GUI**:
   - Once both the server and client are running, interact with the GUI to monitor patient data, search for specific patients by ID, and visualize temperature readings over time.

### Contributors

- Mohamed Hazem
- Mahmoud Mansy
