#include "stdafx.h"
#include "User.h"
#include <iostream>

User::User()
{

}

User::User(std::string usrName, std::string passwd)
{
	this->userName = usrName;
	this->password = passwd;
}

User::User(std::string usrName, std::string passwd, std::string iQuery)
{
	this->userName = usrName;
	this->password = passwd;
	this->inQuery = iQuery;
}

User::~User()
{
}

std::string User::getUserName()
{
	return this->userName;
}

void User::updateUserName(std::string newUsrName)
{
	this->userName = newUsrName;
}

std::string User::getPassword()
{
	return this->password;
}

void User::updatePassword(std::string newPassword)
{
	this->password = newPassword;
}

std::string User::getQuery()
{
	return this->inQuery;
}

void User::updateQuery(std::string query)
{
	this->inQuery = query;
}

std::string User::getMessage()
{
	return this->outMessage;
}

void User::updateMessage(std::string message)
{
	this->outMessage = message;
}

bool User::getStatus()
{
	return this->status;
}

void User::changeStatus(bool newStatus)
{
	this->status = newStatus;
}

bool User::getAdminStatus()
{
	return this->admin;
}

void User::changeAdminStatus(bool newAdminStatus)
{
	this->admin = newAdminStatus;
}

/**void User::getFromInfo_Exchange(Info_Exchange::Info_Exchange info)
{
	std::cout << "testing message" << std::endl;
}
**/
