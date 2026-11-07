# Phishing URL Awareness Checker — Test Results

## Testing Overview

The program was tested using all five sample URLs provided in the EWB Cybersecurity Mini Project Workbook.

Each test compares the expected warning signs with the actual program output.

| Test | URL | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs found | PASS |
| 2 | `http://192.0.2.10/account` | IP hostname and HTTP | IP hostname and HTTP warnings detected | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol and HTTP | @ symbol and HTTP warnings detected | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | 5 or more hostname segments | Hostname segments warning detected | PASS |
| 5 | `https://xn--example.invalid/` | Punycode marker | Punycode warning detected | PASS |

## Individual Test Results

### Test 1: Normal Example URL

**Input:** `https://www.example.com/login`

**Expected:** No listed warning signs.

**Actual:** No listed warning signs found. This does NOT prove that the URL is safe.

**Status:** PASS

### Test 2: IP Address Hostname

**Input:** `http://192.0.2.10/account`

**Expected:** IP-address hostname and HTTP warnings.

**Actual:** Both warnings detected.

**Status:** PASS

### Test 3: @ Symbol in URL

**Input:** `http://example.com@sample.invalid/login`

**Expected:** @ symbol and HTTP warnings.

**Actual:** Both warnings detected.

**Status:** PASS

### Test 4: Multiple Hostname Segments

**Input:** `https://a.b.c.d.e.example.invalid/path`

**Expected:** Warning for 5 or more hostname segments.

**Actual:** Hostname segments warning detected.

**Status:** PASS

### Test 5: Punycode Marker

**Input:** `https://xn--example.invalid/`

**Expected:** Punycode warning.

**Actual:** Punycode warning detected.

**Status:** PASS

## Final Testing Summary

- Total test cases: 5
- Passed: 5
- Failed: 0

**Overall Result: All five sample test cases passed successfully.**

The program checks URL text only. It does not visit websites or guarantee that a URL is safe.
