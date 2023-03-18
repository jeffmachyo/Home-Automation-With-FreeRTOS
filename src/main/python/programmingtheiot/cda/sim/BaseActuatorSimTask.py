#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import random

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.ActuatorData import ActuatorData

class BaseActuatorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, name: str = ConfigConst.NOT_SET, typeID: int = ConfigConst.DEFAULT_ACTUATOR_TYPE, simpleName: str = "Actuator"):
		self.latestActuatorResponse = ActuatorData(typeID = typeID, name = name)
		self.latestActuatorResponse.setAsResponse()
	
		self.name = name
		self.typeID = typeID
		self.simpleName = simpleName
		self.lastKnownCommand = ConfigConst.DEFAULT_COMMAND
		self.lastKnownValue = ConfigConst.DEFAULT_VAL
		
	def getLatestActuatorResponse(self) -> ActuatorData:
		"""
		This can return the current ActuatorData response instance or a copy.
		"""
		pass
	
	def getSimpleName(self) -> str:
		return self.simpleName
	
	def updateActuator(self, data: ActuatorData) -> ActuatorData:
		"""
		NOTE: If 'data' is valid, the actuator-specific work can be delegated
		as follows:
		 - if command is ON: call self._activateActuator()
		 - if command is OFF: call self._deactivateActuator()
		
		Both of these methods will have a generic implementation (logging only) within
		this base class, although the sub-class may override if preferable.
		"""
		if data and self.typeID == data.getTypeID():
			responseCode = ConfigConst.DEFAULT_STATUS

			currentCommand = data.getCommand()
			currentValue = data.getValue()

			if currentCommand == self.lastKnownCommand and currentValue == self.lastKnownValue:
				logging.debug( \
				"New actuator command and value is a repeat. Ignoring: %s %s", \
				str(currentCommand), str(currentValue))
			else:
				logging.debug( \
					"New actuator command and value to be applied: %s %s", \
					str(currentCommand), str(currentValue))
				
				if currentCommand == ConfigConst.COMMAND_ON:
					logging.info("Activating actuator...")
					responseCode = self._activateActuator(val = data.getValue(), stateData = data.getStateData())
				elif currentCommand == ConfigConst.COMMAND_OFF:
					logging.info("Deactivating actuator...")
					responseCode = self._deactivateActuator(val = data.getValue(), stateData = data.getStateData())
				else:
					logging.warning("ActuatorData command is unknown. Ignoring: %s", str(currentCommand))
					responseCode = -1
			
			self.lastKnownCommand = currentCommand
			self.lastKnownValue = currentValue

			actuatorDataInstance = ActuatorData()
			actuatorDataInstance.updateData(data)
			actuatorDataInstance.setStatusCode(responseCode) 
			actuatorDataInstance.setAsResponse()
			self.latestActuatorResponse.updateData(actuatorDataInstance)
			
			return actuatorDataInstance
				
		return None

		
	def _activateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
		"""
		Implement basic logging. Actuator-specific functionality should be implemented by sub-class.
		
		@param val The actuation activation value to process.
		@param stateData The string state data to use in processing the command.
		"""
		msg = "Actuator ON"
		
		logging.info("Simulating %s actuator ON: %s", self.name, msg)
	
		return 0
		
	def _deactivateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
		"""
		Implement basic logging. Actuator-specific functionality should be implemented by sub-class.
		
		@param val The actuation activation value to process.
		@param stateData The string state data to use in processing the command.
		"""
		msg = "Actuator OFF"
		
		logging.info("Simulating %s actuator OFF: %s", self.name, msg)
				
		return 0
		