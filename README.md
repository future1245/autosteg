# AutoStegonography🔍  
**Auto Steganography Detector and Decoder**

AutoStego is a Python tool that automates the detection and decoding of hidden messages inside image files using [Steghide](https://steghide.sourceforge.net/). It also supports optional brute-force password cracking using a wordlist.

---

## 🚀 Features

- Embed secret text into `.jpg` or `.jpeg` images with a password
- Extract hidden messages using a password
- Detect if an image might contain hidden data
- Automatically brute-force weak passwords using `wordlist.txt`

---

## 📁 How to Use

### 1. Requirements

- Python 3
- `steghide` installed on your system  
  (Install with `sudo apt install steghide` on Linux)

### 2. Files Needed

Place the following in the **same folder**:
- `autosteg.py` – the main Python script
- `wordlist.txt` – a list of possible passwords (one per line)
- Any image files you want to test (e.g., `image.jpg`)

---

### 3. Run the Script

```bash
python3 autosteg.py
```
You'll be prompted to enter:
- The image file path  
- The wordlist path  
- (Optional) Output file name

The script will attempt extraction using the wordlist, and notify you if the password is found.

---

### 💡 Example Wordlist Format (wordlist.txt):

123456,
password,
letmein,
secretpass,
admin123

### ⚠️ Disclaimer
This tool is intended for educational and ethical use only. Do not use it on files you don't own or without permission.


### 📄 License
This project is licensed under the MIT License.

### 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---
