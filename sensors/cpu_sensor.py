# sensors/cpu_sensor.py - v1

import psutil

def get_cpu_info():
    return {
        "usage_percent": psutil.cpu_percent(interval=0.5),
        "core_count": psutil.cpu_count(logical=False),
        "thread_count": psutil.cpu_count(logical=True),
    }
