#OV DynamoPythonProject

#Import Common Language Runtime CLR
import clr

#Add and Import RevitServices Reference
clr.AddReference("RevitServices")
import RevitServices

#Import DocumentManager and TransactionManager
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

#Get the current Revit Document
doc = DocumentManager.Instance.CurrentDBDocument

#Dynamo Inputs
input = IN[0]
inputU = UnwrapElement(IN[0])

#Start a Transaction
TransactionManager.Instance.EnsureInTransaction(doc)

#Code Here
##

#Finish Transaction
TransactionManager.Instance.TransactionTaskDone()

#Output
OUT = "output"
