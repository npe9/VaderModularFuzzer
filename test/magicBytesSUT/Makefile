CC = cc
CFLAGS = -Wall
TARGET = magicbytes
TARGET_CMPLOG = magicbytes_cmplog

.PHONY: all clean

all: $(TARGET) $(TARGET_CMPLOG)

$(TARGET): magicbytes.c
	$(CC) $(CFLAGS) $< -o $@

$(TARGET_CMPLOG): magicbytes.c
	AFL_LLVM_CMPLOG=1 $(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(TARGET) $(TARGET_CMPLOG)
