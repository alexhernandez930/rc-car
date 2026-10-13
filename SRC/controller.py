import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick connected")
    exit()

controller = pygame.joystick.Joystick(0)
controller.init()

print(f"Connected to: {controller.get_name()}")

try:
    while True:
        pygame.event.pump()

        # Buttons
        for i in range(controller.get_numbuttons()):
            button = controller.get_button(i)

            if button:
                print(f"Button {i} pressed")

        # Axes
        for i in range(controller.get_numaxes()):
            axis = controller.get_axis(i)

            # PS4 triggers usually rest at -1
            if i == 2 or i == 5:
                if axis > -0.90:
                    print(f"Trigger Axis {i}: {axis:.2f}")

            # Analog sticks normally rest near 0
            else:
                if abs(axis) > 0.10:
                    print(f"Stick Axis {i}: {axis:.2f}")

        pygame.time.wait(100)

except KeyboardInterrupt:
    print("Exiting...")
    pygame.quit()