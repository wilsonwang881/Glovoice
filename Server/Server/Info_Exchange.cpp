#include "stdafx.h"
#include "Info_Exchange.h"


Info_Exchange::Info_Exchange()
{
}


Info_Exchange::~Info_Exchange()
{
}

std::string Info_Exchange::decode()
{
	return this->inMessage;
}

std::string Info_Exchange::encode()
{
	return this->outMessage;
}
