#pragma once

#include<string>

class Info_Exchange
{
	 
private:
	std::string inMessage;
	std::string outMessage;

public:
	Info_Exchange();

	~Info_Exchange();

	std::string decode();

	std::string encode();

};

