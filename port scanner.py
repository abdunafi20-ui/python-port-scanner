import socket

target = input("Enter target IP: ")

print(f"\n[+] Scanning target: {target}\n")

# Open file to save results
file = open("scan_results.txt", "w")
file.write(f"Scan results for {target}\n\n")

# Scan ports 1 to 1000
for port in range(1, 1001):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            file.write(f"[OPEN] Port {port}\n")
            try:
                s.send(b"Hello\r\n")
                banner = s.recv(1024).decode().strip()
                print(f"   ↳ Service: {banner}")
                file.write(f"   ↳ Service: {banner}\n")
            except:
                pass

        s.close()

    except KeyboardInterrupt:
        print("\n[!] Scan stopped by user")
        break

    except socket.gaierror:
        print("[!] Hostname could not be resolved")
        break

    except socket.error:
        print("[!] Could not connect to server")
        break

file.close()

print("\n[✔] Scan completed. Results saved to scan_results.txt")