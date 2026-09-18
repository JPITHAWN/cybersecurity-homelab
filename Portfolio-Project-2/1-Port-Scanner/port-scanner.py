import socket #allows python to access network interface
from concurrent.futures import ThreadPoolExecutor # allows concurrent threads
import argparse #argparse for command line functionality

target = "192.168.56.101" #ip address of target

def singlescan(target, port) -> bool: #scans indicated port and returns bool
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((target, port))
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False

def scanandprint(target, port: int): # calls scanport and prints result to terminal
    if singlescan(target, port):
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSE")

def multiscan(target,lowlim, uplim):
    with ThreadPoolExecutor(max_workers=100) as ex: #j
        for port in range(lowlim, uplim):
            ex.submit(scanandprint, target, port)

parser = argparse.ArgumentParser(description="Simple TCP port scanner")
parser.add_argument("-p", "--port", type=int, help="Scan a single port")
parser.add_argument("-r", "--range", help="Scan a port range, e.g. 1-1000")
args = parser.parse_args()

if args.port:
    scanandprint(target, args.port)
elif args.range:
    lowlim, uplim = map(int, args.range.split("-"))
    multiscan(target, lowlim, uplim + 1)
else:
    multiscan(target, 0, 1024)
