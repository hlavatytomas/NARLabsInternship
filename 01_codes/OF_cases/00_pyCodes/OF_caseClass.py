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
import sh

class OpenFOAMCase:
    
    """initialization of the new OpenFOAMCase"""
    def __init__(self):
        print("New OpenFOAMCase has been initialized.")
        pass
    
    """load OpenFOAMCase from base case directory"""
    def loadOFCaseFromBaseCase(self, baseDir):
        print("OpenFOAMCase has been loaded from base case directory:\n\t%s" % baseDir)
        self.baseDir = baseDir
        # -- OpenFOAMCase directory is initialized as its baseDir, can be changed by changeOFCaseDir(dir)
        self.dir = baseDir
    
    """load OpenFOAMCase from the different OpenFOAMCase"""
    def loadOFCaseFromOFCase(self, parent):
        print("OpenFOAMCase has been loaded from parent OpenFOAMCase with baseCase directory:\n\t\nand the following replaces:\n\t" % (parent.baseDir, parent.replaces))
    
    """change OpenFOAMCase directory"""
    def changeOFCaseDir(self,dir):
        self.dir = dir

    """replace option -- replace inFl (file) what (string) by (string)"""
    def replace(self, inFl, what, by):
        self.replaces.append([inFl, what, by])
    
    """apply changes in OpenFOAMCase dir"""
    def applyChangesInDir(self):
        # -- save path where I start
        whereStart = os.getcwd()
        
        # -- move to OpenFOAMCase directory 
        os.chdir(self.dir)

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

        # -- move back where I start
        os.chdir(whereStart)
    
    """copy OpenFOAMCase.baseDir to OpenFOAMCase.dir"""
    def copyBaseCase(self):
        # -- if OpenFOAMCase.dir exists, remove it
        if os.path.isdir(self.dir): 
            sh.rmtree(self.dir)
        
        # -- copy baseDir to dir
        sh.copytree(self.baseDir,self.dir)

    
