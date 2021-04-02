# Get a fullpage screenshot of a file from Github Public/Private repository

## Clone the repository
```bash
$ git clone https://github.com/shahedex/github_file_fullpage_download.git
```
## Create and activate a Virtual Environment
```bash
$ cd github_file_fullpage_download
$ python3 -m venv venv
$ source venv/bin/activate
```

## Install the required dependencies
```bash
$ pip install -r requirements.txt
```
## Create a ENV file in the project directory
```bash
$ touch .env
$ nano .env
```
## Add the following to the .env file
```bash
GITHUB_USERNAME="your_github_username"
GITHUB_PASSWORD="your_github_password"
GITHUB_TOKEN="your_github_personal_token"
GITHUB_REPOSITORY="the_repository_name"  # i.e, the-ionicus/tini
GITHUB_REPOSITORY_FILE="the_file_location"  # i.e, app/main/forms.py
```
## Run the program to get the screenshot
```bash
$ python github-page.py
```

Open **saved_screenshots** directory to get the **PNG** format file, **converted_pdfs** for the **PDF** version.
