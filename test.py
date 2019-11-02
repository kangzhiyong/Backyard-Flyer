from udacidrone import Drone
from udacidrone.connection import MavlinkConnection

conn = MavlinkConnection('tcp:127.0.0.1:5760', threaded = False, PX4 = False)
drone = Drone(conn)
drone.connection.start()
drone.take_control()
drone.arm()
#drone.set_home_as_current_position()
drone.takeoff(3.0)
drone.cmd_position(2, 1, 3.0, 0)
drone.cmd_position(0, 0, 3, 0)
drone.land()
drone.disarm()
drone.release_control()
drone.stop()