###################################################################################
#   Class that will store and work with Fabric Modules Information on Cisco aci   #
###################################################################################

##################
# Import Section #
##################

import requests
import json

from FabricModule import FabricModule

#####################
# Class Declaration #
#####################

class FabricModuleControllers:

    def __init__(self, ACI_IP, ACI_Cookie, Node_ID, FabricModules_URL):
        self.__ACI_IP_ADDR = ACI_IP
        self.__ACI_Cookie = ACI_Cookie
        self.__Node_ID = Node_ID
        self.__URL = FabricModules_URL
        self.__FabricModules = []
        self.__getFabricModuleInfo()


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
    __FabricModules = []

    ###############
    # Get Methods #
    ###############

    #Get the Fabric Module List
    def getFabricModuleList(self):
        return self.__FabricModules

    #Return the Number of Fabrics Modules into the Lists
    def getNumFabricModuleList(self):
        return len(self.__FabricModules)
    
    ###################################################
    # Return Fabric Modules Attributes based on Index #
    ###################################################

    #Method that return Fabric Module Description based on index
    def getDescription(self, index):
        return self.__FabricModules[index].getDescription()
    
    #Method that return Fabric Module Hardware Version based on index
    def getHardwareVersion(self, index):
        return self.__FabricModules[index].getHardwareVersion()

    #Method that return Fabric Module ID based on index
    def getFabricModuleID(self, index):
        return self.__FabricModules[index].getFabricModuleID()

    #Method that return Fabric Module Manufacturing Time based on index
    def getManufacturingTime(self, index):
        return self.__FabricModules[index].getManufacturingTime()
    
    #Method that return Fabric Module last time modified based on index
    def getLasttimemodified(self, index):
        return self.__FabricModules[index].getLasttimemodified()
    
    #Method that return Fabric Module Model based on index
    def getModel(self, index):
        return self.__FabricModules[index].getModel()

    #Method that return Fabric Module Operational Status based on index
    def getOperationalStatus(self, index):
        return self.__FabricModules[index].getOperationalStatus()

    #Method that return Fabric Module Power Status based on index
    def getPowerStatus(self, index):
        return self.__FabricModules[index].getPowerStatus()
    
    #Method that return Fabric Module HA Status based on index
    def getHA_Status(self, index):
        return self.__FabricModules[index].getHA_Status()

    #Method that return Fabric Module Serial Number based on index
    def getSerialNumber(self, index):
        return self.__FabricModules[index].getSerialNumber()

    #Method that return Fabric Module Type based on index
    def getType(self, index):
        return self.__FabricModules[index].getType()

    #Method that return Fabric Module Uptime based on index
    def getFabricModuleUptime(self, index):
        return self.__FabricModules[index].getFabricModuleUptime()

    #Method that return Fabric Module Vendor based on index
    def getVendor(self, index):
        return self.__FabricModules[index].getVendor()

    ##########################################################
    # Private Method to request the information in Cisco ACI #
    ##########################################################
    
    def __get_request(self, url):
        responds = requests.get(url, cookies=self.__ACI_Cookie, verify=False)
        json_obj = json.loads(responds.content)
        return json_obj
    
    #Private Method that will store all the information related to System Controllers into the System Controller Class List
    def __getFabricModuleInfo(self):

        #Variable that store all the System Controllers information in JSON format
        FabricModuleJson = self.__get_request(self.__URL % (self.__ACI_IP_ADDR, self.__Node_ID))

        if FabricModuleJson['totalCount'] != "0":
            for i in range(0,int(FabricModuleJson['totalCount'])):
                self.__FabricModules.append( FabricModule ( str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['descr']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['hwVer']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['id']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['mfgTm']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['modTs']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['model']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['operSt']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['pwrSt']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['rdSt']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['ser']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['type']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['upTs']),
                                                            str( FabricModuleJson['imdata'][i]['eqptFC']['attributes']['vendor'])))