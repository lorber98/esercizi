import time

l=list(range(100000))
v=list(range(1000))
T1=time.perf_counter()

#print(T1)
#T1_temp=time.perf_counter_ns()
#print(T1_temp)

s=l+v
T2=time.perf_counter()
print(" + execution time: :" , T2-T1, "s")


T3=time.perf_counter()
l.extend(v)
T4=time.perf_counter()
print("extend execution time:", T4-T3 ,"s")
