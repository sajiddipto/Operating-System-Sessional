temp = 0
flag = 0
burstTime, waitingTime, turnaroundTime, completionTime = [], [], [], []
n = int(input("Enter the number of processes: "))
timeQuantum = int(input("Time quantum: "))

print("Enter the burst time of processes: ")
for i in range(n):
    burstTime.append(int(input()))

newList = burstTime[:]
while True:
    for i in range(n):
        if newList[i] > 0:
            if newList[i] > timeQuantum:
                temp += timeQuantum
                newList[i] -= timeQuantum
            else:
                temp += newList[i]
                turnaroundTime[i] = temp
                waitingTime[i] = turnaroundTime[i] - burstTime[i]
                newList[i] = 0
    if sum(newList) == 0:
        break
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(i + 1, "\t\t\t", burstTime[i], "\t\t\t", waitingTime[i], "\t\t\t", turnaroundTime[i])
print("Average waiting time: ", sum(waitingTime) / n)
print("Average turnaround time: ", sum(turnaroundTime) / n)
