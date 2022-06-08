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

# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))
motorSpeed = dict(speedLeft = 0, speedRight = 0) #initally its stationary

#Code to access sensors mwntioned below
def getObstacleDist(sensorHandler_):
        # Get raw sensor readings using API
        rawSR = World.vrep.simxReadProximitySensor( 0 , sensorHandler_, World.vrep.simx_opmode_oneshot_wait)
        #print(rawSR)
        # Calculate Euclidean distance
        if rawSR[1]: # if true, obstacle is within detection range, return distance to obstacle
            return World.math.sqrt(rawSR[2][0]*rawSR[2][0] + rawSR[2][1]*rawSR[2][1] + rawSR[2][2]*rawSR[2][2])
        else: # if false, obstacle out of detection range, return inf.
            return float('inf')

# Code to access sensor3(left),4(front-left),5(front-right),6(right)
def readLeftAndRightSensors():
    ret_s, sensorLeft = World.vrep.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor3',World.vrep.simx_opmode_oneshot_wait)
    ret_s, sensorRight = World.vrep.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor6',World.vrep.simx_opmode_oneshot_wait)
    sensorData = dict(sensorLeft= getObstacleDist(sensorLeft), sensorRight = getObstacleDist(sensorRight) )
    if sensorData["sensorLeft"] == float('inf'):
        sensorData["sensorLeft"] = 1.1
        
    if sensorData["sensorRight"] == float('inf'):
        sensorData["sensorRight"] = 1.1
    return sensorData
def readFrontSensors():
    ret_s, sensorLeft = World.vrep.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor4',World.vrep.simx_opmode_oneshot_wait)
    ret_s, sensorRight = World.vrep.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor5',World.vrep.simx_opmode_oneshot_wait)
    sensorData = dict(sensorLeft= getObstacleDist(sensorLeft), sensorRight = getObstacleDist(sensorRight) )
    if sensorData["sensorLeft"] == float('inf'):
        sensorData["sensorLeft"] = 1.1

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

    directionOfClosestBlock = World.getSensorReading("energySensor").direction
    distanceToCloasestBlock = World.getSensorReading("energySensor").distance
    leftAndRightSensorData = readLeftAndRightSensors()
    frontSensorsLeftAndRight = readFrontSensors()

    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################
    energyBlocksLeft = len(World.findEnergyBlocks())
    


    
   
    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################
    # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)
    # try to collect energy block (will fail if not within range)
    if simulationTime%10000==0:
        print ("Trying to collect a block...",World.collectNearestBlock())
