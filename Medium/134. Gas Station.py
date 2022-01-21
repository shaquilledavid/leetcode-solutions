import pdb

def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    start = 0
    tank = 0
    i = 0
    if len(gas) == 1:
        if gas[0] > cost[0]:
            return 0
        else:
            return -1

    if gas == cost:
        return 0
    #if our gas is lower than the cost to get to the next station then we are stranded
    #if our gas is equal or higher, subtract cost from gas, then add the gas from next station

    while i < len(gas):
        jj = i
        while jj <= len(gas):
            if jj == len(gas):
                if i == 0 and tank >= 0:
                    return i
                elif i == 0 and tank < cost[jj-1]:
                    i += 1
                    tank = 0
                    break
                else:
                    jj = 0 #wrap around

            tank = tank + gas[jj]
            
            if jj == i-1 and tank >= cost[jj]:
                return i
            
            elif tank < cost[jj]:
                i += 1
                tank = 0
                break

            elif tank >= cost[jj]:
                tank = tank - cost[jj]
                jj+=1

    return -1
                
gas = [3,1,1]
cost = [1,2,2]
pdb.set_trace()
canCompleteCircuit(gas, cost)
