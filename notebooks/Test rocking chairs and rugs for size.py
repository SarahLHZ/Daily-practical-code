#Test rocking chairs and rugs for size

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pc
from matplotlib.patches import Ellipse, Circle

fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')
plt.xlim(0, 12)
plt.ylim(0, 12)

ax.add_patch(pc.Rectangle(xy=(2.6, 1.3),    # 左下角坐标
                 width=6.8,
                 height=9.4,
                 fc='steelblue'
                ))

cir1 = Circle(xy = (6.0, 6.0), radius=6, alpha=0.5)   #alpha：透明度。越接近0越透明，越接近1越不透明。
ax.add_patch(cir1)
