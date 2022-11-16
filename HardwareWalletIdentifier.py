import winreg

def main():
    access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    access_key = winreg.OpenKey(access_registry,r'SYSTEM\ControlSet001\Enum\USB')
    
    connected_devices = []

    print("Previously connected devices:")
    print("----------------------------------------")
    for n in range(1000):
        try:
            x = winreg.EnumKey(access_key,n)
            print(x)
            
        except:
            break
    print("----------------------------------------")

if __name__ == '__main__':
    main()