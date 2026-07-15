# LFS CATI tool

## Upload survey files for management.msu

Using tkinter python module to build a gui application for LFS automation. 

### Tool features
The application will allow the user to load an .xls file from Domain and convert it to an .xlsm setup file for the Blaise app. 

To add a logging feature, with the logging module to log events and errors. The logs can be saved to a file for later review.

To add a notification system, we can use message boxes to inform the user of the status of the application, such as when a task is completed successfully or if an error occurs at each stage of the pandas methods working on the DataFrame

### Webhooks integration to MS Teams
To add a feature to send any notifications reported by the logging process on a MS Teams workflow channel via webhooks. 

### Requirements
* Python 3.14
* uv for dependency management and environment setup
* pandas module
* tkinter is a built in python module, does need to be installed
* logging module 