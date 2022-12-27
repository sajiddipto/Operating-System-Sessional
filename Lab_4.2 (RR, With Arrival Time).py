# # With Arrival Time & Taking Time Quantum as 1.
# n = input("Enter the number of processes: ")
# n = int(n)
#
# burstTime = []
# print("Enter the burst time of processes: ")
# for i in range(n):
#     burstTime.append(int(input()))
#
# arrivalTime = []
# print("Enter the arrival time of processes: ")
# for i in range(n):
#     arrivalTime.append(int(input()))
#
# dictionary = dict(zip(burstTime, arrivalTime))
# sortedDictionary = sorted(dictionary.items(), key=lambda x: x[1])
#
# waitingTime = [0] * n
# turnaroundTime = [0] * n
# completionTime = [0] * n
#
# timeQuantum = input("Time quantum: ")
# timeQuantum = int(timeQuantum)
#
# newList = []
# j=0
# while j < n:
#     var = int(list(sortedDictionary[j])[0])
#     newList.append(var)
#     j += 1
# print(newList)
#
# temp = 0
# flag = 0
# while True:
#     for i in range(n):
#         if newList[i] > 0:
#             if newList[i] > timeQuantum:  # if burst time > time quantum *
#                 temp += timeQuantum
#                 newList[i] -= timeQuantum
#             else:
#                 temp += newList[i]
#                 turnaroundTime[i] = temp - arrivalTime[i]
#                 waitingTime[i] = turnaroundTime[i] - burstTime[i]
#                 newList[i] = 0
#     if sum(newList) == 0:
#         break
# print("Process\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
# for i in range(n):
#     print(i + 1, "\t\t\t", burstTime[i], "\t\t\t", arrivalTime[i], "\t\t\t", waitingTime[i], "\t\t\t",
#           turnaroundTime[i])
# print("Average waiting time: ", sum(waitingTime) / n)
# print("Average turnaround time: ", sum(turnaroundTime) / n)
