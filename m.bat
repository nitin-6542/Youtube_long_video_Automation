@echo off
ffmpeg -y -f concat -safe 0 -i mylist.txt -c copy outputf.mp4
pause