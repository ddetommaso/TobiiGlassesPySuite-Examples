# TobiiGlassesPySuite Examples

## What is TobiiGlassesPySuite ?
The TobiiGlassesPySuite is an open-source Python toolkit for exploiting the capabilities of the Tobii Pro Glasses 2 in cross-platform environments.

For more details please visit [here](https://github.com/ddetommaso/TobiiGlassesPySuite).

## Requirements
- Python 2.x or 3.x
- tobiiglassespysuite

## Installing tobiiglassespysuite

```
pip install tobiiglasses
```

## Getting started
```
git clone --recursive https://github.com/ddetommaso/TobiiGlassesPySuite-examples.git
cd TobiiGlassesPySuite-examples
```

# connect.py
A simple Python script showing how to connect with the device

```
cd TobiiGlassesPySuite-examples/controller
python connect.py
[DEBUG]: Connecting to the Tobii Pro Glasses 2 ...
[DEBUG]: Tobii Pro Glasses 2 successful connected!
```

# How to get project ids?
A simple Python script showing how to get project ids of recordings from a
path. Please notice that <path> is the folder where projects.ttgp is located.

```
cd TobiiGlassesPySuite-examples/info
python get_projects.py <path>
```

# How to get recordings ids?
A simple Python script showing how to get recording ids from a path and
providing a project id.

```
cd TobiiGlassesPySuite-examples/info
python get_recordings.py <path> <project_id>
```
