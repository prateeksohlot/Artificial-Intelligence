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
from random import randint
import time
# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))
motorSpeed = dict(speedLeft=0, speedRight=0)

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
    
    nearestBlockDistance = World.getSensorReading('energySensor').distance
    nearestBlockDirection = World.getSensorReading('energySensor').direction
    # leftSensor = World.getSensorReading('ultraSonicSensorLeft')

    if simulationTime%2000==0:
        directionOfRobot= World.robotDirection()
        # print some useful info, but not too often
        print("RobotDirection: %s, BlockDirection: %s, Difference: %s"\
            %(directionOfRobot,nearestBlockDirection,directionOfRobot - nearestBlockDistance))
            
    # Collecting Closet Block
    if World.getSensorReading("energySensor").distance < 0.6:
        motorSpeed = dict(speedLeft=0, speedRight=0)
        World.collectNearestBlock()
  
    ###################################################
    # Navigating the environment using Energy Sensors##
    ###################################################

    if nearestBlockDistance < 0.5:
        motorSpeed = dict(speedLeft=0, speedRight=0)
        World.collectNearestBlock()
    elif round(nearestBlockDirection,1) <  0:
        motorSpeed = dict(speedLeft= nearestBlockDirection/2, speedRight=-nearestBlockDirection/2)
    elif round(nearestBlockDirection,1) > 0 :
        motorSpeed = dict(speedLeft= -nearestBlockDirection/2, speedRight=nearestBlockDirection/2)
    else:
        motorSpeed = dict(speedLeft=2, speedRight=2)    
        
    #######################################################                         
    # Navigating the environment using Ultrasonic Sensors##
    #######################################################

    # if World.getSensorReading('ultraSonicSensorLeft') > 0.4 and World.getSensorReading('ultraSonicSensorRight') > 0.4:       
    #     motorSpeed = dict(speedLeft=3, speedRight=3)
    # elif World.getSensorReading('ultraSonicSensorLeft') < 0.4 and World.getSensorReading('ultraSonicSensorRight') > 0.4:
    #     motorSpeed = dict(speedLeft=2, speedRight=-2)
    # elif World.getSensorReading('ultraSonicSensorRight') < 0.4 and World.getSensorReading('ultraSonicSensorLeft') > 0.4:
    #     motorSpeed = dict(speedLeft=-2, speedRight=2)
    # elif World.getSensorReading('ultraSonicSensorLeft') < 0.4 and World.getSensorReading('ultraSonicSensorRight') < 0.4:
    #     speed = randint(1,30)/10
    #     motorSpeed = dict(speedLeft=speed, speedRight=-speed)
        
    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################
    # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)
    # try to collect energy block (will fail if not within range)
    if simulationTime%10000==0:
        print ("Trying to collect a block...",World.collectNearestBlock())
