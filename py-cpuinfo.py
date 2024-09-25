import cpuinfo
def mostrar_informacion_cpu():
    info_cpu = cpuinfo.get_cpu_info()
    print("Información de la CPU:")
    print(f"Nombre del procesador: {info_cpu['brand_raw']}")
    print(f"Fabricante:{info_cpu['vendor_id_raw', 'Informacion no disponible']}")
    print(f"Modelo: {info_cpu['brand']}")
    print(f"Arquitectura: {info_cpu["arch"]}")
    print(f"Núcleos físicos: {info_cpu['count']}")
    print(f"Frecuencia: {info_cpu['hz_advertised_friendly', 'Informacion no disponible']}")
    print(f"Cache L1: {info_cpu['l1_data_cache_size', 'Informacion no disponible']}")
    print(f"Soporte de 64 bits: {info_cpu['bits']}")
    print(f"Soporte de virtualización: {info_cpu['vmx']}")
    print(f"Soporte de Hyper-Threading: {info_cpu['ht']}")

if __name__ == "__main__":
    mostrar_informacion_cpu()
