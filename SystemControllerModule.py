######################################################################################
#   Class that will store and work with System Controller Information on Cisco aci   #
######################################################################################

##################
# Import Section #
##################

import requests
import json

from SystemController import SystemController

#####################
# Class Declaration #
#####################

class SystemControllerModule:

    def __init__(self, ACI_IP, ACI_Cookie, Node_ID, SystemController_URL):
        self.__ACI_IP_ADDR = ACI_IP
        self.__ACI_Cookie = ACI_Cookie
        self.__Node_ID = Node_ID
        self.__URL = SystemController_URL
        self.__SystemControllers = []
        self.__getSystemControllerModuleInfo()

    #########################
    # Attributes Definition #
    #########################

    #ACI IP Address
    __ACI_IP_ADDR = ""

    #ACI Cookie for querys
    __ACI_Cookie = ""

    #ACI Node ID
    __Node_ID = ""

    #URL that will query for the Linecards information from Cisco APIC
    __URL = ""

    #List that will store all LineCards Info in Objects
    __SystemControllers = []

    ###############
    # Get Methods #
    ###############

    #Get the System Controller List
    def getSystemControllerList(self):
        return self.__SystemControllers
    
    #Return Number of System Controlle into the Lists
    def getNumSystemControllerList(self):
        return len(self.__SystemControllers)

    ###########################################################
    # Return the System Controllers Attributes based on Index #
    ###########################################################

    #Return System Controller Description based on Index
    def getDescription(self, index):
        return self.__SystemControllers[index].getDescription()

    #Return System Controller Hardware Version based on Index
    def getHardwareVersion(self, index):
        return self.__SystemControllers[index].getHardwareVersion()

    #Return System Controller ID based on Index
    def getSystemControllerID(self, index):
        return self.__SystemControllers[index].getSystemControllerID()

    #Return System Controller manufacturing time based on Index
    def getManufacturingTime(self, index):
        return self.__SystemControllers[index].getManufacturingTime()

    #Return System Controller Last time the object was modified based on Index
    def getLastTimeModified(self, index):
        return self.__SystemControllers[index].getLastTimeModified()

    #Return System Controller Model based on Index
    def getModel(self, index):
        return self.__SystemControllers[index].getModel()

    #Return System Controller Operational Status based on Index
    def getOperationalStatus(self, index):
        return self.__SystemControllers[index].getOperationalStatus()

    #Return System Controller Power Status based on Index
    def getPowerStatus(self, index):
        return self.__SystemControllers[index].getPowerStatus()

    #Return System Controller HA Status based on Index
    def getSystemController_HA_Status(self, index):
        return self.__SystemControllers[index].getSystemController_HA_Status()

    #Return System Controller Serial Number based on Index
    def getSerialNumber(self, index):
        return self.__SystemControllers[index].getSerialNumber()

    #Return System Controller Uptime based on Index
    def getSystemControllerUptime(self, index):
        return self.__SystemControllers[index].getSystemControllerUptime()

    #Return System Controller Vendor Name based on Index
    def getVendor(self, index):
        return self.__SystemControllers[index].getVendor()

    ##########################################################
    # Private Method to request the information in Cisco ACI #
    ##########################################################
    
    def __get_request(self, url):
        responds = requests.get(url, cookies=self.__ACI_Cookie, verify=False)
        json_obj = json.loads(responds.content)
        return json_obj

    #Private Method that will store all the information related to System Controllers into the System Controller Class List
    def __getSystemControllerModuleInfo(self):

        #Variable that help us to find all System Controller available into the Switch
        SystemControllerExist = True

        #Normally the System Controller ID start with 1, we check all the possibles System controllers in the While loop
        SystemControllerID = 1

        while SystemControllerExist:

            #Variable that store all the System Controllers information in JSON format
            SystemControllerJson = self.__get_request(self.__URL % (self.__ACI_IP_ADDR, self.__Node_ID, SystemControllerID))

            if SystemControllerJson['totalCount'] == "0":
                SystemControllerExist = False
            else:
                for i in range(0,int(SystemControllerJson['totalCount'])):
                    self.__SystemControllers.append( SystemController ( SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['descr'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['hwVer'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['id'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['mfgTm'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['modTs'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['model'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['operSt'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['pwrSt'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['rdSt'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['ser'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['upTs'],
                                                                        SystemControllerJson['imdata'][i]['eqptSysC']['attributes']['vendor']))

                SystemControllerID = SystemControllerID + 1