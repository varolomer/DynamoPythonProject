#OV DynamoPythonProject

#Import Common Language Runtime CLR and System
import clr
import sys

#Append Custom Library
#sys.path.append(r'path')

#Add References
clr.AddReference('RevitServices')
clr.AddReference('ProtoGeometry')
clr.AddReference('RevitNodes')
clr.AddReference('RevitAPI')

#Import Libraries
import Revit #Nodes in Dynamo
import Autodesk.DesignScript.Geometry as Geometry #Import Dynamo Geometry Library to interact wit Revit
import Autodesk.Revit.DB as DB #Import DB for direct RevitAPI calls. This requires unwrapping and wrapping

#Import DocumentManager and TransactionManager
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

#Import DSType Method and DYN-Revit Conversion Methods
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

#Get the current Revit Document
doc = DocumentManager.Instance.CurrentDBDocument

#############################################Dynamo Inputs
input = IN[0]
inputU = UnwrapElement(IN[0])
#############################################
#Start a Transaction
TransactionManager.Instance.EnsureInTransaction(doc)

#Code Here
##

#Finish Transaction
TransactionManager.Instance.TransactionTaskDone()

#Output
OUT = "output"
