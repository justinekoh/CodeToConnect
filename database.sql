CREATE TABLE IF NOT EXISTS Roles (
	role_id SERIAL PRIMARY KEY,
	name varchar(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Users (
	id SERIAL PRIMARY KEY,
	name varchar(50) NOT NULL,
	foreign key (role_id) references Roles (id) NOT NULL 
);

CREATE TABLE IF NOT EXISTS Requests (
	id SERIAL PRIMARY KEY,
	request_time timestamp not null,
	foreign key (requester_id) references Users (id) NOT NULL
);
