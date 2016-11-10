def get_in():
    nHouses, carryCap = map(int, input().split())
    houses = []
    for i in range(nHouses):
        houseLoc, numMails = map(int, input().split())
        houses.append((houseLoc, numMails))
    return (houses, carryCap)
    
def solve(houses, carryCap):
    pass