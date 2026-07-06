# Orchestrator independent recomputation for W19-A headline points, from the PRINTED matrices
# in data/worker-report.md only. Checks the ALGEBRAIC side (idempotence, row sums, delta, mass
# placement); the geometric certifications (W, H, distances, sigma_g) remain worker-asserted.
from fractions import Fraction as F
def M(rows): return [[F(x) for x in r] for r in rows]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def delta(P): return max(sum(max(-x,0) for x in r) for r in P)

P=M([["163/168","-11/336","1/336","5/336","5/336","5/336","5/336"],
     ["-5/168","325/336","1/336","5/336","5/336","5/336","5/336"],
     ["-5/168","-11/336","337/336","5/336","5/336","5/336","5/336"],
     ["79/168","869/1680","-79/1680","5/336","5/336","5/336","5/336"],
     ["79/168","869/1680","-79/1680","5/336","5/336","5/336","5/336"],
     ["79/168","869/1680","-79/1680","5/336","5/336","5/336","5/336"],
     ["79/168","869/1680","-79/1680","5/336","5/336","5/336","5/336"]])
assert mm(P,P)==P and all(sum(r)==1 for r in P)
assert delta(P)==F(1,16)
assert sum(P[3][j] for j in range(3,7))==F(5,84)

P5=M([["6409/6400","-69/32000","-1/64","3/16000","-341/16000","3/80"],
      ["3/8000","39977/40000","-1/240","1/20000","-341/60000","1/100"],
      ["3/1280","-23/6400","187/192","1/3200","-341/9600","1/16"],
      ["1/2560","-23/38400","-5/1152","19201/19200","-341/57600","1/96"],
      ["21/6400","-161/32000","-7/192","7/16000","45613/48000","7/80"],
      ["-222027/6400000","1702207/32000000","74009/192000","-74009/16000000","25237069/48000000","5991/80000"]])
assert mm(P5,P5)==P5 and all(sum(r)==1 for r in P5)
assert delta(P5)==F(3983,96000)
assert P5[5][5]==F(5991,80000) and F(5991,80000)<F(1,2)

PB=M([["31023/32000","43/16000","-949/32000","9/200","1/80"],
     ["-457/80000","40017/40000","-377/80000","1/200","1/200"],
     ["-51/1250","303/80000","76661/80000","11/160","1/100"],
     ["23129/50000","-74551/1600000","819923/1600000","961/16000","23/2000"],
     ["7770491/12800000","-20353/640000","4572529/12800000","17831/320000","377/32000"]])
assert mm(PB,PB)==PB and all(sum(r)==1 for r in PB)
assert delta(PB)==F(74551,1600000)
assert PB[3][3]+PB[3][4]==F(229,3200)
print("orchestrator recompute OK: 3 headline matrices (m=4 split, rank-5 record, instance B) algebraic side")
