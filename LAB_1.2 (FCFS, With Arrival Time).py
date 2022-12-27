i, j, k, m = 0, 0, 0, 0
burstTimes, turnaroundTimes, waitingTimes, arrivalTimes = [], [], [], []
n = int(input("Enter the number of process: "))

print("Enter burst & arrival times of the processes: ")
while i < n:
    burstTime = int(input())
    burstTimes.append(burstTime)
    arrivalTime = int(input())
    arrivalTimes.append(arrivalTime)
    i += 1

sort = [x for _,x in sorted(zip(arrivalTimes,burstTimes))]
turnaroundTimes.append(burstTimes[0])
temp = burstTimes[0]
while j < n-1:
    temp = temp+burstTimes[j+1]
    turnaroundTimes.append(temp)
    j += 1

while k < n:
    waitingTimes.append(turnaroundTimes[k]-burstTimes[k])
    k += 1

print("P\t\t\tB.T.\t\tT.A.\t\tW.T.")
while m < int(n):
    print("P" + str(m + 1) + "\t\t\t" + str(burstTimes[m]) + "\t\t\t" + str(turnaroundTimes[m]) + "\t\t\t" + str(waitingTimes[m]))
    m += 1

print("\nAverage Burst Time: "+str(sum(burstTimes)/int(n)))
print("Average Turnaround Time: "+str(sum(turnaroundTimes)/int(n)))
print("Average Waiting Time: "+str(sum(waitingTimes)/int(n)))


