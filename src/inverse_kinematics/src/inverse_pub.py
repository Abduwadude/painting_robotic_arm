import math
from spatialmath.base import *
from spatialmath import SE3
import spatialmath.base.symbolic as sym
import numpy as np
import roboticstoolbox as rtb
import rospy

#custom robot kinematics solving

## Creating Robotic arm through defining links and Serial Linkage
Link_1=rtb.DHLink(1.24, -math.pi/2, 0, 0)
Link_2=rtb.DHLink(0,    0,   0, 2.7)
Link_3=rtb.DHLink(0,    -math.pi/2,   0, 0.7)
Link_4=rtb.DHLink(3.02, -math.pi/2, 0, 0)
Link_5=rtb.DHLink(0, math.pi/2, 0, 0)
Link_6=rtb.DHLink(0.72, 0, 0, 0)
irb_robot= rtb.DHRobot([Link_1, Link_2, Link_3, Link_4, Link_5, Link_6])
irb_robot


#inverse kinematics solving

# Selection a point to get inverse kinematics solution as angles
print("point-> x: %2.2f ,y: %2.2f ,z: %2.2f" %(1.5,2.5,2.3) )
point = SE3( 0.4453 , 0.5307 , 0.9  )
point_sol = irb_robot.ikine_LM(point)
print(point_sol)
