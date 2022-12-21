{
	"targets": [
		{
			"target_name": "ffmpeg",
			"sources": ["src/node_ffmpeg.cc"],
			"include_dirs": [
				"<!@(node -p \"require('node-addon-api').include\")",
			],
			"defines": [
				"NAPI_DISABLE_CPP_EXCEPTIONS"
			],
			"libraries": [
				"../src/ffmpeg/libavformat/libavformat.a",
				"../src/ffmpeg/libavcodec/libavcodec.a",
				"../src/ffmpeg/libavutil/libavutil.a",
				"../src/ffmpeg/libavfilter/libavfilter.a",
				"../src/ffmpeg/libavdevice/libavdevice.a",
				"../src/ffmpeg/libswresample/libswresample.a",
				"../src/ffmpeg/libswscale/libswscale.a",
				"../src/libffmpeg.a",
				"-framework AppKit",
				"-framework AudioToolbox",
				"-framework AVFoundation",
				"-framework CoreAudio",
				"-framework CoreFoundation",
				"-framework CoreGraphics",
				"-framework CoreImage",
				"-framework CoreMedia",
				"-framework CoreServices",
				"-framework CoreVideo",
				"-framework Foundation",
				"-framework OpenGL",
				"-framework VideoToolbox",
			]
		}
	],
}