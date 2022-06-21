# CSCB634-PythonTranscriber
Project developed by students at New Bulgarian University for a text-to-speech transcriber using Mozilla Deepspeech.

## Setup
The project does not run directly on Windows or WSL. To run on a Windows machine, please set up a virtual machine with a Linux guest.

### Setup virtual environment

On first setup.

`python3 -m venv venv`

Activate the venv during development.

`source venv/bin/activate`

Deactivate when done.

`deactivate`

### Install pyaudio

`sudo apt-get install python3-pyaudio`


### Install requirements

Ensure the virtual environment is activated

`source venv/bin/activate`

Then install the dependencies.

`pip install -r requirements_dev.txt`
