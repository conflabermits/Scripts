@echo off

SET SOURCE=c:\local\
SET DESTINATION=y:\autoBackup\REWL7060_local\

SET /P ANSWER=Do you want to back up your files from %SOURCE% to %DESTINATION% now? (Y/N)?
echo You chose: %ANSWER%
if /i {%ANSWER%}=={y} (goto :yes)
if /i {%ANSWER%}=={yes} (goto :yes)
goto :no

:yes
robocopy %SOURCE% %DESTINATION% /V /MIR /NP /TEE /XF autoBackupLog.txt /LOG:%SOURCE%autoBackupLog.txt
robocopy %SOURCE% %DESTINATION% autoBackupLog.txt /V
echo Log is saved as %SOURCE%autoBackupLog.txt
pause
exit /b 0

:no
exit /b 1

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
