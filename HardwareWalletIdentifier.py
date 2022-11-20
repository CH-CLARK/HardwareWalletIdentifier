import winreg

def main():
    access_registry = winreg.ConnectRegistry(None,winreg.HKEY_LOCAL_MACHINE)
    access_key = winreg.OpenKey(access_registry,r'SYSTEM\ControlSet001\Enum\USB')
    
    connected_devices = []

    print('Previously connected devices:')
    print("----------------------------------------")
    for n in range(1000):
        try:
            x = winreg.EnumKey(access_key,n)
            print(x)
            connected_devices.append(x)
            
        except:
            break
    print("----------------------------------------")
    print('The following Hardware Wallet may have been connected to this device: ')

    #BitBox
    if any('VID_03EB&PID_2402' in s for s in connected_devices):
        print(' - BitBox01 Hardware Wallet')

    if any('VID_03EB&PID_2403' in s for s in connected_devices):
        print(' BitBox02 Hardware Wallet')

    #JuBiter Blade
    if any('VID_096E&PID_0891' in s for s in connected_devices):
        print(' - JuBiter Blade Hardware Wallet')
    
    #Optimum
    if any('VID_1209&PID_AAAA' in s for s in connected_devices):
        print(' - Optimum Hardware Wallet')

    #SafeWISE CoinSafe
    if any('VID_1209&PID_ABBA' in s for s in connected_devices):
        print(' - SafeWISE CoinSafe Hardware Wallet')
    
    #Trezor
    if 'VID_1209&PID_53C0' in connected_devices or 'VID_1209&PID_53C1' in connected_devices:
        print(' - Trezor Hardware Wallet')

    #Monero 
    if 'VID_1209&PID_B0B0' in connected_devices or 'VID_1209&PID_C0DA' in connected_devices or 'VID1209&PID_D00D' in connected_devices:
        print(' - Monero Hardware Wallet')

    #Secalot
    if 'VID_1209&PID_7000' in connected_devices or 'VID_1209&PID_7001' in connected_devices:
        print(' - Secalot Hardware Wallet')

    #OpenDime
    if any('VID_1209&PID_7551' in s for s in connected_devices):
        print(' - OpenDime Hardware Wallet')

    #Opolo
    if 'VID_1209&PID_9998' in connected_devices or 'VID_1209&PID_9999' in connected_devices:
        print(' - Opolo Hardware Wallet')
    

if __name__ == '__main__':
    main()