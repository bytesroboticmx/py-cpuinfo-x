#Programa que utiliza la librería cpuinfo para mostrar información de la CPU
#Autor:
#Matrícula:
#Version:
#Fecha:
import cpuinfo

def mostrar_informacion_cpu():
    info_cpu = cpuinfo.get_cpu_info()
    print("Información de la CPU:")
    print(f"Nombre del procesador: {info_cpu.get('brand_raw', 'Información no disponible')}")
    print(f"Fabricante: {info_cpu.get('vendor_id_raw', 'Información no disponible')}")
    print(f"Modelo: {info_cpu.get('brand_raw', 'Información no disponible')}")
    print(f"Arquitectura: {info_cpu.get('arch', 'Información no disponible')}")
    print(f"Núcleos físicos: {info_cpu.get('count', 'Información no disponible')}")
    print(f"Frecuencia: {info_cpu.get('hz_advertised_friendly', 'Información no disponible')}")
    print(f"Cache L1: {info_cpu.get('l1_data_cache_size', 'Información no disponible')}")
    print(f"Soporte de 64 bits: {info_cpu.get('bits', 'Información no disponible')}")
    print(f"Soporte de virtualización: {info_cpu.get('vmx', 'Información no disponible')}")
    print(f"Soporte de Hyper-Threading: {info_cpu.get('ht', 'Información no disponible')}")

if __name__ == "__main__":
    mostrar_informacion_cpu()
