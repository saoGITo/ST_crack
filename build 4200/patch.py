import sys
import os

# ARM64 patch patterns (original -> patched)
patches = {
    bytes.fromhex("628F0294"): bytes.fromhex("1F2003D5"),  # BL <func> -> NOP
    bytes.fromhex("5D8F0294"): bytes.fromhex("1F2003D5"),  # BL <func> -> NOP
    bytes.fromhex("F657BDA9F44F01A9FD7B02A9FD8300918F910A94"): bytes.fromhex("200080D2C0035FD61F2003D51F2003D51F2003D5"),
    bytes.fromhex("E6031EAAC7B80A94"): bytes.fromhex("000080D2C0035FD6"),
     
}

def patch_binary(input_file, output_file=None):
    output_file = output_file or f"{os.path.splitext(input_file)[0]}_patched"
    try:
        with open(input_file, 'rb') as f:
            data = bytearray(f.read())

        patched_count = 0
        for original, replacement in patches.items():
            index = 0
            while True:
                index = data.find(original, index)
                if index == -1:
                    break
                print(f"[+] Found patch target at offset 0x{index:X}")
                data[index:index+len(replacement)] = replacement
                patched_count += 1
                index += len(replacement)

        if patched_count == 0:
            print("[-] No patches applied. Patterns not found.")
        else:
            with open(output_file, 'wb') as f:
                f.write(data)
            print(f"[+] Patched {patched_count} location(s). Saved as: {output_file}")

    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python patch.py <input_file> [output_file]")
    else:
        patch_binary(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
