# Useful OS Commands

## Overview

Once an OS Command Injection vulnerability has been confirmed, the next step is often to gather information about the target system.

The PortSwigger material provides several commands that are useful for initial reconnaissance on both Linux and Windows systems.

---

# Current User

Determine the identity of the user running the application.

### Linux

```bash
whoami
```

### Windows

```cmd
whoami
```

---

# Operating System

Identify the operating system.

### Linux

```bash
uname -a
```

### Windows

```cmd
ver
```

---

# Network Configuration

View network interface information.

### Linux

```bash
ifconfig
```

### Windows

```cmd
ipconfig /all
```

---

# Network Connections

Display active network connections.

### Linux

```bash
netstat -an
```

### Windows

```cmd
netstat -an
```

---

# Running Processes

List currently running processes.

### Linux

```bash
ps -ef
```

### Windows

```cmd
tasklist
```

---

# Why These Commands Matter

These commands help identify:

- The account running the application.
- The operating system.
- Network configuration.
- Active network connections.
- Running services and processes.

This information can assist in understanding the environment after confirming a Command Injection vulnerability.

---

# Summary Table

| Purpose | Linux | Windows |
|---------|--------|----------|
| Current User | `whoami` | `whoami` |
| Operating System | `uname -a` | `ver` |
| Network Configuration | `ifconfig` | `ipconfig /all` |
| Network Connections | `netstat -an` | `netstat -an` |
| Running Processes | `ps -ef` | `tasklist` |

---

# Key Takeaways

- Initial reconnaissance helps understand the target environment.
- Different commands are required depending on the operating system.
- The PortSwigger material recommends starting with simple information-gathering commands after identifying a Command Injection vulnerability.