@echo off
REM Place me in StaxRip\Apps\Encoders\Av1anStaxRipWrapper
echo Setting up Python modules (psutil)
cd ..\..\FrameServer\VapourSynth
curl --output get-pip.py https://bootstrap.pypa.io/get-pip.py
.\python.exe get-pip.py
powershell -Command "(Get-Content python39._pth) -replace '#import site', 'import site' | Out-File -encoding ASCII python39._pth"
.\Scripts\pip.exe install psutil
echo Copying lsmas ffms2 to VapourSynth plugin directory (Make sure to disable loading VP plugins!)
copy ..\..\Plugins\Dual\FFMS2\ffms2.dll .\vapoursynth64\plugins
copy ..\..\Plugins\VS\LSmashSource\vslsmashsource.dll .\vapoursynth64\plugins