temp = 0
burstTimes, turnaroundTimes, waitingTimes, arrivalTimes, completionTimes, process = [], [], [], [], [], []
n = int(input("Enter the number of process \n"))

for i in range(n):
    print("Enter burst time of the process " + str(i + 1))
    burstTime = int(input())
    burstTimes.append(burstTime)
    print("Enter arrival time of the process " + str(i + 1))
    arrivalTime = int(input())
    arrivalTimes.append(arrivalTime)
    process.append("P"+str(i+1))

sortedBurst = [x for _, x in sorted(zip(arrivalTimes, burstTimes))]
sortedProcess = [x for _, x in sorted(zip(arrivalTimes, process))]
arrivalTimes.sort()
for i in range(n):
    temp = temp + sortedBurst[i]
    completionTimes.append(temp)
    turnaroundTimes.append(completionTimes[i] - arrivalTimes[i])
    waitingTimes.append(turnaroundTimes[i] - sortedBurst[i])

print("P\t\t\tA.T.\t\tB.T.\t\tT.A.\t\tC.T.\t\tW.T.")
for i in range(n):
    print(str(sortedProcess[i]) + "\t\t\t" + str(arrivalTimes[i]) + "\t\t\t" + str(sortedBurst[i]) + "\t\t\t" + str(turnaroundTimes[i]) + "\t\t\t" + str(completionTimes[i]) +"\t\t\t" + str(waitingTimes[i]))

print("\nAverage Turnaround Time: " + str(sum(turnaroundTimes) / int(n)))
print("Average Waiting Time: " + str(sum(waitingTimes) / int(n)))



