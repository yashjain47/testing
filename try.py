# # import serial
# # import time

# # try:
# #     # Configure the serial port
# #     ser = serial.Serial(
# #         port='/dev/ttyUSB1',  # Replace with your serial port
# #         baudrate=115200,
# #         parity=serial.PARITY_NONE,
# #         stopbits=serial.STOPBITS_ONE,
# #         bytesize=serial.EIGHTBITS,
# #         timeout=1  # Read timeout in seconds
# #     )

# #     time.sleep(2) # Give the microcontroller time to initialize

# #     # Sending data
# #     message = "Hello Microcontroller\r\n" # Include line ending if required
# #     ser.write(message.encode())
# #     ser.flush() # Ensure data is sent

# #     # Reading data
# #     while True:
# #         if ser.in_waiting > 0:
# #             received_data = ser.readline().decode().strip() # Read a line and decode
# #             print(f"Received: {received_data}")
# #         time.sleep(0.1)

# # except serial.SerialException as e:
# #     print(f"Serial port error: {e}")
# # except KeyboardInterrupt:
# #     print("Program terminated by user.")
# # finally:
# #     if 'ser' in locals() and ser.is_open:
# #         ser.close()
# #         print("Serial port closed.")






# import json


# res = {
# "userId": 12345,
# "recommendations": [
# {"title": "Breaking Bad", "genre" : "Drama","rating": 9.5},
# {"title": "Family Man", "genre" : "Action", "rating": 8.8},
# {"title": "Lost in Space", "genre" : "Sci-Fi","rating": 7.2},
# {"title": "Sacred Games", "genre" : "Drama", "rating" : 8.6}
# ]
# }



# # response = json.load(res)
# # print(res)

# # for key,value in res.items():
# #     print(key,value)

# # count=0

# # res['recommendations']
# # for i in res['recommendations']:
# #     if i['rating'] > 8.5:
# #         print(i['title'])
# #         count+=1

# # d = ["recommendations"]

# # for i in res.keys():
# #     if i in d:
# #         print("Found")
# # print(count)


# import psutil
# import time

# def get_battery_status():
#     battery = psutil.sensors_battery()

#     if battery is None:
#         return "❌ No battery detected"

#     percent = battery.percent
#     plugged = battery.power_plugged

#     return percent, plugged


# def check_battery_behavior(interval=60):
#     print("Checking battery behavior...\n")

#     p1, plugged1 = get_battery_status()
#     time.sleep(interval)
#     p2, plugged2 = get_battery_status()

#     if plugged1:
#         print("🔌 Charger connected")
#         if p2 > p1:
#             print("✅ Battery is charging correctly")
#         elif p2 == p1:
#             print("⚠️ Battery NOT charging (percentage stuck)")
#         else:
#             print("❌ Battery discharging while plugged in")
#     else:
#         print("🔋 Running on battery")
#         if p2 < p1:
#             print("✅ Battery is discharging correctly")
#         elif p2 == p1:
#             print("⚠️ Battery NOT discharging (percentage stuck)")
#         else:
#             print("❌ Battery charging without charger (abnormal)")

#     print(f"\nBattery % before: {p1}%")
#     print(f"Battery % after : {p2}%")


# if __name__ == "__main__":
#     check_battery_behavior(interval=60)  # check over 1 minute

