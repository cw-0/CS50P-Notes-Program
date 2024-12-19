import math


RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

raw = []
with open("Numbers.txt", "r") as file:
    for line in file:
        raw.append(line.strip())


numbers = ["1", "2", "3", "4", "5"]

integers = set()
for number in numbers:
    integers.add(number)


sorted_nums = []
for integer in integers:
    sorted_nums.append(integer)



max_num = max(integers)

print("\nSample\n")
print(f"All Numbers: {", ".join(integers)}")
print(f"Numbers Sorted: {", ".join(sorted(sorted_nums))}")
print(f"{GREEN}Highest Value:{RESET} {RED}{int(max_num):,}{RESET}")
print("\n")
print(f"Raw File:\n{YELLOW}{", ".join(raw)}{RESET}")
print(f"\n{GREEN}Highest Value in File:{RESET} {RED}{int(max(raw)):,}{RESET}\n\n")