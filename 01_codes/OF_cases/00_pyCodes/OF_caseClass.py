# -- Python class to store, change and write OpenFOAM case data

# --    usage:
# --        1) load OpenFOAMCase from baseCase or from the different OpenFOAMCase
# --            -- loadOFCaseFromBaseCase(baseDir)
# --                    baseDir -- base case directory
# --            -- loadOFCaseFromOFCase(parent)
# --                    parent -- OpenFOAMCase you want to load from
# --        2) specify what you want to modify in openFoam source files:
# --            options:            
# --                a) replace(in, what, by)
# --                        inFl -- openFoam source file you want to change
# --                        what -- what you want to replace (string)
# --                        by -- new value (string)
# --        3) write OpenFOAMCase to new directory (destDir)
# --            destDir -- where to write OpenFOAMCase

# -- imports 
import numpy as np
import os

class OpenFOAMCase:
    
    """initialization of the new OpenFOAMCase"""
    def __init__(self):
        print("New OpenFOAMCase has been initialized.")
        pass
    
    """load OpenFOAMCase from base case directory"""
    def loadOFCaseFromBaseCase(self, baseDir):
        print("OpenFOAMCase has been loaded from base case directory:\n\t%s" % baseDir)
        self.baseDir = baseDir
    
    """load OpenFOAMCase from the different OpenFOAMCase"""
    def loadOFCaseFromOFCase(self, parent):
        print("OpenFOAMCase has been loaded from parent OpenFOAMCase with baseCase directory:\n\t\nand the following replaces:\n\t" % (parent.baseDir, parent.replaces))

    """replace option -- replace inFl (file) what (string) by (string)"""
    def replace(self, inFl, what, by):
        self.replaces.append([inFl, what, by])
    
    """write openfoam case to given directory"""
    def writeOFCase(self, destDir):
        # -- copy the base case
        if not os.path.exists(destDir):
            os.makedirs(destDir)
        
        # -- make the replaces
        for replace in self.replaces:
            inFl, what, by = replace
            with open(inFl, 'r') as fl:
                linesInFl = fl.readlines()
            for lnI in range(len(linesInFl)):
                if what in linesInFl[lnI]:
                    linesInFl[lnI] = linesInFl[lnI].replace(what,by)
                    print("I have replaced %s by %s in %s." % (what, by, inFl))
            with open(inFl, 'w') as fl:
                for lnI in range(len(linesInFl)):
                    fl.writelines(linesInFl[lnI])


    
