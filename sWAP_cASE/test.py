from sWAP_cASE import swap_case as sc

samples = ["Python","GitHub","Hacktoberfest", "Digital Ocean", "Fr4nkl1n1k3h", "PrograMMinG", "snake_case"]

for string in samples:
    print(f"Sample input: {string}")
    print(f"Output: {sc(string)}")