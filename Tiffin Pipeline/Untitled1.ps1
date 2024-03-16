$wshell = New-Object -ComObject WScript.Shell
Start-Process ms-settings:bluetooth
$wshell.SendKeys("{TAB}")
Start-Sleep 2
$wshell.SendKeys("{TAB}")
Start-Sleep 2
$wshell.SendKeys("{TAB}")
Start-Sleep 2
$wshell.SendKeys("{TAB}")
Start-Sleep 2
$wshell.SendKeys("{TAB}")
Start-Sleep 2
$wshell.SendKeys("{TAB}")
Start-Sleep 2
$wshell.SendKeys("%{TAB}")
Start-Sleep 2