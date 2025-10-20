
#BASE_ADDR = \$$2000
BASE_ADDR  = \$$100
BASE_ADDRx = 0x100

AFLAGS 	+= -oM00
AFLAGS 	+= -oINV
AFLAGS 	+= -oLIS
AFLAGS 	+= -oMAC
AFLAGS 	+= -oNUM
AFLAGS 	+= -oSYM
AFLAGS 	+= -oTXT
AFLAGS 	+= -L

all: ntb ntb60

ntb:   NTB.srec   NTB.hex   NTB.csum
ntb60: NTB60.srec NTB60.hex NTB60.csum
	echo "# ntb60"

	#a09 -oM00 -L -dDATETIME=`date +%s` -dPRGBEG=\$$2000 -dBASICROM=1 -l -s   $< 	# srec NTP.s09
%.bin: %.asm
	a09 $(AFLAGS) -dDATETIME=`date +%s` -dPRGBEG=$(BASE_ADDR) -dBASICROM=1 -l -b$@ $< 2>&1 | tee $*.err

%.srec: %.bin
	objcopy --adjust-vma $(BASE_ADDRx) -I binary $< -O srec $@
	flip2unix  $@

%.hex: %.bin
	xxd -g1 -u -o $(BASE_ADDRx) $< >$@

%.csum: %.bin
	-./bin2checksum.py $< > $*.csum

NTB.bin: NTB.asm
NTB.srec: NTB.bin

NTB60.bin: NTB60.asm
NTB60.srec: NTB60.bin

clean:
	rm -rf NTB.bin NTB.hex NTB.srec NTB.lst
	@-rm -rf NTB60.bin NTB60.hex NTB60.srec NTB60.lst
	@-rm -rf *.err *.csum
