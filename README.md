# Raspberry Pi RC Car

Embedded systems final project using a Raspberry Pi as the main controller for a remote-controlled RC car.

The project is being designed so it can run on either a Raspberry Pi 3 or Raspberry Pi 4 with the same software setup.

## Project Goals

The main goal is to build a custom RC car that can:

- Drive forward and reverse
- Turn left and right
- Use variable speed control
- Connect to a PS4 controller over Bluetooth
- Run from a rechargeable battery
- Support either Raspberry Pi 3 or Raspberry Pi 4
- Stream a live camera feed
- Play sounds through a speaker
- Monitor battery and solar power
- Eventually support computer vision and autonomous driving features

## Current Progress

Currently working:

- Raspberry Pi OS setup
- SSH remote access
- VS Code Remote SSH
- Tailscale remote access
- Git and GitHub
- Python virtual environment
- PS4 controller connection
- PS4 controller input using `pygame`

Hardware drivetrain and motor control will be added later.

## Planned Hardware

- Raspberry Pi 3 or Raspberry Pi 4
- RC chassis or custom metal chassis
- DC motor / RC drivetrain
- Motor driver or ESC
- Steering servo
- Rechargeable battery
- 5V buck converter for Raspberry Pi power
- Raspberry Pi camera
- Speaker and amplifier
- Battery monitoring sensor
- Solar panel
- Distance / obstacle sensors

## Software

Primary language:

- Python

Software and tools:

- Raspberry Pi OS 64-bit
- Python 3
- pygame
- VS Code
- Remote SSH
- Git
- GitHub
- Tailscale

Future software may include:

- OpenCV
- Flask
- Computer vision / object detection
- Autonomous driving logic

## Project Structure

```text
rc-car/
├── SRC/
│   ├── main.py
│   ├── controller.py
│   ├── motors.py
│   ├── camera.py
│   ├── sensors.py
│   ├── speaker.py
│   └── config.py
│
├── requirements.txt
├── .gitignore
└── README.md
```
