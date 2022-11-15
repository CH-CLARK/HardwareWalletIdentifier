import winreg

def main():
    access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    access_key = winreg.OpenKey(access_registry,r'SYSTEM\ControlSet001\Enum\USB')
    


if __name__ == '__main__':
    main()