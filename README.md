# NodeMcu-LED-controller

 ## Instructions to flash firmware:
1. Connect NodeMcu to USB
2. Identify USB port with command: $ dmesg | grep tty
3. Grant permission to write to the USB with command: $ sudo usermod -a -G tty yourname. Reboot pc to make it actual.
4. Install tool for flashing with command: $ pip install esptool
5. Erase flash memory with command: $ esptool.py --port /dev/ttyUSB0 erase_flash
6. Finally, flash the firmware with command: $ esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 firmware.bin
7. connect to REPL over serial with $ picocom /dev/ttyUSB0 -b115200