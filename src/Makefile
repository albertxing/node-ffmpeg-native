ffmpeg.o: ffmpeg/fftools/ffmpeg.c
	$(CC) -Iffmpeg -c -Dmain=ffmpeg_main ffmpeg/fftools/ffmpeg.c

libffmpeg.o: libffmpeg.c libffmpeg.h ffmpeg_main.h
	$(CC) -Iffmpeg -c libffmpeg.c

libffmpeg.a: libffmpeg.o ffmpeg.o
	ar rc libffmpeg.a \
		ffmpeg/fftools/ffmpeg_filter.o \
		ffmpeg/fftools/ffmpeg_hw.o \
		ffmpeg/fftools/ffmpeg_mux.o \
		ffmpeg/fftools/ffmpeg_opt.o \
		ffmpeg/fftools/cmdutils.o \
		ffmpeg/fftools/opt_common.o \
		ffmpeg.o \
		libffmpeg.o
