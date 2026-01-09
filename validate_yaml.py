import yaml
import sys

try:
    with open(r'f:\Casbin_game\pycasbin\.github\workflows\performance-pr.yml', 'r') as f:
        yaml.safe_load(f)
    print("YAML is valid")
except yaml.YAMLError as exc:
    print(f"YAML Error: {exc}")
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
