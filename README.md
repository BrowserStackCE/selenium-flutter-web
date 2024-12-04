# Automating Flutter Web App with Selenium

This repository demonstrates how to automate a Flutter web application using Selenium and BrowserStack. The project includes modifications to enhance automation compatibility and provides a comprehensive setup for running Selenium Python tests.

## Overview

The Flutter web app has been modified for better compatibility with Selenium automation.
A setup to run Selenium tests on BrowserStack using Python and the BrowserStack SDK.
Configuration to run tests on a locally hosted website or live website across various browser platforms.

### Key Features
- Semantic modifications for improved automation
- Cross-browser testing using BrowserStack

## Modified Files in Flutter Project for Automation

### main.dart Changes
```dart
import 'package:flutter/rendering.dart';

// Ensure widget binding and enable semantics
WidgetsFlutterBinding.ensureInitialized();
SemanticsBinding.instance.ensureSemantics();
```

#### Semantic Enhancements
- Added `SemanticsBinding.instance.ensureSemantics()` to activate semantic support
- Improves accessibility and automation compatibility
- Generates pseudo elements for better interaction with testing tools

### adaptive_scaffold.dart Changes
```dart
Semantics(
  identifier: d.title, // Added for easier automation interaction
  child: ListTile(
    leading: Icon(d.icon),
    title: Text(d.title),
    // ... existing implementation
  ),
)
```

#### Automation Improvements
- Wrapped key UI elements with `Semantics` widget
- Added unique identifiers for easier element location
- Enables more reliable Selenium test interactions

## Running the Flutter Web App

### Prerequisites
- Flutter installed on your system
- Chrome browser

### Steps to Run
1. Navigate to the project root directory
2. Run the following command:
   ```bash
   flutter run -d chrome --web-port=3030
   ```

3. Access the web app at: `http://localhost:3030`

## Selenium Python Tests Setup

### Prerequisites
- Python 3
- BrowserStack Account (free trial available)

### Installation
1. Clone the repository:
   ```bash
   git clone -b dev https://github.com/BrowserStackCE/selenium-flutter-web
   cd selenium-flutter-web
   ```

2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip3 install -r requirements.txt
   ```

### BrowserStack Credentials Configuration
**Option 1:** Update `browserstack.yml` with your credentials

**Option 2:** Set environment variables
- Linux/MacOS:
  ```bash
  export BROWSERSTACK_USERNAME=<your-username>
  export BROWSERSTACK_ACCESS_KEY=<your-access-key>
  ```
- Windows:
  ```bash
  setx BROWSERSTACK_USERNAME <your-username>
  setx BROWSERSTACK_ACCESS_KEY <your-access-key>
  ```

### Running Tests

#### Live Website Test
```bash
browserstack-sdk python selenium_tests/live_website_test.py
```

#### Local Website Test
```bash
browserstack-sdk python selenium_tests/local_website_test.py
```

## Additional Notes
- Ensure your BrowserStack credentials are correctly configured
- Cross-browser testing supported via BrowserStack configuration

## Troubleshooting
- Verify Flutter and Python installations
- Check BrowserStack credentials
- Ensure all dependencies are installed correctly
