import subprocess
import os
import platform

os.chdir('/home/rcarpenter')

# if os.uname_result
disk = subprocess.run(["wsl.exe", "-d", "Ubuntu-20.04", "--", "bash", "-lc", "df -h /mnt/c"], capture_output=True, text=True, check=False)

print(disk.returncode)
print(disk.stdout)
print(disk.stderr)
print(platform.uname())


# print(disk_location)