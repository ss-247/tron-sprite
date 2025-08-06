
# core/environment.py - v2

from sensors.cpu_sensor import get_cpu_info
from sensors.memory_sensor import get_memory_info
from sensors.disk_sensor import get_disk_info
from sensors.network_sensor import get_network_info

def get_environment_snapshot():
    snapshot = {
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "network": get_network_info(),
    }
    return snapshot

