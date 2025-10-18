all: NTB.srec NTB.hex

	#a09 -oM00 -L -dDATETIME=`date +%s` -dPRGBEG=\$$2000 -dBASICROM=1 -l -s   $< 	# srec NTP.s09
%.bin: %.asm
	a09 -oM00 -L -dDATETIME=`date +%s` -dPRGBEG=\$$2000 -dBASICROM=1 -l -b$@ $<

%.srec: %.bin
	objcopy --adjust-vma 0x2000 -I binary $< -O srec $@
	flip2unix  $@

%.hex: %.bin
	xxd -g1 -o 0x2000 $< >$@

NTB.bin: NTB.asm
NTB.srec: NTB.bin

clean:
	rm -rf NTB.bin NTB.hex NTB.srec NTB.lst
