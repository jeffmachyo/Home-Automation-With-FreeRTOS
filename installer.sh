#!/bin/bash
export PYTHONPATH="/var/lib/jenkins/workspace/Home Automation Python Build And Test/src/main/python:/var/lib/jenkins/workspace/Home Automation Python Build And Test/src/test/python:$PYTHONPATH"


python3 src/test/python/programmingtheiot/part01/unit/system/SystemCpuUtilTaskTest.py
python3 src/test/python/programmingtheiot/part01/unit/system/SystemMemUtilTaskTest.py
python3 src/test/python/programmingtheiot/part01/unit/common/ConfigUtilTest.py
python3 src/test/python/programmingtheiot/part01/integration/system/SystemPerformanceManagerTest.py
python3 src/test/python/programmingtheiot/part01/integration/app/ConstrainedDeviceAppTest.py
python3 src/test/python/programmingtheiot/part02/integration/app/DeviceDataManagerNoCommsTest.py
python3 src/test/python/programmingtheiot/part02/integration/connection/PersistenceClientAdapterTest.py
python3 src/test/python/programmingtheiot/part02/integration/data/DataIntegrationTest.py
python3 src/test/python/programmingtheiot/part01/integration/system/SystemPerformanceManagerTest.py
python3 src/test/python/programmingtheiot/part02/integration/embedded/HumidityI2cSensorAdapterTaskTest.py
python3 src/test/python/programmingtheiot/part02/integration/embedded/PressureI2cSensorAdapterTaskTest.py
python3 src/test/python/programmingtheiot/part02/integration/embedded/TemperatureI2cSensorAdapterTaskTest.py
python3 src/test/python/programmingtheiot/part02/integration/system/ActuatorAdapterManagerTest.py
# python3 src/test/python/programmingtheiot/part01/integration/system/SystemPerformanceManagerTest.py
# python3 src/test/python/programmingtheiot/part01/integration/system/SystemPerformanceManagerTest.py

echo $PYTHONPATH
