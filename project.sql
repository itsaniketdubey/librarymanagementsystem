create database library;
create table books(
book_id int auto_increment primary key,
title varchar (100) NOT NULL,
author varchar (100) NOT NULL,
stat int default 0,
genreid varchar(10) NOT NULL,
publisher varchar (100) NOT NULL,
price int NOT NULL,
noti int NOT NULL default 0
);


alter table books add constraint foreign key fk (genreid) references genre (genreid) on delete cascade on update cascade;
create table genre(
genreid varchar(10) primary key NOT NULL,
genre_name varchar (50) NOT NULL
);
create table student(
stu_name varchar (50) NOT NULL,
sap_id varchar (10) primary key NOT NULL,
email varchar (70) NOT NULL,
dob date NOT NULL,
contact1 numeric(10) NOT NULL,
contact2 numeric(10),
fine int NOT NULL DEFAULT 0
);
create table borrowes(
borrowed_date date NOT NULL,
return_date date,
due_date date NOT NULL,
book_id int NOT NULL,
sap_id varchar(10) NOT NULL,
primary key (sap_id,book_id)
);
alter table borrowes add constraint foreign key fk1 (sap_id) references student(sap_id) on update cascade on delete cascade;
alter table borrowes add constraint Foreign key fk2 (book_id) references books(book_id) on update cascade on delete cascade;
create table users (
username varchar (50) NOT NULL,
pass varchar (50) NOT NULL,
primary key (username,pass)
);
insert into books (title,author,stat,genreid, publisher,price,noti) values
("Concepts of Physics", "H.C. Verma",1,"1","Bharati Bhawan Publishers",347,1),
("Head First Python","Paul Barry",1,"6","O′Reilly",3137,1),
("The Alchemist","Paulo Coelho",0,"7","Harper",172,6),
("Organic Chemistry","Jonathan Clayden",1,"2","Oxford University Press",2044,1),
("Molecular Biology of the Cell","Bruce Alberts",0,"3","Garland Science",16358,4),
("Fundamentals of Database Systems","Ramez Elmasri",1,"5","Pearson",9476,1),
("The Fault in Our Stars","John Green",7,"7","Penguin",216,1),
("Sapiens: A Brief History of Humankind","Yuval Noah Harari",1,"8","Penguin Random House",396,1),
("Think & Grow Rich","Napoleon Hill",1,"8","Fingerprint Publishing",99,1),
("MSc Chemistry","R. S. Arora ",0,"2","Unique Publishers",492,2);

insert into books (title,author,genreid,publisher,price)values 
( "Algebra 2", "Glencoe McGraw Hill","4", "The McGrawHill Companies Inc.", 440),
("The Boy from Pataliputra","Rahul Mitra","7","Fingerprint Publishing",165),
( "Database System Concepts","Abraham Silberschatz","5","McGraw Hill Education",950),
("University Physics","Young Hugh D.","1","Pearson",806),
("Relativity: The Special and the General Theory","Albert Einstein","1","Fingerprint Publishing",129),
("Handbook of Pysics","Arihant Experts","1","Arihant Publications",190),
("Wiley's Solomons Fryhle & Snyder Organic Chemistry","M S Chouhan","2","Wiley",784),
("The Origin of Species","Charles Darwin","3","Fingerprint Publishing",159),
( "Essential Cell Biology","Dennis Bray","3","Garland Science",5452),
("The Princeton Companion to Mathematics","Timothy Gowers","4","Princeton University Press",9442),
("What Is Mathematics?","Richard Courant","4","OUP USA",2077),
("Principles of Mathematical Analysis","Walter Rudin","4","McGraw Hill Education",348),
("Database Management Systems","Rajiv Chopra","5","S Chand Publishing",499),
( "An Introduction to Database Systems","C.J. Date","5","Pearson",2600),
("Automate the Boring Stuff with Python","Al Sweigart","6","No Starch Press",1650),
("Learning Python","Mark Lutz","6","O′Reilly",1400),
("Learn Python the Hard Way","Zed Shaw","6","Addison-Wesley",2863),
("Harry Potter and the Philosopher's Stone","J.K. Rowling","7","Pottermore Publishing",273),
( "The Psychology of Money","Morgan Housel","8","Jaico Publishing House",262);
select * from books;
insert into genre values 
("1","Physics"),
("2", "Chemistry"),
("3", "Biology"),
("4", "Mathematics"),
("5", "Database Management"),
("6", "Python"),
("7", "Fiction"),
("8", "Non-Fiction");
insert into student (stu_name,sap_id,email,dob,contact1,contact2) values ('Aryan',"001",'aryan@gmail.com',str_to_date('2001-04-10','%Y-%m-%d'),9145678912,1234567891),
						   ('Aniket',"002",'aniket@gmail.com',str_to_date('2001-02-01','%Y-%m-%d'),8456179231,7541323698),
                           ('Rishabh',"003",'rishabh@gmail.com',str_to_date('2001-04-08','%Y-%m-%d'),7894561237,8015467941),
                           ('Vedant',"004",'vedant@gmail.com',str_to_date('2001-12-07','%Y-%m-%d'),7589647123,9258796354),
                           ('Jash',"005",'jash@gmail.com',str_to_date('2001-11-09','%Y-%m-%d'),4567891234,8857412349),
                           ('Dhruv',"006",'dhruv@gmail.com',str_to_date('2001-10-11','%Y-%m-%d'),7456123478,9874561234),
                           ('Tanishq',"007",'tan@gmail.com',str_to_date('2000-10-21','%Y-%m-%d'),7456123478,9874561234),
                           ('Taral','008','taral@gmail.com',str_to_date('2001-06-21','%Y-%m-%d'),9988776655,8797146790),
                           ('Rushabh','009','rushabh@gmail.com',str_to_date('2001-04-11','%Y-%m-%d'),9198906541,9909087291),
                           ('Kris','010','kris@gmail.com',str_to_date('2001-08-11','%Y-%m-%d'),8898850111,8787740222);
                           
insert into student (stu_name,sap_id,email,dob,contact1,contact2) values ('Kshitij','011','kshitij@gmail.com',str_to_date('2001-08-29','%Y-%m-%d'),9572782970,8562728205),
                           ('Vardhaman','012','vardhaman@gmail.com',str_to_date('2001-04-09','%Y-%m-%d'),8089665088 ,8576594660),
                           ('Om','013','om@gmail.com',str_to_date('2001-07-09','%Y-%m-%d'),9475961816,9833475421),
                           ('Yash','014','yash@gmail.com',str_to_date('2001-12-29','%Y-%m-%d'),8518197138 ,9691742996),
                           ('Priyam','015','priyam@gmail.com',str_to_date('2001-10-07','%Y-%m-%d'),8167682344 ,9942330265 );
insert into student(stu_name,sap_id,email,dob,contact1,contact2) values ('Anisha',"016",'anisha@gmail.com',str_to_date('2001-04-15','%Y-%m-%d'),8469728668,3611353554),
                           ('Nishi',"017",'nishi@gmail.com',str_to_date('2001-07-21','%Y-%m-%d'),1770654251,3676903124 ),
                           ('Devika',"018",'devika@gmail.com',str_to_date('2000-05-13','%Y-%m-%d'),9632534586,0262752611 ),
                           ('Aaryanna',"019",'aaryanna@gmail.com',str_to_date('2001-11-06','%Y-%m-%d'),2423135088,0907266753),
                           ('Pooja',"020",'pooja@gmail.com',str_to_date('2001-12-25','%Y-%m-%d'),2134605790,4152723773),
                           ('Diti',"021",'diti@gmail.com',str_to_date('2000-07-10','%Y-%m-%d'),9967843442,7148249494),
                           ('Vrishali',"022",'vrishali@gmail.com',str_to_date('2001-06-27','%Y-%m-%d'),7513054854,7556523273 ),
                           ('Riya',"023",'riya@gmail.com',str_to_date('2001-04-14','%Y-%m-%d'),4732582363 ,1931387729 ),
                           ('Diyoni',"024",'diyoni@gmail.com',str_to_date('2001-09-17','%Y-%m-%d'),7780048616,8358636495),
					       ('Kalyani',"025",'kalyani@gmail.com',str_to_date('2001-07-11','%Y-%m-%d'),5625394849,8495506486 );

insert into borrowes(borrowed_date,return_date,due_date,book_id,sap_id) values
(str_to_date('2021-03-10','%Y-%m-%d'),str_to_date('2021-03-17','%Y-%m-%d'),str_to_date('2021-03-17','%Y-%m-%d'),1,"003"),
(str_to_date('2021-02-02','%Y-%m-%d'),str_to_date('2021-02-09','%Y-%m-%d'),str_to_date('2021-02-09','%Y-%m-%d'),2,"001"),
(str_to_date('2021-03-03','%Y-%m-%d'),str_to_date('2021-03-10','%Y-%m-%d'),str_to_date('2021-03-10','%Y-%m-%d'),4,"005"),
(str_to_date('2021-01-02','%Y-%m-%d'),str_to_date('2021-01-09','%Y-%m-%d'),str_to_date('2021-01-09','%Y-%m-%d'),6,"002"),
(str_to_date('2021-02-20','%Y-%m-%d'),str_to_date('2021-02-27','%Y-%m-%d'),str_to_date('2021-02-27','%Y-%m-%d'),7,"004"),
(str_to_date('2021-01-03','%Y-%m-%d'),str_to_date('2021-01-10','%Y-%m-%d'),str_to_date('2021-01-10','%Y-%m-%d'),8,"003");
insert into borrowes (borrowed_date,due_date,book_id,sap_id) values 
(str_to_date('2021-04-02','%Y-%m-%d'),str_to_date('2021-04-09','%Y-%m-%d'),9,"022");
insert into users values
("user","pass"),
("admin","admin");

select * from borrowes;

update borrowes set return_date = NULL where sap_id = "022";
