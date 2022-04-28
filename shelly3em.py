#!/usr/bin/python3
#
# Script to get data from Shelly3EM and store it in InfluxDB
#
# Author: Michalux
# Version: 1.0
#

import configparser
import urllib3
from urllib.parse import urlencode
import json
import os.path
import sys
import datetime
from datetime import datetime
from influxdb import InfluxDBClient

# Prepare data to write do InfluxDB
def PrepareInfluxData(IfData, fieldname, fieldvalue):
    IfData[0]["fields"][fieldname] = float(fieldvalue)
    return IfData

def Write2InfluxDB(IfData):
    ifclient.write_points(IfData)

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

# CONFIG
configParser = configparser.RawConfigParser()
configFilePath = r'./config.cfg'
configParser.read(configFilePath)

SHELLYIP=configParser.get('Shelly3EM', 'IP')
SHELLYUSERPASS=configParser.get('Shelly3EM', 'userpass')
INFLUXDB = configParser.get("InfluxDB", "influxdb")
IFHOST = configParser.get("InfluxDB", "influxdb_host")
IFPORT = configParser.get("InfluxDB", "influxdb_port")
IFUSER = configParser.get("InfluxDB", "influxdb_user")
IFPASS = configParser.get("InfluxDB", "influxdb_password")
IFDB = configParser.get("InfluxDB", "influxdb_dbname")
verbose = configParser.get("General", "verbose")
termout = configParser.get("General", "terminal_output")
lang = configParser.get("General", "lang")

# Get parameter's definitions to monitor
pfilename="./params_"+lang+".json"
with open(pfilename) as paramfile:
    params=json.loads(paramfile.read())

# Initialise InfluxDB support
if INFLUXDB == "1":
    timestamputc = str(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    ifclient = InfluxDBClient(IFHOST, IFPORT, IFUSER, IFPASS, IFDB)
    InfluxData = [{"measurement": "Shelly3EM", "time": timestamputc, "fields": {}}]

# Initialise HTTP Manager
http = urllib3.PoolManager()
header = urllib3._collections.HTTPHeaderDict()

# Get data from Shelly3EM
header = urllib3.make_headers(basic_auth=SHELLYUSERPASS)
URL='http://'+SHELLYIP+'/status'
try:
  apiresponse = http.request('GET', URL, headers=header)
except:
  print("** Error getting data from Shelly3EM **")
  sys.exit(1)
response = json.loads(apiresponse.data)

if verbose=="1":
    print("** Shelly3EM response: **")
    print(json.dumps(response, indent=4, sort_keys=False, ensure_ascii=False))

# Parse Shelly3EM response
Total=0
TotalR=0
if termout=="1":
  print("Home grid statistics:")
faza=1
for shellydata in response["emeters"]:
  if termout=="1":
    print("Phase "+str(faza))
  for param in params:
    if param != "total_power" and param != "total_sum" and param != "total_returned_sum":
      if termout=="1":
        print(" "+params[param]+": "+str(shellydata[param]))
      param_name=param+"_"+str(faza)
      if param == "total":
        Total+=shellydata[param]
      if param == "total_returned":
        TotalR+=shellydata[param]
      if INFLUXDB=="1":
        PrepareInfluxData(InfluxData, param_name, shellydata[param])
  faza+=1
if termout=="1":
  print(params["total_power"]+" : "+str(response["total_power"]))
  print(params["total_sum"]+" : "+str(Total))
  print(params["total_returned_sum"]+" : "+str(TotalR))
if INFLUXDB=="1":
  PrepareInfluxData(InfluxData, "total_power", response["total_power"])
  PrepareInfluxData(InfluxData, "total_sum", Total)
  PrepareInfluxData(InfluxData, "total_returned_sum", TotalR)

# Write data to Influx Database
if INFLUXDB=="1":
    Write2InfluxDB(InfluxData)
    if verbose=="1":
        print("** Data written to InfluxDB: **")
        print(json.dumps(InfluxData, indent=4, sort_keys=False, ensure_ascii=False))
