ifeq ($(OS), Windows_NT)
	CC = cl
	CCFLAGS += -Fo$@ -Iffmpeg/compat/atomics/win32
	AR = lib
	ARFLAGS = -out:$@
else
	AR = ar
	ARFLAGS += $@
endif

ffmpeg.o: ffmpeg/fftools/ffmpeg.c
	$(CC) $(CCFLAGS) -Iffmpeg -c ffmpeg/fftools/ffmpeg.c

libffmpeg.o: libffmpeg.c libffmpeg.h ffmpeg_main.h
	$(CC) $(CCFLAGS) -Iffmpeg -c libffmpeg.c

libffmpeg.a: libffmpeg.o ffmpeg.o
	$(AR) $(ARFLAGS) \
		ffmpeg/fftools/ffmpeg_filter.o \
		ffmpeg/fftools/ffmpeg_hw.o \
		ffmpeg/fftools/ffmpeg_mux.o \
		ffmpeg/fftools/ffmpeg_opt.o \
		ffmpeg/fftools/cmdutils.o \
		ffmpeg/fftools/opt_common.o \
		ffmpeg.o \
		libffmpeg.o
