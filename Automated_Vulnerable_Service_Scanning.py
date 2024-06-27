#!/usr/bin/python3
import subprocess
import os

def run_nmapAutomator(target_ip, scan_type, output_file):

    script_path = os.path.expanduser("~/Downloads/nmapAutomator/nmapAutomator.sh")
    if not os.path.exists(script_path):
        print(f"Error: nmapAutomator.sh script not found at {script_path}")
        return
    
    command = f"{script_path} {target_ip} {scan_type} > {output_file}"
    try:
        subprocess.run(command, shell=True, check=True)
        print("Scanning finished. Results written to", output_file)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running nmapAutomator: {e}")

def get_scan_type_from_user():

    scan_type_mapping = {
        '1': 'network',
        '2': 'port',
        '3': 'script',
        '4': 'full',
        '5': 'udp',
        '6': 'vulns',
        '7': 'recon',
        '8': 'all'
    }
    
    while True:
        user_choice = input("Choose the type of scanning to perform: ")
        if user_choice in scan_type_mapping:
            return scan_type_mapping[user_choice]
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    target_ip = input("Enter the target IP to scan: ")
    
    # Prompt the user to choose the type of scanning
    print("Scan Types:")
    print("1. Network")
    print("2. Port")
    print("3. Script")
    print("4. Full")
    print("5. UDP")
    print("6. Vulns")
    print("7. Recon")
    print("8. All")
    
    scan_type = get_scan_type_from_user()
    
    output_file = input("Enter the name of the output file: ")
    
    print("Scanning started...")
    run_nmapAutomator(target_ip, scan_type, output_file)
