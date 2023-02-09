#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from apscheduler.schedulers.background import BackgroundScheduler

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.cda.system.SystemCpuUtilTask import SystemCpuUtilTask
from programmingtheiot.cda.system.SystemMemUtilTask import SystemMemUtilTask

from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData



class SystemPerformanceManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self,listener:IDataMessageListener = None):
		configUtil=ConfigUtil()
		self.pollRate = configUtil.getInteger(section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.POLL_CYCLES_KEY, defaultVal = ConfigConst.DEFAULT_POLL_CYCLES)
		self.locationID = configUtil.getProperty(section = ConfigConst.CONSTRAINED_DEVICE, key = ConfigConst.DEVICE_LOCATION_ID_KEY, defaultVal = ConfigConst.NOT_SET)
		
		if (self.pollRate <= 0):
			self.pollRate = ConfigConst.DEFAULT_POLL_CYCLES
			
		self.dataMsgListener = listener
		
		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self.handleTelemetry, 'interval', seconds = self.pollRate)
	
		self.cpuUtilTask = SystemCpuUtilTask()
		self.memUtilTask = SystemMemUtilTask()

		self._managerRunning = False

	def handleTelemetry(self):
		pass
		
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		self.dataMsgListener = listener
	
	def startManager(self):
		logging.info("Started SystemPerformanceManager.")
		
		if (not self.scheduler.running):
			self.isRunning = True
			self.scheduler.start()
			logging.info("Started SystemPerformanceManager.")
		else:
			logging.warning("SystemPerformanceManager scheduler already started. Ignoring.")
		
	def stopManager(self):
		logging.info("Stopping SystemPerformanceManager.")
		
		try:
			self.scheduler.shutdown()
			self.isRunning = False
			logging.info("Stopped SystemPerformanceManager.")
		except:
			logging.warning("SystemPerformanceManager scheduler already stopped. Ignoring.")

	@property
	def isRunning(self) -> bool:
		return self._managerRunning

	@isRunning.setter
	def isRunning(self,val):
		self._managerRunning = val