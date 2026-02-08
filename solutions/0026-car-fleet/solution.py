def car_fleet(target, position, speed):
    # Pair the position and speed, then sort by position in descending order
    cars = sorted(zip(position, speed), reverse=True)
    
    fleets = 0
    time_to_reach = 0
    
    for pos, spd in cars:
        # Calculate the time it takes for the current car to reach the target
        time = (target - pos) / spd
        
        # If the current car takes longer than the last car's time, it forms a new fleet
        if time > time_to_reach:
            fleets += 1
            time_to_reach = time  # Update the time to the current car's time
            
    return fleets