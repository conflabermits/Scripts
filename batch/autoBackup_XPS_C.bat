@echo off

SET SOURCE=C:
SET DESTINATION=B:\XPS\C

if "%1"=="/y" (goto :yes)

SET /P ANSWER=Do you want to back up your files from %SOURCE%\ to %DESTINATION%\ now? (Y/N)?
echo You chose: %ANSWER%
if /i {%ANSWER%}=={y} (goto :yes)
if /i {%ANSWER%}=={yes} (goto :yes)
goto :no

:no
exit /b 1

:yes
robocopy %SOURCE%\ %DESTINATION%\ /V /MIR /NP /TEE /SL /R:2 /W:3 /XF autoBackupLog.txt pagefile.sys hiberfil.sys swapfile.sys "%SOURCE%\bootmgr" "%SOURCE%\BOOTSECT.BAK" /XD %SOURCE%\RECYCLER %SOURCE%\$RECYCLE.BIN "%SOURCE%\System Volume Information" "%SOURCE%\Boot" "%SOURCE%\Recovery" "%SOURCE%\VirtualStore" "%SOURCE%\PerfLogs" "%SOURCE%\Documents and Settings" "%SOURCE%\ProgramData\Microsoft\Crypto" "%SOURCE%\Users\All Users\Microsoft\Crypto" "%SOURCE%\Windows\System32\winevt\Logs" "%SOURCE%\Windows\System32\wbem\AutoRecover" "%SOURCE%\ProgramData\Microsoft\Windows\WER" "%SOURCE%\Users\All Users\Microsoft\Windows\WER" "%SOURCE%\ProgramData\Application Data\Application Data" "%SOURCE%\Users\chris\AppData\Local\Application Data\Application Data" "%SOURCE%\Users\All Users\Application Data\Application Data" "%SOURCE%\Users\chris\Local Settings\Application Data\Application Data" "%SOURCE%\ProgramData\Application Data\Microsoft\Diagnosis" "%SOURCE%\Windows.old" /LOG:%DESTINATION%\autoBackupLog_C.txt
echo Log is saved as %DESTINATION%\autoBackupLog_C.txt
attrib -a -h -s %DESTINATION%
REM exit /b 0

REM Usage :: ROBOCOPY source destination [file [file]...] [options]
REM /E makes Robocopy recursively copy subdirectories, including empty ones.
REM /XN excludes existing files newer than the copy in the source directory. Robocopy normally overwrites those.
REM /V :: produce Verbose output, showing skipped files.
REM /PURGE :: delete dest files/dirs that no longer exist in source.
REM /NP :: No Progress - don't display percentage copied.
REM /TEE :: output to console window, as well as the log file.
REM /XF file [file]... :: eXclude Files matching given names/paths/wildcards.
REM /LOG:file :: output status to LOG file (overwrite existing log).
REM /LOG+:file :: output status to LOG file (append to existing log).
REM /R:n :: number of Retries on failed copies: default 1 million.
REM /W:n :: Wait time between retries: default is 30 seconds.