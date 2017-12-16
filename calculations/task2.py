u1, u2, r1, r2, r3, r4 = 180., 250., 315., 615., 180., 460.

r23 = (r2 * r3)/(r2+r3)
print("R23: ", r23)

ri = (r1*r4)/(r1+r4)
print("Ri: ", ri)

ix = (u2-u1)/(r1+r4)
print("Ix: ", ix)

ui = u2 - r4*ix
print("Ui: ", ui)

ir23 = ui/(ri+r23)
print("Ir23: ", ir23)

ur23 = r23*ir23
print("Ur23: ", ur23)


ir3 = (r2/(r2+r3))*ir23
print("Ir3: ", ir3)
ur3 = ir3*r3
print("Ur3: ", ur3)
