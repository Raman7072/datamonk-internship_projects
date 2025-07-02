# 🚀 Dual Boot Ubuntu 24.04.2 LTS with Windows 10/11 – Complete Guide

Planning to run both Windows and Ubuntu on your system? Here's a simplified and content-rich walkthrough to make your **dual-boot setup** smooth and safe! ⚙️🐧🪟

---

## 📋 Before You Begin
✅ **Backup your data**  
✅ **Ensure 50GB+ free space**  
✅ **Disable BitLocker & RAID**  
✅ **Switch SATA mode to AHCI**

---

## ❓ Why Disable BitLocker? 🔒

**BitLocker** encrypts your entire Windows drive for security. However, **Ubuntu cannot resize encrypted partitions**.  
🔧 **Must be disabled** before installation or Ubuntu won’t detect Windows ➡️ install fails or data loss risk!

---

## 🔽 Step 1: Download Ubuntu & Rufus

- 📥 [Ubuntu ISO](https://ubuntu.com/download/desktop)
- 🛠️ [Rufus](https://rufus.ie)

---

## 💽 Step 2: Create Bootable USB Using Rufus

### 🔧 Why Rufus?

Rufus formats your USB & writes the Ubuntu ISO in a bootable format.

### 📝 How To:

1. Plug in USB (8GB+)
2. Open **Rufus**
   - **Device**: Select USB
   - **Boot selection**: Choose Ubuntu ISO
   - **Partition scheme**: GPT
   - **Target system**: UEFI
   - **File system**: FAT32
3. Click **Start** ➡️ Choose **ISO Image Mode**
4. Wait till completion ✅

---

## 🖥️ Step 3: Prepare Windows

### 1. 🔓 Disable BitLocker
`Control Panel > System & Security > BitLocker Drive Encryption > Turn off`

### 2. 🧱 Shrink Partition
`Win + X > Disk Management > Shrink C: by 50,000 MB`

### 3. ⚡ Disable Fast Startup
`Power Options > Choose what power button does > Uncheck fast startup`

### 4. 🔐 Disable Secure Boot (Optional)
`BIOS > Boot tab > Disable Secure Boot & set SATA Mode to AHCI`

> 💡 **Why AHCI?**  
RAID confuses Ubuntu; AHCI ensures Linux sees your disk correctly!

---

## 💻 Step 4: Boot From USB

1. Insert USB  
2. Reboot ➡️ **Press F12/ESC/F10**  
3. Select USB drive ➡️ Click **Try or Install Ubuntu**

---

## 🧰 Step 5: Install Ubuntu

1. Click **Install Ubuntu**
2. Choose:
   - **Language** > Continue
   - **Normal Install** + tick updates/tools > Continue
3. At “Installation Type”:
   - ✅ If available: **Install Ubuntu alongside Windows**
   - ❌ If not: Choose **Something Else**
     - Select **free space**
     - Create:
       - `/` (root): ext4, 40GB+
       - (optional) **Swap** = RAM size

⚠️ **DO NOT format Windows partition**

4. Set timezone, username, password ➡️ Start install  
5. Click **Restart Now**, eject USB 🔄

---

## 🔃 Step 6: Boot Options via GRUB

🎛️ After restart:
- **Ubuntu** to use Linux 🐧  
- **Windows Boot Manager** for Windows 🪟

---

## 🧩 Common Issues & Fixes

| ❌ Problem | ✅ Fix |
|-----------|--------|
| Ubuntu doesn't detect Windows | Check UEFI mode, use GPT USB, try Boot Repair |
| BitLocker prevents boot | Disable BitLocker before resizing partitions |
| No bootable device found | BIOS: Enable USB boot, disable Secure Boot, set AHCI |
| Black screen after boot | Use `nomodeset` at GRUB (press `e`, change line, `F10`) |
| Wi-Fi/Drivers missing | Use Ethernet or USB tether, then:  
```bash
sudo apt update && sudo apt upgrade  
sudo ubuntu-drivers autoinstall
```

---

## 📚 Resources

- 🔗 [Ubuntu Dual Boot Docs](https://help.ubuntu.com)
- 📺 **Videos**:  
   - “How to Dual Boot Ubuntu 24.04 & Windows”  
   - “Install Ubuntu 24.04 on Windows 10/11 – Step-by-Step”

---

👨‍💻 Enjoy your **dual-boot Ubuntu + Windows** system! 🔥 Power of choice at your fingertips 💻🐧🪟  
