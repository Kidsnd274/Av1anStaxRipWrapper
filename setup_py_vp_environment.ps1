# Place me in StaxRip\Apps\Encoders\Av1anStaxRipWrapper
echo "Creating Portable VapourSynth install..."
mkdir temp
cd temp
Invoke-WebRequest -Uri "https://www.7-zip.org/a/7zr.exe" -OutFile "7z.exe"
Invoke-WebRequest -Uri "https://github.com/vapoursynth/vapoursynth/releases/download/R61/VapourSynth64-Portable-R61.7z" -OutFile "VapourSynth64-Portable-R61.7z"
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.10.9/python-3.10.9-embed-amd64.zip" -OutFile "python-3.10.9-embed-amd64.zip"
mkdir ..\VapourSynth
cd ..\VapourSynth
..\temp\7z.exe x ..\temp\VapourSynth64-Portable-R61.7z -y
Expand-Archive ..\temp\python-3.10.9-embed-amd64.zip -DestinationPath . -Force
Remove-Item -Recurse -Force ..\temp
echo "Setting up Python modules psutil"
Invoke-WebRequest -Uri "https://bootstrap.pypa.io/get-pip.py" -OutFile "get-pip.py"
.\python.exe get-pip.py
(Get-Content python310._pth) -replace '#import site', 'import site' | Out-File -encoding ASCII python310._pth
.\Scripts\pip.exe install psutil
echo "Copying lsmas ffms2 to VapourSynth plugin directory"
copy ..\..\..\Plugins\Dual\FFMS2\ffms2.dll .\vapoursynth64\plugins
copy ..\..\..\Plugins\Dual\L-Smash-Works\LSMASHSource.dll .\vapoursynth64\plugins
pause