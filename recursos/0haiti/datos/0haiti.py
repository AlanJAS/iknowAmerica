# -*- coding: utf-8 -*-

from gettext import gettext as _

NAME = _('Haiti')

STATES = [
    (1, _('Norte'), 254, 587, 283, 0),
    (2, _('Noroeste'), 253, 384, 232, 0),
    (3, _('Noreste'), 252, 695, 310, 0),
    (4, _('Artibonite'), 251, 532, 361, 0),
    (5, _('Oeste'), 250, 628, 583, 0),
    (6, _('Sur'), 249, 208, 644, 0),
    (7, _('Sudeste'), 248, 552, 650, 0),
    (8, _("Grand'Anse"), 247, 107, 593, 0),
    (9, _('Centro'), 246, 673, 421, 0),
    (10, _('Dominican Republic'), 245, 765, 550, 90),
    (11, _('Cuba'), 244, 33, 68, 0),
    (12, _('Tortuga Island'), 243, 454, 150, 0),
    (13, _('Gonâve Island'), 242, 384, 493, -30),
    (14, _('Grande Cayemite Island'), 241, 199, 544, 0),
    (15, _('Cow Island'), 240, 236, 726, 0)
]

CAPITALS = [
    (16, _('Port-au-Prince'), 580, 576, 0, -60, -14),
    (17, _('Cap-Haïtien'), 608, 236, 1, 10, -14),
    (18, _('Fort Liberte'), 706, 263, 1, -15, -14),
    (19, _('Gonaives'), 486, 328, 1, -10, 14),
    (20, _('Hinche'), 660, 412, 1, 0, -14),
    (21, _('Jacmel'), 526, 663, 1, 0, 14),
    (22, _('Jeremie'), 102, 552, 1, 0, -14),
    (23, _('Les Cayes'), 198, 675, 1, 0, -14),
    (24, _('Port de Paix'), 450, 195, 1, -10, -14)
]

CITIES = [
    (25, _('Anse a Galets'), 437, 500, 2, -20, 14),
    (26, _("Anse d'Hainault"), 18, 594, 2, 50, 14),
    (27, _('Aquin'), 298, 651, 2, 0, -14),
    (28, _('Baie de Henne'), 348, 268, 2, -10, 14),
    (29, _('Bainet'), 468, 677, 2, -10, 14),
    (30, _('Belle Anse'), 647, 659, 2, 15, -14),
    (31, _('Cotes de Fer'), 410, 676, 2, -15, -14),
    (32, _('Croix des Bouquets'), 607, 572, 2, 85, 0),
    (33, _('Dame Marie'), 26, 575, 2, 49, 0),
    (34, _('Ennery'), 537, 316, 2, 0, 14),
    (35, _('Grande Riviere du Nord'), 615, 284, 2, 30, 14),
    (36, _('Kenscoff'), 593, 606, 2, 10, 14),
    (37, _('Lafond'), 498, 407, 2, 0, -14),
    (38, _('Le Borgne'), 523, 218, 2, -15, 14),
    (39, _('Leogane'), 498, 589, 2, 20, 14),
    (40, _('Les Anglais'), 80, 641, 2, -10, 14),
    (41, _('Limbé'), 560, 252, 2, 0, 14),
    (42, _('Manneville'), 649, 556, 2, 20, -14),
    (43, _('Marigot'), 585, 660, 2, 15, 14),
    (44, _('Miragoane'), 382, 610, 2, 0, -14),
    (45, _('Mirebalais'), 639, 497, 2, -20, -14),
    (46, _('Mole Saint Nicolas'), 307, 231, 2, 0, -14),
    (47, _('Montrouis'), 482, 464, 2, 10, 14),
    (48, _('Pestel'), 190, 583, 2, -20, 14),
    (49, _('Petionville'), 592, 587, 2, 47, 0),
    (50, _('Petit Goave'), 444, 612, 2, -20, 14),
    (51, _('Petit Trou de Nippes'), 269, 587, 2, 30, -14),
    (52, _('Port Salut'), 156, 704, 2, 0, 14),
    (53, _('Saint Marc'), 483, 424, 2, -25, 14),
    (54, _('Saint Raphael'), 609, 324, 2, 30, 14),
    (55, _('Trouin'), 494, 630, 2, -10, 14),
    (56, _('Verrettes'), 543, 433, 2, 15, 14)
]

RIVERS = [
    (57, _('Les Trois Rivières River'), 254, 455, 253, -45),
    (58, _('Artibonito River'), 253, 725, 384, -45),
    (59, _('Bouyaha River'), 252, 604, 345, -50),
    (60, _('Guayamouc River'), 251, 696, 415, -50),
    (61, _('Canot River'), 250, 578, 376, -40),
    (62, _('Artibonite River'), 249, 538, 443, -40),
    (63, _('Lake of Pélicre'), 248, 679, 481, 0),
    (64, _('Lake Étang Saumâtre'), 247, 667, 581, 0),
    (65, _('Jacmel Bay'), 246, 532, 682, 0),
    (66, _('Port-au-Prince Bay'), 245, 523, 555, 0),
    (67, _('Canal of Saint Marc'), 244, 456, 481, -40),
    (68, _('Canal of the Gonâve'), 243, 384, 561, -20),
    (69, _('Henne Bay'), 242, 349, 283, 0),
    (70, _('Tortue Bay'), 241, 461, 338, 0),
    (71, _('Grand Pierre Bay'), 240, 458, 375, 0),
    (72, _('Mancenille Bay'), 239, 696, 235, 0),
    (73, _('Canal of the Tortue'), 238, 440, 179, 0),
    (74, _('Gulf of Gonâve'), 237, 358, 379, 90),
    (75, _('Windward Passage'), 236, 157, 148, -30),
    (76, _('Caribbean Sea'), 235, 440, 793, 0),
    (77, _('Atlantic Ocean'), 234, 561, 88, 0)
]

ROUTES = []

STATS = [
    (_('Capital:'), _('Port-au-Prince')),
    ('', _("(18º32' N - 72º20' W)")),
    (_('Language:'), _('French') + ', ' + _('Haitian Creole')),
    (_('Government:'), _('Transitional government')),
    (_('President:'), _('Vacant')),
    (_('Prime Minister:'), _('Alix Didier Fils-Aimé')),
    (_('Independence:'), _('from France')),
    ('', _('declared: %s') % _('January 1, 1804')),
    (_('Area:'), '27 750' + ' ' + _('km²')),
    (_('Population:'), '11 906 095 (2025)'),
    (_('GDP:'), 'USD 32 080 000 000 (2025)'),
    (_('HDI:'), _('Medium') + ' - 0.554 (2023, #166)'),
    (_('Currency:'), _('Gourde')),
    (_('Updated:'), '2026-09-25'),
]
