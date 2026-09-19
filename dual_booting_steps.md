# Ubuntu 22.04 Dual-Boot Installation Guide

Quick reference for installing Ubuntu 22.04.5 LTS alongside Windows using a separate partition.

---

## 1. Prepare Windows

1. Back up important files.
2. Open **Disk Management**.
3. Identify the unused partition you want to give to Ubuntu.
4. Delete only that partition so it becomes **Unallocated space**.
5. Do not create a new Windows volume from that unallocated space.

### Important disk mapping used in this setup

| Device | Purpose | Action |
|---|---|---|
| `/dev/nvme0n1` | Windows SSD | Do not erase or format |
| `/dev/nvme0n1p1` | EFI System Partition | Reuse, do not format |
| `/dev/nvme0n1p3` | Windows C: | Do not touch |
| `/dev/nvme0n1p4` | Windows Recovery | Do not touch |
| `/dev/sda1` | D: | Do not touch |
| `/dev/sda2` | F: | Do not touch |
| `/dev/sda3` | E: | Do not touch |
| `/dev/sda4` | Ubuntu partition | Ubuntu is installed here |

> Device names can differ on another computer. Always verify the sizes and contents before making changes.

---

## 2. Create the Ubuntu USB

Using Rufus:

- Select the Ubuntu ISO file:
  `ubuntu-22.04.5-desktop-amd64.iso`
- Partition scheme: **GPT**
- Target system: **UEFI**
- Click **Start**
- If asked, choose **ISO Image mode**
- Accept the warning that the USB will be erased

---

## 3. Boot from the USB

1. Restart the computer.
2. Press the boot-menu key, such as `F12` depending on the laptop.
3. Select:

   `USB Hard Drive (UEFI)`

4. Choose:

   `Try or Install Ubuntu`

---

## 4. Ubuntu Installer Settings

On **Updates and other software**:

- Select **Normal installation**
- Enable **Download updates while installing Ubuntu**
- Enable **Install third-party software for graphics, Wi-Fi hardware and additional media formats**

---

## 5. Choose Installation Type

Because the computer has two physical disks:

1. Select **Something else**.
2. Carefully identify the correct unallocated space.
3. Do not use **Erase disk and install Ubuntu**.

---

## 6. Create the Ubuntu Partition

Select the unallocated space intended for Ubuntu and click `+`.

Use these settings:

- Size: use the available unallocated space
- Type: **Primary**
- Location: **Beginning of this space**
- Use as: **Ext4 journaling file system**
- Mount point: `/`

Click **OK**.

The final Ubuntu partition in this setup was:

```text
/dev/sda4
Filesystem: ext4
Mount point: /
Size: approximately 200 GB
```

---

## 7. Configure the EFI Partition

Select the existing Windows EFI partition:

```text
/dev/nvme0n1p1
```

Set it as:

```text
EFI System Partition
```

Important:

- Do **not** format it.
- Do not delete it.
- Do not create another EFI partition unless specifically required.

---

## 8. Boot Loader Location

In this setup, the boot loader location was:

```text
/dev/nvme0n1
```

This is the Windows SSD containing the existing EFI partition.

---

## 9. Check “Write the Changes to Disks?”

Before confirming, verify that:

- The Ubuntu partition, such as `/dev/sda4`, is formatted as `ext4`.
- Windows C: is not being formatted.
- `/dev/sda1`, `/dev/sda2`, and `/dev/sda3` are not being formatted.
- The EFI partition is not being formatted.

If anything unexpected appears, choose **Go Back**.

If only the intended Ubuntu partition is being formatted, click **Continue**.

---

## 10. Complete Installation

1. Wait for Ubuntu to finish installing.
2. Click **Restart Now** when prompted.
3. If asked:

   `Remove the installation medium, then press ENTER`

   remove the USB and press `Enter`.

---

## 11. MOK Screen

If the blue **Perform MOK management** screen appears:

1. Select **Enroll MOK**.
2. Select **Continue**.
3. Confirm the enrollment if asked.
4. If the final screen shows **Reboot**, select it.

Do not select:

- Enroll key from disk
- Enroll hash from disk

unless you are intentionally enrolling a specific key or hash.

---

## 12. Choosing Windows or Ubuntu

After restarting, a boot menu may show:

- Ubuntu
- Advanced options for Ubuntu
- Windows Boot Manager

Choose:

- **Ubuntu** to start Ubuntu
- **Windows Boot Manager** to start Windows

---

## 13. Important Safety Rules

- Never select **Erase disk and install Ubuntu** unless you intentionally want to erase the selected disk.
- Never format the Windows C: partition.
- Never format the Windows EFI partition during this setup.
- Always verify disk names and partition sizes before clicking Continue.
- Keep a backup of important files before modifying partitions.
- Do not remove the USB while installation is still running unless the installer asks you to.

---

## 14. Quick Mental Model

```text
Windows SSD (/dev/nvme0n1)
├── EFI partition
├── Windows C:
└── Windows Recovery

Data disk (/dev/sda)
├── D: (/dev/sda1)
├── Ubuntu (/dev/sda4)
├── F: (/dev/sda2)
└── E: (/dev/sda3)
```

## Most Important Reminder

> Windows was on `/dev/nvme0n1`; Ubuntu was installed into `/dev/sda4`.
> Do not format or delete the Windows partitions.
