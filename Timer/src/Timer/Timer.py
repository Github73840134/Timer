import time
import _thread
timers = {}
ONE_SHOT = 0
PERIODIC = 1
def timerrunner(tid):
	global timers
	if timers[tid].mode == 0:
		timers[tid].finished = 0xa4
		i = 0
		while i != timers[tid].period:
			time.sleep(0.001)
			if timers[tid].state == 4:
				i = 0
				timers[tid].state = 0
			if timers[tid].state == None:
				timers[tid].finished = 0xaa
				return
			if timers[tid].state == 2:
				timers[tid].finished = 0x02
				i = 0
				timers[tid].period = None
			if timers[tid].state == 1:
				timers[tid].finished = 0xa2
				if i == None:
					i = 0
			if timers[tid].state == 3:
				timers[tid].finished = 0xa2
				while timers[tid].state == 3:
					pass
				timers[tid].finished = 0xa4
			i += 1
		timers[tid].state = None
		timers[tid].finished = 0xff
		if timers[tid].interrupt:
			_thread.interrupt_main()
			timers[tid].callback()
		else:
			timers[tid].callback()
	elif timers[tid].mode == 1:
		while True:
			timers[tid].finished = 0xa4
			i = 0
			while i != timers[tid].period:
				time.sleep(0.001)
				if timers[tid].state == 4:
					i = 0
					timers[tid].state = 0
				if timers[tid].state == None:
					timers[tid].finished = 0xaa
					return
				if timers[tid].state == 2:
					timers[tid].finished = 0xa2
					i = 0
					timers[tid].period = None
				if timers[tid].state == 1:
					timers[tid].finished = 0xa2
					if i == None:
						i = 0
				if timers[tid].state == 3:
					timers[tid].finished = 0xa2
					while timers[tid].state == 3:
						pass
					timers[tid].finished = 0xa4
				i += 1
			timers[tid].finished = 0xff
			if timers[tid].interrupt:
				_thread.interrupt_main()
				timers[tid].callback()
			else:
				timers[tid].callback()

class Timer:
	'''Returns a timer object'''
	ONE_SHOT = 0
	PERIODIC = 1
	NOT_STARTED = 0x02
	RUNNING = 0xa2
	PAUSED = 0xa4
	DUMPED = 0xaa
	FINISHED = 0xff
	class timeratrib(object):
		period = None
		mode = None
		callback = None
		state = None
		interrupt = None
		finished = 0x02
	def __init__(self,tid):
		global timers
		timers[tid] = Timer.timeratrib()
		self.timerdata = timers[tid]
		self.tid = tid
	def init(self,period=0,mode=ONE_SHOT,interrupt=False,callback=None):
		'''Sets the timers deta\n
		period (int): timer length in milliseconds\n
		mode (int): Set the timer mode\n
		Can be the following\n
		- Timer.ONE_SHOT: A timer that only runs once.\n
		- Timer.PERIODIC: A timer that runs forever until de-initalized,dumped,or canceled.\n
		interrupt (bool) (Defaults to false): Whether to interrupt main before executing callback.\n
		callback (object): The function to call whent the timer is finished\n
		'''
		global timers
		self.timerdata.period = period
		self.timerdata.mode = mode
		if callback != None:
			self.timerdata.callback = callback
		else:
			self.timerdata.callback = lambda: exec('pass')
		self.timerdata.state = 0
		self.timerdata.state = interrupt
		timers[self.tid] = self.timerdata
	def start(self):
		'''Starts the timer.'''
		global timers
		timers[self.tid] = self.timerdata
		if self.timerdata.state != 2:
			_thread.start_new_thread(timerrunner,(self.tid,))
	def cancel(self):
		'''Cancels the timer.'''
		global timers
		self.timerdata.state = 2
		timers[self.tid] = self.timerdata
	def pause(self):
		'''Pauses the timer'''
		global timers
		self.timerdata.state = 3
		timers[self.tid] = self.timerdata
	def reset(self):
		'''Resets the timer from 0.'''
		global timers
		self.timerdata.state = 4
		timers[self.tid] = self.timerdata
	def setCallback(self,callback):
		'''Set's the timers callback.'''
		global timers
		self.timerdata.callback = callback
		timers[self.tid] = self.timerdata
	def dump(self):
		'''Kills the timer while keeping its data in memory.'''
		global timers
		self.timerdata.state = None
		timers[self.tid] = self.timerdata
	def deinit(self):
		'''Kills the timer and removes it form memory.'''
		global timers
		self.timerdata.state = None
		timers[self.tid] = self.timerdata
		time.sleep(0.01)
		timers.pop(self.tid)
	def status(self):
		'''Returns the timer status'''
		return timers[self.tid].finished
		
