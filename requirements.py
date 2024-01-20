import os
import sys
import subprocess
import pkg_resources

REQUIRED_PYTHON = (3, 11)
REQUIRED_PACKAGES = ["setuptools", "openai==0.28", "numpy", "pandas"]


def check_python_version():
    if sys.version_info < REQUIRED_PYTHON:
        sys.exit("Python %s.%s or later is required.\n" % REQUIRED_PYTHON)

def check_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
        print("pip is installed.")
    except subprocess.CalledProcessError:
        print("pip is not installed. Attempting to install...")
        try:
            subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
            print("pip installed successfully.")
        except subprocess.CalledProcessError:
            sys.exit("Failed to install pip. Please install pip manually and try again.")

def check_and_install_packages():

    for package in REQUIRED_PACKAGES:
        try:
            dist = pkg_resources.get_distribution(package)
            print('{} ({}) is installed'.format(dist.key, dist.version))
        except pkg_resources.DistributionNotFound:
            print('{} is NOT installed. Attempting to install...'.format(package))
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print('{} installed successfully.'.format(package))
            except subprocess.CalledProcessError:
                sys.exit('Failed to install {}. Please install it manually and try again.'.format(package))

def run_all_checks():
    check_python_version()
    check_pip()
    check_and_install_packages()

def create_files():
    if not os.path.exists('config.ini'):
        with open('config.ini', 'w') as config_file:
            config_file.write('[DEFAULT]\n')
            config_file.write('API_KEY = your_api_key_here\n')
            config_file.write('JOB_POSTING_FILE = job_posting.txt\n')
            config_file.write('RESUME_FILE = resume.txt\n')
            config_file.write('RECOMMENDATIONS_FILE = recommendations.txt\n')

    if not os.path.exists('resume.txt'):
        with open('resume.txt', 'w') as resume_file:
            resume_file.write('Your resume goes here.\n')

    if not os.path.exists('job_posting.txt'):
        with open('job_posting.txt', 'w') as job_posting_file:
            job_posting_file.write('The job posting goes here.\n')