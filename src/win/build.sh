#!/bin/bash
cd ffmpeg
type -a link
./configure --target-os=win64 --arch=x86_64 --toolchain=msvc 
