#include <napi.h>
#include <iostream>
#include <string>

extern "C" {
#include "libffmpeg.h"
}

Napi::Value Run(const Napi::CallbackInfo& args) {
	Napi::Env env = args.Env();

	char** argv = new char*[args.Length() + 2];

	argv[0] = "ffmpeg";
	
	std::cout << "hello from node_ffmpeg! " << args.Length() << " args: ";

	for (int i = 0; i < args.Length(); i++) {
		Napi::String nstr = args[i].ToString();
		std::string str(nstr);

		char* arg = new char[str.length() + 1];
		strcpy(arg, str.c_str());
		
		std::cout << str << " ";

		argv[i + 1] = arg;
	}
	
	std::cout << std::endl;

	argv[args.Length() + 1] = nullptr;

	ffmpeg(args.Length() + 1, argv);

	for (int i = 1; i < args.Length() + 1; i++) {
		delete[] argv[i];
	}

	delete[] argv;
}

Napi::Object Init(Napi::Env env, Napi::Object exports) {
	exports.Set(Napi::String::New(env, "ffmpeg"), Napi::Function::New(env, Run));
	return exports;
}

NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init)
