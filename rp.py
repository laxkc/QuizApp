from rplidar import RPLidar

PORT_NAME = '/dev/ttyUSB0'  # Adjust if necessary
BAUDRATE = 256000  # Use 256000 for RPLIDAR A3

lidar = RPLidar(PORT_NAME, baudrate=BAUDRATE)

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
