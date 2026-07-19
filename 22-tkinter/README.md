# LFS CATI tool

### Upload survey files for management.msu

Using tkinter python module to build a gui application for LFS automation.

#### Tool features

The application will allow the user to load an .xls file from Domain and convert it to an .xlsm setup file for the Blaise app. The tool creates a pandas DataFrame from the original Domain .xls file, meaning that the original .xls file is not altered. The whole process works on the pandas DataFrame (variable is `df` in code) and saves it as an upload file: `LFS Upload Template 2026.xlsm` and a `.txt` version as `sample.txt`. The user will upload these files to `X:\CATI\LFS CATI\DataIn`

To add a `logging` feature, with the logging module to log events and errors. The logs can be saved to a file for later review.

To add a `notification` system, we can use message boxes to inform the user of the status of the application, such as when a task is completed successfully or if an error occurs as the pandas methods are working on the DataFrame

#### Webhooks integration to MS Teams

To add a feature to send any notifications reported by the logging process on a MS Teams workflow channel via `webhooks`.

#### Requirements

* Python 3.14
* uv for dependency management and environment setup. uv will sync any dependecies the user
* pandas module
* openpyxl module
* tkinter and os are built in python modules, does need to be installed, as these come with python
* logging module

These dependencies are in the pyproject.toml file.

```python
    dependencies = [
        "logging>=0.4.9.6",
        "openpyxl>=3.1.5",
        "pandas>=3.0.3",
    ]
```

To install these modules into your local LFS app folder run

```bash
    uv sync
```

To check they are installed in the app folder

```bash
    uv pip list
```
