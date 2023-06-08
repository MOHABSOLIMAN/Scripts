import urllib.request
import subprocess
import os
import zipfile
import time

# # Installing Python 3.6.0
# PYTHON_VERSION = "3.6.0"
# PYTHON_DOWNLOAD_URL = f"https://www.python.org/ftp/python/{PYTHON_VERSION}/python-{PYTHON_VERSION}-amd64.exe"
# PYTHON_INSTALL_DIR = f"C:\\Python{PYTHON_VERSION}"
#
# print(f"Downloading Python {PYTHON_VERSION}...")
# urllib.request.urlretrieve(PYTHON_DOWNLOAD_URL, f"python-{PYTHON_VERSION}-amd64.exe")
#
# print(f"Installing Python {PYTHON_VERSION} silently...")
# subprocess.run([f"python-{PYTHON_VERSION}-amd64.exe", "/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0", "/norestart"])
#
# print("Cleaning up...")
# os.remove(f"python-{PYTHON_VERSION}-amd64.exe")
#
# print(f"Python {PYTHON_VERSION} has been installed to {PYTHON_INSTALL_DIR}.")
url = "https://repo.msys2.org/distrib/msys2-x86_64-latest.exe"

# Installing Msys2
filename_msys = "msys2-x86_64-latest.exe"
print(f"Downloading Msys2 : {filename_msys}...")
urllib.request.urlretrieve(url, filename_msys)

# Run the MSYS2 installer with default options and no UI
print(f"Installing MSYS2 : {filename_msys} silently...")
subprocess.run([filename_msys, "/S", "/D=C:\\msys64"])

# Add MSYS2 to the system PATH
subprocess.run(["setx", "PATH", "%PATH%;C:\\msys64\\usr\\bin"])

# Attempt to delete the downloaded file (may fail due to file being in use)
for i in range(10):
    try:
        print("Cleaning up...")
        os.remove(filename_msys)
        break
    except PermissionError:
        print(f"Attempt {i+1} to delete {filename_msys} failed. Retrying in 10 second...")
        time.sleep(10)

# # Installing CMake 3.15.0
#
# # Download the latest version of cMake
# # Download CMake installer
# subprocess.run(["powershell", "-Command", "(New-Object System.Net.WebClient).DownloadFile('https://github.com/Kitware/CMake/releases/download/v3.20.2/cmake-3.20.2-windows-x86_64.msi', 'cmake-3.20.2-windows-x86_64.msi')"])
#
# # Install CMake silently
# subprocess.run(["msiexec", "/i", "cmake-3.20.2-windows-x86_64.msi", "/quiet", "/norestart"])
#
# # Delete downloaded files
# #os.remove("cmake-3.20.2-windows-x86_64.msi")
#
# # Install protobuf development files
# os.system('pip install protobuf')
#
# # Install protobuf compiler
# url = 'https://github.com/protocolbuffers/protobuf/releases/download/v3.20.1/protobuf-cpp-3.20.1.zip'
# filename = 'protoc-3.20.1-win64.zip'
# urllib.request.urlretrieve(url, filename)
# with zipfile.ZipFile(filename, 'r') as zip_ref:
#     zip_ref.extractall('proto')
# os.environ['PATH'] += os.pathsep + os.path.abspath('proto/bin')
# # Clone the OSI repository
# # Clone the OSI repository
# os.system('git clone https://github.com/OpenSimulationInterface/open-simulation-interface.git')
# os.chdir('open-simulation-interface')
#
# # Build and install OSI
# os.mkdir('build')
# os.chdir('build')
# os.system('cmake -G "Visual Studio 16 2019" -A x64 ..')
# os.system('cmake --build . --config Release')