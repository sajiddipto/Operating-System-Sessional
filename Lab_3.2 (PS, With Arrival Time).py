# #With Arrival Time
# i, j, k, m, p, q, r = 0, 0, 0, 0, 0, 0, 0
# process, burstTimes, turnaroundTimes, waitingTimes, arrivalTimes, priorities = [], [], [], [], [], []
# n = input("Enter the number of process: ")
# while p < int(n): #Process Loop
#     process.append("P"+str(p+1))
#     p += 1
# print("Enter burst times of the processes: ")
# while i < int(n): #Burst Time Loop
#     burstTime = input()
#     burstTimes.append(int(burstTime))
#     i += 1
# print("Enter arrival times of the processes: ")
# while r < int(n): #Arrival Time Loop
#     arrivalTime = input()
#     arrivalTimes.append(int(arrivalTime))
#     r += 1
# print("Enter the priorities of the processes: ")
# while q < int(n): #Priority Loop
#     priority = input()
#     priorities.append(int(priority))
#     q += 1
#
# dictionary = dict(zip(burstTimes, arrivalTimes))
# sortedDictionary0 = sorted(dictionary.items(), key=lambda x: x[1])
# print(sortedDictionary0)
#
# dictionary = dict(zip(burstTimes, priorities))
# sortedDictionary1 = sorted(dictionary.items(), key=lambda x: x[1])
# print(sortedDictionary1)
#
# dictionary = dict(zip(process, priorities))
# sortedDictionary2 = sorted(dictionary.items(), key=lambda x: x[1])
# print(sortedDictionary2)
#
# priorities.sort()
# print(priorities)
#
# turnaroundTimes.append(int(list(sortedDictionary0[0])[0]))
# print(list(sortedDictionary0[0])[0])
# temp = int(list(sortedDictionary0[0])[0])
# print(temp)
#
# while j < int(n) - 1:
#     temp = int(temp) + int(list(sortedDictionary1[j+1])[0])
#     print(temp)
#     turnaroundTimes.append(temp)
#     j += 1
# print(turnaroundTimes)
#
# while k < int(n):
#     waitingTimes.append(int(turnaroundTimes[k]) - int(list(sortedDictionary1[k])[0]))
#     k += 1
#
# print("P    " +"Priority    " + "B.T.   " + "T.A.   " + "W.T.   ")
# while m < int(n):
#     print(str(list(sortedDictionary2[m])[0])+"    "+ str(priorities[m])+"         " +str(list(sortedDictionary1[m])[0])+ "      " + str(turnaroundTimes[m]) + "      " + str(waitingTimes[m]))
#     m += 1
#
# print("Average Turnaround Time: " + str(sum(turnaroundTimes) / int(n)))
# print("Average Waiting Time: " + str(sum(waitingTimes) / int(n)))
