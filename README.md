# File Organizer

This is a command-line Python application designed to automatically sort and organize files within a specified directory based on their file extensions. It moves files into dedicated subdirectories to reduce clutter.

## Features

* Categorizes files into specific target folders including Images, Documents, Audio, Video, Archives, and Executables.
* Places unrecognized file formats into an Others folder automatically.
* Includes built-in collision prevention to avoid overwriting existing files with duplicate names in the destination folders.

## Default Folder Mapping

* Images: .jpg, .jpeg, .png, .gif, .bmp, .svg, .webp
* Documents: .pdf, .docx, .doc, .txt, .xlsx, .xls, .pptx, .ppt, .csv
* Audio: .mp3, .wav, .aac, .flac, .ogg
* Video: .mp4, .mov, .avi, .mkv, .flv
* Archives: .zip, .rar, .7z, .tar, .gz
* Executables: .exe, .msi

## Prerequisites

Python 3.x must be installed on your operating system. Ensure that Python is added to your environment system variables (PATH) during installation.
