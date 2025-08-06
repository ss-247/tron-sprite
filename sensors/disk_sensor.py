# sensors/disk_sensor.py - v1

import psutil

def get_disk_info():
    disk = psutil.disk_usage('/')
    return {
        "total": f"{disk.total // (1024 ** 3)} GB",
        "used": f"{disk.used // (1024 ** 3)} GB",
        "percent": f"{disk.percent}%",
    }
