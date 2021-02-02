ECHO Open folder
::my nvidia-smi folder (nvidia-smi.exe can be found on two different folders, either is ok)
cd /d c:\Program Files\NVIDIA Corporation\NVSMI
::cd /d c:\Windows\System32\DriverStore\FileRepository\nvami.inf_amd64_42b7e5f6a9e28f81

::method from https://stackoverflow.com/questions/57100015/how-do-i-run-nvidia-smi-on-windows
ECHO NVIDIA-SMI
::use `-l < time you want it to refresh >` to keep window
call nvidia-smi.exe -l 3