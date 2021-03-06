# Make sure to have the server side running in V-REP:
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simExtRemoteApiStart(19999)
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
import Lab1_Agents_Task1_World as World

# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))

while robot: # main Control loop
    #######################################################
    # Perception Phase: Get information about environment #
    #######################################################
    simulationTime = World.getSimulationTime()
    if simulationTime%1000==0:
        # print some useful info, but not too often
        print ('Time:',simulationTime,\
               'ultraSonicSensorLeft:',World.getSensorReading("ultraSonicSensorLeft"),\
               "ultraSonicSensorRight:", World.getSensorReading("ultraSonicSensorRight"))

    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################
    if simulationTime<6000:
        motorSpeed = dict(speedLeft=2, speedRight=2)

    # Wait untill block is picked up
    elif simulationTime<11000:
        motorSpeed = dict(speedLeft=0, speedRight=0)

    # Back up
    elif simulationTime<11500:
        motorSpeed = dict(speedLeft=-2, speedRight=-2)

    # Turn left
    elif simulationTime<12951:
        motorSpeed = dict(speedLeft=-2, speedRight=2)

    # Move towards second block
    elif simulationTime<22000:
        motorSpeed = dict(speedLeft=2, speedRight=2)

    # Wait for pickup
    elif simulationTime<30500:
        motorSpeed = dict(speedLeft=0, speedRight=0)

    # Back up
    elif simulationTime<38000:
        motorSpeed = dict(speedLeft=-2, speedRight=-2)

    # Turn Left
    elif simulationTime<39500:
        motorSpeed = dict(speedLeft=-2, speedRight=2)

    # Move forward for lineup
    elif simulationTime<48000:
        motorSpeed = dict(speedLeft=2, speedRight=2)

    # Turn right
    elif simulationTime<49650:
        motorSpeed = dict(speedLeft=2, speedRight=-2)

    # Move forward towards the third block
    elif simulationTime<63000:
        motorSpeed = dict(speedLeft=2, speedRight=2)  
        
    else:
        motorSpeed = dict(speedLeft=0, speedRight=0)
        
    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################
    # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)
    # try to collect energy block (will fail if not within range)
    if simulationTime%10000==0:
        print ("Trying to collect a block...",World.collectNearestBlock())
