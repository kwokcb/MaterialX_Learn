import pefile

pe = pefile.PE("slang.dll")

for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
    if exp.name:
        print(exp.name.decode())
