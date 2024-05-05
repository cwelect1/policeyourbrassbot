# Roberto: The Autonomous Rover

## Introduction

Roberto is an autonomous rover designed to navigate and complete missions in a flat-range environment, preferably an indoor or outdoor range with a flat surface like asphalt. This project aims to create a reliable and efficient rover capable of traveling between waypoints while avoiding obstacles.

## Prototype 1: Front-Wheel Drive Rover

The first prototype was a front-wheel drive rover built using a Tupperware container mounted on a 20x20 extruded aluminum frame. It featured 6.5' hoverboard wheels in the front and two caster wheels in the rear, chosen for their ability to navigate a flat range and overcome any casings it might get stuck on. However, this prototype encountered a couple of issues:

- The hoverboard wheels required a specific, expensive ESC, and two cheap ESCs were burned out during testing.
- The components were haphazardly placed inside the container, resulting in a messy wiring situation.

## Prototype 2: RC Chassis-Based Rover (Roberto)

For the second iteration, an RC chassis (INJORA RC Frame Chassis Assembled Frame Chassis for 1/10 RC Crawler SCX10 II) was used as the base for Roberto. The following components were utilized:

- INJORA RC Frame Chassis: [Link](https://www.amazon.com/Assembled-Chassis-Crawler-Upgrades-Without/dp/B07Q11X193?th=1)
- 25KG Digital Servo High Torque: [Link](https://www.amazon.com/ANNIMOS-Digital-Torque-Waterproof-Control/dp/B07GJ6ZCVY)
- GoolRC 60A Brushed ESC Electronic Speed Controller: [Link](https://www.amazon.com/GoolRC-Brushed-Electronic-Controller-Replacement/dp/B0BG4ZB4QD)
- Pixhawk4 (reused from Prototype 1): [Link](https://www.amazon.com/pixhawk-4/s?k=pixhawk+4)
- Readytosky M8N GPS Module (reused from Prototype 1): [Link](https://shorturl.at/lpDU2)
- Raspberry Pi 4 B: [Link](https://www.microcenter.com/product/622539/pi4modelB8gb?src=raspberrypi)
- LiPo battery: [Link](https://shorturl.at/cdrPR)
- LiPo Charger: [Link](https://shorturl.at/dmH26)
- 915Mhz 100MW Radio Telemetry Air and Ground Data Transmit Module: [Link](https://www.amazon.com/YoungRC-Telemetry-Transmit-Pixhawk-Controller/dp/B0C4LBZGRG)
- Flysky Controller and receiver: [Link](https://shorturl.at/DEUV5)
- UBEC Power Module: [Link](https://t.ly/xTYPt)
- Solder Kit: [Link](https://t.ly/piTnM)
- Allen Key set: [Link](https://t.ly/bNFA7)
- M3 assortment set: [Link](https://t.ly/n6eyz)

# Build Process

## 1. Raspberry Pi Configuration

Before assembling Roberto, it is highly recommended that the Raspberry Pi is formatted and configured first. This will save you from the hassle of accessing the SD card in a hard-to-reach spot later on. Start by downloading the appropriate operating system image for your Raspberry Pi model (e.g., Raspberry Pi OS) and write it to the SD card using a tool like Etcher or Raspberry Pi Imager. Once the SD card is ready, insert it into the Raspberry Pi and perform the initial setup, including configuring the Wi-Fi connection, enabling SSH, and updating the system packages. This will allow you to access the Raspberry Pi remotely using SSH from your computer terminal, eliminating the need for physical access to the SD card.

## 2. Chassis Assembly

The RC car chassis serves as the foundation for Roberto. Depending on the specific chassis you purchased, it may come fully assembled or require some assembly. In the case of the INJORA RC Frame Chassis, you will need to install the wheels. Use an Allen key to tighten the screws and ensure that the wheels are securely attached to the chassis. The chassis provides a sturdy base and sufficient ground clearance for Roberto to navigate various terrains.

## 3. Brushed ESC and Motor Connection

Mount the brushed ESC (Electronic Speed Controller) to the motor and establish the necessary connections. Refer to the documentation provided with your ESC and motor to identify the correct wiring configuration. Typically, the ESC will have three wires (positive, negative, and signal) that need to be connected to the corresponding terminals on the motor. Ensure that the connections are secure and properly insulated to prevent short circuits.

## 4. Servo Installation

Install the servo onto the front frame of the chassis. The servo is responsible for steering Roberto. Pay close attention to the alignment and mounting of the servo to ensure that Roberto drives straight. If the installation is not optimal, it can cause Roberto to veer off course. Refer to the servo's documentation for guidance on proper installation and calibration.

## 5. LiPo Battery Connection

Attach the LiPo battery to Roberto's chassis, following the manufacturer's guidelines. Ensure that the battery is securely mounted and the connections are properly made. Double-check the polarity of the battery connections to avoid damage to the components. Before proceeding further, verify that all components are receiving the correct power supply by connecting them to the battery and testing their functionality.

## 6. RC Receiver and Controller Setup

Connect the RC receiver to Roberto and pair it with the Flysky controller. This step is crucial to ensure that you have manual control over Roberto before proceeding with the autonomous setup. Follow the instructions provided with your specific RC receiver and controller to establish the connection. Test the functionality of the controller by moving the joysticks and verifying that Roberto responds accordingly. Having manual control will be invaluable for troubleshooting and testing purposes.

## 7. GPS Module Assembly

Assemble the GPS module and mount it securely on Roberto's chassis. The Injora chassis typically comes with pre-drilled holes that allow you to attach the GPS stand using screws. Ensure that the arrow on the GPS module is pointing towards the front of the vehicle. This orientation is essential for accurate navigation. If the GPS stand is damaged or broken, you can temporarily use a 3D-printed replacement until you can obtain a new one.

## 8. Pixhawk and Raspberry Pi Integration

Connect the Pixhawk flight controller and Raspberry Pi to Roberto's chassis and establish the necessary connections between the components. Refer to the documentation provided by the manufacturers for detailed instructions on wiring and configuration. The Pixhawk typically has dedicated ports for GPS, telemetry, and other peripherals. Make sure to connect the components to the correct ports to ensure proper communication and functionality. The Raspberry Pi will serve as the companion computer, running the necessary software for autonomous navigation and control.

## 9. Cable Management

Use electrical tape and cable ties to keep the wiring tidy and organized. Route the cables neatly along the chassis, avoiding any moving parts or potential snag points. A clean and well-managed wiring setup not only improves the aesthetics of Roberto but also reduces the risk of loose connections or damage to the cables during operation.

## 10. Telemetry Module and Mission Planner

Install the telemetry module on Roberto and configure it to establish a connection with Mission Planner. The telemetry module enables wireless communication between Roberto and your computer, allowing you to monitor its status, send commands, and receive telemetry data. Follow the documentation provided with your telemetry module to set up the connection properly. Once connected, you can use Mission Planner to plan waypoints, monitor Roberto's progress, and analyze telemetry data.

# Setting up Autonomous Missions

1. **SSH into the Raspberry Pi:** To establish a secure connection with the Raspberry Pi, use the SSH protocol. Open your computer's command terminal and enter the following command: 
    ```
    ssh username@raspberrypi_ip_address
    ```
    Replace `username` with the username you set up during the formatting of the Raspberry Pi, and `raspberrypi_ip_address` with the IP address assigned to your Raspberry Pi. When prompted, enter the password you configured during the setup process. If you have forgotten your credentials, you may need to reformat the Raspberry Pi and set up a new username and password.

2. **Download Python files and install libraries:** Once you have successfully logged into the Raspberry Pi via SSH, navigate to the directory where you want to store your Python files. Use the following command to download the necessary files from the GitHub repository: 
    ```
    git clone https://github.com/your_repository_url
    ```
    Replace `your_repository_url` with the URL of the GitHub repository containing the required Python files for your autonomous mission. After downloading the files, navigate to the project directory and install the required libraries. You can typically do this using the pip package manager. For example: 
    ```
    pip install dronekit
    pip install pymavlink
    ```

3. **Create a virtual environment (optional):** In some cases, you may need to create a virtual environment to avoid conflicts with existing Python libraries. To create a virtual environment, use the following command: 
    ```
    python3 -m venv myenv
    ```
    Replace `myenv` with your desired name for the virtual environment. To activate the virtual environment, run: 
    ```
    source myenv/bin/activate
    ```
    Once activated, you can install the necessary libraries within the virtual environment using pip as mentioned in step 2.

4. **Navigate to the Python files:** Use the `cd` command to navigate to the directory where your Python files are located. For example: 
    ```
    cd /path/to/your/python/files
    ```
    Replace `/path/to/your/python/files` with the actual path to the directory containing your Python files.

5. **Run the connection test:** To ensure that the Raspberry Pi is properly connected to the Pixhawk and ready for autonomous missions, run the `connection_test.py` file. Use the following command: 
    ```
    python connection_test.py
    ```
    If the connection is successful, you should see a message indicating that the Raspberry Pi is connected to the Pixhawk and ready to receive commands.

6. **Edit the location-based movement file:** Open the `location_based_movement.py` file using the nano text editor with the following command: 
    ```
    nano location_based_movement.py
    ```
7. **Inside the file, locate the section where you need to specify the GPS coordinates of your waypoints.*** Enter the latitude, longitude, and altitude for each waypoint in the format specified in the file. For example: 
    ```
    waypoints = [

        (latitude1, longitude1, altitude1),

        (latitude2, longitude2, altitude2),

        # Add more waypoints as needed

    ]
    ```
    Save the changes by pressing Ctrl+X, then Y, and finally Enter.

7. **Run the location-based movement file:** To start the autonomous mission, run the location_based_movement.py file using the following command: 
    ```
    python location_based_movement.py
    ```
    The rover should now begin navigating to the specified waypoints autonomously. Monitor the progress of the mission through the command terminal or any connected telemetry software like Mission Planner. If the rover successfully reaches all the waypoints, congratulations! You have successfully set up and executed an autonomous mission.

    Remember to always prioritize safety and follow proper precautions when working with autonomous vehicles. Ensure that you have a clear line of sight to the rover and are ready to take manual control if necessary. DO NOT attempt to do this on a street, your Rover may run away and get crushed by a car.

# Challenges and Solutions

## Challenge: Difficulty in connecting the Pixhawk to the Raspberry Pi.
**Solution:** Ensure that you have the correct wiring connections between the Pixhawk and Raspberry Pi. Refer to the wiring diagrams and documentation specific to your Pixhawk model. Double-check the pin assignments and make sure the connections are secure. If you're still having issues, try using a different USB cable or port on the Raspberry Pi.

## Challenge: Issues with the Raspberry Pi not booting or not being accessible via SSH.
**Solution:** First, make sure that the Raspberry Pi is properly powered and the power supply is sufficient. Check if the LED lights on the Raspberry Pi are indicating any activity. If the issue persists, try reformatting the SD card and reinstalling the operating system. Ensure that SSH is enabled in the Raspberry Pi configuration settings.

## Challenge: The rover is not moving or responding to commands.
**Solution:** Check the battery connections and ensure that the rover is properly powered. Verify that the ESC and motor connections are correct and secure. Make sure that the RC receiver is properly bound to the transmitter and the channels are configured correctly. Use the `connection_test.py` script to confirm the communication between the Raspberry Pi and the Pixhawk.

## Challenge: The rover is not following the specified waypoints accurately.
**Solution:** Ensure that the GPS module is properly connected and has a clear view of the sky. Verify that the GPS coordinates of the waypoints are accurate and entered correctly in the `location_based_movement.py` file. Check the GPS status in Mission Planner or other telemetry software to confirm that the rover is receiving a valid GPS signal.

## Challenge: The rover is behaving erratically or not stabilizing during autonomous missions.
**Solution:** Make sure that the Pixhawk is properly calibrated, including the accelerometer, compass, and radio calibration. Follow the calibration procedures outlined in the Pixhawk documentation. Check the PID tuning parameters and adjust them if necessary to achieve stable flight behavior.

## Challenge: Difficulty in installing required libraries or dependencies.
**Solution:** Double-check that you are using the correct version of Python and pip. Ensure that you have a stable internet connection to download the necessary packages. If you encounter conflicts with existing libraries, consider creating a virtual environment to isolate the project dependencies. Consult the documentation or forums for the specific library you are having trouble with.

## Challenge: The rover loses connection or telemetry data during the mission.
**Solution:** Check the telemetry module connections and ensure that the antennas are securely attached. Verify that the telemetry settings in Mission Planner or other ground control software match the settings on the rover. Ensure that the rover is within the range of the telemetry module and there are no obstructions interfering with the signal.

## Challenge: The code is not running or throwing errors.
**Solution:** Double-check the syntax and indentation of your Python code. Verify that all the required libraries are imported correctly. Check for any missing dependencies or incompatible versions. Consult the error messages and traceback to identify the specific line or section causing the issue. Seek help from forums, documentation, or the robotics community if needed.


## Author Information

- **Author:** Grigori A. Lopez-Garcia
- **Major:** Digital Media Design
- **University:** Harvard Extension
- **Graduation Year:** 2023
- **Email:** grl322@g.harvard.edu
