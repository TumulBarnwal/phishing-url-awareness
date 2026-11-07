# Phishing URL Awareness Checker

## 1. Project Overview

The Phishing URL Awareness Checker is a Python-based command-line application that checks URL text for common warning signs associated with phishing links.

The program helps users identify potentially suspicious URL characteristics before interacting with unexpected links.

**Important:** This tool only analyses URL text. It does not visit websites, perform online scans, or guarantee that a URL is safe.

## 2. Features

The program checks for six warning signs:

1. **@ Symbol:** Detects the presence of an `@` symbol in the URL.
2. **Unusually Long URL:** Detects URLs longer than 100 characters.
3. **IP Address Hostname:** Detects when an IP address is used instead of a domain name.
4. **Multiple Hostname Segments:** Detects hostnames containing five or more segments.
5. **Punycode Marker:** Detects the `xn--` marker in a hostname.
6. **HTTP Instead of HTTPS:** Detects URLs that use HTTP instead of HTTPS.

## 3. Additional Improvements

The following improvements have been added:

- **Repeated URL Checking:** Users can check multiple URLs without restarting the program.
- **Quit Option:** Users can enter `q` to exit the application.
- **Malformed Input Handling:** Invalid URL formats are handled without crashing the program.
- **Warning Explanations:** Each detected warning includes a short explanation.

## 4. Technologies Used

- Python 3
- Python built-in libraries:
  - `urllib.parse`
  - `ipaddress`

No external Python packages are required.

## 5. Requirements

- Python 3.10 or above.
- A terminal or command prompt.
- No additional package installation is necessary.

## 6. How to Run

1. Download or clone this repository.
2. Open a terminal in the project directory.
3. Run the following command:

```bash
python phishing_checker.py
```

4. Enter a URL when prompted.
5. Enter another URL to continue checking.
6. Type `q` to quit.

## 7. Example Output

```text
Phishing URL Awareness Checker

Enter a URL to check:
http://192.0.2.10/account

WARNING: The hostname is an IP address instead of a domain name.
WARNING: The URL uses HTTP instead of HTTPS.

Summary: REVIEW CAREFULLY.
```

## 8. Testing

The program was tested using all five sample URLs provided in the project workbook.

- Total test cases: 5
- Passed: 5
- Failed: 0

Detailed expected and actual results are available in `tests/test_samples.md`.

## 9. Screenshots

The `screenshots` folder contains:

- `sample_run.png` — example of the program checking a URL.
- `test_results.png` — evidence of the sample URL test results.

## 10. Limitations

- The program analyses URL text only.
- It does not visit or open websites.
- It does not use online databases or external APIs.
- It cannot detect every phishing URL.
- A URL with no detected warning signs is not necessarily safe.

## 11. Ethical Use

This project is intended for cybersecurity awareness and educational purposes. Users should avoid entering passwords or personal information through unexpected links.

## 12. Author

**Tumul Barnwal**

Cybersecurity Mini Project — EWB Edutech
