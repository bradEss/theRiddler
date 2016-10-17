def prob(n,probsBuilderDict):
    '''
       This function determines the probability that you will land
       on space n in the course of the game.

       In order to land on n, then you had to have landed on one of
       the preceeding six spaces in the turn immediately before.

       Basically there are six possibilities:
           Land on space n-6 and roll a 6,
           land on space n-5 and roll a 5,
           land on space n-4 and roll a 4,
           land on space n-3 and roll a 3,
           land on space n-2 and roll a 2,
           land on space n-1 and roll a 1.
           
           i.e land on space n-i and roll an i (where 1<=i<=6)

       So, the probability that you land on n is tied into the probability
       of landing on each of the six preceeding spaces.

       And since each i has a probability of 1/6, then the probability of

       landing on space n-1 and rolling an i is prob(n-1) * 1/6

       This means that prob(n) = Sum (prob(n-i)) * 1/6 for i = 1 to 6

       Put more briefly, prob(n) equals
       the average of prob(n-1) through prob(n-6).
       
       Special case: If a coin is placed on space n-i, then the game ends if
       you land on that.  So we have to remove that probability from our equation
       since it's the impossible to land on n after landing on n-i.

       That is essentially what the builder list is for.  It is the probability of
       landing on each space, except we put a 0 in the builder for all of the coin
       positions.
    '''
    prob = 0
    # print("n:" + str(n))
    for i in range(n-6,n):
        prob += probsBuilderDict[i] * 1/6
        #print("i:" + str(i) + " probsBuilder:" + repr(probsBuilderDict[i]) + " cumulativeProb:" + repr(prob))
    return prob

def allProbs(coins):
    '''
      First thing we will do is create a list to store the "builder" values.
      This builder list is used solely to calculate the probability of the
      following spaces.  Each entry is essentially equal to the respective
      value in the probability list, but it contains a 0 for each coin position,
      since the game ends if you land on a coin.

      Also, to start the builder list, we have to define values for 0 through -5.
      The values for -1 through -5 are obviously 0, since those aren't spaces on
      the board.  And the value for 0 is 1, since the token starts there and is
      therefore a certainty.
    '''
    probsBuilderDict={}
    probsDict={}
    probsBuilderDict[-5]=0
    probsBuilderDict[-4]=0
    probsBuilderDict[-3]=0
    probsBuilderDict[-2]=0
    probsBuilderDict[-1]=0
    probsBuilderDict[0]=1
    
    for n in range(1,1001):
        probsDict[n]=prob(n,probsBuilderDict)
        if coins.count(n) == 1:
            probsBuilderDict[n]=0
            #print(str(n) + " " + repr(probsDict[n]) + " coin")
        else:
            probsBuilderDict[n]=probsDict[n]
            #print(str(n) + " " + repr(probsDict[n]))

    return probsDict

def populate():
    coins = [0,1,2]
    maxProb = 0.0
    maxProbNonConsecutiveCoins = 0.0
    minProb = 1.0

    import datetime
    import time
    print("Start time: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    
    for i in range(1,99):
        coins[0]=i
        for j in range(i+1,100):
            coins[1]=j
            if j // 100 == j/100:
                print("    Round " + str(i) + "." + str(j) + " time: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
            for k in range(j+1,101):
                coins[2]=k
                probsDict = {}
                probsDict=allProbs(coins)

                probsI = probsDict[i]
                probsJ = probsDict[j]
                probsK = probsDict[k]
                
                coinsString = str(i) + "," + str(j) + "," + str(k)                 
                probsString = repr(probsI) + "," + repr(probsJ) + "," + repr(probsK)
                totalProb = probsI + probsJ + probsK

                if totalProb > maxProb:
                    #print("newMax: Coins: (" + coinsString + ") Probs: (" + probsString + ") TotalProb: " + repr(totalProb)) 
                    maxProb = totalProb
                    coinsStringMaxProb = coinsString
                    probsStringMaxProb = probsString
                    totalProbMaxProb = totalProb

                if j-i>1 and k-j>1 and totalProb > maxProbNonConsecutiveCoins:
                    #print("newMaxNonConsecutiveCoins: Coins: (" + coinsString + ") Probs: (" + probsString + ") TotalProb: " + repr(totalProb)) 
                    maxProbNonConsecutiveCoins = totalProb
                    coinsStringMaxProbNonConsecutiveCoins = coinsString
                    probsStringMaxProbNonConsecutiveCoins= probsString
                    totalProbMaxProbNonConsecutiveCoins = totalProb

                if totalProb < minProb:
                    minProb = totalProb
                    coinsStringMinProb = coinsString
                    probsStringMinProb = probsString
                    totalProbMinProb = totalProb

    print("Max Probability: Coins: (" + coinsStringMaxProb + ") Probs: (" + probsStringMaxProb + ") TotalProb: " + repr(totalProbMaxProb)) 
    print("Max Probability w/ non-Consecutive Coins: Coins: (" + coinsStringMaxProbNonConsecutiveCoins + ") Probs: (" + probsStringMaxProbNonConsecutiveCoins + ") TotalProb: " + repr(totalProbMaxProbNonConsecutiveCoins)) 
    print("Min Probability: Coins: (" + coinsStringMinProb + ") Probs: (" + probsStringMinProb + ") TotalProb: " + repr(totalProbMinProb)) 
    print("End time: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    

populate()
