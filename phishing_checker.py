
from urllib.parse import urlparse
import ipaddress


def inspect_url(raw_url):
    """Check a URL for the six warning signs in the workbook."""

    url = raw_url.strip()

    if not url:
        return ["ERROR: URL cannot be empty."]

    # Add HTTP if the user does not provide a scheme.
    if "://" not in url:
        url = "http://" + url

    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname or ""

    except ValueError:
        return ["ERROR: Invalid URL format. Could not inspect this URL."]

    if (
        parsed_url.scheme.lower() not in ("http", "https")
        or not hostname
        or any(char.isspace() for char in url)
    ):
        return ["ERROR: Invalid URL format. Please enter a valid HTTP or HTTPS URL."]

    findings = []

    # 1. Check for @ symbol
    if "@" in url:
        findings.append(
            "WARNING: The URL contains an @ symbol. "
            "This can be used to disguise the actual destination."
        )

    # 2. Check URL length
    if len(url) > 100:
        findings.append(
            "WARNING: The URL is longer than 100 characters. "
            "Unusually long URLs can hide suspicious details."
        )

    # 3. Check for an IP address as hostname
    try:
        ipaddress.IPv4Address(hostname)
        is_ip_address = True
    except ValueError:
        is_ip_address = False

    if is_ip_address:
        findings.append(
            "WARNING: The hostname is an IP address instead of a domain name."
        )

    # 4. Check hostname segments
    segments = hostname.rstrip(".").split(".")

    if len(segments) >= 5:
        findings.append(
            "WARNING: The hostname has 5 or more segments. "
            "This unusual structure deserves attention."
        )

    # 5. Check for punycode
    if "xn--" in hostname.lower():
        findings.append(
            "WARNING: The hostname contains the xn-- punycode marker. "
            "It may represent an internationalised domain name."
        )

    # 6. Check HTTP instead of HTTPS
    if parsed_url.scheme.lower() == "http":
        findings.append(
            "WARNING: The URL uses HTTP instead of HTTPS. "
            "The connection is not protected by HTTPS."
        )

    if not findings:
        findings.append(
            "No listed warning signs found. "
            "This does NOT prove that the URL is safe."
        )

    return findings


def main():
    print("========================================")
    print("     Phishing URL Awareness Checker")
    print("========================================")
    print("This tool checks URL text only.")
    print("It does not visit or open any website.")
    print("Type 'q' to quit.")

    while True:
        url = input("\nEnter a URL to check: ").strip()

        if url.lower() == "q":
            print("\nThank you for using the checker. Goodbye!")
            break

        print("\n--------------- RESULTS ---------------")

        findings = inspect_url(url)

        for number, finding in enumerate(findings, start=1):
            print(f"{number}. {finding}")

        # Review summary
        if any(finding.startswith("WARNING:") for finding in findings):
            print("\nSummary: REVIEW CAREFULLY.")
            print("One or more warning signs were detected.")
        elif any(finding.startswith("ERROR:") for finding in findings):
            print("\nSummary: INPUT COULD NOT BE CHECKED.")
        else:
            print("\nSummary: NO LISTED WARNING SIGNS FOUND.")

        print("\nRemember: Never enter passwords through unexpected links.")
        print("A URL with no warning signs is not guaranteed to be safe.")
        print("---------------------------------------")


if __name__ == "__main__":
    main()
