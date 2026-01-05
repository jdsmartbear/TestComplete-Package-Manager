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

[Files]
Source: "dist\tcpm.exe"; DestDir: "{app}"; Flags: ignoreversion

[Code]

const
  WM_SETTINGCHANGE = $001A;

procedure BroadcastEnvironmentChange();
begin
  SendMessage(HWND_BROADCAST, WM_SETTINGCHANGE, 0, 'Environment');
end;

procedure AddToSystemPath();
var
  PathValue: string;
  AppDir: string;
begin
  AppDir := ExpandConstant('{app}');

  if RegQueryStringValue(
    HKLM,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path',
    PathValue
  ) then
  begin
    if Pos(AppDir, PathValue) = 0 then
    begin
      RegWriteStringValue(
        HKLM,
        'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
        'Path',
        PathValue + ';' + AppDir
      );
      BroadcastEnvironmentChange();
    end;
  end;
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    AddToSystemPath();
  end;
end;