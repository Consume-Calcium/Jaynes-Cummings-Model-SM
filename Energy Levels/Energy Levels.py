import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.plot([0.5,1.5], [0,0], 'k-')
plt.text(0.8,0.1, r'$|g,0\rangle$')

plt.plot([1.5,2.5], [0.75,0.75], 'k-')
plt.plot([1.5,2.5], [1.25,1.25], 'k-')
plt.plot([0,2], [1,1], 'k--', alpha = 0.3)
plt.plot([2.5,6], [0.75,0.75], 'k--', alpha = 0.3)
plt.plot([2.5,6], [1.25,1.25], 'k--', alpha = 0.3)
plt.text(2,1.35, r'$|e,0\rangle$', ha = 'center')
plt.text(2,0.55, r'$|g,1\rangle$', ha = 'center')
plt.text(6.1, 1, r'$\pm \lambda \hbar$', va = 'center')

plt.plot([2.5,3.5], [1.6,1.6], 'k-')
plt.plot([2.5,3.5], [2.4,2.4], 'k-')
plt.plot([0,3], [2,2], 'k--', alpha = 0.3)
plt.plot([3.5,6], [1.6,1.6], 'k--', alpha = 0.3)
plt.plot([3.5,6], [2.4,2.4], 'k--', alpha = 0.3)
plt.text(3,2.5, r'$|e,1\rangle$', ha = 'center')
plt.text(3,1.4, r'$|g,2\rangle$', ha = 'center')
plt.text(3.8,1.8, 'emission', va = 'center', color = 'blue')
plt.text(1.3,2.2, 'absorption', va = 'center', color = 'orange')
plt.text(6.1, 2, r'$\pm \lambda \hbar \sqrt{2}$', va = 'center')

plt.plot([4,5], [3.5,3.5], 'k-')
plt.plot([4,5], [4.5,4.5], 'k-')
plt.plot([0,4.5], [4, 4], 'k--', alpha = 0.3)
plt.plot([5,6], [3.5,3.5], 'k--', alpha = 0.3)
plt.plot([5,6], [4.5,4.5], 'k--', alpha = 0.3)
plt.text(4.5,4.6, r'$|e,N-1\rangle$', ha = 'center')
plt.text(4.5,3.3, r'$|g,N\rangle$', ha = 'center')
plt.text(6.1, 4, r'$\pm \lambda \hbar \sqrt{N}$', va = 'center')

plt.plot([6, 6], [2.7, 2.7], 'ko', markersize = 2)
plt.plot([6, 6], [2.95, 2.95], 'ko', markersize = 2)
plt.plot([6, 6], [3.2, 3.2], 'ko', markersize = 2)


ax = plt.gca()

arrow1 = FancyArrowPatch((3.5, 2.4), (3.5, 1.6),
                        connectionstyle='arc3,rad=-1',
                        arrowstyle='->', mutation_scale=15, color='blue')

arrow2 = FancyArrowPatch((2.5, 1.6), (2.5, 2.4),
                        connectionstyle='arc3,rad=-1',
                        arrowstyle='->', mutation_scale=15, color='orange')

arrow3 = FancyArrowPatch((6, 0.75), (6, 1.25),
                        connectionstyle='arc3,rad=0',
                        arrowstyle='<->', mutation_scale=15, color='black')

arrow4 = FancyArrowPatch((6, 1.6), (6, 2.4),
                        connectionstyle='arc3,rad=0',
                        arrowstyle='<->', mutation_scale=15, color='black')

arrow5 = FancyArrowPatch((6, 3.5), (6, 4.5),
                        connectionstyle='arc3,rad=0',
                        arrowstyle='<->', mutation_scale=15, color='black')

ax.add_patch(arrow1)
ax.add_patch(arrow2)
ax.add_patch(arrow3)
ax.add_patch(arrow4)
ax.add_patch(arrow5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylabel(r'Energy / $\hbar \omega$')
ax.set_xlabel('Number of quanta')
ax.set_yticks([0, 1, 2, 4], [r'$-\frac{1}{2}$', r'$\frac{1}{2}$', r'$\frac{3}{2}$', r'$N-\frac{1}{2}$'])
ax.set_xticks([1, 2, 3, 4.5], [0, 1, 2, "N"])
ax.set_xlim([0.5, 6.5])

plt.show()