# -- Python class to store, change and write OpenFOAM case data

# --    usage:
# --        1) load OpenFOAMCase from baseCase or from the different OpenFOAMCase
# --            -- loadOFCaseFromBaseCase(baseDir)
# --                    baseDir -- base case directory
# --            -- loadOFCaseFromOFCase(parent)
# --                    parent -- OpenFOAMCase you want to load from
# --        2) (optional) change OpenFOAMCase.dir (where the changes will be made), default -- baseDir
# --            -- changeOFCaseDir(dir)
# --        3) (optional) copy OpenFOAMCase.basedir to OpenFOAMCase.dir
# --            -- copyBaseCase()
# --        4) specify what you want to modify in openFoam source files:
# --            options:            
# --                a) replace(in, what, by)
# --                        inFl -- openFoam source file you want to change
# --                        what -- what you want to replace (string)
# --                        by -- new value (string)
# --        5) make above specified changes to files in OpenFOAMCase.dir
# --            -- applyChangesInDir()
# --        6) run commands in OpenFOAMCase.dir
# --            -- runCommand(commands)

# -- imports 
import numpy as np
import os
import shutil as sh

class OpenFOAMCase:
    
    """initialization of the new OpenFOAMCase"""
    def __init__(self):
        # -- save starting directory
        self.whereIStart = os.getcwd()
        print("New OpenFOAMCase has been initialized, starting directory is:\n\t%s"%self.whereIStart)
    
    """load OpenFOAMCase from base case directory"""
    def loadOFCaseFromBaseCase(self, baseDir):
        print("OpenFOAMCase.baseCase has been set to :\n\t%s" % baseDir)
        self.baseDir = baseDir
        # -- OpenFOAMCase directory is initialized as its baseDir, can be changed by changeOFCaseDir(dir)
        self.dir = baseDir
    
    """load OpenFOAMCase from the different OpenFOAMCase"""
    def loadOFCaseFromOFCase(self, parent):
        print("OpenFOAMCase has been loaded from parent OpenFOAMCase.")
    
    """change OpenFOAMCase directory"""
    def changeOFCaseDir(self,dir):
        self.dir = dir
        print("OpenFOAMCase directory has been changed from:\n\t%s to %s."%(self.baseDir,dir))

    """copy OpenFOAMCase.baseDir to OpenFOAMCase.dir"""
    def copyBaseCase(self):
        # -- if OpenFOAMCase.dir exists, remove it
        if os.path.isdir(self.dir): 
            sh.rmtree(self.dir)

        # -- copy baseDir to dir
        sh.copytree(self.baseDir,self.dir)
        print("OpenFOAMCase.baseDir has been copied to OpenFOAMCase.dir:\n\t %s --> %s"%(self.baseDir,self.dir))

    """replace option -- replace inFl (file) what (string) by (string)"""
    def replace(self, inFl, what, by):
        self.replaces.append([inFl, what, by])
    
    """apply changes in OpenFOAMCase dir"""
    def applyChangesInDir(self):
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
                    print("In %s, I have replaced %s by %s." % (inFl, what, by))
            with open(inFl, 'w') as fl:
                for lnI in range(len(linesInFl)):
                    fl.writelines(linesInFl[lnI])

        # -- move back where I start
        os.chdir(self.whereIStart)
    
    """run commands in OpenFOAMCase dir"""
    def runCommand(self,commands):
        # -- move to OpenFOAMCase directory 
        os.chdir(self.dir)

        # -- runCommand
        print("I will execute commands in %s:"%self.dir)
        for commandI in range(len(commands)):
            command = commands[commandI]
            print("\t%d. %s"%(commandI+1,command))
            os.system(command)
        
        # -- move back where I start
        os.chdir(self.whereIStart)

    
