from rplidar import RPLidar

PORT_NAME = '/dev/ttyUSB0'

lidar = RPLidar(PORT_NAME, baudrate=115200)

try:
    info = lidar.get_info()
    print("LIDAR Info:", info)

    health = lidar.get_health()
    print("LIDAR Health:", health)

except Exception as e:
    print("Error:", e)

finally:
    lidar.disconnect()
