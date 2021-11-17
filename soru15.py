# -*- coding: utf-8 -*-
"""
Let's assume that the ball dropped from a height of 20m rises less than 10% of the previous one with each ascent. Calculate the distance it takes until it jumps 1 cm.

20m yükseklikten düşen topun her çıkışta bir önceki topun %10'undan daha az yükseldiğini varsayalım. 1 cm zıplayana kadar aldığı mesafeyi hesaplayın.
"""
height=20
hcm=height*100
top=0
b=0
while hcm>1:
    top=b+top
    hcm=hcm*0.9
    b=hcm*2
print("result..: ",top)

