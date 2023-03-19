#!/bin/bash
export PYTHONPATH="/var/lib/jenkins/workspace/Home Automation Python Build And Test/src/main/python:/var/lib/jenkins/workspace/Home Automation Python Build And Test/src/test/python:$PYTHONPATH"

# rm -rf out/build CMakelists.txt
# cmake -S . -B out/build
# make -C out/build
python3 src/test/python/programmingtheiot/part01/unit/system/SystemCpuUtilTaskTest.py
echo $PYTHONPATH
