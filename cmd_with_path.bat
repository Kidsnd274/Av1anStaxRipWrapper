@echo off
REM This batch script needs to be run in StaxRip\Apps\Encoders\Av1anStaxRipWrapper!
echo.
echo This batch script needs to be run in StaxRip\Apps\Encoders\Av1anStaxRipWrapper!
SET PATH=..\Av1an;..\aomenc;..\rav1e;..\SVT-AV1;..\x264;..\x265;..\..\Support\MKVToolNix;.\VapourSynth;%PATH%
echo =================================================
echo Av1anStaxRipWrapper
echo https://github.com/Kidsnd274/Av1anStaxRipWrapper
echo.
echo Path set, you can now access encoder tools
echo No need to use -s flag for scripts
echo =================================================
echo.
cmd /K
exit