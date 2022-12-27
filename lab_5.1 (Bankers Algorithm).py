processNumber = int(input("Enter the number of processes: "))
resourceNumber = int(input("Enter the number of resources: "))

def calculateNeed(need, maximum, allocated):
    for i in range(processNumber):
        for j in range(resourceNumber):
            need[i][j] = maximum[i][j] - allocated[i][j]

def isSafe(available, maximum, allocated):
    need = []
    for i in range(processNumber):
        l = []
        for j in range(resourceNumber):
            l.append(0)
        need.append(l)

    calculateNeed(need, maximum, allocated)
    finish = [0] * processNumber
    safeSeq = [0] * processNumber
    work = [0] * resourceNumber
    
    for i in range(resourceNumber):
        work[i] = available[i]

    count = 0
    while (count < processNumber):
        found = False
        for p in range(processNumber):
            if (finish[p] == 0):

                for j in range(resourceNumber):
                    if (need[p][j] > work[j]):
                        break

                if (j == resourceNumber - 1):

                    for k in range(resourceNumber):
                        work[k] += allocated[p][k]

                    safeSeq[count] = p
                    count += 1
                    finish[p] = 1
                    found = True

        if (found == False):
            print("\nSystem is not in safe state")
            return False

    print("\nSystem is in safe state.",
          "\nSafe sequence is: ", end=" ")
    print(*safeSeq)

    return True


# Driver code
if __name__ == "__main__":
    
    print("\nEnter the resource allocations of each process: ")
    allocated = []
    for i in range(processNumber):
        al = []
        print("\nFor P"+str(i))
        for j in range(resourceNumber):
            al.append(int(input()))
        allocated.append(al)
    
    print("\nEnter the maximum resources of each process: ")
    maximum = []
    for i in range(processNumber):
        mx = []
        print("\nFor P"+str(i))
        for j in range(resourceNumber):
            mx.append(int(input()))
        maximum.append(mx)
    
    print("\nEnter the available resources of each process: ")
    available = []
    for i in range(resourceNumber):
        av = int(input())
        available.append(av)

    isSafe(available, maximum, allocated)
