#  Implement the moving average for the 1-D array.
babar_scores= [10,50,100,99,50,0,49,100,99,50]

def calculate_avg(arr, time_stamp):
    stop=0
    window_period=[]
    n = len(arr)

    # loop
    for i in range(0,n,time_stamp):
        stop+=time_stamp
        sliced_array = arr[0:stop]
        mean = sum(sliced_array)/len(sliced_array)
        print(f"window btw 0 to {stop}: ",mean )
        window_period.append( mean)
    
    return window_period

days = calculate_avg(babar_scores, 3)
print(days)