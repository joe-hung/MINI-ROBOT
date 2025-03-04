import math
import matplotlib.pyplot as plt
import numpy as np

start_time = 0 # sec
end_time = 30 # sec
control_period_ = 0.001 # s
freq_n = 0.25 # hz
amplitude = 50 # mm
PI = math.pi

def sine_wave_input():
    """
    TODO: Implement sine wave signal with a natural frequency (freq_n) 
            of 0.25hz sampled every 0.001 sec (control_period_).
    """
    global start_time
    global end_time 
    global control_period_
    global freq_n
    global amplitude
    global PI
    
    wave_signal = []
    
    # print(int((end_time-start_time)/control_period_))
    
    for i in range(int((end_time-start_time)/control_period_)):
        y = amplitude*math.sin(2*PI*freq_n*control_period_*i) 
        wave_signal.append(y)
    return wave_signal

def triangle_wave_input(): 
    """
    TODO: Implement triangle wave signal with a natural frequency (freq_n) 
            of 0.25hz sampled every 0.001 sec (control_period_).
    """
    global start_time
    global end_time 
    global control_period_
    global freq_n
    global amplitude

    wave_signal = []
    
    # print(int((end_time-start_time)/control_period_))


    for i in range(int((end_time-start_time)/control_period_)):
        t = (2*PI*freq_n*control_period_*i) % (2*PI)
        if t <= PI/2 :
            y = amplitude*t/(PI/2)
        elif t >= 3*PI/2 :
            y = amplitude*(t-2*PI)/(PI/2)
        else:
            y = amplitude - amplitude*(t-PI/2)/(PI/2)
        wave_signal.append(y)
    return wave_signal

if __name__ == '__main__':
    
    sine = sine_wave_input()
    tri = triangle_wave_input()
    t = []
    for i in range(int((end_time-start_time)/control_period_)):
        t.append(i*control_period_)
        
    fig, ax = plt.subplots()
    ax.axhline(y=50, color="black", linestyle="--")
    ax.axhline(y=0, color="black", linestyle=":")
    ax.axhline(y=-50, color="black", linestyle="--")
    ax.plot(t, sine, linewidth=2, label="sine wave")
    ax.plot(t, tri, linewidth=2, label="triangle wave")
    ax.set(xlim=(start_time, end_time), xlabel="t (s)", ylabel="amplitude (mm)")
    ax.legend(fontsize=14)
    plt.show()
    