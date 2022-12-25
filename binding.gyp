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
				"../src/libffmpeg/ffmpeg/libavformat/libavformat.a",
				"../src/libffmpeg/ffmpeg/libavcodec/libavcodec.a",
				"../src/libffmpeg/ffmpeg/libavutil/libavutil.a",
				"../src/libffmpeg/ffmpeg/libavfilter/libavfilter.a",
				"../src/libffmpeg/ffmpeg/libavdevice/libavdevice.a",
				"../src/libffmpeg/ffmpeg/libswresample/libswresample.a",
				"../src/libffmpeg/ffmpeg/libswscale/libswscale.a",
				"../src/libffmpeg/libffmpeg.a",
			],
			"conditions": [
				["OS=='mac'", {
					"libraries": [
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
						"-framework VideoToolbox"
					]
				}],
				["OS=='win'", {
					"libraries": [
						"psapi.lib",
						"ole32.lib",
						"strmiids.lib",
						"uuid.lib",
						"oleaut32.lib",
						"shlwapi.lib",
						"gdi32.lib",
						"vfw32.lib",
						"secur32.lib",
						"ws2_32.lib",
						"mfuuid.lib",
						"ole32.lib",
						"strmiids.lib",
						"ole32.lib",
						"user32.lib",
						"user32.lib",
						"bcrypt.lib",
						"ole32.lib",
						"psapi.lib",
						"shell32.lib"
					]
				}]
			]
		}
	],
}