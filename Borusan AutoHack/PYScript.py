import serial
import time
import random
import requests

# Arduino'nun bağlı olduğu seri portu ve baud rate'i ayarla
ser = serial.Serial('/dev/ttyACM0', 9600) # Port adını Arduino'nun bağlı olduğu porta göre değiştirin
time.sleep(2) # Arduino'nun başlamasını beklemek için

def simulate_gps_data():
    """ GPS koordinatlarını simüle et """
    latitude = round(random.uniform(-90, 90), 6)
    longitude = round(random.uniform(-180, 180), 6)
    return f"{latitude},{longitude}"

def simulate_acceleration_data():
    """ İvme sensörü verilerini simüle et """
    acceleration_x = random.uniform(-5, 5)
    acceleration_y = random.uniform(-5, 5)
    acceleration_z = random.uniform(-5, 5)
    return f"{acceleration_x},{acceleration_y},{acceleration_z}"

def is_sharp_maneuver(acceleration_x, acceleration_y):
    """ Makas atma hareketini tespit et """
    return abs(acceleration_x) > 4.0 or abs(acceleration_y) > 4.0

def send_to_arduino(message):
    """ Arduino'ya mesaj gönder """
    ser.write(message.encode())

def send_location_to_server(latitude, longitude):
    """ GPS koordinatlarını sunucuya gönder """
    url = "http://example.com/api/location"  # Sunucunuzun URL'si
    data = {"latitude": latitude, "longitude": longitude}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Location successfully sent to the server.")
        else:
            print("Failed to send location.")
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    while True:
        gps_data = simulate_gps_data()
        acceleration_data = simulate_acceleration_data()
        latitude, longitude, acc_x, acc_y, _ = gps_data + ',' + acceleration_data.split(',')

        if is_sharp_maneuver(float(acc_x), float(acc_y)):
            send_to_arduino('ALERT\n')
            send_location_to_server(latitude, longitude)

        time.sleep(1)

if _name_ == '_main_':
    main()