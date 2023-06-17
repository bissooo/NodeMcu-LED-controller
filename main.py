# Import required libraries
import machine
import socket
 # Set up the LEDs with custom names
led_bottom = machine.PWM(machine.Pin(0), freq=1000, duty=512)
led_middle = machine.PWM(machine.Pin(5), freq=1000, duty=512)
led_top = machine.PWM(machine.Pin(4), freq=1000, duty=512)
 # Default LED intensity is 50%
led_bottom_intensity = 50
led_middle_intensity = 50
led_top_intensity = 50
 # Define the web page HTML
def web_page():
    html = """<!DOCTYPE html>
    <html>
        <head>
            <title>ESP8266 LED Control</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
            <h1>ESP8266 LED Control</h1>
            <p>Current {} Intensity: <strong>{}</strong>%</p>
            <p>Current {} Intensity: <strong>{}</strong>%</p>
            <p>Current {} Intensity: <strong>{}</strong>%</p>
            <form method="get">
                <div>
                    <label for="intensity0">{} Intensity (0-100%):</label>
                    <input type="number" id="intensity0" name="intensity0" min="0" max="100" value="{}">
                </div>
                <div>
                    <label for="intensity1">{} Intensity (0-100%):</label>
                    <input type="number" id="intensity1" name="intensity1" min="0" max="100" value="{}">
                </div>
                <div>
                    <label for="intensity2">{} Intensity (0-100%):</label>
                    <input type="number" id="intensity2" name="intensity2" min="0" max="100" value="{}">
                </div>
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>""".format("LED Bottom", led_bottom_intensity, "LED Middle", led_middle_intensity, "LED Top", led_top_intensity, "LED Bottom", led_bottom_intensity, "LED Middle", led_middle_intensity, "LED Top", led_top_intensity)
    return html
 # Set up the socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
 # Main loop
while True:
    # Accept incoming connections
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
     # Receive and process the request
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
     # Ignore requests for favicon.ico
    if '/favicon.ico' in request:
        conn.close()
        continue
     # Check if the request contains the LED intensity value
    intensity_pos = request.find('/?intensity=')
    if intensity_pos != -1:
        intensity_end = request.find('&', intensity_pos)
        if intensity_end == -1:
            intensity_end = request.find(' ', intensity_pos)
        if intensity_end != -1:
            intensity_str = request[intensity_pos+12:intensity_end]
            try:
                led_bottom_intensity, led_middle_intensity, led_top_intensity = map(int, intensity_str.split(','))
            except ValueError:
                print("Invalid LED intensity value, using default value of 50")
                led_bottom_intensity = 50
                led_middle_intensity = 50
                led_top_intensity = 50
            led_bottom.duty(int(led_bottom_intensity * 10.23))
            led_middle.duty(int(led_middle_intensity * 10.23))
            led_top.duty(int(led_top_intensity * 10.23))
     # Send the response
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()