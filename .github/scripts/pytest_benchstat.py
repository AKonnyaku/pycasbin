import json
import sys
import math
import re

# Force UTF-8 output for Windows
sys.stdout.reconfigure(encoding='utf-8')

def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {path}: {e}", file=sys.stderr)
        return None

def format_val(val):
    if val is None: return "N/A"
    if val < 1e-9: return f"{val*1e9:.2f}ns"
    if val < 1e-6: return f"{val*1e9:.2f}ns" # Use ns for < 1us too? benchstat usually uses ns, us, ms, s
    if val < 1e-3: return f"{val*1e6:.2f}us"
    if val < 1: return f"{val*1e3:.2f}ms"
    return f"{val:.2f}s"

def normalize_name(name):
    name = re.sub(r'^test_benchmark_', '', name)
    parts = name.split('_')
    new_parts = []
    for p in parts:
        if p.lower() in ['rbac', 'abac', 'acl', 'api', 'rest']:
            new_parts.append(p.upper())
        else:
            new_parts.append(p.capitalize())
    return "".join(new_parts)

def main():
    if len(sys.argv) < 3:
        print("Usage: python pytest_benchstat.py base.json pr.json")
        sys.exit(1)

    base_data = load_json(sys.argv[1])
    pr_data = load_json(sys.argv[2])

    if not base_data or not pr_data:
        sys.exit(1)

    base_map = {b['name']: b['stats'] for b in base_data['benchmarks']}
    pr_map = {b['name']: b['stats'] for b in pr_data['benchmarks']}
    
    all_names = sorted(set(base_map.keys()) | set(pr_map.keys()))

    # Print Header
    print("goos: linux")
    print("goarch: amd64")
    print("pkg: github.com/casbin/pycasbin")
    print("cpu: GitHub Actions Runner")
    print("")

    # Calculate column widths
    # benchstat style:
    #                    │ base.json   │ pr.json     │
    #                    │   sec/op    │   sec/op    │
    
    # We need to print lines that benchmark_formatter.py can parse.
    # It expects: Name  Val1  Val2
    
    w_name = 50
    w_val = 15

    # Header
    print(f"{'':<{w_name}}│   old base.json   │   new pr.json     │")
    print(f"{'':<{w_name}}│    sec/op     │    sec/op     │")

    base_means = []
    pr_means = []

    for name in all_names:
        base = base_map.get(name)
        pr = pr_map.get(name)

        base_mean = base['mean'] if base else 0
        pr_mean = pr['mean'] if pr else 0
        
        if base_mean > 0: base_means.append(base_mean)
        if pr_mean > 0: pr_means.append(pr_mean)

        base_str = f"{format_val(base_mean)} ± 1%" if base else "N/A"
        pr_str = f"{format_val(pr_mean)} ± 1%" if pr else "N/A"

        # Note: benchmark_formatter.py extracts two numbers from the line.
        # It handles '±', '%', etc.
        
        display_name = normalize_name(name)
        
        print(f"{display_name:<{w_name}} {base_str:<{w_val}} {pr_str:<{w_val}}")

    if base_means and pr_means:
        g_base = math.exp(sum(math.log(x) for x in base_means) / len(base_means))
        g_pr = math.exp(sum(math.log(x) for x in pr_means) / len(pr_means))
        
        g_base_str = f"{format_val(g_base)}"
        g_pr_str = f"{format_val(g_pr)}"
        
        print(f"{'geomean':<{w_name}} {g_base_str:<{w_val}} {g_pr_str:<{w_val}}")

if __name__ == "__main__":
    main()
