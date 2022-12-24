curl --output get-pip.py https://bootstrap.pypa.io/get-pip.py
.\python.exe get-pip.py
.\Scripts\pip.exe install psutil
powershell -Command "(Get-Content python39._pth) -replace '#import site', 'import site' | Out-File -encoding ASCII python39._pth"
REM (Get-Content python39._pth) -replace '#import site', 'import site' | Out-File -encoding ASCII python39._pth