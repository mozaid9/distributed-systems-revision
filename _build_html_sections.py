import subprocess
import sys
from pathlib import Path


SCRIPTS = [
    "_s01_crypto.py",
    "_s02_tls.py",
    "_s03_iam.py",
    "_s04_architecture.py",
    "_s05_apis.py",
    "_s06_express.py",
    "_s07_apidocs.py",
    "_s08_messaging.py",
    "_s09_cloud.py",
    "_s10_resilience.py",
    "_s11_containers.py",
    "_s12_kubernetes.py",
    "_s13_data.py",
    "_s14_networking.py",
    "_s15_terraform.py",
    "_s16_code_reading.py",
    "_s17_diagrams.py",
    "_s18_technique.py",
    "_s19_rapid.py",
]


def main():
    base = Path(__file__).resolve().parent
    for name in SCRIPTS:
        subprocess.run([sys.executable, str(base / name)], check=True)


if __name__ == "__main__":
    main()
