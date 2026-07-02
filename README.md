# PRODIGY_FS_01 - System Administration Automation Suite

A comprehensive automation toolkit for system administrators featuring PowerShell scripts, Python utilities, and batch automation tools for Windows system management.

## 🎯 Overview

PRODIGY_FS_01 is a collection of automation scripts and utilities designed to streamline system administration tasks. It includes PowerShell scripts for advanced system operations, Python utilities for cross-platform automation, and batch files for quick administration tasks.

## 📋 Key Features

- 🔧 **System Configuration** - Automate system setup and configuration
- 🔐 **Security Management** - User account and permission management
- 📊 **System Monitoring** - Monitor system resources and health
- 🗂️ **File Operations** - Batch file processing and management
- 🌐 **Network Administration** - Network configuration and diagnostics
- 📝 **Log Management** - Automated log rotation and analysis
- ⚙️ **Service Management** - Service deployment and management
- 🔄 **Scheduled Tasks** - Create and manage automated tasks

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Primary Scripting** | PowerShell (66.3%) |
| **Utilities** | Python (19.2%) |
| **Configuration** | HTML (5.7%) |
| **System Scripts** | Shell (5.4%) |
| **Batch Processing** | Batchfile (3.4%) |

## 📂 Project Structure

```
PRODIGY_FS_01/
├── Scripts/                    # Main scripts directory
│   ├── PowerShell/
│   │   ├── system-setup.ps1
│   │   ├── user-management.ps1
│   │   ├── backup-automation.ps1
│   │   ├── monitoring.ps1
│   │   └── network-config.ps1
│   ├── Python/
│   │   ├── system_audit.py
│   │   ├── log_parser.py
│   │   └── utils.py
│   ├── Batch/
│   │   ├── cleanup.bat
│   │   └── maintenance.bat
│   └── Shell/
│       └── cross-platform.sh
├── README.md                   # Documentation
└── LICENSE                     # License file
```

## 🔌 Script Components

### **PowerShell Scripts**
Advanced Windows system administration scripts:

#### System Setup
- OS configuration
- Network setup
- Windows Update configuration
- Firewall rules
- Registry modifications

#### User Management
- User account creation/deletion
- Group management
- Permission assignment
- Profile management

#### Backup Automation
- Scheduled backups
- Backup verification
- Restore procedures
- Archive management

#### Monitoring
- System resource monitoring
- Service health checks
- Disk space monitoring
- CPU/Memory tracking
- Event log analysis

#### Network Configuration
- IP configuration
- DNS settings
- Network adapter management
- VPN setup
- Remote access configuration

### **Python Utilities**
Cross-platform automation tools:

#### System Audit
```python
# System auditing capabilities
- Hardware inventory
- Software inventory
- Security audit
- Performance analysis
- Configuration backup
```

#### Log Parser
```python
# Log processing
- Parse various log formats
- Filter and search
- Generate reports
- Alert on errors
- Archive old logs
```

### **Batch Files**
Quick Windows maintenance scripts:

#### Cleanup
- Temporary file removal
- Cache clearing
- Disk optimization
- System restore point creation

#### Maintenance
- Disk defragmentation
- Update checks
- System optimization
- Driver updates

## 🚀 Getting Started

### Prerequisites
- Windows 10/Server 2016 or higher
- PowerShell 5.0+
- Python 3.7+ (for Python scripts)
- Administrator privileges
- Git (optional)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Jananisri05/PRODIGY_FS_01.git
cd PRODIGY_FS_01
```

2. **Or download as ZIP**
   - Extract to desired location
   - Navigate to Scripts directory

### Running PowerShell Scripts

1. **Open PowerShell as Administrator**
```powershell
Start-Process powershell -Verb RunAs
```

2. **Set Execution Policy (if needed)**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3. **Run a script**
```powershell
.\script-name.ps1
```

### Running Python Scripts

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Run Python script**
```bash
python script_name.py
```

### Running Batch Files

1. **Double-click the .bat file**
   Or run from Command Prompt:
```cmd
cd Scripts\Batch
cleanup.bat
```

## 📝 PowerShell Script Examples

### System Setup
```powershell
# Enable Remote Desktop
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name 'fDenyTSConnections' -Value 0

# Configure Windows Firewall
Netsh advfirewall set allprofiles state on
```

### User Management
```powershell
# Create new user
New-LocalUser -Name "Username" -Password (ConvertTo-SecureString "Password" -AsPlainText -Force)

# Add user to group
Add-LocalGroupMember -Group "Administrators" -Member "Username"
```

### System Monitoring
```powershell
# Get CPU usage
Get-WmiObject Win32_Processor | Select-Object LoadPercentage

# Get disk space
Get-Volume | Select-Object DriveLetter, Size, SizeRemaining
```

### Backup Automation
```powershell
# Create scheduled backup
$trigger = New-ScheduledTaskTrigger -Daily -At 2am
$action = New-ScheduledTaskAction -Execute "backup.ps1"
Register-ScheduledTask -TaskName "DailyBackup" -Trigger $trigger -Action $action
```

## 🐍 Python Script Examples

### System Audit
```python
import psutil
import json

def audit_system():
    audit_data = {
        'cpu': psutil.cpu_count(),
        'memory': psutil.virtual_memory().total,
        'disk': psutil.disk_usage('/').total,
        'processes': len(psutil.pids())
    }
    return json.dumps(audit_data, indent=2)
```

### Log Parsing
```python
import re
from datetime import datetime

def parse_log(log_file):
    errors = []
    with open(log_file, 'r') as f:
        for line in f:
            if 'ERROR' in line or 'FAIL' in line:
                errors.append(line.strip())
    return errors
```

## 🔧 Configuration

### PowerShell Configuration File
```powershell
# $PSProfile
$profile = "$PROFILE"

# Add custom functions
function Get-SystemHealth {
    # Implementation
}
```

### Python Configuration
```python
# config.py
CONFIG = {
    'LOG_DIR': 'C:\\Logs',
    'BACKUP_DIR': 'C:\\Backups',
    'RETENTION_DAYS': 30,
    'ALERT_THRESHOLD': 90
}
```

## 📊 System Requirements

### Hardware
- 2GB RAM minimum
- 100MB disk space
- Network connectivity (for remote operations)

### Software
- Windows 10 or later / Windows Server 2016 or later
- .NET Framework 4.5+
- PowerShell 5.0+
- Python 3.7+ (for Python scripts)

## 🔐 Security Considerations

1. **Run with caution** - Always review scripts before execution
2. **Backup first** - Create system restore points
3. **Test in isolated environment** - Test scripts on non-critical systems first
4. **Use signed scripts** - Digitally sign scripts for production
5. **Restrict permissions** - Limit script access to authorized users
6. **Monitor execution** - Enable script block logging

### Enable Script Block Logging
```powershell
New-ItemProperty -Path "HKLM:\Software\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -Name "EnableScriptBlockLogging" -Value 1
```

## 📚 Common Tasks

### Create System Restore Point
```powershell
Checkpoint-Computer -Description "Before Update" -RestorePointType "Manual"
```

### List Running Services
```powershell
Get-Service | Where-Object {$_.Status -eq "Running"}
```

### Check Windows Update Status
```powershell
Get-WindowsUpdate -ListOnly
```

### Export Event Log
```powershell
wevtutil epl Security "C:\Logs\security.evtx"
```

## 🐛 Troubleshooting

### Script Execution Error
```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

### Permission Denied
- Run PowerShell as Administrator
- Check UAC settings
- Verify file permissions

### Python Module Not Found
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 📈 Performance Optimization

- Use parameter validation to catch errors early
- Implement error handling and retry logic
- Use background jobs for long-running tasks
- Cache results when appropriate
- Implement logging for debugging

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/new-script`)
3. Add your script with documentation
4. Test thoroughly
5. Push to branch and submit Pull Request

## 📄 License

[Add your license here]

## ⚠️ Disclaimer

These scripts are provided "as-is" without warranty. The author is not responsible for data loss or system damage resulting from script execution. Always test in a safe environment first.

## 📞 Support

For issues or questions:
- Open a GitHub issue
- Check documentation and examples
- Review PowerShell help: `Get-Help command-name`

## 🎓 Learning Resources

- [PowerShell Documentation](https://docs.microsoft.com/en-us/powershell/)
- [Python Official Docs](https://www.python.org/doc/)
- [Windows Administration](https://docs.microsoft.com/en-us/windows-server/)
- [System Administration Best Practices](https://www.microsoft.com/)

## 🔗 Related Resources

- [PowerShell Gallery](https://www.powershellgallery.com/)
- [GitHub: Awesome PowerShell](https://github.com/janikvonrotz/awesome-powershell)
- [Python PyPI](https://pypi.org/)

---

**Last Updated**: December 2025  
**Language Composition**: PowerShell 66.3%, Python 19.2%, HTML 5.7%, Shell 5.4%, Batchfile 3.4%  
**Status**: Active Development  
**Target Platform**: Windows Server, Windows 10+
