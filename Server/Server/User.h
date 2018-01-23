#pragma once

#include <string>
#include "Info_Exchange.h"

class User
{

private:
	std::string userName;
	std::string password;
	std::string userID;
	std::string inQuery;
	std::string outMessage;

	bool status;
	bool admin;

public:
	User();

	User(std::string usrName, std::string passwd);

	User(std::string usrName, std::string passwd, std::string iQuery);

	~User();

	std::string getUserName();

	void updateUserName(std::string newUsrName);

	std::string getPassword();

	void updatePassword(std::string newPassword);

	std::string getQuery();

	void updateQuery(std::string query);

	std::string getMessage();

	void updateMessage(std::string message);

	bool getStatus();

	void changeStatus(bool newStatus);

	bool getAdminStatus();

	void changeAdminStatus(bool newAdminStatus);

	//std::string info_exchange(Info_Exchange info);

};