::ECHO Open folder
::add my nvidia-smi folder to PATH variable
::cd /d c:\Program Files\NVIDIA Corporation\NVSMI

::method from https://stackoverflow.com/questions/57100015/how-do-i-run-nvidia-smi-on-windows
ECHO NVIDIA-SMI
::use `-l < time you want it to refresh >` to keep window
call nvidia-smi.exe -l 5