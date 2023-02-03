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

from ast import Constant
import requests
import json
import getCookie
import yaml
import argparse

from termcolor import colored
from datetime import date
from PowerSupplyUnitClass import PowerSupplyUnitsClass
from LinesCardModule import LinesCardModule
from SupervisorClass import SupervisorClass
from ChassisClass import ChassisClass
from SystemControllerModule import SystemControllerModule
from FabricModuleControllers import FabricModuleControllers

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
        self.__SystemController_List = []
        self.__FabricModule_List = []
        self.__ACI_Cookie = ""
        self.__Chassis_Query = ""
        self.__Supervisor_Query = ""
        self.__LineCards_Query = ""
        self.__PowerSupply_Query = ""
        self.__SystemController_Query = ""
        self.__FabricModule_Query = ""
        self.__URLs = ""
        self.__args = self.__get_args()
        self.__FabricName = ""
        self.__Read_Yaml_File()
        self.__Query_Generator()
        self.__Fabric_Nodes()


    #########################
    # Attributes Definition #
    #########################

    #Constat Variable ( ACI IP Address and User/Password )
    __Constant = ""

    #Variable that will store all the URL required by retrieve information from Cisco APIC
    __URLs = ""

    #Class that evaluate arguments in the script
    __args = ""

    #Variable that store the Fabric name
    __FabricName = ""

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

    #System Controllers List
    __SystemController_List = []

    #Fabric Module List
    __FabricModule_List = []

    ####################################
    # Cookie Variables for APIC Querys #
    ####################################

    #Cookie for all Fabric Node Querys
    __ACI_Cookie = ""

    #Cookie for all Chassis Querys
    __Chassis_Query = ""

    #Cookie for all Supervisor Querys
    __Supervisor_Query = ""

    #Cookie for all Line Cards Querys
    __LineCards_Query = ""

    #Cookie for all Power Supplys Querys
    __PowerSupply_Query = ""

    #Cookie for all the System Controller Querys
    __SystemController_Query = ""

    #Cookie for all the Fabric Module Querys
    __FabricModule_Query = ""

    ##########################
    # Get Methods definition #
    ##########################

    #Defining the Argument function that allow the verbose mode
    def __get_args(self):
        parser = argparse.ArgumentParser()

        #Method that enable verbose mode
        parser.add_argument('-v',
                        help='Verbose mode',
                        action='store_true',
                        required=False)

        return parser.parse_args()

    #Method that get the Querys
    def __Query_Generator(self):
        self.__ACI_Cookie        =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password, self.__URLs['URLs']['Token'])
        self.__Chassis_Query     =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password, self.__URLs['URLs']['Token'])
        self.__Supervisor_Query  =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password, self.__URLs['URLs']['Token'])
        self.__LineCards_Query   =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password, self.__URLs['URLs']['Token'])
        self.__PowerSupply_Query =  getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password, self.__URLs['URLs']['Token'])
        self.__SystemController_Query = getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password, self.__URLs['URLs']['Token'])
        self.__FabricModule_Query = getCookie.get_cookie(self.__Constant.apic, self.__Constant.User, self.__Constant.Password, self.__URLs['URLs']['Token'])

    #Function that read the Cisco ACI URL for RESCONF querys in YAML file
    def __Read_Yaml_File(self):
        with open('url.yaml') as file:
            try:
                self.__URLs = yaml.safe_load(file)
            except yaml.YAMLError as exc:
                exit(print("Error reading from URL.YAML file"))

    #Check the numbers of Nodes and return a JSON variable
    def __get_request(self, url):
        responds = requests.get(url, cookies=self.__ACI_Cookie, verify=False)
        json_obj = json.loads(responds.content)
        return json_obj

    #Method that print the process evolution
    def __print_Node_Info(self, method,node, node_type, FrameSize, bool, color):

        #Check the length of the string
        strig_len = len("|     %s data from %s %s: %s" % (method, node_type, str(node), method))

        #True if the options are Retrieve or Loading
        #False if the option is Completed
        #Those are differents because the last one don't override the line output
        if bool:
            print("|     %s data from %s %s: %s" % (colored(method, color), colored(str(node_type).upper(), color), str(node), colored(method, color))+ ' ' * ((FrameSize - strig_len) - 2), "|", end="\r")
        else:
            print("|     %s data from %s %s: %s" % (colored(method, color), colored(str(node_type).upper(), color), str(node), colored(method, color))+ ' ' * ((FrameSize - strig_len) - 2), "|")

    def printAux(self):
        print("+----------------------------------------------------------------------+")

    #Export ACI Inventory in JSON Format
    def ExportInventoryJsonFormat(self):

        #URL to obtain the Fabric Name
        URL = self.__URLs['URLs']['Fabric_Name'] % self.__Constant.apic

        #Print The process of the Fabric Name
        print("|     Retriving Fabric Name: ", end = "\r")

        #Variable that store all the FANs information in JSON format
        self.__FabricName = self.__get_request(URL)

        #Json Format for all the Fabric Information
        Fabric_Json = { "Fabric Name" : self.__FabricName['imdata'][0]['infraCont']['attributes']['fbDmNm'],
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
                                    "Line Card" : {},
                                    "System Controller" : {},
                                    "Fabric Modules" : {}
                                }
                        }
                    }

        #Fabric List Based on number of nodes
        Fabric_Json['data']['Chassis'] = []

        #Start Retrieving data
        self.printAux()

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

            #we create the lists for Supervisors, Power Supplys, Lines Cards, System Controllers & Fabric Modules
            Fabric_Json['data']['Chassis'][i]['Supervisor'] = []
            Fabric_Json['data']['Chassis'][i]['Power Supply'] = []
            Fabric_Json['data']['Chassis'][i]['Line Card'] = []
            Fabric_Json['data']['Chassis'][i]['System Controller'] = []
            Fabric_Json['data']['Chassis'][i]['Fabric Modules'] = []

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
                
                #We complete the Line Cards List into the Chassis ID i with the supervisor information
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

                #We complete the System Controller info into the Chassis ID i
                for k in range (0, len(self.__SystemController_List[i].getSystemControllerList())):
                    SystemControllerModule = {
                        'Description' : self.__SystemController_List[i].getDescription(k),
                        'Hardware Version' : self.__SystemController_List[i].getHardwareVersion(k),
                        'System Controller ID' : self.__SystemController_List[i].getSystemControllerID(k),
                        'Manufacturing Time' : self.__SystemController_List[i].getManufacturingTime(k),
                        'Last time Object modified' : self.__SystemController_List[i].getLastTimeModified(k),
                        'Model' : self.__SystemController_List[i].getModel(k),
                        'Operational Status' : self.__SystemController_List[i].getOperationalStatus(k),
                        'Power Status' : self.__SystemController_List[i].getPowerStatus(k),
                        'System Controller HA Status' : self.__SystemController_List[i].getSystemController_HA_Status(k),
                        'Serial Number' : self.__SystemController_List[i].getSerialNumber(k),
                        'System Controller Uptime' : self.__SystemController_List[i].getSystemControllerUptime(k),
                        'System Controller Vendor' : self.__SystemController_List[i].getVendor(k)
                    }
                    Fabric_Json['data']['Chassis'][i]['System Controller'].append(SystemControllerModule)

                #We complete the Fabric Module info into the Chassis ID i
                for k in range (0, len(self.__FabricModule_List[i].getFabricModuleList())):
                    FabricModule = {
                        'Description' : self.__FabricModule_List[i].getDescription(k),
                        'Hardware Version' : self.__FabricModule_List[i].getHardwareVersion(k),
                        'Fabric Module ID' : self.__FabricModule_List[i].getFabricModuleID(k),
                        'Manufacturing Time' : self.__FabricModule_List[i].getManufacturingTime(k),
                        'Last time Object modified' : self.__FabricModule_List[i].getLasttimemodified(k),
                        'Model' : self.__FabricModule_List[i].getModel(k),
                        'Operational Status' : self.__FabricModule_List[i].getOperationalStatus(k),
                        'Power Status' : self.__FabricModule_List[i].getPowerStatus(k),
                        'Fabric Module Status' : self.__FabricModule_List[i].getHA_Status(k),
                        'Serial Number' : self.__FabricModule_List[i].getSerialNumber(k),
                        'Type' : self.__FabricModule_List[i].getType(k),
                        'Fabric Module Uptime' : self.__FabricModule_List[i].getFabricModuleUptime(k),
                        'Vendor' : self.__FabricModule_List[i].getVendor(k)
                    }
                    Fabric_Json['data']['Chassis'][i]['Fabric Modules'].append(FabricModule)


        #We use the Date Class in order to know when the Output File was created
        today = date.today()
        
        #We create the Filename based on the APIC name and Date
        Filename =  "Inventory" + "-" + self.__FabricName['imdata'][0]['infraCont']['attributes']['fbDmNm'] + "-" + today.strftime("%d-%m-%Y") + ".json"

        #We create the JSON File
        #If the File exist we override the file
        try:
            OutputFile = open( Filename , "x" )
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

        #Variable for frame Size, in our Script value 72
        FrameSize = len("|                      Retriving data from APIC                        |")

        #Print only if the verbose mode was enable
        if self.__args.v:
            
            #Print the Information collected by the APICs
            self.printAux()     
            print("|                      Retriving data from APIC                        |")
            self.printAux()

        #Variable that store Fabric Name in the Fabric
        FabricName = self.__get_request(self.__URLs['URLs']['Fabric_Name_Second_Option'] % self.__Constant.apic)

        #Variable that store number of nodes in the Fabric
        numNodes = self.__get_request(self.__URLs['URLs']['Num_Nodes_Plus_IDs'] % self.__Constant.apic)

        #Variable that store all the IDs information in JSON format
        FABRIC_IDS = self.__get_request(self.__URLs['URLs']['Num_Nodes_Plus_IDs'] % self.__Constant.apic)

        #Print only if the verbose mode was enable
        if self.__args.v:
            #Print The process of the Fabric Name
            Name_Index = len("|     Retriving Fabric Name: %s" % colored(FabricName['imdata'][0]['infraCont']['attributes']['fbDmNm'],'green'))

            print("|     Retriving Fabric Name: %s" % colored(FabricName['imdata'][0]['infraCont']['attributes']['fbDmNm'],'green') + ' ' * ((FrameSize - Name_Index) + 7), "|")

            #Cheking the difference between the output and free space
            index_aux = len("|     Number of Nodes in the Fabric: %s" + numNodes['totalCount'])

            #Printing the total devices in the Fabric
            print("|     Number of Nodes in the Fabric: %s" % colored(numNodes['totalCount'], 'green') + ' ' * (FrameSize - index_aux), "|")

            self.printAux()

        #Object creation with for loop
        for i in range( 0, int(FABRIC_IDS['totalCount'] )):

            #Build Node ID List with all Nodes ID in the fabric
            self.__Node_ID_List.append( FABRIC_IDS['imdata'][i]['fabricNode']['attributes']['id'] )

            #Build Chassis List with all the information about Node Chassis
            self.__Chassis_List.append( ChassisClass ( self.__Constant.apic , self.__Chassis_Query , self.__Node_ID_List[i] , self.__URLs['URLs']['Chassis'] ))

            #Print only if the verbose mode was enable
            if self.__args.v:
                    self.__print_Node_Info("Retriving", self.__Node_ID_List[i], self.__Chassis_List[i].getRole(), FrameSize, True, "red")

            #Build Supervisor List with the information about the supervisors
            if(int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number):
                self.__Supervisor_List.append( SupervisorClass ( self.__Constant.apic , self.__Supervisor_Query , self.__Node_ID_List[i] , self.__URLs['URLs']['Supervisor'] ))
            else:
                self.__Supervisor_List.append(0)

            #Print only if the verbose mode was enable
            if self.__args.v:
                    self.__print_Node_Info("Processing", self.__Node_ID_List[i], self.__Chassis_List[i].getRole(), FrameSize, True, "yellow")

            #Build LineCard List with the information about the Line Cards
            if(int(self.__Node_ID_List[i]) > self.__Constant.APIC_Number):
                self.__LineCards_List.append( LinesCardModule ( self.__Constant.apic , self.__LineCards_Query , self.__Node_ID_List[i] , self.__URLs['URLs']['Linecards'] ))
            else:
                self.__LineCards_List.append(0)

            #Build Power Supply Lists with the information about Power Supply Node
            self.__PowerSupply_List.append( PowerSupplyUnitsClass ( self.__Constant.apic , self.__PowerSupply_Query , self.__Node_ID_List[i] , self.__URLs['URLs']['Power_Supply'] ))

            #Build System Controller Lists
            self.__SystemController_List.append(SystemControllerModule (self.__Constant.apic , self.__SystemController_Query , self.__Node_ID_List[i] , self.__URLs['URLs']['System_Controller']))

            #Build Fabric Module List
            self.__FabricModule_List.append(FabricModuleControllers (self.__Constant.apic , self.__FabricModule_Query , self.__Node_ID_List[i] , self.__URLs['URLs']['Fabric_Module']))

            #Print only if the verbose mode was enable
            #This part show the completed process
            if self.__args.v:
                    self.__print_Node_Info("Completed", self.__Node_ID_List[i], self.__Chassis_List[i].getRole(), FrameSize, False, "green")

        #Print only if the verbose mode was enable
        if self.__args.v:

            #We use the Date Class in order to know when the Output File was created
            today = date.today()
        
            #We create the Filename based on the APIC name and Date
            Filename =  "Inventory" + "-" + FabricName['imdata'][0]['infraCont']['attributes']['fbDmNm'] + "-" + today.strftime("%d-%m-%Y") + ".json"

            #Print Last 
            self.printAux()

            #Filename Size
            FilenameJsonFileSize = len("|     File Name: %s" % Filename)

            #Print Last 
            self.printAux()

            #Generating JSON File name Size
            GenJsonFileSize = len("|     Generating JSON File: %s" % colored('Complete', 'green'))

            #Print JSON File Name
            print("|     Generating JSON File: %s" % colored('Complete', 'green'), '     ' ,' ' * (FrameSize - GenJsonFileSize), "|")
            print("|     File Name: %s" % colored(Filename, 'green'),' ' * (FrameSize - FilenameJsonFileSize - 3), "|")