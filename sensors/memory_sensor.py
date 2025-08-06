# sensors/memory_sensor.py - v1

import psutil

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "total": f"{mem.total // (1024 ** 2)} MB",
        "used": f"{mem.used // (1024 ** 2)} MB",
        "percent": f"{mem.percent}%",
    }
