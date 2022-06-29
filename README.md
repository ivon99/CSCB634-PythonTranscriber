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

## Run

To run the project, firstly ensure the virtual environment is activated

`source venv/bin/activate`

Then download the model:

`curl -LO https://github.com/mozilla/DeepSpeech/releases/download/v0.6.0/deepspeech-0.6.0-models.tar.gz`

Extract it:

`tar -xvzf deepspeech-0.6.0-models.tar.gz`

Rename the directory:

`mv deepspeech-0.6.0-models models`

Run the project:

`python3 main.py`
