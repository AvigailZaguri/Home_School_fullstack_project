insert into class
VALUES ('first'),
('second'),
('third'),
('fourth'),
('fifth')
insert into student
VALUES
('Shira Levi','first','shira@gmail.com','0589658478'),
('Leah Gad','first','leah@gmail.com','0556532545'),
('Moria Rony','second','moria@gmail.com','0549958687'),
('Moshe Gol','second','moshe@gmail.com','0549958687'),
('David Gold','third','david@gmail.com','025454254'),
('Gila Shan','third','gila@gmail.com','0565656548'),
('Sara Mor','fourth','sara@gmail.com','0565656671'),
('Sari Lor','fourth','sari@gmail.com','0565656621'),
('Ayala Chen','fifth','ayalac@gmail.com','0565656222'),
('Talya Ben','fifth','talyab@gmail.com','0565656631')
insert into teacher
VALUES
('Chava Lev', 'chaval@gmail.com', '0505656631'),
('Moshe Dain', 'moshed@gmail.com', '0504141320'),
('Lotem Hiki', 'lotemh@gmail.com', '0525343520'),
('Vered Shai', 'veredshai@gmail.com', '0505656123'),
('Daivid Turd', 'daividturd@gmail.com', '0505656222')
insert into subject_
VALUES
(Null,'Chava Lev', 'Math', 'https://us04web.zoom.us/j/74707087738?pwd=V3BnbTRoUjh5czdDOUdRVnAzT3lPdz09'),
(Null,'Moshe Dain', 'English', 'https://us04web.zoom.us/j/74707087738?pwd=V3BnbTRoUjh5czdDOUdRVnAzT3lPdz09'),
(Null,'Lotem Hiki', 'History', 'https://us04web.zoom.us/j/74707087738?pwd=V3BnbTRoUjh5czdDOUdRVnAzT3lPdz09'),
(Null,'Vered Shai', 'Art', 'https://us04web.zoom.us/j/74707087738?pwd=V3BnbTRoUjh5czdDOUdRVnAzT3lPdz09'),
(Null,'Daivid Turd', 'Tanach', 'https://us04web.zoom.us/j/74707087738?pwd=V3BnbTRoUjh5czdDOUdRVnAzT3lPdz09')
insert into week_schedule
VALUES
('first', 1, '09:00:00',1),
('first', 1, '10:00:00',2),
('first', 1, '11:00:00',4),
('first', 2, '09:00:00',5),
('first', 2, '10:00:00',1),
('first', 2, '12:00:00',2),
('first', 3, '09:00:00',1),
('first', 3, '10:00:00',2),
('first', 3, '11:00:00',3),
('first', 4, '09:00:00',5),
('first', 4, '10:00:00',1),
('first', 4, '12:00:00',2),
('first', 5, '09:00:00',1),
('first', 5, '10:00:00',2),
('first', 5, '11:00:00',4),
('first', 6, '09:00:00',3),
('first', 6, '10:00:00',1)
insert into week_schedule
VALUES
('first', 3, '12:00',5)


insert into task
values
(null,'first',3,'09:00:00','2021-01-12', 'Solve all the exercises on pages: 22-27.'),
(null,'first',3,'10:00:00','2021-01-12', 'Complete all sentences on pages: 12-16.'),
(null,'first',3,'11:00:00','2021-01-12', 'Answer to the questions on the book page 5.'),
(null,'first',4,'09:00:00','2021-01-13', 'Start studying to the test.'),
(null,'first',4,'10:00:00','2021-01-13', 'Complete all sentences on pages: 10-14.'),
(null,'first',4,'12:00:00','2021-01-13', 'Solve all the exercises on pages: 20-25.')

insert into student_task
(name_,task_id)
values
('Shira Levi',1),
('Shira Levi',2),
('Shira Levi',3),
('Shira Levi',4),
('Shira Levi',5),
('Shira Levi',6),
('Leah Gad',1),
('Leah Gad',2),
('Leah Gad',3),
('Leah Gad',4),
('Leah Gad',5),
('Leah Gad',6)
