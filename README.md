# cintel-04-local

Welcome to cintel-04-local! This project module is designed to help you transition from browser-based Python and PyShiny development to local development on your own machine. While it may require some initial effort, the benefits of local development, such as increased control and efficiency, make it well worth the investment.

## Getting Started

### Prerequisites

Before starting, ensure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Git](https://git-scm.com/)

### Example Project

Check out an example of a local PyShiny project [here](https://github.com/denisecase/pyshiny-penguins-dashboard-express).

## Action 1: Create a GitHub Project Repo

1. Login to GitHub and navigate to Repositories.
2. Create a new project repo named `cintel-04-local` with a default `README.md` and a default `.gitignore` for Python.
3. Add a file named `requirements.txt` with the following packages:
   
- faicons
- palmerpenguins
- pandas
- pyarrow
- plotly
- seaborn
- shiny
- shinylive
- shinywidgets

4. Add a file named `app.py` (exactly!) and paste in the content from your P3 Shiny `app.py`. Commit the changes.

## Action 2: Download Python

1. Visit [Python's official website](https://www.python.org/downloads/).
2. Download the latest Python version for your operating system.

## Action 3: Install Python, Add to Path, and Verify

### Install Python

- **Windows:** Run the installer, check "Add Python to your Path", and click “Install Now”.
- **macOS:** Open the downloaded .pkg file and follow the on-screen instructions.
- **Linux:** Use your distribution's package manager (e.g., `sudo apt-get install python3`).

### Verify Installation

- **Windows:** Open PowerShell and run the following commands:
```bash
python --version
py --version
py -m pip --version
```

