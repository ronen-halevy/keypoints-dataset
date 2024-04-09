import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

import numpy as np


from matplotlib.patches import Ellipse

class BodyPart:
    def __init__(self, width, height, xy, color='blue', name=''):
        self.name=name
        self.w =width
        self.h =height
        self.xy=xy
        self.color=color


    def ellipse(self, alpha=0.5):
        return Ellipse(xy=self.xy, width=self.w, height=self.h, color=self.color,  alpha=alpha)
    def rect(self, angle=0):
        return Rectangle(xy=self.xy, width=self.w, height=self.h, color=self.color, angle=angle)

class Person:
    def __init__(self, height, xloc, color):
        head_width=height/7 # 80/640
        head_height=height/7 # 60/640
        head_x=xloc
        head_y=height
        body_h=3*head_height
        body_w=1.2*head_width
        thigh_w=0.5*head_width
        thigh_h=2*head_height
        leg_w=0.5*head_width
        leg_h=2*head_height
        arm_h=0.5*head_width
        arm_w=1.2*head_width
        fore_arm_w=1.2*head_width
        fore_arm_h=0.4*head_width
        self.patches=[]
        self.head = BodyPart(width=head_width, height=head_height, xy=[head_x, head_y], name='self.head')
        self.patches.append(self.head.ellipse())
        leye_c = [self.head.xy[0] - self.head.w/6, self.head.xy[1] + self.head.h/6]
        self.l_eye = BodyPart(width=self.head.w/4, height=self.head.h/7, xy=leye_c, color='black', name='self.l_eye')
        self.patches.append(self.l_eye.ellipse())
        reye_c=[self.head.xy[0] + self.head.w/6, self.head.xy[1] + self.head.h/6]
        self.r_eye = BodyPart(width=self.head.w/4, height=self.head.h/8, xy=reye_c, color='black', name='self.r_eye')
        self.patches.append(self.r_eye.ellipse())
        lear_c=[self.head.xy[0] - self.head.w/2, self.head.xy[1]]
        self.l_ear = BodyPart(width=self.head.w/8, height=self.head.h/4, xy=lear_c, color='black', name='self.r_eye')
        self.patches.append(self.l_ear.ellipse())
        rear_c = [self.head.xy[0] + self.head.w/2, self.head.xy[1]]
        self.r_ear = BodyPart(width=self.head.w/8, height=self.head.h/4, xy=rear_c, color='black', name='self.r_eye')
        self.patches.append(self.r_ear.ellipse())

        self.nose = BodyPart(width=self.l_eye.w/2, height=self.l_eye.h, xy=[self.head.xy[0], self.head.xy[1]], color='black', name='self.mouth')
        self.patches.append(self.nose.ellipse())

        self.mouth = BodyPart(width=self.l_eye.w, height=self.l_eye.h, xy=[self.head.xy[0], self.head.xy[1]-self.head.h/4], color='black', name='self.mouth')
        self.patches.append(self.mouth.ellipse())

        body_c = [self.head.xy[0], self.head.xy[1]-self.head.h/2-body_h/2]
        self.body = BodyPart(width=body_w, height=body_h, xy=body_c, color=color, name='self.body')
        self.patches.append(self.body.ellipse())

        lthigh_c = [self.body.xy[0]-self.body.w/3, self.body.xy[1]-self.body.h/4-thigh_h/2]
        self.l_thigh = BodyPart(width=thigh_w, height=thigh_h, xy=lthigh_c, color=color, name='self.l_thigh')
        self.patches.append(self.l_thigh.ellipse())

        rthigh_c = [self.body.xy[0]+self.body.w/3, self.body.xy[1]-self.body.h/4-thigh_h/2]
        self.r_thigh = BodyPart(width=thigh_w, height=thigh_h, xy=rthigh_c, color=color, name='self.r_thigh')
        self.patches.append(self.r_thigh.ellipse())

        lleg_c = [self.l_thigh.xy[0], self.l_thigh.xy[1]-self.l_thigh.h/4-leg_h/2]
        self.l_leg = BodyPart(width=leg_w, height=leg_h, xy=lleg_c, color=color, name='self.l_leg')
        self.patches.append(self.l_leg.ellipse())

        rleg_c=[self.r_thigh.xy[0], self.r_thigh.xy[1]-self.r_thigh.h/4-leg_h/2]
        self.r_leg = BodyPart(width=leg_w, height=leg_h, xy=rleg_c, color=color, name='self.r_leg')
        self.patches.append(self.r_leg.ellipse())

        larm_c = [self.body.xy[0]-arm_w/1.5, self.body.xy[1]+body_h/3]
        self.l_arm = BodyPart(width=arm_w, height=arm_h, xy=larm_c, color=color, name='self.l_arm')
        self.patches.append(self.l_arm.ellipse())

        rarm_c = [self.body.xy[0]+arm_w/1.5, self.body.xy[1]+body_h/3]
        self.r_arm = BodyPart(width=arm_w, height=arm_h, xy=rarm_c, color=color, name='self.r_arm')
        self.patches.append(self.r_arm.ellipse())

        lforearm_c = [self.l_arm.xy[0]-0.8*fore_arm_w , self.l_arm.xy[1]]
        self.l_forearm = BodyPart(width=fore_arm_w, height=fore_arm_h, xy=lforearm_c, color=color, name='self.l_arm')
        self.patches.append(self.l_forearm.ellipse())

        rforearm_c=[self.r_arm.xy[0]+0.8*fore_arm_w, self.r_arm.xy[1]]
        self.r_forearm = BodyPart(width=fore_arm_w, height=fore_arm_h, xy=rforearm_c, color=color, name='self.r_arm')
        self.patches.append(self.r_forearm.ellipse())

        # find keypoints by solving ellipse intersections equations:
        lshouder=self.ellipse_eq(body_c, body_w,body_h, larm_c, arm_w,arm_h)[0] # body and right arm
        rshouder=self.ellipse_eq(body_c, body_w,body_h, rarm_c, arm_w,arm_h)[0] # body and right arm

        lelbow=self.ellipse_eq(larm_c, arm_w,arm_h, lforearm_c, fore_arm_w,fore_arm_h)[0] # body and right arm
        relbow=self.ellipse_eq(rarm_c, arm_w,arm_h, rforearm_c, fore_arm_w,fore_arm_h)[0] # body and right arm

        lhip=self.ellipse_eq(body_c, body_w,body_h, lthigh_c, thigh_w,thigh_h)[0] # body and right arm
        rhip=self.ellipse_eq(body_c, body_w,body_h, rthigh_c, thigh_w,thigh_h)[0] # body and right arm

        lknee = self.ellipse_eq(lthigh_c, thigh_w, thigh_h, lleg_c , leg_w, leg_h)[0]  # body and right arm
        rknee = self.ellipse_eq(rthigh_c, thigh_w, thigh_h, rleg_c , leg_w, leg_h)[0]  # body and right arm


        # temp for horiz:
        lforearm_c = self.l_forearm.ellipse().get_center()
        l_wrist = [lforearm_c[0]-fore_arm_w/2, lforearm_c[1]]

        rforearm_c = self.r_forearm.ellipse().get_center()
        r_wrist = [rforearm_c[0]+fore_arm_w/2, rforearm_c[1]]


        lankle = [lleg_c[0]-leg_h/2, lleg_c[1]]

        rankle = [rleg_c[0]-leg_h/2, rleg_c[1]]





        # p1 = BodyPart(width=0.01, height=0.01, xy=lshouder[0], color='black', name='self.l_arm')
        # self.patches.append(p1.ellipse())
        # p1 = BodyPart(width=0.01, height=0.01, xy=lshouder[1], color='black', name='self.l_arm')
        # self.patches.append(p1.ellipse())

        keypoints = {'nose':self.head.xy[0],
                     'left-eye': leye_c,
                     'right-eye':reye_c,
                     'left-ear': lear_c,
                     'right-ear': rear_c,
                     'left-shoulder':lshouder,
                     'right-shoulder': rshouder,
                    'left-elbow':lelbow,
                    'right-elbow':relbow,
                    'left-wrist':l_wrist,
                    'right-wrist':r_wrist,
                    'left-hip':lhip,
                    'right-hip':rhip,
                    'left-knee':lknee,
                    'right-knee':rknee,
                    'left-ankle':lankle,
                    'right-ankle':rankle
        }

    def ellipse_eq(self, xy_c1, w1,h1, xy_c2, w2,h2):
            x1, y1 = xy_c1
            x2, y2 = xy_c2
            import sympy as sym
            x, y = sym.symbols('x,y')
            Eq1 = sym.Eq((x-x1)**2/((w1/2)**2) + (y-y1)**2/((h1/2)**2),1)
            Eq2 = sym.Eq((x-x2)**2/((w2/2)**2) + (y-y2)**2/((h2/2)**2),1)
            sol = sym.solve([Eq1,Eq2],(x,y))
            x, y = sol[0]
            dd= (x - x1) ** 2 / ((h1 ) ** 2) + (y - y1) ** 2 / ((w1 ) ** 2)
            cc = (x-x2)**2/((h2/2)**2) + (y-y2)**2/((w2/2)**2)
            return sol




height=0.8
xloc = 0.5
person = Person(height, xloc, color='blue')

from matplotlib.collections import PatchCollection
collection = PatchCollection(person.patches, cmap=plt.cm.hsv, alpha=0.3, match_original=True)
# collection.set_array(np.array(colors))
fig, ax = plt.subplots()
ax.add_collection(collection)
# plt.plot(person.sol[0], [person.sol[1][1], person.sol[1][0]], 'r*')

plt.show()


plt.savefig('foo1.jpeg')
