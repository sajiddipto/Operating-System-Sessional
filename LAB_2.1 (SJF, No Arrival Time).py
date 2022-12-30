temp = 0
burstTimes, turnaroundTimes, waitingTimes, process = [], [], [], []
n = int(input("Enter the number of process \n"))

for i in range(n):
    print("Enter burst times of the processes "+str(i+1))
    burstTime = int(input())
    burstTimes.append(burstTime)
    process.append("P"+str(i+1))

sortedProcess = [x for _, x in sorted(zip(burstTimes, process))]
burstTimes.sort()
for i in range(n):
    temp = temp + burstTimes[i]
    turnaroundTimes.append(temp)
    waitingTimes.append(turnaroundTimes[i] - burstTimes[i])

print("P\t\t\tB.T.\t\tT.A.\t\tC.T.\t\tW.T.")
for i in range(n):
    print(str(sortedProcess[i]) + "\t\t\t" + str(burstTimes[i]) + "\t\t\t" + str(turnaroundTimes[i]) + "\t\t\t" +str(turnaroundTimes[i]) + "\t\t\t" + str(waitingTimes[i]))

print("\nAverage Turnaround Time: " + str(sum(turnaroundTimes) / int(n)))
print("Average Waiting Time: " + str(sum(waitingTimes) / int(n)))
