#include <stdio.h>
#include "ffmpeg_main.h"

int ffmpeg(int argc, char** argv) {
	printf("%s\n", "hello world from libffmpeg");
	return ffmpeg_main(argc, argv);
}
