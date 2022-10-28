import os, sys;
import resource;

# Importing psutil
sys.stderr = open(os.devnull, "w");
try:
    import psutil;
except:
    print("Actual psutil modules not found");
finally:
    sys.stderr = sys.__stderr__

class Utils:
    
    @staticmethod
    def printMemoryConsumption(process):
        print("Process memory method1: " + str(process.memory_info().rss / 1000000) + "MB");
        # print("Process memory method2: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000 ) + "MB" );

        
        