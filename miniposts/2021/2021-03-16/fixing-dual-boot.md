# Fixing dual boot on my laptop

I am using a dual boot laptop - Windows and Linux.  Today I rebooted my
laptop and it couldn't boot to Linux anymore.  Just a lone blinking cursor
on a black screen.  What a bummer.

I figured it was a problem with the bootloader.

There are two ways to setup a bootloader for dual-booting system:

- use GRUB bootloader: it's an easy option - just install Linux after Windows
  and everything will be fine.  There is a drawback though - Windows will not be
  able to upgrade itself to a new version which comes out regularly;

- use Windows bootloader: more difficult to setup and, as it turned out, more
  fragile, but Windows will be able to upgrade itself.  I've been using this
  option for a while.

To setup the windows bootloader to boot linux one copies the grub
boot sector and adds it as a boot record using `bcdedit` tool.  My problem
was that most likely the GRUB boot sector was updated, but the windows bootloader
was still using the old one.

I wrote a script in Python to copy the GRUB boot sector and added
a new boot record to the windows bootloader.  That's how I fixed the boot
problem.

Leaving it [here](./get-boot-sector.py) to use next time the boot process
breaks :)
