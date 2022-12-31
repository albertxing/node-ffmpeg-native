#!/bin/bash
set -x

# NVIDIA
git clone https://github.com/FFmpeg/nv-codec-headers
cd nv-codec-headers
make install PREFIX=/usr
cd ..

# AMD
git clone https://github.com/GPUOpen-LibrariesAndSDKs/AMF
cp -r AMF/amf/public/include /usr/include/AMF

# ffmpeg
cd ffmpeg
export PATH="/c/Program Files/Microsoft Visual Studio/2022/Enterprise/VC/Tools/MSVC/14.34.31933/bin/HostX64/x64/":$PATH
./configure --target-os=win64 --arch=x86_64 --toolchain=msvc --extra-cflags="-DCommandLineToArgvW=_CommandLineToArgvW_"
make -j4

# libffmpeg
cd ..
make libffmpeg.a

# cleanup
rm -rf nv-codec-headers
rm -rf AMF
