# MS D G H D G
#http://tinyurl.com/ya36wvlw
u1, u2, r1, r2, r3, r4, r5, r6, r7, r8 = 105., 85., 420., 980., 330., 280., 310., 710., 240., 200.

u = u1 + u2

r12 = (r1*r2)/(r1 + r2)
r78 = (r7*r8)/(r7 + r8)

#print(r12)
#print(r78)

rtr = r4+r5+r6

ra = (r4 * r5) / rtr
rb = (r4 * r6) / rtr
rc = (r5 * r6) / rtr

#print(ra)
#print(rb)
#print(rc)

r12a = r12 + ra
r3b = r3 + rb
r123ab = (r12a*r3b)/(r12a+r3b)

rekv = r123ab + r78 + rc
i = u/rekv

ur123ab = r123ab * i
ir12a = ur123ab / r12a


ur12 = ir12a * r12
ir1 = ur12 / r1
ur1 = ir1 * r1

print(ur1)
