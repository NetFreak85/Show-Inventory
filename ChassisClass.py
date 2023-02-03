########################################################################################
#   Class that will storage and print information about the Chasis in the Cisco ACI    #
########################################################################################

##################
# Import Section #
##################

import requests
import json

#####################
# Class Declaration #
#####################

class ChassisClass:

    def __init__(self, ACI_IP, ACI_Cookie, Node_ID, Chassis_URL):
        self.__ACI_IP_ADDR = ACI_IP
        self.__ACI_Cookie = ACI_Cookie
        self.__Node_ID = Node_ID
        self.__URL = Chassis_URL
        self.__description = ""
        self.__ID = ""
        self.__Model = ""
        self.__OperationalStatus = ""
        self.__Role = ""
        self.__SerialNumber = ""
        self.__Status = ""
        self.__Vendor = ""
        self.__getSupervisorInfo()

    #########################
    # Attributes Definition #
    #########################
    
    #ACI IP Address
    __ACI_IP_ADDR = ""

    #ACI Cookie for querys
    __ACI_Cookie = ""

    #ACI Node ID
    __Node_ID = ""

    #Chassis Description
    __description = ""

    #Chassis ID
    __ID = ""

    #Chassis Model
    __Model = ""

    #Chassis Operational Status
    __OperationalStatus = ""

    #Chassis Role
    __Role = ""

    #Chassis Serial Number
    __SerialNumber = ""

    #Chassis Status
    __Status = ""

    #Chassis Vendor
    __Vendor = ""

    #URL that will query for the Chassis information from Cisco APIC
    __URL = ""

    ###############
    # Get Methods #
    ###############

    #Return Chassis Description
    def getDescription(self):
        return self.__description
    
    #Return Chassis ID
    def getID(self):
        return self.__ID

    #Return Chassis Model
    def getModel(self):
        return self.__Model
    
    #Return Chassis Operational Status
    def getOperationalStatus(self):
        return self.__OperationalStatus

    #Return Chassis Role
    def getRole(self):
        return self.__Role
    
    #Return Chassis Serial Number
    def getSerialNumber(self):
        return self.__SerialNumber

    #Return Chassis Status
    def getStatus(self):
        return self.__Status
    
    #Return Chassis Vendor
    def getVendor(self):
        return self.__Vendor

    ##########################################################
    # Private Method to request the information in Cisco ACI #
    ##########################################################
    
    def __get_request(self, url):
        responds = requests.get(url, cookies=self.__ACI_Cookie, verify=False)
        json_obj = json.loads(responds.content)
        return json_obj

    ###############################
    # Get Supervisors Information #
    ###############################

    def __getSupervisorInfo(self):

        #Variable that store all the FANs information in JSON format
        CHASSIS_INFO = self.__get_request(self.__URL % (self.__ACI_IP_ADDR, self.__Node_ID))

        #Copy values to Class attributes from JSON output
        self.__description = CHASSIS_INFO['imdata'][0]['eqptCh']['attributes']['descr']
        self.__ID = CHASSIS_INFO['imdata'][0]['eqptCh']['attributes']['id']
        self.__Model = CHASSIS_INFO['imdata'][0]['eqptCh']['attributes']['model']

        if str(CHASSIS_INFO['imdata'][0]['eqptCh']['attributes']['role']) == "8":
            self.__Role = "APIC"
        else:
            self.__Role = CHASSIS_INFO['imdata'][0]['eqptCh']['attributes']['role']
        
        self.__OperationalStatus = CHASSIS_INFO['imdata'][0]['eqptCh']['attributes']['operSt']
        self.__SerialNumber = CHASSIS_INFO['imdata'][0]['eqptCh']['attributes']['ser']
        self.__Status = CHASSIS_INFO['imdata'][0]['eqptCh']['attributes']['operStQual']
        self.__Vendor = CHASSIS_INFO['imdata'][0]['eqptCh']['attributes']['vendor']