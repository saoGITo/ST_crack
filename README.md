# ST_crack
Cracked Sublime Text for ARM64 architecture (Apple Silicon)

Usage: python3 patcher.py <input_file> [output_file]

EXample:
python3 patcher.py sublime_text

then

cp sublime_text_patched "/Applications/Sublime Text.app/Contents/MacOS/sublime_text"

sudo xattr -rc /Applications/Sublime\ Text.app

codesign -s - --force --deep "/Applications/Sublime Text.app/Contents/MacOS/sublime_text"
