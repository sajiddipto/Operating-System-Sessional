# i, j, k, m, p = 0, 0, 0, 0, 0
# burstTimes, turnaroundTimes, waitingTimes, arrivalTimes = [], [], [], []
# n = input("Enter the number of process: ")
# print("Enter arrival times of the processes: ")
# while p < int(n):
#    arrivalTime = input()
#    arrivalTimes.append(int(arrivalTime))
#    p += 1
# print("Enter burst times of the processes: ")
# while i < int(n):
#     burstTime = input()
#     burstTimes.append(int(burstTime))
#     i += 1
#
# dictionary = dict(zip(arrivalTimes, burstTimes))
# sortedDictionary = sorted(dictionary.items(), key=lambda x: x[0])
# print(sortedDictionary)
#
# turnaroundTimes.append(int(burstTimes[0]))
# temp = int(burstTimes[0])
# while j < int(n) - 1:
#     temp = int(temp) + int(burstTimes[j + 1])
#     turnaroundTimes.append(temp)
#     j += 1
#
# while k < int(n):
#     waitingTimes.append(int(turnaroundTimes[k]) - int(burstTimes[k]))
#     k += 1
#
# print("P    " + "B.T.  " + "T.A.  " + "W.T.  ")
# while m < int(n):
#     print("P" + str(m + 1) + "    " + str(burstTimes[m]) + "     " + str(turnaroundTimes[m]) + "    " + str(
#         waitingTimes[m]))
#     m += 1
#
# print("\nAverage Burst Time: " + str(sum(burstTimes) / int(n)))
# print("Average Turnaround Time: " + str(sum(turnaroundTimes) / int(n)))
# print("Average Waiting Time: " + str(sum(waitingTimes) / int(n)))
