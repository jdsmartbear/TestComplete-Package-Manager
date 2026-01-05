[Setup]
AppName=TestComplete Package Manager
AppVersion=0.1.1
DefaultDirName={commonpf}\TestComplete Package Manager
DefaultGroupName=TestComplete Package Manager
OutputBaseFilename=tcpm-setup
Compression=lzma
SolidCompression=yes
ArchitecturesInstallIn64BitMode=x64os
PrivilegesRequired=admin
UninstallDisplayName=TestComplete Package Manager
UninstallFilesDir={app}

[Files]
Source: "dist\tcpm.exe"; DestDir: "{app}"; Flags: ignoreversion

[Registry]
; Add install directory to system PATH
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; \
    ValueType: expandsz; ValueName: "Path"; \
    ValueData: "{olddata};{app}"; \
    Check: NeedsAddPath

[Code]
function NeedsAddPath(): Boolean;
var
  Paths: string;
begin
  if RegQueryStringValue(
    HKLM,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path',
    Paths
  ) then
    Result := Pos(ExpandConstant('{app}'), Paths) = 0
  else
    Result := True;
end;