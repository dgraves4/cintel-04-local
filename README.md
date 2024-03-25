# cintel-04-local

Welcome to cintel-04-local! This project module is designed to help you transition from browser-based Python and PyShiny development to local development on your own machine. While it may require some initial effort, the benefits of local development, such as increased control and efficiency, make it well worth the investment.

## Getting Started

### Example Project

Check out an example of a local PyShiny project [here](https://github.com/denisecase/pyshiny-penguins-dashboard-express).

### Prerequisites

Before starting, ensure you have the following installed on your machine:

- **Python**: Install the most recent version from [python.org](https://www.python.org/downloads/).
- **Git**: Download and install Git from [git-scm.com](https://git-scm.com/).
- **Visual Studio Code (VS Code)**: Download from [code.visualstudio.com](https://code.visualstudio.com/).
- **VS Code Extensions**: Install the Python 

## Configurations
Configure Git by setting up your user name and email using the following commands in your terminal. Change the values to your name and email address. This is a one-time setup.

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
```

## Set up the Project
### Verify Installations
1. Open the project folder in VS Code.
2. Open a new terminal. On Windows, ensure the terminal type is PowerShell.
3. Run the following commands in the terminal one at a time to verify installations.
```bash
py --version
git --version
git config user.name
git config user.email
```

### Python Project Virtual Environment
1. Run the following commands in the terminal from the root project folder.
```bash
py -m venv .venv
```
2. Activate the project virtual environment.
   - On Windows:
```bash
source .venv\Scripts\Activate
```
3. Verify: Generally when the environment is active, (.venv) will appear in the terminal prompt.

### Install Packages into the Active Project Virtual Environment
With the project virtual environment active in the terminal, run the following commands to install the necessary packages.
```bash
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```

### Run the App
With your project virtual environment active in the terminal, run the app with live reloading and automatically open it in the browser.
```bash
shiny run --reload --launch-browser penguins/app.py
```

### Build the App to Docs Folder and Test Locally
1. Remove any existing assets and use shinylive export to build the app in the penguins folder to the docs folder.
```bash
shiny static-assets remove
shinylive export penguins docs
```
2. Serve the app locally from the docs folder to test before publishing to GitHub Pages.
```bash
py -m http.server --directory docs --bind localhost 8008
```

### After Editing, Git Add/Commit/Push Changes to GitHub
After editing project files, use Git add/commit/push changes to the main branch of the repository.
```bash
git add .
git commit -m "Your commit message"
git push origin main
```  
### Publish the App with GitHub Pages (one-time setup)
The first time you set up an app, configure the repository settings to publish the app with GitHub Pages.
1. Go to the repository on GitHub and navigate to the Settings tab.
2. Scroll down and click the Pages section.
3. Select branch main as the source for the site and change from the root folder to the docs folder to publish from.
4. Click Save and wait for the site to build.
5. Edit the "About" section of the repository to include a link to the live app.

## About
This project aims to provide a comprehensive guide for setting up a local development environment for Python projects using Visual Studio Code and Git. It covers the installation of necessary tools, configuration steps, project setup, and deployment using GitHub Pages.

### Sources

This is based on the project example and README documentation and code examples found at: https://github.com/denisecase/pyshiny-penguins-dashboard-express

From https://shiny.posit.co/py/docs/user-interfaces.html. This version has been modified slightly for hosting with GitHub Pages.
