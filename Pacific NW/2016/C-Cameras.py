def get_problem():
    # First line contains n, k, and r:
    numHouses, numCameras, distance = map(int, input().split())
    # houses: 0 if no camera at a house, 1 if camera:
    houses = [0 for house in range(numHouses)]
    # Next numCameras lines contain locations of the existing cameras:
    for i in range(numCameras):
        camLocation = int(input().strip())
        # This location is 1-indexed, but we need 0-indexed, so subtract 1:
        houses[camLocation - 1] = 1
    return (numHouses, houses, distance)
    
def solve_problem(numHouses, houses, distance):
    """
    Strategy: Every set of "distance" consecutive houses must have cameras.
    First we look at the left-most set (house[0] through house[distance - 1]).
    If this set doesn't have enough cameras, we should add a camera to the
    right side of the set. (If we put a camera on the left side, it can only
    help complete this specific set, whereas if we put it on the right side,
    it may help cover another set somewhere farther to the right.)
    
    Next, we look at the set one house to the right, and the rule to put
    new cameras on the right side still applies, because we know every set
    to the left already has enough cameras, but sets to the right might not
    have enough yet.
    """
    start = 0
    end = distance - 1
    curCameras = sum(houses[start:end+1]) # Number of cameras in current set
    camsAdded = 0 # Number of cameras that we have added
    
    # Add a "dummy" house at the end so we don't get an index out of range
    # error after finishing the last set (this won't change the problem):
    houses.append(0)
    
    while (end < numHouses):
        # Fix current set:
        while curCameras < 2:
            if houses[end] == 0:
                houses[end] = 1
            else:
                houses[end-1] = 1
            curCameras += 1
            camsAdded += 1
        # Advance to next set:
        if houses[start] == 1:
            curCameras -= 1
        start += 1
        end += 1
        if houses[end] == 1:
            curCameras += 1
    print(camsAdded)

# You wouldn't want to waste time doing the following in an actual contest:
def main():
    solve_problem(*get_problem())
    
if __name__ == "__main__":
    main()