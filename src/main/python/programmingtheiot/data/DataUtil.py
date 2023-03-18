#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# 
import json
import logging

from decimal import Decimal
from json import JSONEncoder

from programmingtheiot.data import BaseIotData
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DataUtil():
	"""
	This class is used to facilitate the conversion of CDA data to JSON
	objects and vice-versa
	
	"""

	def __init__(self, encodeToUtf8 = False):
		self.encodeToUtf8 = encodeToUtf8
		logging.info("Created DataUtil instance.")
	
	def actuatorDataToJson(self, data: ActuatorData = None)-> json:
		"""
		Returns the converted actuator data json to the caller.
		
		@return json object
		"""
		if (data is not None):
			jsonData = json.dumps(data, indent = 4, cls = JsonDataEncoder)
			return jsonData
		else:
			logging.debug("No actuator data present to convert to JSON, returning 'None' object")
			return None
	
	def sensorDataToJson(self, data: SensorData = None)-> json:
		"""
		Returns the converted sensor data json to the caller.
		
		@return json object
		"""
		if (data is not None):
			if (self.encodeToUtf8):
				jsonData = json.dumps(data, indent = 4, cls = JsonDataEncoder).encode('utf8')
			else:
				jsonData = json.dumps(data, indent = 4, cls = JsonDataEncoder)
			return jsonData
		else:
			logging.debug("No sensor data present to convert to JSON, returning 'None' object")
			return None

	def systemPerformanceDataToJson(self, data: SystemPerformanceData = None)-> json:
		"""
		Returns the converted system performance data json to the caller.
		
		@return json object
		"""
		if (data is not None):
			jsonData = json.dumps(data, indent = 4, cls = JsonDataEncoder)
			return jsonData
		else:
			logging.debug("No sensor data present to convert to JSON, returning 'None' object")
			return None
	
	def jsonToActuatorData(self, jsonData: str = None)-> ActuatorData:
		"""
		Returns an actuator data instance converted from JSON to the caller.
		
		@return ActuatorData
		"""
		if (jsonData is not None):
			jsonData = jsonData.replace("\'", "\"").replace('False', 'false').replace('True', 'true')
			jsonStruct = json.loads(jsonData,parse_float = Decimal)

			ad = ActuatorData()
			self._updateData(ad,jsonStruct)
			
			return ad

		logging.warn("JSON data is NULL and therefore returning NULL")
		return None
		
	def _updateData(self,obj:BaseIotData,jsonStruct):
		for key in jsonStruct:
			if (key in vars(obj)):
				setattr(obj,key,jsonStruct[key])
			else:
				logging.warn("JSON data contains key not mappable to object: %s", key)

	def jsonToSensorData(self, jsonData: str = None)-> SensorData:
		"""
		Returns a sensor data instance converted from JSON to the caller.
		
		@return SensorData
		"""
		if (jsonData is not None):
			jsonData = jsonData.replace("\'", "\"").replace('False', 'false').replace('True', 'true')
			jsonStruct = json.loads(jsonData,parse_float = Decimal)

			sd = SensorData()
			self._updateData(sd,jsonStruct)
			
			return sd

		logging.warn("JSON data is NULL and therefore returning NULL")
		return None
	
	def jsonToSystemPerformanceData(self, jsonData: str = None)-> SystemPerformanceData:
		"""
		Returns a SystemPerformanceData instance converted from JSON to the caller.
		
		@return SystemPerformanceData
		"""
		if (jsonData is not None):
			jsonData = jsonData.replace("\'", "\"").replace('False', 'false').replace('True', 'true')
			jsonStruct = json.loads(jsonData,parse_float = Decimal)

			sd = SystemPerformanceData()
			self._updateData(sd,jsonStruct)
			
			return sd
	
class JsonDataEncoder(JSONEncoder):
	"""
	Convenience class to facilitate JSON encoding of an object that
	can be converted to a dict.
	
	"""
	def default(self, o):
		return o.__dict__
	