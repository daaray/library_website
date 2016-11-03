# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-03 21:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dirbrowse', '0031_auto_20161014_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dirbrowsepage',
            name='content_specialist',
            field=models.ForeignKey(choices=[(44, 'Ricardo R Andrade'), (125, 'Jeffry D. Archer'), (85, 'Dean W. Armstrong'), (51, 'Dale Arntson'), (149, 'Kathleen Arthur'), (184, 'Melina Avery'), (1883, 'Shauna Babcock'), (54, 'Brian Balsamo'), (247, 'Terry Banks'), (55, 'Timothy Barnaby'), (177, 'Michelle B Bass'), (167, 'Linda Beezhold'), (205, 'Paul Belloni'), (82, 'David Bietila'), (71, 'Charles Blair'), (4906, 'Emma Boettcher'), (226, 'Steven Boozer'), (90, 'David Borycz'), (83, 'David W. Bottorff'), (225, 'Samuel B Brown'), (182, 'Michael D. Brown'), (99, 'Ellen Bryan'), (43, 'Amy M Buckland'), (211, 'Vicki Burwell-Rankin'), (56, 'Bradley Busenius'), (65, 'Maura Byrne'), (227, 'Sherry Byrne'), (134, 'John Carey'), (248, 'Timothy Clark'), (180, 'Miranda Clower'), (241, 'Steve Coats'), (66, 'Christine Colburn'), (102, 'Evelyn Collier'), (76, 'Kevin A Collier'), (77, 'James Collins'), (78, 'Christopher Cronin'), (250, 'Theodore Cueller'), (249, 'Tyler Danstrom'), (213, 'Renee Darosky'), (126, 'Judith Dartt'), (84, 'Dora Davis'), (235, 'Subrata De'), (86, 'Will Degenhard'), (228, 'Sean Dempsey'), (178, 'Melanie Dial'), (254, 'Thomas Dousa'), (255, 'Thomas Drueke'), (4835, 'Jennifer Dunlap'), (214, 'Ronald Durham'), (96, 'Elizabeth Edwards'), (68, 'Charles Ellington'), (186, 'Michael C Evans'), (201, 'Octavia Fallwell'), (88, 'David Farley'), (140, 'June P. Farris'), (152, 'Kathleen Feeney'), (69, 'Lily Fieg'), (229, 'Sean Filipov'), (179, 'M. Constance Fleischer'), (107, 'Greg Fleming'), (172, 'Lynn Franco'), (2469, 'David H Frankel'), (4815, 'Jennifer Frary'), (212, 'Raymond Gadke'), (148, 'Julia Gardner'), (252, 'Timothy Garrison'), (111, 'Joseph Gerdeman'), (204, 'Patti Gibbons'), (58, 'Barbara Gilbert'), (103, 'Fabian Gonzalez'), (52, 'Ashley Locke Gosselar'), (132, 'Jaymes B Grider'), (116, 'Gerald Hall'), (142, 'Jamal Hamilton'), (79, 'Catherine Hardy'), (232, 'Susan Harkins'), (89, 'Diana Rose Harper'), (118, 'Jamaar Harris'), (119, 'Jennifer Hart'), (166, 'Laurie Haugland'), (154, 'Kiku Hibino'), (4878, 'Taylor Hixson'), (110, 'Geraldine Hogue'), (98, 'Eileen Ielmini'), (253, 'Todd Ito'), (61, 'Brenda Johnson'), (70, 'Charlotte Jones'), (129, 'John Jung'), (135, 'John Kaderbek'), (4816, 'Kera Kelly'), (187, 'Mark Kennel'), (191, 'Michael Kenny'), (59, 'Barbara Kern'), (123, 'Hyerye Kim'), (131, 'Jenny Kim'), (42, 'Anne Knafl'), (207, 'Priya Kuppuraju'), (120, 'Hannah Landsman'), (236, 'Scott Landvatter'), (164, 'David K. Larsen'), (137, 'Jackie Larson'), (267, 'Simon Lee'), (39, 'Andrew D Lee'), (237, 'Sandra Levy'), (192, 'Melanie Levy'), (234, 'Sheri Lewis'), (46, 'Ann Lindsey'), (121, 'Holly Lipschultz'), (100, 'Elisabeth Long'), (168, 'Lyonette Louis-Jacques'), (41, 'Andrew John Lovdahl'), (57, 'Benita Luke'), (108, 'Grace Lyons'), (73, 'Cheryl Malmborg'), (113, 'Gary Mamlin'), (174, 'Amy Mantrone'), (74, 'Clint Marcy'), (175, 'Catherine M. Mardikes'), (158, 'Kristin E Martin'), (4967, 'Susan Martin'), (217, 'Renee Martonik'), (169, 'Janet L Mather'), (4834, 'Anita Marie Mechler'), (200, 'Edd Merkel'), (185, 'Stacey Metralexis'), (50, 'Daniel Meyer'), (130, 'Jon Miller'), (266, 'Yuan Mo'), (159, 'Kiya Moody'), (242, 'Steven Moore'), (189, 'James Mouw'), (75, 'Colleen Mullarkey'), (97, 'Erica Myles'), (269, 'Youli Na'), (62, 'Brittan Nannenga'), (219, 'Rose Navarro'), (2764, 'Olaf Nelson'), (87, 'Daryl Nelson'), (60, 'Benjamin Niespodziany'), (114, 'Greg Nimmo'), (139, 'James Nye'), (47, 'Adrianne Okoh'), (256, 'Tod Olson'), (265, 'Yasmin Omer'), (221, 'Ru Orb'), (48, 'Anderson Orsburn'), (196, 'Natascha Owens'), (128, 'Jee-Young Park'), (4833, 'Arnisha Parker'), (115, 'Gail Parks'), (124, 'James Anthony Patterson'), (243, 'Scott Perry'), (141, 'Julie Piacentine'), (49, 'Aaron Platte'), (222, 'Robert Pleshar'), (206, 'Laura Pontillo'), (91, 'Darryl Poole'), (160, 'Karen Prack'), (173, 'Mallory A Price'), (262, 'Bill Pugh'), (264, 'Xiaowen Qian'), (170, 'Liping Qin'), (209, 'Sheila Ralston'), (210, 'Emily Raney'), (216, 'Laura Ring'), (4842, 'Jason Robertson'), (223, 'Rachel Rosenberg'), (92, 'Darrin Rosenthal'), (45, 'Andrew Rusin'), (194, 'Marlis J. Saleh'), (208, 'Patricia Sayre-McCoy'), (109, 'George Schell'), (183, 'Margaret A. Schilt'), (260, 'William A. Schwesig'), (146, 'Joseph T Scott'), (104, 'Fred Seaton'), (143, 'James Server'), (198, 'Natasha Sharp'), (4879, 'Allyson E Smally'), (199, 'Nancy Spiegel'), (161, 'Kaitlin A Springmier'), (224, 'Rebecca Starkey'), (106, 'Julie R. Stauffer'), (80, 'Carol Stewart'), (244, 'Christopher Alexander Straughn'), (251, 'Teresa E Sullivan'), (1157, 'Sem C Sutter'), (144, 'James M. Swanson'), (93, 'Deborah Taylor'), (64, 'Brandon Tharp'), (72, 'Christie Thomas'), (101, 'Emily Anne Treptow'), (53, 'Andrea Twiss-Brooks'), (188, 'Marcene Tyler'), (81, 'Catherine Uecker'), (151, 'Keith Waclena'), (259, 'Larisa Walsh'), (176, 'Mary Lee Ward'), (231, 'Sarah G. Wenzel'), (94, 'Debra A Werner'), (171, 'Linda Wheatley-Irving'), (263, 'William White'), (190, 'Peggy Wilkins'), (112, "G'Jordan Williams"), (203, 'Patricia A. Williams'), (246, 'Shelia Wright-Coney'), (133, 'Jiaxun Benjamin Wu'), (127, 'Jin Xu'), (268, 'Ayako Yoshimura'), (163, 'Kathy Zadrozny'), (270, 'Yuan Zhou'), (271, 'Xiaoquan Zhu'), (5090, 'Karen Yu')], null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dirbrowse_dirbrowsepage_content_specialist', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='dirbrowsepage',
            name='editor',
            field=models.ForeignKey(choices=[(44, 'Ricardo R Andrade'), (125, 'Jeffry D. Archer'), (85, 'Dean W. Armstrong'), (51, 'Dale Arntson'), (149, 'Kathleen Arthur'), (184, 'Melina Avery'), (1883, 'Shauna Babcock'), (54, 'Brian Balsamo'), (247, 'Terry Banks'), (55, 'Timothy Barnaby'), (177, 'Michelle B Bass'), (167, 'Linda Beezhold'), (205, 'Paul Belloni'), (82, 'David Bietila'), (71, 'Charles Blair'), (4906, 'Emma Boettcher'), (226, 'Steven Boozer'), (90, 'David Borycz'), (83, 'David W. Bottorff'), (225, 'Samuel B Brown'), (182, 'Michael D. Brown'), (99, 'Ellen Bryan'), (43, 'Amy M Buckland'), (211, 'Vicki Burwell-Rankin'), (56, 'Bradley Busenius'), (65, 'Maura Byrne'), (227, 'Sherry Byrne'), (134, 'John Carey'), (248, 'Timothy Clark'), (180, 'Miranda Clower'), (241, 'Steve Coats'), (66, 'Christine Colburn'), (102, 'Evelyn Collier'), (76, 'Kevin A Collier'), (77, 'James Collins'), (78, 'Christopher Cronin'), (250, 'Theodore Cueller'), (249, 'Tyler Danstrom'), (213, 'Renee Darosky'), (126, 'Judith Dartt'), (84, 'Dora Davis'), (235, 'Subrata De'), (86, 'Will Degenhard'), (228, 'Sean Dempsey'), (178, 'Melanie Dial'), (254, 'Thomas Dousa'), (255, 'Thomas Drueke'), (4835, 'Jennifer Dunlap'), (214, 'Ronald Durham'), (96, 'Elizabeth Edwards'), (68, 'Charles Ellington'), (186, 'Michael C Evans'), (201, 'Octavia Fallwell'), (88, 'David Farley'), (140, 'June P. Farris'), (152, 'Kathleen Feeney'), (69, 'Lily Fieg'), (229, 'Sean Filipov'), (179, 'M. Constance Fleischer'), (107, 'Greg Fleming'), (172, 'Lynn Franco'), (2469, 'David H Frankel'), (4815, 'Jennifer Frary'), (212, 'Raymond Gadke'), (148, 'Julia Gardner'), (252, 'Timothy Garrison'), (111, 'Joseph Gerdeman'), (204, 'Patti Gibbons'), (58, 'Barbara Gilbert'), (103, 'Fabian Gonzalez'), (52, 'Ashley Locke Gosselar'), (132, 'Jaymes B Grider'), (116, 'Gerald Hall'), (142, 'Jamal Hamilton'), (79, 'Catherine Hardy'), (232, 'Susan Harkins'), (89, 'Diana Rose Harper'), (118, 'Jamaar Harris'), (119, 'Jennifer Hart'), (166, 'Laurie Haugland'), (154, 'Kiku Hibino'), (4878, 'Taylor Hixson'), (110, 'Geraldine Hogue'), (98, 'Eileen Ielmini'), (253, 'Todd Ito'), (61, 'Brenda Johnson'), (70, 'Charlotte Jones'), (129, 'John Jung'), (135, 'John Kaderbek'), (4816, 'Kera Kelly'), (187, 'Mark Kennel'), (191, 'Michael Kenny'), (59, 'Barbara Kern'), (123, 'Hyerye Kim'), (131, 'Jenny Kim'), (42, 'Anne Knafl'), (207, 'Priya Kuppuraju'), (120, 'Hannah Landsman'), (236, 'Scott Landvatter'), (164, 'David K. Larsen'), (137, 'Jackie Larson'), (267, 'Simon Lee'), (39, 'Andrew D Lee'), (237, 'Sandra Levy'), (192, 'Melanie Levy'), (234, 'Sheri Lewis'), (46, 'Ann Lindsey'), (121, 'Holly Lipschultz'), (100, 'Elisabeth Long'), (168, 'Lyonette Louis-Jacques'), (41, 'Andrew John Lovdahl'), (57, 'Benita Luke'), (108, 'Grace Lyons'), (73, 'Cheryl Malmborg'), (113, 'Gary Mamlin'), (174, 'Amy Mantrone'), (74, 'Clint Marcy'), (175, 'Catherine M. Mardikes'), (158, 'Kristin E Martin'), (4967, 'Susan Martin'), (217, 'Renee Martonik'), (169, 'Janet L Mather'), (4834, 'Anita Marie Mechler'), (200, 'Edd Merkel'), (185, 'Stacey Metralexis'), (50, 'Daniel Meyer'), (130, 'Jon Miller'), (266, 'Yuan Mo'), (159, 'Kiya Moody'), (242, 'Steven Moore'), (189, 'James Mouw'), (75, 'Colleen Mullarkey'), (97, 'Erica Myles'), (269, 'Youli Na'), (62, 'Brittan Nannenga'), (219, 'Rose Navarro'), (2764, 'Olaf Nelson'), (87, 'Daryl Nelson'), (60, 'Benjamin Niespodziany'), (114, 'Greg Nimmo'), (139, 'James Nye'), (47, 'Adrianne Okoh'), (256, 'Tod Olson'), (265, 'Yasmin Omer'), (221, 'Ru Orb'), (48, 'Anderson Orsburn'), (196, 'Natascha Owens'), (128, 'Jee-Young Park'), (4833, 'Arnisha Parker'), (115, 'Gail Parks'), (124, 'James Anthony Patterson'), (243, 'Scott Perry'), (141, 'Julie Piacentine'), (49, 'Aaron Platte'), (222, 'Robert Pleshar'), (206, 'Laura Pontillo'), (91, 'Darryl Poole'), (160, 'Karen Prack'), (173, 'Mallory A Price'), (262, 'Bill Pugh'), (264, 'Xiaowen Qian'), (170, 'Liping Qin'), (209, 'Sheila Ralston'), (210, 'Emily Raney'), (216, 'Laura Ring'), (4842, 'Jason Robertson'), (223, 'Rachel Rosenberg'), (92, 'Darrin Rosenthal'), (45, 'Andrew Rusin'), (194, 'Marlis J. Saleh'), (208, 'Patricia Sayre-McCoy'), (109, 'George Schell'), (183, 'Margaret A. Schilt'), (260, 'William A. Schwesig'), (146, 'Joseph T Scott'), (104, 'Fred Seaton'), (143, 'James Server'), (198, 'Natasha Sharp'), (4879, 'Allyson E Smally'), (199, 'Nancy Spiegel'), (161, 'Kaitlin A Springmier'), (224, 'Rebecca Starkey'), (106, 'Julie R. Stauffer'), (80, 'Carol Stewart'), (244, 'Christopher Alexander Straughn'), (251, 'Teresa E Sullivan'), (1157, 'Sem C Sutter'), (144, 'James M. Swanson'), (93, 'Deborah Taylor'), (64, 'Brandon Tharp'), (72, 'Christie Thomas'), (101, 'Emily Anne Treptow'), (53, 'Andrea Twiss-Brooks'), (188, 'Marcene Tyler'), (81, 'Catherine Uecker'), (151, 'Keith Waclena'), (259, 'Larisa Walsh'), (176, 'Mary Lee Ward'), (231, 'Sarah G. Wenzel'), (94, 'Debra A Werner'), (171, 'Linda Wheatley-Irving'), (263, 'William White'), (190, 'Peggy Wilkins'), (112, "G'Jordan Williams"), (203, 'Patricia A. Williams'), (246, 'Shelia Wright-Coney'), (133, 'Jiaxun Benjamin Wu'), (127, 'Jin Xu'), (268, 'Ayako Yoshimura'), (163, 'Kathy Zadrozny'), (270, 'Yuan Zhou'), (271, 'Xiaoquan Zhu'), (5090, 'Karen Yu')], null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dirbrowse_dirbrowsepage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='dirbrowsepage',
            name='page_maintainer',
            field=models.ForeignKey(choices=[(44, 'Ricardo R Andrade'), (125, 'Jeffry D. Archer'), (85, 'Dean W. Armstrong'), (51, 'Dale Arntson'), (149, 'Kathleen Arthur'), (184, 'Melina Avery'), (1883, 'Shauna Babcock'), (54, 'Brian Balsamo'), (247, 'Terry Banks'), (55, 'Timothy Barnaby'), (177, 'Michelle B Bass'), (167, 'Linda Beezhold'), (205, 'Paul Belloni'), (82, 'David Bietila'), (71, 'Charles Blair'), (4906, 'Emma Boettcher'), (226, 'Steven Boozer'), (90, 'David Borycz'), (83, 'David W. Bottorff'), (225, 'Samuel B Brown'), (182, 'Michael D. Brown'), (99, 'Ellen Bryan'), (43, 'Amy M Buckland'), (211, 'Vicki Burwell-Rankin'), (56, 'Bradley Busenius'), (65, 'Maura Byrne'), (227, 'Sherry Byrne'), (134, 'John Carey'), (248, 'Timothy Clark'), (180, 'Miranda Clower'), (241, 'Steve Coats'), (66, 'Christine Colburn'), (102, 'Evelyn Collier'), (76, 'Kevin A Collier'), (77, 'James Collins'), (78, 'Christopher Cronin'), (250, 'Theodore Cueller'), (249, 'Tyler Danstrom'), (213, 'Renee Darosky'), (126, 'Judith Dartt'), (84, 'Dora Davis'), (235, 'Subrata De'), (86, 'Will Degenhard'), (228, 'Sean Dempsey'), (178, 'Melanie Dial'), (254, 'Thomas Dousa'), (255, 'Thomas Drueke'), (4835, 'Jennifer Dunlap'), (214, 'Ronald Durham'), (96, 'Elizabeth Edwards'), (68, 'Charles Ellington'), (186, 'Michael C Evans'), (201, 'Octavia Fallwell'), (88, 'David Farley'), (140, 'June P. Farris'), (152, 'Kathleen Feeney'), (69, 'Lily Fieg'), (229, 'Sean Filipov'), (179, 'M. Constance Fleischer'), (107, 'Greg Fleming'), (172, 'Lynn Franco'), (2469, 'David H Frankel'), (4815, 'Jennifer Frary'), (212, 'Raymond Gadke'), (148, 'Julia Gardner'), (252, 'Timothy Garrison'), (111, 'Joseph Gerdeman'), (204, 'Patti Gibbons'), (58, 'Barbara Gilbert'), (103, 'Fabian Gonzalez'), (52, 'Ashley Locke Gosselar'), (132, 'Jaymes B Grider'), (116, 'Gerald Hall'), (142, 'Jamal Hamilton'), (79, 'Catherine Hardy'), (232, 'Susan Harkins'), (89, 'Diana Rose Harper'), (118, 'Jamaar Harris'), (119, 'Jennifer Hart'), (166, 'Laurie Haugland'), (154, 'Kiku Hibino'), (4878, 'Taylor Hixson'), (110, 'Geraldine Hogue'), (98, 'Eileen Ielmini'), (253, 'Todd Ito'), (61, 'Brenda Johnson'), (70, 'Charlotte Jones'), (129, 'John Jung'), (135, 'John Kaderbek'), (4816, 'Kera Kelly'), (187, 'Mark Kennel'), (191, 'Michael Kenny'), (59, 'Barbara Kern'), (123, 'Hyerye Kim'), (131, 'Jenny Kim'), (42, 'Anne Knafl'), (207, 'Priya Kuppuraju'), (120, 'Hannah Landsman'), (236, 'Scott Landvatter'), (164, 'David K. Larsen'), (137, 'Jackie Larson'), (267, 'Simon Lee'), (39, 'Andrew D Lee'), (237, 'Sandra Levy'), (192, 'Melanie Levy'), (234, 'Sheri Lewis'), (46, 'Ann Lindsey'), (121, 'Holly Lipschultz'), (100, 'Elisabeth Long'), (168, 'Lyonette Louis-Jacques'), (41, 'Andrew John Lovdahl'), (57, 'Benita Luke'), (108, 'Grace Lyons'), (73, 'Cheryl Malmborg'), (113, 'Gary Mamlin'), (174, 'Amy Mantrone'), (74, 'Clint Marcy'), (175, 'Catherine M. Mardikes'), (158, 'Kristin E Martin'), (4967, 'Susan Martin'), (217, 'Renee Martonik'), (169, 'Janet L Mather'), (4834, 'Anita Marie Mechler'), (200, 'Edd Merkel'), (185, 'Stacey Metralexis'), (50, 'Daniel Meyer'), (130, 'Jon Miller'), (266, 'Yuan Mo'), (159, 'Kiya Moody'), (242, 'Steven Moore'), (189, 'James Mouw'), (75, 'Colleen Mullarkey'), (97, 'Erica Myles'), (269, 'Youli Na'), (62, 'Brittan Nannenga'), (219, 'Rose Navarro'), (2764, 'Olaf Nelson'), (87, 'Daryl Nelson'), (60, 'Benjamin Niespodziany'), (114, 'Greg Nimmo'), (139, 'James Nye'), (47, 'Adrianne Okoh'), (256, 'Tod Olson'), (265, 'Yasmin Omer'), (221, 'Ru Orb'), (48, 'Anderson Orsburn'), (196, 'Natascha Owens'), (128, 'Jee-Young Park'), (4833, 'Arnisha Parker'), (115, 'Gail Parks'), (124, 'James Anthony Patterson'), (243, 'Scott Perry'), (141, 'Julie Piacentine'), (49, 'Aaron Platte'), (222, 'Robert Pleshar'), (206, 'Laura Pontillo'), (91, 'Darryl Poole'), (160, 'Karen Prack'), (173, 'Mallory A Price'), (262, 'Bill Pugh'), (264, 'Xiaowen Qian'), (170, 'Liping Qin'), (209, 'Sheila Ralston'), (210, 'Emily Raney'), (216, 'Laura Ring'), (4842, 'Jason Robertson'), (223, 'Rachel Rosenberg'), (92, 'Darrin Rosenthal'), (45, 'Andrew Rusin'), (194, 'Marlis J. Saleh'), (208, 'Patricia Sayre-McCoy'), (109, 'George Schell'), (183, 'Margaret A. Schilt'), (260, 'William A. Schwesig'), (146, 'Joseph T Scott'), (104, 'Fred Seaton'), (143, 'James Server'), (198, 'Natasha Sharp'), (4879, 'Allyson E Smally'), (199, 'Nancy Spiegel'), (161, 'Kaitlin A Springmier'), (224, 'Rebecca Starkey'), (106, 'Julie R. Stauffer'), (80, 'Carol Stewart'), (244, 'Christopher Alexander Straughn'), (251, 'Teresa E Sullivan'), (1157, 'Sem C Sutter'), (144, 'James M. Swanson'), (93, 'Deborah Taylor'), (64, 'Brandon Tharp'), (72, 'Christie Thomas'), (101, 'Emily Anne Treptow'), (53, 'Andrea Twiss-Brooks'), (188, 'Marcene Tyler'), (81, 'Catherine Uecker'), (151, 'Keith Waclena'), (259, 'Larisa Walsh'), (176, 'Mary Lee Ward'), (231, 'Sarah G. Wenzel'), (94, 'Debra A Werner'), (171, 'Linda Wheatley-Irving'), (263, 'William White'), (190, 'Peggy Wilkins'), (112, "G'Jordan Williams"), (203, 'Patricia A. Williams'), (246, 'Shelia Wright-Coney'), (133, 'Jiaxun Benjamin Wu'), (127, 'Jin Xu'), (268, 'Ayako Yoshimura'), (163, 'Kathy Zadrozny'), (270, 'Yuan Zhou'), (271, 'Xiaoquan Zhu'), (5090, 'Karen Yu')], null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dirbrowse_dirbrowsepage_maintainer', to='staff.StaffPage'),
        ),
    ]
