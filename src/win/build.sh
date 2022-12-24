#!/bin/bash
set -x

git clone https://github.com/FFmpeg/nv-codec-headers
cd nv-codec-headers
make install PREFIX=/usr
cd ..

cd ffmpeg
export PATH="/c/Program Files/Microsoft Visual Studio/2022/Enterprise/VC/Tools/MSVC/14.34.31933/bin/HostX64/x64/":$PATH
./configure --target-os=win64 --arch=x86_64 --toolchain=msvc
make -j4
cd ..
make libffmpeg.a
