# Pomodoro-app

This repository contains two implementations of a Pomodoro timer:

* **Tkinter** – a desktop application for Windows users.
* **Streamlit** – a web version that can be easily deployed.

## Features

- Customisable work and break durations
- Ability to run multiple cycles
- Progress bars and improved styling
- Simple desktop version using Tkinter

## Running the Streamlit version

Install the dependencies and launch the app:

```bash
pip install -r requirements.txt
streamlit run Streamlit/app.py
```

The app will start on `http://localhost:8501`.

## Deploying

You can deploy the Streamlit version using [Streamlit Community Cloud](https://streamlit.io/cloud) or any other platform that supports running Python applications. Simply point the deployment to `Streamlit/app.py`.

## Running the Tkinter version

```bash
python Tkinter/main.py
```

This requires a Windows system for toast notifications.
