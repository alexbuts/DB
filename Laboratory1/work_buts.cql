insert into keyspace1."Stores_Holiday_Presents_Client"(holiday_name,season_year,store_properties,present_name,store_name,count_items,passport_num,character) values ('Easter','spring',{'Location':{'Kyiv','Dnipro'}},'Smartphone','Comfy',9,103,{name:'Alex',age: 21,gender :'M',family_state: 'Notmarried'});
insert into keyspace1."Stores_Holiday_Presents_Client"(holiday_name,season_year,store_properties,present_name,store_name,count_items,passport_num,character) values ('Christmas','winter',{'Location':{'Kyiv','Dnipro'}},'Smartphone','Comfy',9,102,{name:'Valera',age: 54,gender :'M',family_state: 'married'});
insert into keyspace1."Stores_Holiday_Presents_Client"(holiday_name,season_year,store_properties,present_name,store_name,count_items,passport_num,character) values ('8 March','spring',{'Location':{'Kyiv','Kharkiv'},'Bank':{'Privat','Deutchebank'}},'Flowers','Silpo',9,101,{name:'Olga',age: 28,gender :'W',family_state: 'Notmarried'});

select * from keyspace1."Stores_Holiday_Presents_Client";
 update keyspace1."Stores_Holiday_Presents_Client" set count_items = 8 ,store_properties = {'Location':{'Kyiv','Lviv'}}
 where holiday_name = '8 March' and present_name ='Flowers' and passport_num= 101 and store_name = 'Silpo';
 
 update keyspace1."Stores_Holiday_Presents_Client" set season_year = 'Autinm' 
 where holiday_name = 'Christmas' and  present_name ='Smartphone' and passport_num = 102 and store_name ='Comfy';
  
  update keyspace1."Stores_Holiday_Presents_Client" set character = {name:'Olga',age: 30,gender :'W',family_state: 'Notmarried'}
   where holiday_name = '8 March' and present_name ='Flowers' and passport_num= 101 and store_name = 'Silpo' ;
 
 
   
DELETE season_year FROM keyspace1."Stores_Holiday_Presents_Client"
where holiday_name = '8 March' and present_name ='Flowers' and passport_num= 101 and store_name = 'Silpo';


DELETE store_properties FROM keyspace1."Stores_Holiday_Presents_Client"
where holiday_name = '8 March' and present_name ='Flowers' and passport_num= 101 and store_name = 'Silpo';


DELETE store_properties FROM keyspace1."Stores_Holiday_Presents_Client"
 where holiday_name = 'Christmas' and  present_name ='Smartphone' and passport_num = 102 and store_name ='Comfy';

SELECT * FROM keyspace1."Stores_Holiday_Presents_Client";




SELECT store_properties,present_name
FROM keyspace1."Stores_Holiday_Presents_Client"
WHERE  character={name:'Valera',age: 54,gender :'M',family_state: 'married'};


SELECT *
FROM keyspace1."Stores_Holiday_Presents_Client" 
WHERE passport_num=102;



SELECT character,season_year
FROM keyspace1."Stores_Holiday_Presents_Client"
WHERE passport_num=101;


SELECT store_name,present_name
FROM keyspace1."Stores_Holiday_Presents_Client"
WHERE season_year='winter';

create index Ind on keyspace1."Stores_Holiday_Presents_Client" (season_year);
create index Ind2 on keyspace1."Stores_Holiday_Presents_Client" (character);
 