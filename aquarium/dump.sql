-- Database: test

-- DROP DATABASE IF EXISTS test;



DROP TABLE IF EXISTS espece CASCADE;
DROP TABLE IF EXISTS animal CASCADE;
DROP TABLE IF EXISTS vivre CASCADE;
DROP TABLE IF EXISTS bassin CASCADE;
DROP TABLE IF EXISTS FAIRE CASCADE;
DROP TABLE IF EXISTS activite CASCADE;
DROP TABLE IF EXISTS emploi_temps CASCADE;
DROP TABLE IF EXISTS secteur CASCADE;
DROP TABLE IF EXISTS contenir CASCADE;
DROP TABLE IF EXISTS employer CASCADE;
DROP TABLE IF EXISTS affecter CASCADE;
DROP TABLE IF EXISTS effectuer CASCADE;
DROP TABLE IF EXISTS role_responsable CASCADE;
DROP TABLE IF EXISTS stock CASCADE;
DROP TABLE IF EXISTS role_gestionnaire CASCADE;
DROP TABLE IF EXISTS lieu_transfert CASCADE;
DROP TABLE IF EXISTS transferer CASCADE;
DROP TABLE IF EXISTS appartient CASCADE;
DROP TABLE IF EXISTS cohabitation CASCADE;




CREATE TABLE animal (
    id_animaux integer PRIMARY KEY,
    nom_animal varchar(50),
    sexe char(1),
    signe_distinctif text,
    date_arriver date NOT NULL,
    date_depart date
);

CREATE TABLE bassin (
    id_bassin varchar(50) PRIMARY KEY,
    capacite_max int NOT NULL,
    volume real NOT NULL,
    etat_eau char(10) NOT NULL
);



CREATE TABLE espece (
    id_espece integer PRIMARY KEY,
    id_animaux integer,
    esperance_de_vie interval,
    regime_alimentaire text ,
    niveau_menace int CHECK(niveau_menace BETWEEN 0 AND 10),
    FOREIGN KEY (id_animaux) REFERENCES animal(id_animaux)
);

CREATE TABLE appartient (
    id_espece integer PRIMARY KEY,
    id_animaux integer,
    FOREIGN KEY (id_animaux) REFERENCES animal(id_animaux),
    FOREIGN KEY (id_espece) REFERENCES espece(id_espece)
);


CREATE TABLE cohabitation (
    id_cohabitation integer PRIMARY KEY,
    id_espece integer,
    FOREIGN KEY (id_espece) REFERENCES espece(id_espece)
);




CREATE TABLE vivre (
    id_bassin varchar(50),
    id_animaux  integer,
    FOREIGN KEY  (id_bassin)  REFERENCES bassin(id_bassin),
    FOREIGN KEY (id_animaux) REFERENCES animal(id_animaux) ON UPDATE CASCADE

);

CREATE TABLE activite (
    id_activite varchar(50) PRIMARY KEY,
    jour text NOT NULL,
    horaire TIMESTAMP,
    ouverture char(3) NOT NULL,
    type_activite text NOT NULL
);


CREATE TABLE emploi_temps (
    id_emploi_temps varchar(55) PRIMARY KEY,
    nombre_heure text

);


CREATE TABLE FAIRE (
    id_bassin varchar(55),
    id_emploi_temps varchar(55),
    id_activite varchar(50),
    PRIMARY KEY (id_bassin,id_activite,id_emploi_temps),
    FOREIGN KEY  (id_bassin) REFERENCES bassin(id_bassin),
    FOREIGN KEY (id_activite) REFERENCES activite(id_activite) ON DELETE CASCADE,
    FOREIGN KEY (id_emploi_temps) REFERENCES emploi_temps(id_emploi_temps)

);








CREATE TABLE secteur (
    id_secteur varchar(50) PRIMARY KEY,
    nom_secteur varchar(50) NOT NULL,
    localisation varchar(50) NOT NULL
);


CREATE TABLE contenir (
    id_bassin varchar(55),
    id_secteur varchar(50),
    PRIMARY KEY(id_bassin,id_secteur),
    FOREIGN KEY (id_bassin) REFERENCES bassin(id_bassin),
    FOREIGN KEY (id_secteur) REFERENCES secteur(id_secteur)

);




CREATE TABLE employer (
    num_securite_social varchar(55) PRIMARY KEY,
    adresse text NOT NULL,
    nom_employer varchar(50) NOT NULL ,
    prenom_employer varchar(55) NOT NULL,
    date_naissance date NOT NULL
);




CREATE TABLE affecter (
    num_securite_social varchar(55),
    id_secteur varchar(50),
    PRIMARY KEY(id_secteur,num_securite_social),
    FOREIGN KEY (num_securite_social)  REFERENCES employer(num_securite_social),
    FOREIGN KEY (id_secteur) REFERENCES secteur(id_secteur)

);



CREATE TABLE effectuer(
  id_activite varchar(50),
  num_securite_social varchar(55),
  PRIMARY KEY(id_activite,num_securite_social),
  FOREIGN KEY (id_activite) REFERENCES activite(id_activite) ON DELETE CASCADE,
  FOREIGN KEY (num_securite_social) REFERENCES employer(num_securite_social)
);



CREATE TABLE role_responsable (
    id_bassin varchar(55),
    num_securite_social varchar(55),

    PRIMARY KEY(id_bassin,num_securite_social),
    FOREIGN KEY (id_bassin) REFERENCES bassin(id_bassin) ,
    FOREIGN KEY (num_securite_social) REFERENCES employer(num_securite_social) ON UPDATE CASCADE


);

CREATE TABLE stock (
    id_stock serial PRIMARY KEY,
    quantite_nourriture integer
);




CREATE TABLE role_gestionnaire(

    id_stock serial,
    num_securite_social varchar(55),
    PRIMARY KEY(id_stock,num_securite_social),
    FOREIGN KEY (id_stock) REFERENCES stock(id_stock),
    FOREIGN KEY (num_securite_social) REFERENCES employer(num_securite_social) ON UPDATE CASCADE


);




CREATE TABLE lieu_transfert(
    id_transfert varchar(50) PRIMARY KEY,
    lieu_naissance text,
    deces text,
    autre text
  );

CREATE TABLE transferer(
    id_animaux integer,
    id_transfert varchar(50),
    FOREIGN KEY (id_animaux) REFERENCES animal(id_animaux),
    FOREIGN KEY (id_transfert) REFERENCES lieu_transfert(id_transfert)
  );


insert into animal values(80,'poisson perroquet','F','nageoire','2000-02-19');
insert into animal values(65,'Demoiselle','M','nageoire','2000-02-19','2005-02-19');
insert into animal values(91,'dytique abeille','F','marcus foncée','2000-02-19');
insert into animal values(18,'Aeschne bleue','M','marcus foncée','2000-02-19');
insert into animal values(54,'etoile de mer','F','couleur','2000-02-19','2005-02-19');
insert into animal values(79,'oursin','F','couleur','2000-02-19','2005-02-19');
insert into animal values(15,'Dauphin','M','nageoire','2000-02-19','2005-02-19');
insert into animal values(185,'Requin aveugle des roches','M','nageoire','2000-02-19','2005-02-19');

insert into secteur values('sect_poisson','poisson tropicaux','sect 4');
insert into secteur values('sect_mammifere_m','mammifère marin','sect 56');
insert into secteur values('sect_echin','echinodermes','sect 7');
insert into secteur values('sect_insecte','insecte de mer','sect 20');
insert into secteur values('sect_Brachaelurus waddi','Brachaelurus waddi','sect A0');

insert into lieu_transfert(id_transfert,lieu_naissance) values('transf1','Aquarium');
insert into lieu_transfert(id_transfert,lieu_naissance)  values('transf2','Aquarium Paris');
insert into lieu_transfert values('transf3','Aquarium','Décèdé');
insert into lieu_transfert(id_transfert,lieu_naissance) values('transf4','Aquarium');
insert into lieu_transfert(id_transfert,lieu_naissance) values('transf5','Aquarium Paris');
insert into lieu_transfert(id_transfert,lieu_naissance)  values('transf6','Aquarium Paris');
insert into lieu_transfert values('transf7','Aquarium','Décèdé');
insert into lieu_transfert values('transf8','Aquarium','Décèdé');

insert into bassin values('numero 1',350,480000,'propre');
insert into bassin values('numero 2',450,180000,'sale');
insert into bassin values('numero 3',150,80000,'sale');
insert into bassin values('numero 4',850,1080000,'propre');
insert into bassin values('numero 5',750,780000,'sale');
insert into bassin values('numero 6',650,980000,'propre');
insert into bassin values('numero 7',950,680000 ,'propre');
insert into bassin values('numero 8',950,680000 ,'propre');

insert into activite values('act_1','lundi', '2001-02-16 10:30:00','oui','nourrissage');
insert into activite values('act_2','lundi','2001-02-16  17:30:00','non','nourrissage');
insert into activite values('act_3','mardi','2001-02-16  14:30:00','non','nourrissage');
insert into activite values('act_4','mardi ','2001-02-16  11:30:00','oui','nourrissage');
insert into activite values('act_5','mercredi', '2001-02-16 13:45:00','oui','nourrissage');
insert into activite values('act_6','mercredi', '2001-02-16 20:50:40','oui','nourrissage');
insert into activite values('act_7','vendredi','2001-02-16 14:30:00','non','inspection de la qualité de l''eau');
insert into activite values('act_8','samedi ','2001-02-16 20:38:40','non','inspection de la qualité de l''eau');
insert into activite values('act_9','dimanche', '2001-02-16 13:45:00','non','inspection de la qualité de l''eau');
insert into activite values('act_10','jeudi', '2001-02-16 14:30:00','oui','bilan véterinaire');
insert into activite values('act_11','vendredi', '2001-02-16 17:30:00','oui','bilan véterinaire');
insert into activite values('act_12','samedi', '2001-02-16 10:30:00','oui','bilan véterinaire');

insert into employer values('a-122-bb','5 rue Adert','Veld','Jean','1956-02-19');
insert into employer values('bb-333-cc','12 avenue dubois','Gruyère','Lilia','2001-02-16');
insert into employer values('432-UFD','92 rue du chateau','Madre','Guillaume','2000-08-04');
insert into employer values('zz-144-V','1 allée des bois ','Load','Maela','1999-12-20');
insert into employer values('a-172-gtb','5 rue Adert','Veldus','Savier','1901-01-05');
insert into employer values('bb-353-oc','12 avenue dubois','Jardin','Laure','1960-02-16');
insert into employer values('732-UFssD','92 rue du chateau','Vervene','Julien','1940-08-20');
insert into employer values('qq-1a4-V77','1 allée des bois ','admistrer','Adrien','1980-05-07');

insert into emploi_temps values('emploi_du_temps1','8h à 19h');
insert into emploi_temps values('emploi_du_temps2',' 15h à 19h');
insert into emploi_temps values('emploi_du_temps3','8h à 13h');
insert into emploi_temps values('emploi_du_temps4','10h à 17h30');
insert into emploi_temps values('emploi_du_temps5','11h à 14h');
insert into emploi_temps values('emploi_du_temps6','8h à 12h');
insert into emploi_temps values('emploi_du_temps7','17h à 20h30');
insert into emploi_temps values('emploi_du_temps8','7h30 à 16h');

insert into espece values(1,80,'10 months','herbivore',0);
insert into espece values(2,65,'10 months','herbivore',0);
insert into espece values(3,91,'10 weeks','herbivore',3);
insert into espece values(4,18,'10 weeks','herbivore',3);
insert into espece values(5,54,'200 years ','carnivore', 4 );
insert into espece values(6,79,'200 years ','piscivores', 4 );
insert into espece values (7,15,'50 years','herbivore ',5 );
insert into espece values(8,185 ,'150 years','carnivore',10);




insert into transferer values(80,'transf1');
insert into transferer values(65,'transf2');
insert into transferer values(91,'transf3');
insert into transferer values(18,'transf4');
insert into transferer values(54,'transf5');
insert into transferer values(79,'transf6');
insert into transferer values(15,'transf7');
insert into transferer values(185,'transf8');

insert into contenir values('numero 1','sect_poisson');
insert into contenir values('numero 2','sect_poisson');
insert into contenir values('numero 3','sect_mammifere_m');
insert into contenir values('numero 4','sect_mammifere_m');
insert into contenir values('numero 5','sect_echin');
insert into contenir values('numero 6','sect_echin');
insert into contenir values('numero 7','sect_insecte');
insert into contenir values('numero 8','sect_Brachaelurus waddi');


insert into affecter values('a-122-bb','sect_mammifere_m');
insert into affecter values('bb-333-cc','sect_poisson');
insert into affecter values('432-UFD','sect_echin');
insert into affecter values('zz-144-V','sect_insecte');
insert into affecter values('a-172-gtb','sect_insecte');
insert into affecter values('bb-353-oc','sect_echin');
insert into affecter values('732-UFssD','sect_mammifere_m');
insert into affecter values('qq-1a4-V77','sect_mammifere_m');
insert into affecter values('qq-1a4-V77','sect_Brachaelurus waddi');



-- à corriger
insert into role_responsable values('numero 1','a-122-bb');
insert into role_responsable values('numero 2','a-122-bb');
insert into role_responsable values('numero 3','a-122-bb');
insert into role_responsable values('numero 4','bb-333-cc');
insert into role_responsable values('numero 5','bb-333-cc');
insert into role_responsable values('numero 6','432-UFD');
insert into role_responsable values('numero 7','432-UFD');
insert into role_responsable values('numero 8','432-UFD');

insert into stock(quantite_nourriture) values(100);
insert into stock(quantite_nourriture) values(15);
insert into stock(quantite_nourriture) values(20);
insert into stock(quantite_nourriture) values(40);

insert into role_gestionnaire values(1,'732-UFssD');
insert into role_gestionnaire values(2,'qq-1a4-V77');
insert into role_gestionnaire values(3,'732-UFssD');
insert into role_gestionnaire values(4,'qq-1a4-V77');
---








insert into cohabitation values(1,2);
insert into cohabitation values(4,3);
insert into cohabitation values(5,4);
insert into cohabitation values(6,7);
insert into cohabitation values(8,8);










insert into vivre values('numero 1', 80);
insert into vivre values('numero 1', 18);
insert into vivre values('numero 3', 65);
insert into vivre values('numero 4',79);
insert into vivre values('numero 5', 80);
insert into vivre values('numero 5', 54);
insert into vivre values('numero 6',18);
insert into vivre values('numero 6',65);
insert into vivre values('numero 4',79);
insert into vivre values('numero 7',91);
insert into vivre values('numero 7',15);
insert into vivre values('numero 8',185);



insert into effectuer values('act_1','a-122-bb');
insert into effectuer values('act_2','bb-333-cc');
insert into effectuer values('act_3','432-UFD');
insert into effectuer values('act_4','zz-144-V');
insert into effectuer values('act_5','a-172-gtb');
insert into effectuer values('act_6','bb-353-oc');
insert into effectuer values('act_7','732-UFssD');
insert into effectuer values('act_8','qq-1a4-V77');
insert into effectuer values('act_9','qq-1a4-V77');
insert into effectuer values('act_10','732-UFssD');
insert into effectuer values('act_11','bb-353-oc');
insert into effectuer values('act_12','a-172-gtb');



insert into FAIRE values('numero 1','emploi_du_temps1','act_1');
insert into FAIRE values('numero 7','emploi_du_temps2','act_2');
insert into FAIRE values('numero 5','emploi_du_temps3','act_3');
insert into FAIRE values('numero 6','emploi_du_temps4','act_4');
insert into FAIRE values('numero 4','emploi_du_temps5','act_5');
insert into FAIRE values('numero 3','emploi_du_temps6','act_6');
insert into FAIRE values('numero 2','emploi_du_temps7','act_7');
insert into FAIRE values('numero 1','emploi_du_temps8','act_8');
insert into FAIRE values('numero 6','emploi_du_temps5','act_9');
insert into FAIRE values('numero 7','emploi_du_temps4','act_10');
insert into FAIRE values('numero 5','emploi_du_temps3','act_11');
insert into FAIRE values('numero 4','emploi_du_temps6','act_12');
insert into FAIRE values('numero 8','emploi_du_temps2','act_12');



