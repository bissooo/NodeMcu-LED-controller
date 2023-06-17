# NodeMcu-LED-controller

 ## Instructions to flash firmware:
1. Connect NodeMcu to USB
2. Identify USB port with command: $ dmesg | grep tty
3. Grant permission to write to the USB with command: $ sudo chmod 0777 /dev/ttyUSB0
4. Install tool for flashing with command: $ pip install esptool
5. Erase flash memory with command: $ esptool.py --port /dev/ttyUSB0 erase_flash
6. Finally, flash the firmware with command: $ esptool.py --port /dev/ttyUSB0 write_flash esp8266-20170108-v1.8.7.bin