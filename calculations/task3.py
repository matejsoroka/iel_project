# H
import numpy as np

def changeCol(matrix, col, mi):

    for i in [0,1,2]:
        matrix[i][col] = mi[i]

    return matrix

u, i1, i2 = 130., 0.95, 0.5
r1, r2, r3, r4, r5 = 47., 39., 58., 28., 25.
i3 = u / r2
g1, g2, g3, g4, g5 = 1/r1, 1/r2, 1/r3, 1/r4, 1/r5

m = np.array([ [g1 + g2 + g3, -g2 - g3, 0], [-g2 - g3, g2 + g3 + g5, -g5], [0, -g5, g4 + g5] ])
mi = [i1 + i3, -i3, i2]

mdet = np.linalg.det(m)

ma = m.copy()
ma = changeCol(ma, 0, mi)
madet = np.linalg.det(ma)

mb = m.copy()
mb = changeCol(mb, 1, mi)
mbdet = np.linalg.det(mb)

mc = m.copy()
mc = changeCol(mc, 2, mi)
mcdet = np.linalg.det(mc)

ua = madet / mdet
ub = mbdet / mdet
uc = mcdet / mdet

print("Ua:", ua)
print("Ub:", ub)
print("Uc:", uc)
ur4 = uc
ur5 = uc - ub

ir5 = ur5 / r5

print("Ur5", ur5)
print("Ir5", ir5)
