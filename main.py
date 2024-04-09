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



height=0.8
loc_x = 0.5
head_width=height/7 # 80/640
head_height=height/7 # 60/640
head_x=loc_x
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



head = BodyPart(width=head_width, height=head_height, xy=[head_x, head_y], name='head')
l_eye = BodyPart(width=head.w/4, height=head.h/7, xy=[head.xy[0] - head.w/6, head.xy[1] + head.h/6], color='black', name='l_eye')
r_eye = BodyPart(width=head.w/4, height=head.h/8, xy=[head.xy[0] + head.w/6, head.xy[1] + head.h/6], color='black', name='r_eye')
l_ear = BodyPart(width=head.w/8, height=head.h/4, xy=[head.xy[0] - head.w/2, head.xy[1]], color='black', name='r_eye')
r_ear = BodyPart(width=head.w/8, height=head.h/4, xy=[head.xy[0] + head.w/2, head.xy[1]], color='black', name='r_eye')
nose = BodyPart(width=l_eye.w/2, height=l_eye.h, xy=[head.xy[0], head.xy[1]], color='black', name='mouth')
mouth = BodyPart(width=l_eye.w, height=l_eye.h, xy=[head.xy[0], head.xy[1]-head.h/4], color='black', name='mouth')

body = BodyPart(width=body_w, height=body_h, xy=[head.xy[0], head.xy[1]-head.h/2-body_h/2], name='body')

l_thigh = BodyPart(width=thigh_w, height=thigh_h, xy=[body.xy[0]-body.w/3, body.xy[1]-body.h/4-thigh_h/2], name='l_thigh')
r_thigh = BodyPart(width=thigh_w, height=thigh_h, xy=[body.xy[0]+body.w/3, body.xy[1]-body.h/4-thigh_h/2], name='r_thigh')


l_leg = BodyPart(width=leg_w, height=leg_h, xy=[l_thigh.xy[0], l_thigh.xy[1]-l_thigh.h/4-leg_h/2], name='l_leg')
r_leg = BodyPart(width=leg_w, height=leg_h, xy=[r_thigh.xy[0], r_thigh.xy[1]-r_thigh.h/4-leg_h/2], name='r_leg')



l_arm = BodyPart(width=arm_w, height=arm_h, xy=[body.xy[0]-arm_w/1.5, body.xy[1]+body_h/3], name='l_arm')
r_arm = BodyPart(width=arm_w, height=arm_h, xy=[body.xy[0]+arm_w/1.5, body.xy[1]+body_h/3], name='r_arm')


l_forearm = BodyPart(width=fore_arm_w, height=fore_arm_h, xy=[l_arm.xy[0]-0.8*fore_arm_w , l_arm.xy[1]], name='l_arm')
r_forearm = BodyPart(width=fore_arm_w, height=fore_arm_h, xy=[r_arm.xy[0]+0.8*fore_arm_w, r_arm.xy[1]], name='r_arm')



im_w = 640
im_h = 640

fig, ax = plt.subplots()
# ax.set(xlim=(0,im_w), ylim=(0, im_h), aspect="equal")
yy=head.ellipse()
yy.angle=90
ax.add_patch(yy)
ax.add_patch(l_eye.ellipse())
ax.add_patch(r_eye.ellipse())

ax.add_patch(l_ear.ellipse())
ax.add_patch(r_ear.ellipse())

ax.add_patch(nose.ellipse())

ax.add_patch(mouth.ellipse())
ax.add_patch(body.ellipse())
ax.add_patch(l_thigh.ellipse())
ax.add_patch(r_thigh.ellipse())
ax.add_patch(l_leg.ellipse())
ax.add_patch(r_leg.ellipse())

ax.add_patch(l_arm.ellipse())
ax.add_patch(r_arm.ellipse())
# ax.add_patch(l_forearm.rect(90))
# ax.add_patch(r_forearm.rect(-90)) # -130:
ax.add_patch(l_forearm.ellipse())
ax.add_patch(r_forearm.ellipse())


plt.axis('off')
# plt.figure(figsize=(640,480))

# plt.show()
plt.savefig('foo.jpeg')
