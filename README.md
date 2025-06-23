# curl-to-sqlmap-request

A simple Python tool to convert a `curl` command into an HTTP request file compatible with SQLMap (`-r` option).

## 🔧 Features

- Accepts a `curl` command as input
- Extracts URL, method, headers, and data
- Outputs a properly formatted HTTP request file (`request.txt`) for use with SQLMap

## 🚀 Usage

### 1. Clone the repo

```bash
git clone https://github.com/bnggfxc/curl-to-sqlmap-request.git
cd curl-to-sqlmap-request
