def rankTeams(votes):
    """
    :type votes: List[str]
    :rtype: str
    """
    if len(votes) == 1:
        return votes[0]

    ranking = {}
    
    #for every ballot in the votes
    #figure out the value per vote
    #add that value to ranking

    maximum = len(votes[0]) #we will know how much a top vote is worth

    for ballot in votes:
        value = maximum
        i = 0
        while value > 0:
            if ballot[i] not in ranking:
                ranking[ballot[i]] = value
                value -= 1
                i += 1
            else:
                ranking[ballot[i]] += value
                value -= 1
                i += 1

    s = ''
    while len(ranking) > 0:
        max_key = max(ranking, key=ranking.get)
        print(ranking)
        s = s + max_key
        ranking.pop(max_key)

    return s
