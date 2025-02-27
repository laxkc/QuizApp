from rplidar import RPLidar

# Set the correct port for your RPLIDAR (e.g., '/dev/ttyUSB0' or '/dev/ttyS0' for UART)
PORT_NAME = '/dev/ttyUSB0'

# Initialize the LIDAR
lidar = RPLidar(PORT_NAME)

try:
    print("Starting LIDAR scan...")
    for scan in lidar.iter_scans():
        for (_, angle, distance) in scan:
            print(f"Angle: {angle:.2f}°, Distance: {distance:.2f}mm")
except KeyboardInterrupt:
    print("Stopping LIDAR...")
finally:
    lidar.stop()
    lidar.disconnect()
