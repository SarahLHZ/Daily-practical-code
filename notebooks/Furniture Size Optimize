#Test rocking chairs and rugs for size

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as pc
from matplotlib.patches import Ellipse, Circle

fig1 = plt.figure()
ax = fig1.add_subplot(111, aspect = 'equal')
plt.xlim(0, 12)
plt.ylim(0, 12)

ax.add_patch(pc.Rectangle(xy=(2.6, 1.3),    #Lower left corner coordinates
                 width=6.8,
                 height=9.4,
                 fc='steelblue'
                ))

cir1 = Circle(xy = (6.0, 6.0), radius=6, alpha=0.5)   #alpha：Transparency. The closer it is to 0, the more transparent it is, and the closer it is to 1, the more opaque it is.
ax.add_patch(cir1)
