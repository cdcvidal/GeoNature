SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

---------
--DATAS--
---------

INSERT INTO gn_meta.t_datasets VALUES 
(1, 'Contact aléatoire', 'Observation aléatoire de la faune, de la flore ou de la fonge', 1, 2, 2, 2, 2, true, NULL, '2017-06-01 00:00:00', '2017-06-01 00:00:00')
,(2, 'ATBI Lauvitel', 'Inventaire biologique généralisé sur la réserve du Lauvitel', 1, 2, 2, 2, 2, true, NULL, '2017-06-01 00:00:00', '2017-06-01 00:00:00');

INSERT INTO gn_synthese.t_modules (id_module, name_module, desc_module, entity_module_pk_field, url_module, target, picto_module, groupe_module, active) VALUES 
(1, 'Contact faune flore', 'Données issues du contact aléatoire', 'pr_contact.t_occurrences_contact.id_occurrence_contact', '/contact', NULL, NULL, 'CONTACT', true);

INSERT INTO pr_contact.t_releves_contact VALUES 
(1,1,1,'2017-01-01','2017-01-01',1500,1565,FALSE,'web',now(),now(),'Exemple test','01010000206A0800002E988D737BCC2D41ECFA38A659805841','0101000020E61000000000000000001A40CDCCCCCCCC6C4640')
,(2,1,1,'2017-01-08','2017-01-08',1600,1600,FALSE,'web',now(),now(),'Autre exemple test','01010000206A0800002E988D737BCC2D41ECFA38A659805841','0101000020E61000000000000000001A40CDCCCCCCCC6C4640');
SELECT pg_catalog.setval('pr_contact.t_releves_contact_id_releve_contact_seq', 2, true);

INSERT INTO pr_contact.t_occurrences_contact VALUES 
(1,1,343,65,177,30,182,91,347,163,1,'Gil','Gees',60612,'Lynx Boréal','Taxref V9.0','','','Poil',FALSE, now(),now(),'Test')
,(2,1,343,65,177,30,182,91,347,163,1,'Gil D','Gees',351,'Grenouille rousse','Taxref V9.0','','','Poils de plumes',FALSE, now(),now(),'Autre test')
,(3,2,343,65,177,30,182,91,347,163,1,'Donovan M','Gees',67111,'Ablette','Taxref V9.0','','','Poils de plumes',FALSE, now(),now(),'Troisieme test');
SELECT pg_catalog.setval('pr_contact.t_occurrences_contact_id_occurrence_contact_seq', 3, true);

INSERT INTO pr_contact.cor_role_releves_contact VALUES 
(1,1)
,(2,1);


INSERT INTO  pr_contact.cor_counting_contact (id_counting_contact, id_occurrence_contact, id_nomenclature_life_stage, id_nomenclature_sex, id_nomenclature_obj_count, id_nomenclature_type_count, count_min, count_max) VALUES
(1,1,4,190,166,107,5,5)
,(2,1,4,191,166,107,1,1),
(3,2,4,191,166,107,1,1),
(4,3,4,191,166,107,1,1);
SELECT pg_catalog.setval('pr_contact.cor_counting_contact_id_counting_contact_seq', 4, true);