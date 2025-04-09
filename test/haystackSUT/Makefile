CC = cc
CFLAGS = -Wall
TARGET = haystack

.PHONY: all clean

all: $(TARGET)

$(TARGET): haystack.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f $(TARGET) 