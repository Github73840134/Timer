# Timer
Version 1.0
## Description
Timer is module ported from micropython's ```machine.Timer``` and adapted to work with Python

## Timer(tid)
Returns a timer object with the folowing functions
### init(period,mode,interrupt,callback)
Sets the timers data  
#### period (int): 
timer length in milliseconds.  
#### mode (var):
Can be the folowing  
- ```Timer.ONE_SHOT```: A timer that only runs once
- ```Timer.PERIODIC```: A timer that runs forever until deinitalized
#### interrupt (bool)
*Defaults to ```False```*  
Whether to interupt main before executing callback  
#### callback (object)
The function to call when the timer is finished.
### cancel()
Cancels the timer and waits to be re-initalized
### start()
Starts the timer
### pause()
Pauses the timer
### reset()
Restarts the timer from 0
### deinit()
Kills the timer and removes it form memory.
### dump()
Kills the timer while keeping its data in memory.
### setCallback(callback)
Set's the timers callback.
#### callback (object)
The function to call when the timer is finished.
### status()
Returns the timer status
## Constants
- ```Timer.ONE_SHOT```: A timer that only runs once
- ```Timer.PERIODIC```: A timer that runs forever until deinitalized
- ```Timer.NOT_RUNNING```: The timer is not started
- ```Timer.PAUSED```: The timer is paused
- ```Timer.FINISHED```: The timer is finished
- ```Timer.DUMPED```:The timer was dumped
