# Website Status Checker

A Python automation tool that checks the availability of multiple websites and displays their HTTP status codes.

## Features

- Monitor multiple websites at once
- Check website availability automatically
- Display HTTP status codes
- Handle connection errors gracefully
- Beginner-friendly Python automation project

## Technologies Used

- Python
- Requests Library

## Project Structure

```
website_status_checker.py
README.md
```

## How It Works

1. Stores website URLs in a list.
2. Sends HTTP requests to each website.
3. Retrieves the response status code.
4. Displays whether the website is online or unavailable.
5. Handles errors using exception handling.

## Installation

Install the required library:

```bash
pip install requests
```

## Usage

Run the script:

```bash
python3 website_status_checker.py
```

## Example Output

```text
https://www.google.com → Online ✅
https://www.github.com → Online ✅
https://www.openai.com → Status Code: 403
```

## Common HTTP Status Codes

| Status Code | Meaning |
|------------|---------|
| 200 | Success |
| 301 | Redirect |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

## Learning Outcomes

- Python Automation
- HTTP Requests
- Website Monitoring
- Error Handling
- Working with APIs and Web Services

## Future Improvements

- Export results to CSV
- Add email notifications
- Schedule automatic checks
- Monitor hundreds of websites

## Author

Geethika Yeggina