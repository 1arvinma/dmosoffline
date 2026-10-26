#include "version.iss"
#define Root AddBackslash(SourcePath) + "..\.."
[Setup]
AppId={{1E186B2C-AC25-4D86-BC29-F605F160E2D1}
AppName=DMOS Table
AppVersion={#DMOSVersion}
AppPublisher=Quest LLC / quest.rasht
DefaultDirName={localappdata}\Programs\DMOS Table
DefaultGroupName=DMOS Table
PrivilegesRequired=lowest
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
OutputDir={#Root}\dist
OutputBaseFilename=DMOS-OpenSource-{#DMOSVersion}-Windows-Setup
Compression=lzma2/fast
SolidCompression=no
WizardStyle=modern
UninstallDisplayIcon={app}\DMOS.exe
CloseApplications=yes
RestartApplications=no
UsePreviousAppDir=yes
UsePreviousTasks=yes
UsePreviousGroup=yes
[Files]
Source: "{#Root}\dist\Windows\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; Excludes: "debug.log,chrome_debug.log,*.dmp"
[Tasks]
Name: desktopicon; Description: "Create a desktop shortcut"; Flags: unchecked
[Icons]
Name: "{group}\DMOS Table"; Filename: "{app}\DMOS.exe"
Name: "{autodesktop}\DMOS Table"; Filename: "{app}\DMOS.exe"; Tasks: desktopicon
[Run]
Filename: "{app}\DMOS.exe"; Description: "Open DMOS Table"; Flags: nowait postinstall skipifsilent

[Code]
function NextVersionPart(var Value: String): Integer;
var Separator: Integer; Piece: String;
begin
  Separator := Pos('.', Value);
  if Separator > 0 then begin Piece := Copy(Value, 1, Separator - 1); Delete(Value, 1, Separator); end
  else begin Piece := Value; Value := ''; end;
  Result := StrToIntDef(Piece, 0);
end;
function IsNewerVersion(Installed, Proposed: String): Boolean;
var Index, ExistingPart, ProposedPart: Integer;
begin
  Result := False;
  for Index := 1 to 4 do begin
    ExistingPart := NextVersionPart(Installed); ProposedPart := NextVersionPart(Proposed);
    if ExistingPart > ProposedPart then begin Result := True; Exit; end;
    if ExistingPart < ProposedPart then Exit;
  end;
end;
function InitializeSetup(): Boolean;
var InstalledVersion: String;
begin
  Result := True;
  if RegQueryStringValue(HKCU, 'Software\Microsoft\Windows\CurrentVersion\Uninstall\{1E186B2C-AC25-4D86-BC29-F605F160E2D1}_is1', 'DisplayVersion', InstalledVersion) then
    if IsNewerVersion(InstalledVersion, '{#DMOSVersion}') then begin
      MsgBox('A newer DMOS Table version is already installed. This installer will not downgrade it. Use a separate profile and a backup for rollback.', mbError, MB_OK);
      Result := False;
    end;
end;
