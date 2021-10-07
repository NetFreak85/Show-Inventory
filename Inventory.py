#####################################################
# Inventory Class that will Show all the Fabric S/N #
# The Script will provide the following information #
#   Chassis Serial Number                           #
#   Supervisor Serial Number                        #
#   Line Cards Serial Number                        #
#   Power Supply Serial Number                      #
#####################################################

##################
# Import Section #
##################

import requests
import json
import getCookie
import csv
from datetime import date
from PowerSupplyUnitClass import PowerSupplyUnitsClass
from LinesCardModule import LinesCardModule
from SupervisorClass import SupervisorClass
from ChassisClass import ChassisClass

#################
#Class Definition
#################

class Inventory:
    
    def __init__ (self, Constant):
        self.__Constant = Constant
        self.__Node_ID_List = []
        self.__Chassis_List = []
        self.__LineCards_List = []
        self.__PowerSupply_List = []
        self.__ACI_Cookie = ""
        self.__Chassis_Query = ""
        self.__Supervisor_Query = ""
        self.__LineCards_Query = ""
        self.__PowerSupply_Query = ""
        self.__Query_Generator()
        self.__Fabric_Nodes()

    #########################
    # Attributes Definition #
    #########################

    #Constat Variable ( ACI IP Address and User/Password )
    __Constant = ""

    #Node IDs List
    __Node_ID_List = []

    #Chassis Object Lists
    __Chassis_List = []

    #Supervisors Object Lists
    __Supervisor_List = []

    #Line Cards Lines
    __LineCards_List = []

    #Power Supplys Lists
    __PowerSupply_List = []

    ####################################
    # Cookie Variables for APIC Querys #
    ####################################

    #Cookie for all Fabric Node Querys
    __ACI_Cookie = ""

    #Cookie for all Chassis Query
    __Chassis_Query = ""

    #Cookie for all Supervisor Querys
    __Supervisor_Query = ""

    #Cookie for all Line Cards Query
    __LineCards_Query = ""

    #Cookie for all Power Supplys Query
    __PowerSupply_Query = ""

    ##########################
    # Get Methods definition #
    ##########################

    #Method that get the Querys
    def __Query_Generator(self):
        self.__ACI_Cookie        =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password)
        self.__Chassis_Query     =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password)
        self.__Supervisor_Query  =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password)
        self.__LineCards_Query   =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password)
        self.__PowerSupply_Query =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password)

    #Check the numbers of Nodes and return a JSON variable
    def __get_request(self, url):
	    responds = requests.get(url, cookies=self.__ACI_Cookie, verify=False)
	    json_obj = json.loads(responds.content)
	    return json_obj

    #Export ACI Inventory in CSV Format
    def ExportInventoryCsvFormat(self):

        #URL to obtain the Fabric Name
        URL = "https://%s/api/node/mo/topology/pod-1/node-1.json?query-target=children&target-subtree-class=infraCont" % self.__Constant.apic

        #Variable that store all the FANs information in JSON format
        FABRIC_NAME = self.__get_request(URL)

        #We use the Date Class in order to know when the Output File was created
        today = date.today()
        
        #Filename based on Component, Fabric name and Date
        CHASSIS_Filename =  "Inventory-Chassis" + "-" + FABRIC_NAME['imdata'][0]['infraCont']['attributes']['fbDmNm'] + "-" + today.strftime("%d-%m-%Y") + ".csv"
        SUPERVISOR_Filename = "Inventory-Supervisor" + "-" + FABRIC_NAME['imdata'][0]['infraCont']['attributes']['fbDmNm'] + "-" + today.strftime("%d-%m-%Y") + ".csv"
        POWER_SUPPLY_Filename = "Inventory-PowerSupply" + "-" + FABRIC_NAME['imdata'][0]['infraCont']['attributes']['fbDmNm'] + "-" + today.strftime("%d-%m-%Y") + ".csv"
        LINE_CARD_Filename = "Inventory-LineCard" + "-" + FABRIC_NAME['imdata'][0]['infraCont']['attributes']['fbDmNm'] + "-" + today.strftime("%d-%m-%Y") + ".csv"

        #We create the CSV Chassis File
        #If the File exist we override the file
        try:
            ChassisFile = open( CHASSIS_Filename , "x" )
            ChassisFile.write("Component, Node ID, description, Model, OperationalStatus, Role, SerialNumber, Status, Vendor")
            ChassisFile.write("\n")

            for index in range ( 0, int(len(self.__Node_ID_List ))):
                if int(self.__Node_ID_List[index]) > int(self.__Constant.APIC_Number):
                    ChassisFile.write("Chassis, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[index], self.__Chassis_List[index].getDescription() ,self.__Chassis_List[index].getModel() ,self.__Chassis_List[index].getOperationalStatus() ,self.__Chassis_List[index].getRole() ,self.__Chassis_List[index].getSerialNumber() ,self.__Chassis_List[index].getStatus() ,self.__Chassis_List[index].getVendor()))
                else:
                    ChassisFile.write("Chassis, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[index], self.__Chassis_List[index].getDescription() ,self.__Chassis_List[index].getModel() ,self.__Chassis_List[index].getOperationalStatus() ,"APIC" ,self.__Chassis_List[index].getSerialNumber() ,self.__Chassis_List[index].getStatus() ,self.__Chassis_List[index].getVendor()))
                ChassisFile.write("\n")
            ChassisFile.close()
        except:
            ChassisFile = open( CHASSIS_Filename , "w" )
            ChassisFile.write("Component, Node ID, description, Model, OperationalStatus, Role, SerialNumber, Status, Vendor")
            ChassisFile.write("\n")

            for index in range ( 0, int(len(self.__Node_ID_List ))):
                if int(self.__Node_ID_List[index]) > int(self.__Constant.APIC_Number):
                    ChassisFile.write("Chassis, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[index], self.__Chassis_List[index].getDescription() ,self.__Chassis_List[index].getModel() ,self.__Chassis_List[index].getOperationalStatus() ,self.__Chassis_List[index].getRole() ,self.__Chassis_List[index].getSerialNumber() ,self.__Chassis_List[index].getStatus() ,self.__Chassis_List[index].getVendor()))
                else:
                    ChassisFile.write("Chassis, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[index], self.__Chassis_List[index].getDescription() ,self.__Chassis_List[index].getModel() ,self.__Chassis_List[index].getOperationalStatus() ,"APIC" ,self.__Chassis_List[index].getSerialNumber() ,self.__Chassis_List[index].getStatus() ,self.__Chassis_List[index].getVendor()))
                ChassisFile.write("\n")

            ChassisFile.close()

        #We create the CSV Supervisor File
        #If the File exist we override the file 
        try:
            SupervisorFile = open( SUPERVISOR_Filename , "x" )
            SupervisorFile.write("Component, Node ID, Supervisor ID, Description, Operational Status, Power Status, Serial Number, Vendor, Model, Hardware Version, Uptime")
            SupervisorFile.write("\n")

            for i in range ( 0, len(self.__Node_ID_List )):
                if int(self.__Node_ID_List[i]) > int(self.__Constant.APIC_Number):
                    for k in range (0 , len( self.__Supervisor_List[i].getSupervisorList())): 
                        SupervisorFile.write("Supervisor, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[i], self.__Supervisor_List[i].getSupervisor_ID(k), self.__Supervisor_List[i].getDescription(k), self.__Supervisor_List[i].getOperational_Status(k), self.__Supervisor_List[i].getPowerStatus(k), self.__Supervisor_List[i].getSerial_Number(k), self.__Supervisor_List[i].getVendor(k), self.__Supervisor_List[i].getModel(k), self.__Supervisor_List[i].getHardwareVersion(k), self.__Supervisor_List[i].getUpTime(k)))
                        SupervisorFile.write("\n")
            
            SupervisorFile.close()
        except:
            SupervisorFile = open( SUPERVISOR_Filename , "w" )
            SupervisorFile.write("Component, Node ID, Supervisor ID, Description, Operational Status, Power Status, Serial Number, Vendor, Model, Hardware Version, Uptime")
            SupervisorFile.write("\n")

            for i in range ( 0, len(self.__Node_ID_List )):
                if int(self.__Node_ID_List[i]) > int(self.__Constant.APIC_Number):
                    for k in range (0 , len( self.__Supervisor_List[i].getSupervisorList())): 
                        SupervisorFile.write("Supervisor, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[i], self.__Supervisor_List[i].getSupervisor_ID(k), self.__Supervisor_List[i].getDescription(k), self.__Supervisor_List[i].getOperational_Status(k), self.__Supervisor_List[i].getPowerStatus(k), self.__Supervisor_List[i].getSerial_Number(k), self.__Supervisor_List[i].getVendor(k), self.__Supervisor_List[i].getModel(k), self.__Supervisor_List[i].getHardwareVersion(k), self.__Supervisor_List[i].getUpTime(k)))
                        SupervisorFile.write("\n")
            
            SupervisorFile.close()

        #We create the CSV Line Card File
        #If the File exist we override the file
        try:
            LINE_CARD_File = open( LINE_CARD_Filename, "x")
            LINE_CARD_File.write("Component, Node ID, Line Card ID, Description, Hardware Version, Model, Operational Status, Power Status, Serial Number, Vendor, UP Time")
            LINE_CARD_File.write("\n")

            for i in range ( 0, len(self.__Node_ID_List )):
                if int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number:
                    for k in range (0, len( self.__LineCards_List[i].getLineCardList())):
                        LINE_CARD_File.write("Line Card, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[i], self.__LineCards_List[i].getID(k), self.__LineCards_List[i].getDescription(k), self.__LineCards_List[i].getHardwareVersion(k), self.__LineCards_List[i].getModel(k), self.__LineCards_List[i].getOperationalStatus(k), self.__LineCards_List[i].getPowerStatus(k), self.__LineCards_List[i].getSerialNumber(k), self.__LineCards_List[i].getVendor(k), self.__LineCards_List[i].getUpTime(k)))
                        LINE_CARD_File.write("\n")

            LINE_CARD_File.close()
        except:
            LINE_CARD_File = open( LINE_CARD_Filename, "w")
            LINE_CARD_File.write("Component, Node ID, Line Card ID, Description, Hardware Version, Model, Operational Status, Power Status, Serial Number, Vendor, UP Time")
            LINE_CARD_File.write("\n")

            for i in range ( 0, len(self.__Node_ID_List )):
                if int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number:
                    for k in range (0, len( self.__LineCards_List[i].getLineCardList())):
                        LINE_CARD_File.write("Line Card, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[i], self.__LineCards_List[i].getID(k), self.__LineCards_List[i].getDescription(k), self.__LineCards_List[i].getHardwareVersion(k), self.__LineCards_List[i].getModel(k), self.__LineCards_List[i].getOperationalStatus(k), self.__LineCards_List[i].getPowerStatus(k), self.__LineCards_List[i].getSerialNumber(k), self.__LineCards_List[i].getVendor(k), self.__LineCards_List[i].getUpTime(k)))
                        LINE_CARD_File.write("\n")

            LINE_CARD_File.close()

        #We create the CSV Power Supply File
        #If the File exist we override the file
        try:
            POWER_SUPPLY_Filename = open( POWER_SUPPLY_Filename, "x")
            POWER_SUPPLY_Filename.write("Component, Node ID, Power Supply ID, Description, Model, Serial Number, Vendor, Fan Operational Status, Hardware Version")
            POWER_SUPPLY_Filename.write("\n")

            for i in range ( 0, len(self.__Node_ID_List )):
                if int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number:
                    for k in range (0 , len( self.__PowerSupply_List[i].getFanList())):
                        POWER_SUPPLY_Filename.write("Power Supply, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[i], self.__PowerSupply_List[i].getPowerSupplyID(k), self.__PowerSupply_List[i].getPowerSupplyDescription(k), self.__PowerSupply_List[i].getPowerSupplyModel(k), self.__PowerSupply_List[i].getPowerSupplySerialNumber(k), self.__PowerSupply_List[i].getPowerSupplyVendor(k), self.__PowerSupply_List[i].getPowerSupplyOperationalStatus(k), self.__PowerSupply_List[i].getHardwareVersion(k)))
                        POWER_SUPPLY_Filename.write("\n")

            POWER_SUPPLY_Filename.close()
        except:
            POWER_SUPPLY_Filename = open( POWER_SUPPLY_Filename, "w")
            POWER_SUPPLY_Filename.write("Component, Node ID, Power Supply ID, Description, Model, Serial Number, Vendor, Fan Operational Status, Hardware Version")
            POWER_SUPPLY_Filename.write("\n")
            
            for i in range ( 0, len(self.__Node_ID_List )):
                if int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number:
                    for k in range (0 , len( self.__PowerSupply_List[i].getFanList())):
                        POWER_SUPPLY_Filename.write("Power Supply, %s, %s, %s, %s, %s, %s, %s, %s" % (self.__Node_ID_List[i], self.__PowerSupply_List[i].getPowerSupplyID(k), self.__PowerSupply_List[i].getPowerSupplyDescription(k), self.__PowerSupply_List[i].getPowerSupplyModel(k), self.__PowerSupply_List[i].getPowerSupplySerialNumber(k), self.__PowerSupply_List[i].getPowerSupplyVendor(k), self.__PowerSupply_List[i].getPowerSupplyOperationalStatus(k), self.__PowerSupply_List[i].getHardwareVersion(k)))
                        POWER_SUPPLY_Filename.write("\n")

            POWER_SUPPLY_Filename.close()

    #Export ACI Inventory in JSON Format
    def ExportInventoryJsonFormat(self):

        #URL to obtain the Fabric Name
        URL = "https://%s/api/node/mo/topology/pod-1/node-1.json?query-target=children&target-subtree-class=infraCont" % self.__Constant.apic

        #Variable that store all the FANs information in JSON format
        FABRIC_NAME = self.__get_request(URL)

        #Json Format for all the Fabric Information
        Fabric_Json = { "Fabric Name" : FABRIC_NAME['imdata'][0]['infraCont']['attributes']['fbDmNm'],
                        "Total Nodes" : len(self.__Node_ID_List ), 
                        "data" : {
                                "Chassis" : {
                                    'Supervisor ID' : "",
                                    'Description' : "",
                                    'Operational Status' : "",
                                    'PowerStatus' : "",
                                    'Serial_Number' : "",
                                    'Vendor' : "",
                                    'Model' : "",
                                    'Hardware Version' : "",
                                    'UP Time' : "",
                                    "Supervisor" : {},
                                    "Power Supply" : {},
                                    "Line Card" : {}
                                }
                        }
                    }
        
        #Fabric List Based on number of nodes
        Fabric_Json['data']['Chassis'] = []

        #We create all the Chassis information into the Json variable
        for i in range ( 0, len(self.__Node_ID_List )):
            Chassis = {
                    'Node ID'       :   self.__Node_ID_List[i],
                    'description' : self.__Chassis_List[i].getDescription(),
                    'Model' : self.__Chassis_List[i].getModel(),
                    'OperationalStatus' : self.__Chassis_List[i].getOperationalStatus(),
                    'Role' : self.__Chassis_List[i].getRole(),
                    'SerialNumber' : self.__Chassis_List[i].getSerialNumber(),
                    'Status' : self.__Chassis_List[i].getStatus(),
                    'Vendor' : self.__Chassis_List[i].getVendor(),
            }

            Fabric_Json['data']['Chassis'].append(Chassis)

            #we create the lists for Supervisors, Power Supplys and Lines Cards
            Fabric_Json['data']['Chassis'][i]['Supervisor'] = []
            Fabric_Json['data']['Chassis'][i]['Power Supply'] = []
            Fabric_Json['data']['Chassis'][i]['Line Card'] = []

            #If the Node is not a APIC we detect the Supervisor, Power Supply and Lines cards information
            if int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number:

                #We complete the Supervisor List into the Chassis ID i with the super visor information
                for k in range (0 , len( self.__Supervisor_List[i].getSupervisorList())): 
                    Supervisor = {
                            'Supervisor ID' : self.__Supervisor_List[i].getSupervisor_ID(k),
                            'Description' : self.__Supervisor_List[i].getDescription(k),
                            'Operational Status' : self.__Supervisor_List[i].getOperational_Status(k),
                            'PowerStatus' : self.__Supervisor_List[i].getPowerStatus(k),
                            'Serial_Number' : self.__Supervisor_List[i].getSerial_Number(k),
                            'Vendor' : self.__Supervisor_List[i].getVendor(k),
                            'Model' : self.__Supervisor_List[i].getModel(k),
                            'Hardware Version' : self.__Supervisor_List[i].getHardwareVersion(k),
                            'UP Time' : self.__Supervisor_List[i].getUpTime(k)
                    }
                    Fabric_Json['data']['Chassis'][i]['Supervisor'].append(Supervisor)
            
                #We complete the Power Supply List into the Chassis ID i with the super visor information
                for k in range (0 , len( self.__PowerSupply_List[i].getFanList())):
                    PowerSupply = {
                        'ID' : self.__PowerSupply_List[i].getPowerSupplyID(k),
                        'Description' : self.__PowerSupply_List[i].getPowerSupplyDescription(k), 
                        'Model' : self.__PowerSupply_List[i].getPowerSupplyModel(k),
                        'Serial_Number' : self.__PowerSupply_List[i].getPowerSupplySerialNumber(k),
                        'Vendor' : self.__PowerSupply_List[i].getPowerSupplyVendor(k),
                        'Fan_Operational_Status' : self.__PowerSupply_List[i].getPowerSupplyOperationalStatus(k),
                        'Hardware_Version' : self.__PowerSupply_List[i].getHardwareVersion(k)
                    }
                    Fabric_Json['data']['Chassis'][i]['Power Supply'].append(PowerSupply)
                
                #We complete the Line Cards List into the Chassis ID i with the super visor information
                for k in range (0, len( self.__LineCards_List[i].getLineCardList())):
                    LineCard = {
                        'ID' : self.__LineCards_List[i].getID(k),
                        'Description' : self.__LineCards_List[i].getDescription(k),
                        'Hardware_Version' : self.__LineCards_List[i].getHardwareVersion(k),
                        'Model' : self.__LineCards_List[i].getModel(k), 
                        'Operational_Status' : self.__LineCards_List[i].getOperationalStatus(k), 
                        'Power_Status' : self.__LineCards_List[i].getPowerStatus(k),
                        'Serial_Number' : self.__LineCards_List[i].getSerialNumber(k), 
                        'Vendor' : self.__LineCards_List[i].getVendor(k),
                        'UP_Time' : self.__LineCards_List[i].getUpTime(k),
                    }
                    Fabric_Json['data']['Chassis'][i]['Line Card'].append(LineCard)

        #We use the Date Class in order to know when the Output File was created
        today = date.today()
        
        #We create the Filename based on the APIC name and Date
        Filename =  "Inventory" + "-" + FABRIC_NAME['imdata'][0]['infraCont']['attributes']['fbDmNm'] + "-" + today.strftime("%d-%m-%Y") + ".json"
        
        #We create the JSON File
        #If the File exist we override the file
        try:
            OutputFile = open( Filename , "x" )
            OutputFile.write(json.dumps(Fabric_Json, indent = 4))
            OutputFile.close()
        except:
            OutputFile = open( Filename , "w" )
            OutputFile.write(json.dumps(Fabric_Json, indent = 4))
            OutputFile.close()

    #Print ACI Inventory method
    def printInventory(self):
        print("-----------------------------------------------")
        for i in range ( 0, len(self.__Node_ID_List )):
            
            ######################
            # Print Node Section #
            ######################
            print("Node ID                 : " + self.__Node_ID_List[i])
            
            #########################
            # Print Chassis Section #
            #########################
            if (int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number):
                print("Role                    : " + self.__Chassis_List[i].getRole())
            else:
                print("Role                    : APIC")

            print("Chadis S/N              : " + self.__Chassis_List[i].getSerialNumber())
            print("Model                   : " + self.__Chassis_List[i].getModel())
            
            ############################
            # Print Supervisor Section #
            ############################
            if(int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number): 
                for k in range (0 , len( self.__Supervisor_List[i].getSupervisorList())): 
                    print("Supervisor ID           : " + str(self.__Supervisor_List[i].getSupervisor_ID(k)) + "    S/N : " + str(self.__Supervisor_List[i].getSerial_Number(k)))
                    print("Supervisor Description  : " + str(self.__Supervisor_List[i].getDescription(k)))
                    print("Supervisor Model        : " + str(self.__Supervisor_List[i].getModel(k)))

            ##############################
            # Print Power Supply Section #
            ##############################
            for k in range (0 , len( self.__PowerSupply_List[i].getFanList())):
                print("FAN ID                  : " + str(self.__PowerSupply_List[i].getPowerSupplyID(k)) + "    S/N : " + str(self.__PowerSupply_List[i].getPowerSupplySerialNumber(k)))

            ############################
            # Print Line Cards Section #
            ############################
            if(int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number):
                for k in range (0, len( self.__LineCards_List[i].getLineCardList())):
                    print("Line Card S/N           : " + str(self.__LineCards_List[i].getSerialNumber(k)))

            print("-----------------------------------------------")

    #Private Methods to construct the Node IDs Lists Attribute
    def __Fabric_Nodes(self):
        #URL to get the Numbers of nodes in the Fabrics and its IDs
        URL = "https://%s/api/node/class/fabricNode.json?&order-by=fabricNode.modTs|desc" % self.__Constant.apic

        #Variable that store all the IDs information in JSON format
        FABRIC_IDS = self.__get_request(URL)

        #Object creation with for loop
        for i in range( 0, int(FABRIC_IDS['totalCount'] )):
            #Build Node ID List with all Nodes ID in the fabric
            self.__Node_ID_List.append( FABRIC_IDS['imdata'][i]['fabricNode']['attributes']['id'] )
            
            #Build Chassis List with all the information about Node Chassis
            self.__Chassis_List.append( ChassisClass ( self.__Constant.apic , self.__Chassis_Query , self.__Node_ID_List[i] ))

            #Build Supervisor List with the information about the supervisors
            if(int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number):
                self.__Supervisor_List.append( SupervisorClass ( self.__Constant.apic , self.__Supervisor_Query , self.__Node_ID_List[i] ))
            else:
                self.__Supervisor_List.append(0)

            #Build LineCard List with the information about the Line Cards
            if(int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number):
                self.__LineCards_List.append( LinesCardModule ( self.__Constant.apic , self.__LineCards_Query , self.__Node_ID_List[i] ))
            else:
                self.__LineCards_List.append(0)

            #Build Power Supply Lists with the information about Power Supply Node
            self.__PowerSupply_List.append( PowerSupplyUnitsClass ( self.__Constant.apic , self.__PowerSupply_Query , self.__Node_ID_List[i] ))