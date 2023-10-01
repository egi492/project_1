import psutil
import platform
from datetime import datetime


def get_size (bytes, suffix="B"):
    factor = 1024
    for unit in ["" , "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

          
print("="*40, "СИСТЕМНАЯ ИНФОРМАЦИЯ" , "="*40 )

uname = platform.uname()
print(f"СИСТЕМА: {uname.system}")
print(f"ИМЯ УЗЛА: {uname.node}")
print(f"ВЫПУСК:{uname.release}")
print(f"ВЕРСИЯ:{uname.version}")
print(f"МАШИНА:{uname.machine}")
print(f"ПРОЦЕССОР:{uname.processor}")


print("="*40, "ИНФОРМАЦИЯ О ПРОЦЕССОРЕ" , "="*40 )

print("ФИЗИЧЕСКИЕ ЯДРА:",psutil.cpu_count(logical=False))
print("ВСЕГО ЯДЕР:",psutil.cpu_count(logical=True))

cpufreq = psutil.cpu_freq()
print(f"МАКСИМАЛЬНАЯ ЧАСТОТА: {cpufreq.max:.2f}Mгц")
print(f"МИНИМАЛЬНАЯ ЧАСТОТА: {cpufreq.min:.2f}Mгц")
print(f"ТЕКУЩАЯ ЧАСТОТА: {cpufreq.current:.2f}Mгц")

print("ЗАГРУЖЕННОСТЬ ПРОЦЕССОРА НА ЯДРО:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"ЯДРО {i}: {percentage} %")
print(f"ОБЩАЯ ЗАГРУЖЕННОСТЬ ПРОЦЕССОРА: {psutil.cpu_percent()}%")


print("="*40, "ОБЩАЯ ИНФОРМАЦИЯ О ПАМЯТИ" , "="*40 )

svmen = psutil.virtual_memory()
print(f"ОБЪЕМ: {get_size(svmen.total)}")
print(f"СВОБОДНО: {get_size(svmen.free)}")
print(f"ИСПОЛЬЗУЕТСЯ: {get_size(svmen.used)}")
print(f"ПРОЦЕНТ: {svmen.percent}%")

print("="*40, "ПАМЯТЬ ПОДКАЧКИ" , "="*40 )

swap = psutil.swap_memory()
print(f"ОБЪЕМ: {get_size(swap.total)}")
print(f"СВОБОДНО: {get_size(swap.free)}")
print(f"ИСПОЛЬЗУЕТСЯ: {get_size(swap.used)}")
print(f"ПРОЦЕНТ: {swap.percent}%")


print("="*40, "ИНФОРМАЦИЯ О ДИСКЕ" , "="*40 )

partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== ДИСК: {partition.device} ===")
    print(f" ТИП ФАЙЛОВОЙ СИСТЕМЫ: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue 
    print(f" ОБЩИЙ ОБЪЁМ: {get_size(partition_usage.total)}")
    print(f" ИСПОЛЬЗУЕТСЯ: {get_size(partition_usage.used)}")
    print(f" СВОБОДНО: {get_size(partition_usage.free)}")
    print(f" ПРОЦЕНТ: {partition_usage.percent}%")
