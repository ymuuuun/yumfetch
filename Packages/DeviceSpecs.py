import platform
import psutil

class Specs:
    def __init__(self) -> None:
        self.system = platform.system()
        self.cpu = platform.processor()
        self.architecture = platform.architecture()[0]
        self.memory = f"Available : {psutil.virtual_memory().available} / Used : {psutil.virtual_memory().used}"
        self.machine = platform.machine()
        self.python_version = platform.python_version()
        self.battery = f"Power Left : {psutil.sensors_battery().percent} / Charging : {psutil.sensors_battery().power_plugged}"
        self.runtime = psutil.boot_time()

        
