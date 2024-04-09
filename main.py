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


    def ellipse(self):
        return Ellipse(xy=self.xy, width=self.w, height=self.h, color=self.color,  alpha=0.5)
    def rect(self, angle=0):
        return Rectangle(xy=self.xy, width=self.w, height=self.h, color=self.color, angle=angle)

class Person:
    def __init__(self, height, xloc):
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
        self.head = BodyPart(width=head_width, height=head_height, xy=[head_x, head_y], name='self.head')
        self.l_eye = BodyPart(width=self.head.w/4, height=self.head.h/7, xy=[self.head.xy[0] - self.head.w/6, self.head.xy[1] + self.head.h/6], color='black', name='self.l_eye')
        self.r_eye = BodyPart(width=self.head.w/4, height=self.head.h/8, xy=[self.head.xy[0] + self.head.w/6, self.head.xy[1] + self.head.h/6], color='black', name='self.r_eye')
        self.l_ear = BodyPart(width=self.head.w/8, height=self.head.h/4, xy=[self.head.xy[0] - self.head.w/2, self.head.xy[1]], color='black', name='self.r_eye')
        self.r_ear = BodyPart(width=self.head.w/8, height=self.head.h/4, xy=[self.head.xy[0] + self.head.w/2, self.head.xy[1]], color='black', name='self.r_eye')
        self.nose = BodyPart(width=self.l_eye.w/2, height=self.l_eye.h, xy=[self.head.xy[0], self.head.xy[1]], color='black', name='self.mouth')
        self.mouth = BodyPart(width=self.l_eye.w, height=self.l_eye.h, xy=[self.head.xy[0], self.head.xy[1]-self.head.h/4], color='black', name='self.mouth')

        self.body = BodyPart(width=body_w, height=body_h, xy=[self.head.xy[0], self.head.xy[1]-self.head.h/2-body_h/2], name='self.body')

        self.l_thigh = BodyPart(width=thigh_w, height=thigh_h, xy=[self.body.xy[0]-self.body.w/3, self.body.xy[1]-self.body.h/4-thigh_h/2], name='self.l_thigh')
        self.r_thigh = BodyPart(width=thigh_w, height=thigh_h, xy=[self.body.xy[0]+self.body.w/3, self.body.xy[1]-self.body.h/4-thigh_h/2], name='self.r_thigh')

        self.l_leg = BodyPart(width=leg_w, height=leg_h, xy=[self.l_thigh.xy[0], self.l_thigh.xy[1]-self.l_thigh.h/4-leg_h/2], name='self.l_leg')
        self.r_leg = BodyPart(width=leg_w, height=leg_h, xy=[self.r_thigh.xy[0], self.r_thigh.xy[1]-self.r_thigh.h/4-leg_h/2], name='self.r_leg')

        self.l_arm = BodyPart(width=arm_w, height=arm_h, xy=[self.body.xy[0]-arm_w/1.5, self.body.xy[1]+body_h/3], name='self.l_arm')
        self.r_arm = BodyPart(width=arm_w, height=arm_h, xy=[self.body.xy[0]+arm_w/1.5, self.body.xy[1]+body_h/3], name='self.r_arm')

        self.l_forearm = BodyPart(width=fore_arm_w, height=fore_arm_h, xy=[self.l_arm.xy[0]-0.8*fore_arm_w , self.l_arm.xy[1]], name='self.l_arm')
        self.r_forearm = BodyPart(width=fore_arm_w, height=fore_arm_h, xy=[self.r_arm.xy[0]+0.8*fore_arm_w, self.r_arm.xy[1]], name='self.r_arm')


    def plot(self, ax):
        ax.add_patch(self.head.ellipse())
        ax.add_patch(self.l_eye.ellipse())
        ax.add_patch(self.r_eye.ellipse())
        ax.add_patch(self.l_ear.ellipse())
        ax.add_patch(self.r_ear.ellipse())
        ax.add_patch(self.nose.ellipse())
        ax.add_patch(self.mouth.ellipse())
        ax.add_patch(self.body.ellipse())
        ax.add_patch(self.l_thigh.ellipse())
        ax.add_patch(self.r_thigh.ellipse())
        ax.add_patch(self.l_leg.ellipse())
        ax.add_patch(self.r_leg.ellipse())
        ax.add_patch(self.l_arm.ellipse())
        ax.add_patch(self.r_arm.ellipse())
        ax.add_patch(self.l_forearm.ellipse())
        ax.add_patch(self.r_forearm.ellipse())


# plt.figure(figsize=(640,480))
fig, ax = plt.subplots()
# plt.show()

height=0.8
xloc = 0.5
person = Person(height, xloc)
person.plot(ax)
plt.axis('off')
# im_w = 640
# im_h = 640

plt.savefig('foo1.jpeg')
