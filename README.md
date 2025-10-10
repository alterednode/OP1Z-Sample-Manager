# opz-sample-manager
flask app built with PyQt5 to handle everything with samples on the op-z

Very early in development! Has bugs, UI is unintuitive. Everything is subject to change.

### Run app using:
```python main.py``` after installing dependencies in ```requirements.txt```

### Using the sample manager:
- Select the sample loader page
- Select the directory of your OP-Z in `Utility Settings` if you haven't (you will be prompted if it's missing)
- Click "List Files" at the top
- Add, remove, rearrange files as you see fit. Any file you drop will be automatically converted to the correct format for the OP-Z. Make sure you have FFMPEG installed, and if you're on Windows, set the path in `Utility Settings`.

### Using the sample converter
- Select the sample converter page
- Drop your audio file into the corresponding category (drum or synth sample)
- Sample will be automatically converted
- Sample is stored in "converted" directory inside. Click `Open Converted Directory`

### Using the config editor
- The config editor displays the OP-Z config options visually
- These screen is a work in progress
- You can toggle settings, type in boxes, edit the DMX config
- When you're done, click `Save Changes` at the top

## Screenshots
### Home Page:
![home page](/screenshots/homepage.png)

### Sample Manager:
![sample manager](/screenshots/samplemanager.png)

### Sample Converter:
![sample converter](/screenshots/sampleconverter.png)

### Config File Editor:
![config file editor](/screenshots/configeditor.png)

### Utility Settings:
![utility settings](/screenshots/utilitysettings.png)
