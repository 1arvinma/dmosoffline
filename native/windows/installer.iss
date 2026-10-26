#define Root AddBackslash(SourcePath) + "..\.."
[Setup]
AppId={{1E186B2C-AC25-4D86-BC29-F605F160E2D1}
AppName=DMOS Table
AppVersion=1.2.0
AppPublisher=Quest LLC / quest.rasht
DefaultDirName={localappdata}\Programs\DMOS Table
DefaultGroupName=DMOS Table
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputDir={#Root}\dist
OutputBaseFilename=DMOS-OpenSource-1.2.0-Windows-Setup
Compression=lzma2/fast
SolidCompression=no
WizardStyle=modern
UninstallDisplayIcon={app}\DMOS.exe
CloseApplications=yes
RestartApplications=no
[Files]
Source: "{#Root}\dist\Windows\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Excludes: "debug.log,chrome_debug.log,*.dmp"
[Tasks]
Name: desktopicon; Description: "Create a desktop shortcut"; Flags: unchecked
[Icons]
Name: "{group}\DMOS Table"; Filename: "{app}\DMOS.exe"
Name: "{autodesktop}\DMOS Table"; Filename: "{app}\DMOS.exe"; Tasks: desktopicon
[Run]
Filename: "{app}\DMOS.exe"; Description: "Open DMOS Table"; Flags: nowait postinstall skipifsilent
