#############################################################################################################
#   Class that will perform the ACI Get method to ACI and store the information in the PowerSupply Class    #
#############################################################################################################

##################
# Import Section #
##################

import requests
import json
from PowerSupply import PowerSupply

#####################
# Class Declaration #
#####################

class PowerSupplyUnitsClass:

    def __init__(self, ACI_IP, ACI_Cookie, Node_ID, PowerSupply_URL):
        self.__ACI_IP_ADDR = ACI_IP
        self.__ACI_Cookie = ACI_Cookie
        self.__Node_ID = Node_ID
        self.__URL = PowerSupply_URL
        self.__Internal_Fan_List = []
        self.__getPowerSupplyInfo()

    #########################
    # Attributes Definition #
    #########################

    #ACI IP Address
    __ACI_IP_ADDR = ""

    #ACI Cookie for querys
    __ACI_Cookie = ""

    #ACI Node ID
    __Node_ID = ""

    #URL that will query for the Power Supply information from Cisco APIC
    __URL = ""

    #List that will store all FAN Info in Objects
    __Internal_Fan_List = []

    ###############
    # Get Methods #
    ###############

    #Get ACI IP Address Method
    def getACI_IP_ADDR(self):
        return self.__ACI_IP_ADDR
    
    #Get ACI Cookie
    def getACI_Cookie(self):
        return self.__ACI_Cookie
    
    #Get ACI Node ID
    def getNode_ID(self):
        return self.__Node_ID

    #Get the Fan List
    def getFanList(self):
        return self.__Internal_Fan_List
    
    #Return Number of Fan Lists
    def getNumFanList(self):
        return len(self.__Internal_Fan_List)

    ###############################################
    # Return Supervisor Attributes based on Index #
    ###############################################

    #Return FAN ID Number Based on Index
    def getPowerSupplyID(self, index):
        return self.__Internal_Fan_List[index].getID()

    #Return FAN Description Based on Index
    def getPowerSupplyDescription(self, index):
        return self.__Internal_Fan_List[index].getDescription()

    #Return Power Supply Model Based on Index
    def getPowerSupplyModel(self, index):
        return self.__Internal_Fan_List[index].getModel()

    #Return Power Supply Serial Number Based on Index
    def getPowerSupplySerialNumber(self, index):
        return self.__Internal_Fan_List[index].getSerialNumber()

    #Return Power Supply Vendor Based on Index
    def getPowerSupplyVendor(self, index):
        return self.__Internal_Fan_List[index].getVendor()

    #Return Power Supply Operational Status Based on Index
    def getPowerSupplyOperationalStatus(self, index):
        return self.__Internal_Fan_List[index].getFanOperationalStatus()

    #Return Power Supply Hardware Version Based on Index
    def getHardwareVersion(self, index):
        return self.__Internal_Fan_List[index].getHardwareVersion()

    ##########################################################
    # Private Method to request the information in Cisco ACI #
    ##########################################################

    def __get_request(self, url):
        responds = requests.get(url, cookies=self.__ACI_Cookie, verify=False)
        json_obj = json.loads(responds.content)
        return json_obj

    ######################################
    # Get Power Supply Units Information #
    ######################################

    def __getPowerSupplyInfo(self):

        #Variable that store all the Power Supply Units information in JSON format
        FAN_INFO = self.__get_request(self.__URL % (self.__ACI_IP_ADDR, self.__Node_ID))

        #Object creation with for loop
        for i in range(0,int(FAN_INFO['totalCount'])):
            self.__Internal_Fan_List.append( PowerSupply (  FAN_INFO['imdata'][i]['eqptPsu']['attributes']['id'], 
                                                            FAN_INFO['imdata'][i]['eqptPsu']['attributes']['descr'], 
                                                            FAN_INFO['imdata'][i]['eqptPsu']['attributes']['model'],
                                                            FAN_INFO['imdata'][i]['eqptPsu']['attributes']['ser'],
                                                            FAN_INFO['imdata'][i]['eqptPsu']['attributes']['vendor'],
                                                            FAN_INFO['imdata'][i]['eqptPsu']['attributes']['fanOpSt'],
                                                            FAN_INFO['imdata'][i]['eqptPsu']['attributes']['hwVer']))