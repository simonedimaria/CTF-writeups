ext2file = "unzipped"

with open(ext2file, "r+b") as ext2:
    ext2.seek(0x400 + 0x38)  # seek to super block + magic number offset
    ext2.write(b"\x53\xef")  # wite ext2 magic number in little endian (0xef53)