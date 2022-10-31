import os, sys;
import resource;

class Utils:
    
    @staticmethod
    def printMemoryConsumption(process):
        print("Process memory by method 1: " + str(process.memory_info().rss / 1000000) + "MB");
        # print("Process memory method2: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000 ) + "MB" );

        
        