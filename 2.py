n = int(input())
print(f'{str((n // 3600) % 24).rjust(2, "0")}:{str((n // 60) % 60).rjust(2, "0")}:{str(n % 60).rjust(2, "0")}')
