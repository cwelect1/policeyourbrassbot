from PyRoombaAdapter import PyRoombaAdapter

def main():
    PORT = "/dev/ttyUSB0"
    adapter = PyRoombaAdapter(PORT)
    # adapter.send_drive_cmd(-100, -1000)
    # adapter.send_drive_direct(-100, 100)
    import math
    # adapter.move(0.1, math.radians(-10))
    # adapter.send_drive_pwm(80, 80)
    # adapter.send_drive_pwm(-200, -200)
    # adapter.send_moters_cmd(False, True, True, True, False)
    # adapter.send_pwm_moters(-55, -25, 25)
    # adapter.send_buttons_cmd(dock=True)
    # sleep(1.0)

    adapter.move(0.2, math.radians(0.0))
    sleep(1.0)
    adapter.move(0, math.radians(-20))
    sleep(6.0)
    adapter.move(0.2, math.radians(0.0))
    sleep(1.0)
    adapter.move(0, math.radians(20))
    sleep(6.0)

    # adapter.move(-0.1, 0)
    # sleep(1.0)


if __name__ == '__main__':
    main()