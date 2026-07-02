#!/usr/bin/env python3
"""Certify the best GENUINE-recipient (dist>=tau/4) invisible-mass instances
   exactly, and the max-H joint.  These are the halo-robust cap-kill candidates."""
from fractions import Fraction as F
from certify import certify

print("################ A) max genuine sigt_g (search4f Sg seed12) ################")
A_C=[[F('-3/80'),F('23/400'),F('5/12'),F('-1/200'),F('341/600')]]
A_R2=[[F('3/80')],[F('1/100')],[F('1/16')],[F('1/96')],[F('7/80')]]
certify(A_C,A_R2,"A: max genuine sigt_g/tau ~0.37, delta~0.041")

print("\n\n################ B) max-H with genuine sigt_g (search4f Ht seed41) ################")
B_C=[[F('1/2'),F('-1/20'),F('11/20')],[F('257/400'),F('-7/200'),F('157/400')]]
B_R2=[[F('9/200'),F('1/80')],[F('1/200'),F('1/200')],[F('11/160'),F('1/100')]]
certify(B_C,B_R2,"B: H/tau~0.46 with genuine sigt_g/tau~0.33, delta~0.047")
