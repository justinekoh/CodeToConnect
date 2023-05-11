DROP TABLE IF EXISTS ClientConfigurations;
DROP TABLE IF EXISTS Roles;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Requests;
DROP TABLE IF EXISTS AuditLogs;

-- optional: created_at timestamp NOT NULL, is_deleted boolean not null default false, deleted_at timestamp
-- check numeric
-- check bigserial vs serial

CREATE TABLE IF NOT EXISTS ClientConfigurations (
	id SERIAL PRIMARY KEY,
	name varchar(100) NOT NULL,
	gross_amount_tolerance numeric NOT NULL,
	commission_tolerance numeric NOT NULL
);

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
	foreign key (requester_id) references Users (id) NOT NULL,
	foreign key (verifier_id) references Users (id), -- can either reject or approve
	foreign key (client_configuration_id) references ClientConfigurations (id) NOT NULL,
	gross_amount_tolerance_to numeric NOT NULL,
	commission_tolerance_to numeric NOT NULL
);

CREATE TABLE IF NOT EXISTS AuditLogs (
	id SERIAL PRIMARY KEY,
	created_at timestamp NOT NULL,
	status_id integer NOT NULL,
	foreign key (request_id) references Requests (id) NOT NULL,
	foreign key (requester_id) references Users (id) NOT NULL,
	foreign key (verifier_id) references Users (id),
	foreign key (client_configuration_id) references ClientConfigurations (id) NOT NULL,
	gross_amount_tolerance_from numeric NOT NULL,
	gross_amount_tolerance_to numeric NOT NULL,
	commission_tolerance_from numeric NOT NULL,
	commission_tolerance_to numeric NOT NULL
);

