T = "0xffffffff00000001/"
I = "9/3/1"
P = "/0."
from fractions import Fraction
from time import sleep
import base64

commands = [Fraction(3, 2), 196608, 16, 0, 3, 16]

user_input = input("Initialize:")

# Function to check if the input is an integer
def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if is_integer(user_input):
    commands[0] = int(user_input)
else:
    try:
        user_fraction = Fraction(user_input)
        commands[0] = user_fraction
    except ValueError:
        print("Invalid input. Please enter a valid integer or fraction.")

if user_input == '1':
    commands[0] = Fraction(3, 2)
    print("Input changed to 3/2")
elif is_integer(user_input):
    commands[0] = int(user_input)
else:
    try:
        user_fraction = Fraction(user_input)
        commands[0] = user_fraction
    except ValueError:
        print()

Tip = [user_input, 196608, 16, 0, 3, 16]
print(Tip)

def r30(a, b, c):
    if (a, b, c) in [(0, 1, 1), (1, 0, 0), (1, 0, 1), (0, 1, 0)]:
        return 1
    else:
        return 0

def calculate_denominator():
    r = [int(x) for x in format(int(input("T:")), '08b')]
    cx, step = 180, 25
    c, cn = [0] * cx, [0] * cx
    c[cx // 2:cx // 2 + 8] = r

    last_value = None  # To store the last value printed by r30

    for _ in range(step):
        print(''.join(['0' if e == 0 else '1' for e in c[90:123]]))
        for i in range(cx):
            x = c[i - 1] if i > 0 else 0
            z = c[i + 1] if i < cx - 1 else 0
            cn[i] = r30(x, c[i], z)
        c = cn[:]
        last_value = int(''.join(['1' if e == 1 else '0' for e in c[90:122]]))

    return last_value

# Get the last value printed by r30
last_denominator = calculate_denominator()

# Update the Fraction object 'ip' with the last denominator value
ip = Fraction(255, last_denominator + 1)

commands = [Fraction(4, 3), 196608, 16, 0, 3, 16]

def slash(I, P):
    while I:
        print(I)
        if I[0] == '/':
            I = I[1:]
        else:
            for c in P:
                if c == "/":
                    I = I[1:]
                elif c == "\\":
                    I = c + I
                else:
                    break
            if not I:
                break

input_val = None

while ip:
    eip = -ip if input_val else ip
    if eip < 0:
        input_val -= 1
    ci = eip % len(commands)
    if ci < 0:
        ci += len(commands)
    cmd = commands[int(ci)]
    if isinstance(cmd, int):
        print(f"{cmd}")
        sleep(0.02)
    ip *= Fraction(cmd)

    if cmd == 3:
        break

def m(n):
    if n > 100:
        return n - 10
    return m(m(n + 11))

initial_hex_value = "100100100100100"  # Initial hex value for conversion to binary
q, r, w = bin(int(initial_hex_value, 16))[2:], '101110101011011101001110101110101110100000', 3

while q[w:]:
    if r[0] == '0':
        q = q[1:]
    else:
        r = r[1:] + r[0]
        if q[0] == '1':
            q += r[0]
    r = r[1:] + r[0]
    q = str(m(int(q)))

    # Convert Base64 to hexadecimal representation

    hex_address1 = int(q.encode('utf-8').hex(), 36)
    hex_address1 = "0x{:x}".format(hex_address1)

    hex_address2 = int(q.encode('utf-8').hex(), 35)
    hex_address2 = "0x{:x}".format(hex_address2)

    hex_address3 = int(q.encode('utf-8').hex(), 34)
    hex_address3 = "0x{:x}".format(hex_address3)

    hex_address4 = int(q.encode('utf-8').hex(), 33)
    hex_address4 = "0x{:x}".format(hex_address4)

    hex_address5 = int(q.encode('utf-8').hex(), 32)
    hex_address5 = "0x{:x}".format(hex_address5)

    hex_address6 = int(q.encode('utf-8').hex(), 31)
    hex_address6 = "0x{:x}".format(hex_address6)

    hex_address7 = int(q.encode('utf-8').hex(), 30)
    hex_address7 = "0x{:x}".format(hex_address7)

    hex_address8 = int(q.encode('utf-8').hex(), 29)
    hex_address8 = "0x{:x}".format(hex_address8)

    hex_address9 = int(q.encode('utf-8').hex(), 28)
    hex_address9 = "0x{:x}".format(hex_address9)

    hex_address10 = int(q.encode('utf-8').hex(), 27)
    hex_address10 = "0x{:x}".format(hex_address10)

    hex_address11 = int(q.encode('utf-8').hex(), 26)
    hex_address11 = "0x{:x}".format(hex_address11)

    hex_address12 = int(q.encode('utf-8').hex(), 25)
    hex_address12 = "0x{:x}".format(hex_address12)

    hex_address13 = int(q.encode('utf-8').hex(), 24)
    hex_address13 = "0x{:x}".format(hex_address13)

    hex_address14 = int(q.encode('utf-8').hex(), 23)
    hex_address14 = "0x{:x}".format(hex_address14)

    hex_address15 = int(q.encode('utf-8').hex(), 22)
    hex_address15 = "0x{:x}".format(hex_address15)

    hex_address16 = int(q.encode('utf-8').hex(), 21)
    hex_address16 = "0x{:x}".format(hex_address16)

    hex_address17 = int(q.encode('utf-8').hex(), 20)
    hex_address17 = "0x{:x}".format(hex_address17)

    hex_address18 = int(q.encode('utf-8').hex(), 19)
    hex_address18 = "0x{:x}".format(hex_address18)

    hex_address19 = int(q.encode('utf-8').hex(), 18)
    hex_address19 = "0x{:x}".format(hex_address19)

    hex_address20 = int(q.encode('utf-8').hex(), 17)
    hex_address20 = "0x{:x}".format(hex_address20)

    hex_address21 = int(q.encode('utf-8').hex(), 16)
    hex_address21 = "0x{:x}".format(hex_address21)

    hex_address22 = int(q.encode('utf-8').hex(), 15)
    hex_address22 = "0x{:x}".format(hex_address22)

    hex_address23 = int(q.encode('utf-8').hex(), 14)
    hex_address23 = "0x{:x}".format(hex_address23)

    hex_address24 = int(q.encode('utf-8').hex(), 13)
    hex_address24 = "0x{:x}".format(hex_address24)

    hex_address25 = int(q.encode('utf-8').hex(), 12)
    hex_address25 = "0x{:x}".format(hex_address25)

    hex_address26 = int(q.encode('utf-8').hex(), 11)
    hex_address26 = "0x{:x}".format(hex_address26)

    hex_address27 = int(q.encode('utf-8').hex(), 10)
    hex_address27 = "0x{:x}".format(hex_address27)

    
    print(hex_address1,',',hex_address2,',',hex_address3,',',hex_address4,',',hex_address5,',',hex_address6,',',hex_address7,',',hex_address8,',',hex_address9,',',hex_address10,',',hex_address11,',',hex_address12,',',hex_address13,',',hex_address14,',',hex_address15,',',hex_address16,',',hex_address17,',',hex_address18,',',hex_address19,',',hex_address20,',',hex_address21,',',hex_address22,',',hex_address23,',',hex_address24,',',hex_address25,',',hex_address26,',',hex_address27)

