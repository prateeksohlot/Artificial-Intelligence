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

global motorSpeed # global variable to store motor speed
motorSpeed = dict(speedLeft= 0 , speedRight=  0 )
#######################################################
# Perception Phase: Get information about environment #
#######################################################

'''
We can observe that the robot is equipped a total of 16 ultrasonic sensors in the robot.
'''
def getObstacleDist(sensorHandler_):
    # Get raw sensor readings using API
    rawSR = World.vrep.simxReadProximitySensor(robot.clientID, sensorHandler_, World.vrep.simx_opmode_oneshot_wait)
    #print(rawSR)
    # Calculate Euclidean distance
    if rawSR[1]: # if true, obstacle is within detection range, return distance to obstacle
        return World.math.sqrt(rawSR[2][0]*rawSR[2][0] + rawSR[2][1]*rawSR[2][1] + rawSR[2][2]*rawSR[2][2])
    else: # if false, obstacle out of detection range, return inf.
        return float('inf')


def sideSensorData():
    _, sensorLeft = World.vrep.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor3',World.vrep.simx_opmode_oneshot_wait)
    _, sensorRight = World.vrep.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor6',World.vrep.simx_opmode_oneshot_wait)
    sensorData = dict(sensorLeft= getObstacleDist(sensorLeft), sensorRight = getObstacleDist(sensorRight) )
    if sensorData["sensorLeft"] == float('inf'):
        sensorData["sensorLeft"] = 1.1
        
    if sensorData["sensorRight"] == float('inf'):
        sensorData["sensorRight"] = 1.1
    return sensorData

def parallelSensorData():
    sensors = []
    for sensorIndex in [8,9,16,1]:
        _, newSensor = World.vrep.simxGetObjectHandle(0, 'Pioneer_p3dx_ultrasonicSensor%s'%(sensorIndex),World.vrep.simx_opmode_oneshot_wait)
        sensors.append(dict(index= sensorIndex, distance= getObstacleDist(newSensor)))    
    if sensors[0]["distance"] == float('inf'):
        sensors[0]["distance"]  = 1.1

    if sensors[1]["distance"]  == float('inf'):
        sensors[1]["distance"]  = 1.1
    
    if sensors[2]["distance"] == float('inf'):
        sensors[2]["distance"]  = 1.1

    if sensors[3]["distance"]  == float('inf'):
        sensors[3]["distance"]  = 1.1
    return sensors

def followWall():
    stopFollowWall = False
    nearestBlockDistance = World.getSensorReading("energySensor").distance
    
    while not stopFollowWall:
        
        updatedBlockDistance = World.getSensorReading("energySensor").distance
        sideSensor = sideSensorData()
        parallelSensor = parallelSensorData()
        print("Side Sensor Data :", sideSensor)
        print("Parallel Sensor :", parallelSensor)


        #remember(8 and 9 are right) and (16 and 1 are left)
        differenceRightParallel = parallelSensor[0]["distance"] - parallelSensor[1]["distance"]
        
        
        # Check if robot should try to go for new block or if robot can pick up plock.
        if (updatedBlockDistance + 0.3 < nearestBlockDistance) or (updatedBlockDistance < 0.5):
            stopFollowWall = True
            break

        # Align so follow wall by using sensor 8 and 9, parallell sensors on the right of the robot
        if ((round(differenceRightParallel,2) < 0) or  (parallelSensor[0]["distance"] >  0.6 and parallelSensor[1]["distance"] > 0.6 and sideSensor["sensorLeft"] > 0.4)) :            
            motorSpeed = dict(speedLeft= 0 , speedRight=  0.1 + (abs(differenceRightParallel) ) ) 
        

        elif round(differenceRightParallel,2 ) > 0 and sideSensor["sensorLeft"] > 0.4 :            
            motorSpeed = dict(speedLeft = 1 +  (differenceRightParallel * 2 ), speedRight=0  ) 

        else:
            motorSpeed = dict(speedLeft= 1 - (1.1-sideSensor["sensorLeft"]) * 2   , speedRight=  1 + (1.1-sideSensor["sensorLeft"]) * 2 )     
        
        World.setMotorSpeeds(motorSpeed)

    
totalBlocks = len(World.findEnergyBlocks())
print("Total blocks:", totalBlocks)
timeStuck = 0


while robot: # main Control loop

    nearestBlockDistance = World.getSensorReading('energySensor').distance
    nearestBlockDirection = World.getSensorReading('energySensor').direction
    sideSensors = sideSensorData()
    parallelSensors = parallelSensorData()  

    #######################################################
    # Perception Phase: Get information about environment #
    #######################################################
    simulationTime = World.getSimulationTime()
    if simulationTime%4000==0:
        # print some useful info, but not too often
        print ('Time:',simulationTime,\
               'ultraSonicSensorLeft:',World.getSensorReading("ultraSonicSensorLeft"),\
               "ultraSonicSensorRight:", World.getSensorReading("ultraSonicSensorRight"))
        directionOfRobot= World.robotDirection() 

        print("Time :", simulationTime)
        print("RobotDirection: %s, BlockDirection: %s, Difference: %s"\
                %(directionOfRobot,nearestBlockDirection,directionOfRobot - nearestBlockDistance))
        print("Side Sensors", sideSensors)
        print("Parallel Sensors", parallelSensors)

    # if nearestBlockDistance < 0.5:
    #     motorSpeed = dict(speedLeft=0, speedRight=0)
    #     World.collectNearestBlock()
    # elif round(nearestBlockDirection,1) <  0:
    #     motorSpeed = dict(speedLeft= nearestBlockDirection/2, speedRight=-nearestBlockDirection/2)
    # elif round(nearestBlockDirection,1) > 0 :
    #     motorSpeed = dict(speedLeft= -nearestBlockDirection/2, speedRight=nearestBlockDirection/2)
    # else:
    #     motorSpeed = dict(speedLeft=2, speedRight=2)    
    
    #Check for getting stuck in wall
    if (World.getSensorReading("ultraSonicSensorLeft") < 0.3) and  (World.getSensorReading("ultraSonicSensorRight")  < 0.3):
        timeStuck += 1
        print(f'Stuck for {timeStuck} cycles')
        if timeStuck == 15:
            followWall()
            timeStuck = 0

    # #Check for picking up blocks
    if nearestBlockDistance < 0.5:        
        motorspeed = dict(speedLeft=0, speedRight=0)
        picked = World.collectNearestBlock()
        if picked == 'Energy collected :)':
            totalBlocks -= 1
            print(f'{totalBlocks} blocks are left')
            picked = ' '

            if totalBlocks == 0:
                print('All blocks collected :)')
                break

    # #Aligning to Nearest Block
    elif round(nearestBlockDirection,1) <  0:
        motorSpeed = dict(speedLeft= nearestBlockDirection , speedRight=-nearestBlockDirection ) 
    elif round(nearestBlockDirection,1) > 0 :
        motorSpeed = dict(speedLeft= nearestBlockDirection , speedRight=-nearestBlockDirection ) 
    else:
        if(sideSensors["sensorLeft"] > 0.2 and sideSensors["sensorRight"] >0.2):
            motorSpeed = dict(speedLeft= 2  , speedRight= 2 ) 
        else:
            motorSpeed = dict(speedLeft= 2 - (2.2 - sideSensors["sensorRight"])  , speedRight= 2 - (2.2 - sideSensors["sensorLeft"]) ) 

    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################   
    World.setMotorSpeeds(motorSpeed)
   
