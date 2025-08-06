# sensors/network_sensor.py - v1

import psutil

def get_network_info():
    net_io = psutil.net_io_counters()
    return {
        "sent": f"{net_io.bytes_sent // (1024 ** 2)} MB",
        "recv": f"{net_io.bytes_recv // (1024 ** 2)} MB",
        "packets_sent": net_io.packets_sent,
        "packets_recv": net_io.packets_recv,
    }
