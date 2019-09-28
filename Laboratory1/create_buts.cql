CREATE KEYSPACE keyspace1
WITH replication = {
	'class' : 'SimpleStrategy',
	'replication_factor' : 1
};

create type keyspace1.person_type(
	name text,
	age int,
	gender text,
	family_state text
) ;


CREATE TABLE keyspace1."Client" (
holiday_name text,
present_name text,
passport_num int,
character frozen <person_type>,
PRIMARY KEY (passport_num)

);







CREATE TABLE keyspace1."Presents" (
present_name text,
store_name text,
count_items int static,
PRIMARY KEY (store_name,present_name)

);




CREATE TABLE keyspace1."Holiday" (
 holiday_name text,
 season_year text , 
 PRIMARY KEY (holiday_name)
);


CREATE TABLE keyspace1."Stores" (
	store_name text,
	store_properties MAP<text, FROZEN<SET<text>>>,
	PRIMARY KEY (store_name)
);

CREATE TABLE keyspace1."Stores_Holiday_Presents_Client"(
	 holiday_name text,
 season_year text , 
	store_properties MAP<text, FROZEN<SET<text>>>,
	present_name text,
store_name text,
count_items int static,
	passport_num int,
character frozen <person_type>,
PRIMARY KEY((passport_num),store_name,holiday_name,present_name)
);