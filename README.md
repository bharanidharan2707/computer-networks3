# Internet Speed Test

## Project Overview
Internet Speed Test is a beginner-level Computer Networks project developed using Python and Flask. It measures the internet connection's download speed, upload speed, and ping (latency).

## Features
- Check internet download speed.
- Check internet upload speed.
- Measure ping (latency).
- Simple and user-friendly web interface.
- Display test results instantly.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript
- speedtest-cli

## Project Structure

```text
InternetSpeedTest/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Internet-Speed-Test.git
```

### 2. Open the project folder

```bash
cd Internet-Speed-Test
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment (Windows)

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5002
```

## Sample Output

The application displays:

- Download Speed: Mbps
- Upload Speed: Mbps
- Ping: ms

*Actual results depend on your internet connection and the selected test server.*

## Networking Concepts
- Internet connectivity
- Download and upload bandwidth
- Network latency (ping)
- Client-server communication
- HTTP requests and responses

## Purpose
This project was developed for learning basic Computer Networks concepts and Python web application development.

## Author
Bharanidharan

## License
This project is created for educational purposes.
