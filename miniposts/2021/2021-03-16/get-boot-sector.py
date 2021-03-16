import os
import sys
import datetime

def main():
    # use diskpart to find out the required partition
    #   diskpart
    #   list disk
    #   select disk=0
    #   list partition
    part = r"\\?\Harddisk0Partition3"
    boot_sector = None
    with open(part, 'rb') as f:
        boot_sector = f.read(512)

    if boot_sector.find(b'GRUB ') == -1:
        print("GRUB boot sector is not found", file=sys.err)
        os.exit(10)
    else:
        file_name = f"boot-grub-{datetime.date.today().isoformat()}.bin"
        with open(file_name, "wb") as f:
            f.write(boot_sector)
        print("Boot sector found and stored to "+file_name)
        print()
        print("Use commands like below to add a new boot entry:")
        print('  bcdedit /create /d "Linux-2020-03-16" /application bootsector')
        print('  bcdedit /set {975077e6-ed02-11ea-9a7a-8a613237b011} device partition=c:')
        print('  bcdedit /set {975077e6-ed02-11ea-9a7a-8a613237b011} path \\boot-grub-2021-03-16.bin')
        print('  bcdedit /displayorder {975077e6-ed02-11ea-9a7a-8a613237b011} /addlast')
        print('  bcdedit /default {975077e6-ed02-11ea-9a7a-8a613237b011}')
        print()
        print("To remove old records run:")
        print("  bcedit")
        print("  bcedit /delete {record-id}")


if __name__ == '__main__':
    main()
