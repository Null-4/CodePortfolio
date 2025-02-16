#1st attempt at a powershell script

#set the error preferences
$oldErrorPreference = $ErrorActionPreference

$ErrorActionPreference = "Stop"

#this section is going to ask for the file

$filepath = Read-Host "Please enter the files name or path"

    #checking if file exists and then opens it or creats it
try{
    if (Test-Path $filepath) {
        Write-Host "Found requested file! opening with notebook..."
        Start-Process notepad.exe $filepath
    }
    else {
        Write-Host "File not found or doesnt exist! Creating file and opening..."
        New-Item -Path $filepath -ItemType File
        Start-Process Notepad.exe $filepath 
    }
}
catch{
    Write-host "Error found: $($_.Exception.message)"
}
finally{
    $ErrorActionPreference = $oldErrorPreference
}