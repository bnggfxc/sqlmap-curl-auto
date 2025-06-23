import re

def curl_to_sqlmap_request(curl_command, output_file="req.txt"):
    # Extract the URL
    url_match = re.search(r"curl '(.*?)'", curl_command)
    url = url_match.group(1) if url_match else None

    if not url:
        print("Invalid curl format: URL not found.")
        return

    # Extract headers
    headers = re.findall(r"-H '(.*?)'", curl_command)
    header_dict = {}
    for h in headers:
        if ":" in h:
            key, val = h.split(":", 1)
            header_dict[key.strip()] = val.strip()

    # Determine method
    method = "GET"
    if "-X POST" in curl_command or "--data" in curl_command or "--data-raw" in curl_command:
        method = "POST"

    # Extract data
    data_match = re.search(r"--data(?:-raw)? '(.*?)'", curl_command)
    data = data_match.group(1) if data_match else None

    # Extract host/path
    from urllib.parse import urlparse
    parsed = urlparse(url)
    path = parsed.path + ("?" + parsed.query if parsed.query else "")
    host = parsed.netloc

    # Build the request file
    request_lines = []
    request_lines.append(f"{method} {path} HTTP/1.1")
    request_lines.append(f"Host: {host}")
    for key, val in header_dict.items():
        if key.lower() != "host":  # skip host to avoid duplication
            request_lines.append(f"{key}: {val}")
    if method == "POST":
        request_lines.append("")  # separate headers from body
        request_lines.append(data)

    # Save to file
    with open(output_file, "w") as f:
        f.write("\n".join(request_lines))

    print(f"[+] Request written to {output_file}")

# Example usage
if __name__ == "__main__":
    print("Paste your full curl command:")
    curl = input()
    curl_to_sqlmap_request(curl)
