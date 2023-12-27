import serial
import time
import re

digits = [
    [
        "  000  ",
        " 0   0 ",
        " 0   0 ",
        " 0   0 ",
        " 0   0 ",
        "  000  "
    ],
    [
        "   1 ",
        "  11 ",
        " 1 1 ",
        "   1 ",
        "   1 ",
        "   1 "
    ],
    [
        "  222  ",
        " 2   2 ",
        "    2  ",
        "   2   ",
        "  2    ",
        " 22222 "
    ],
    [
        " 333  ",
        "    3 ",
        " 333  ",
        "    3 ",
        "    3 ",
        " 333  "
    ],
    [
        " 4  4 ",
        " 4  4 ",
        " 4444 ",
        "    4 ",
        "    4 ",
        "    4 "
    ],
    [
        " 5555 ",
        " 5    ",
        " 555  ",
        "    5 ",
        "    5 ",
        " 555  "
    ],
    [
        "    6  ",
        "   6   ",
        "  666  ",
        " 6   6 ",
        " 6   6 ",
        "  666  "
    ],
    [
        " 77777 ",
        "     7 ",
        "    7  ",
        "   7   ",
        "  7    ",
        " 7     "
    ],
    [
        "  88  ",
        " 8  8 ",
        "  88  ",
        " 8  8 ",
        " 8  8 ",
        "  88  "
    ],
    [
        "  999  ",
        " 9   9 ",
        " 9   9 ",
        "  999  ",
        "   9   ",
        "  9    "
    ]
]

def my_print(n):
    to_print = ["","","","","",""]
    for char in str(n):
        dig = digits[int(char)]
        for i in range(6):
            to_print[i] += dig[i]
    for line in to_print:
        print(line)
    print("")


exp = r"^-?[0-9]+\.[0-9]+ -?[0-9]+\.[0-9]+ -?[0-9]+\.[0-9]+$"

# Replace 'COM3' with the appropriate port name for your system
serial_port = '/dev/ttyACM0'
baud_rate = 115200

# Establish a connection to the serial port
ser = serial.Serial(serial_port, baud_rate, timeout=1)

i = 0
f = open(f"data2_{i}.txt", "w")
my_print(i)

do = True

try:
    while do:
        # Read data from the serial port
        data = ser.readline().decode('utf-8').strip()

        # If data received, print it
        if data:
            if re.search(exp, data):
                f.write(data)
                f.write("\n")
            elif data == "s":
                i += 1
                my_print(i)
                f.close()
                f = open(f"data2_{i}.txt", "w")
            elif data == "n":
                do = False
                f.close
                ser.close()
            else:
                print(data)
            # Give the device time to send data again
            time.sleep(0.005)

# To close the serial port gracefully, use Ctrl+C to break the loop
except KeyboardInterrupt:
    print("Closing the serial port.")
    ser.close()
