# -*- coding: utf-8 -*-

from gettext import gettext as _

NAME = _('Canada')

STATES = [
    (1, _('Yukon'), 254, 72, 298, 0),
    (2, _('British Columbia'), 253, 74, 467, 60),
    (3, _('Alberta'), 252, 155, 489, 0),
    (4, _('Saskatchewan'), 251, 229, 527, 70),
    (5, _('Manitoba'), 250, 305, 542, 70),
    (6, _('Ontario'), 249, 403, 594, 0),
    (7, _('Québec'), 248, 547, 560, 0),
    (8, _('Newfoundland'), 247, 634, 501, 0),
    (9, _('New Brunswick'), 246, 634, 625, 45),
    (10, _('Northwest Territories'), 245, 234, 367, 0),
    (11, _('Banks Island'), 244, 235, 213, 0),
    (12, _('Victoria Island'), 243, 280, 272, 0),
    (13, _('Baffin Island'), 242, 475, 293, -45),
    (14, _('Ellesmere Island'), 241, 406, 142, 70),
    (15, _('Nova Scotia'), 240, 689, 646, 45),
    (16, _('Greenland'), 239, 558, 157, 0),
    (17, _('Iceland'), 238, 728, 128, 45),
    (18, _('Alaska'), 237, 42, 197, 0),
    (19, _('United States'), 236, 195, 775, 0)
]

CAPITALS = [
    (20, _('Ottawa'), 541, 671, 0, -15, -14),
    (21, _('Charlottetown'), 672, 610, 1, -30, -16),
    (22, _('Edmonton'), 161, 516, 1, 30, -14),
    (23, _('Fredericton'), 640, 637, 1, 0, 14),
    (24, _('Halifax'), 673, 638, 1, 35, 0),
    (25, _('Québec'), 585, 639, 1, -43, 0),
    (26, _('Regina'), 230, 589, 1, 0, 14),
    (27, _("Saint John's"), 758, 544, 1, -25, 14),
    (28, _('Toronto'), 500, 703, 1, -50, 0),
    (29, _('Victoria'), 34, 545, 1, 0, 14),
    (30, _('Whitehorse'), 61, 325, 1, 0, 14),
    (31, _('Winnipeg'), 305, 612, 1, 0, 14),
    (32, _('Yellowknife'), 205, 380, 1, 0, -14)
]

CITIES = [
    (33, _('Alert'), 432, 78, 2, 0, 14),
    (34, _('Calgary'), 142, 552, 2, -10, 14),
    (35, _('Cambridge Bay'), 294, 298, 2, 20, 14),
    (36, _('Chibougamau'), 539, 599, 2, 0, 14),
    (37, _('Chisasibi'), 484, 540, 2, 0, -14),
    (38, _('Churchill'), 344, 476, 2, 0, 14),
    (39, _('Dawson'), 75, 262, 2, 0, 14),
    (40, _('Echo Bay'), 210, 319, 2, 0, 14),
    (41, _('Fort Smith'), 209, 423, 2, 0, 14),
    (42, _('Frobisher Bay'), 522, 369, 2, 0, 14),
    (43, _('Gander'), 735, 528, 2, 0, -14),
    (44, _('Goose Bay'), 650, 499, 2, 0, -14),
    (45, _('Hamilton'), 498, 719, 2, 40, 0),
    (46, _('Hay River'), 185, 403, 2, -25, 14),
    (47, _('Inuvik'), 143, 236, 2, 0, 14),
    (48, _('Lethbridge'), 148, 580, 2, 0, 14),
    (49, _('Montreal'), 564, 666, 2, 25, 14),
    (50, _('Moosonee'), 469, 587, 2, -15, -14),
    (51, _('Prince George'), 88, 472, 2, -10, 14),
    (52, _('Prince Rupert'), 32, 432, 2, 25, 14),
    (53, _('Rankin Inlet'), 362, 408, 2, 0, 14),
    (54, _('Resolute'), 359, 219, 2, 0, 14),
    (55, _('Saskatoon'), 217, 560, 2, 30, -14),
    (56, _('Schefferville'), 588, 501, 2, 0, 14),
    (57, _('Sudbury'), 481, 664, 2, 0, 14),
    (58, _('Sydney'), 698, 605, 2, 20, 14),
    (59, _('Thunder Bay'), 385, 640, 2, 0, 14),
    (60, _('Vancouver'), 49, 539, 2, 10, -14),
    (61, _('Watson Lake'), 93, 362, 2, 0, 14),
    (62, _('Windsor'), 469, 736, 2, 0, 14)
]

RIVERS = [
    (63, _('Yukon River'), 254, 45, 183, -45),
    (64, _('Mackenzie River'), 253, 133, 320, -80),
    (65, _('Saskatchewan River'), 248, 214, 515, -20),
    (66, _('Nelson River'), 247, 330, 497, 30),
    (67, _('Columbia River'), 246, 91, 591, 60),
    (68, _('Lake Great Bear'), 252, 194, 309, -45),
    (69, _('Lake Great Slave'), 251, 203, 415, 0),
    (70, _('Lake Athabasca'), 250, 226, 453, 0),
    (71, _('Lake Reindeer'), 249, 262, 486, 0),
    (72, _('St. Lawrence River'), 243, 566, 634, 60),
    (73, _('Lake Superior'), 242, 398, 627, 0),
    (74, _('Lake Michigan'), 241, 406, 714, -60),
    (75, _('Lake Huron'), 240, 465, 690, 45),
    (76, _('Lake Erie'), 239, 495, 753, 45),
    (77, _('Lake Ontario'), 238, 533, 710, 0),
    (78, _('Lake Winnipeg'), 237, 305, 579, 0),
    (79, _('Atlantic Ocean'), 236, 683, 776, 60),
    (80, _('Pacific Ocean'), 235, 19, 419, 90),
    (81, _('Beaufort Sea'), 234, 167, 179, -45),
    (82, _('Chukchi Sea'), 233, 70, 65, 0),
    (83, _('Greenland Sea'), 232, 673, 50, 0),
    (84, _('Labrador Sea'), 231, 625, 379, 0),
    (85, _('Baffin Bay'), 230, 492, 240, -45),
    (86, _('Hudson Bay'), 229, 413, 455, 0),
    (87, _('Arctic Ocean'), 228, 268, 66, 0),
    (88, _('Norwegian Sea'), 227, 744, 259, 90)
]

ROUTES = []

STATS = [
    (_('Capital:'), _('Ottawa') + ' ' + _("(45º24' N - 75º40' W)")),
    (_('Language:'), _('English') + ' , ' + _('French')),
    (_('Government:'), _('Federal parliamentary monarchy')),
    (_('Monarch:'), _('Charles III')),
    (_('Governor Gen.:'), _('Louise Arbour')),
    (_('Prime Minister:'), _('Mark Carney')),
    (_('Independence:'), _('from United Kingdom')),
    ('', _('declared: %s') % _('July 1, 1867')),
    ('', _('recognized: %s') % _('December 11, 1931')),
    (_('Area:'), '9 984 670' + ' ' + _('km²')),
    (_('Population:'), '41 651 653 (2025)'),
    (_('GDP:'), 'USD 2 320 000 000 000 (2025)'),
    (_('HDI:'), _('Very High') + ' - 0.939 (2023, #16)'),
    (_('Currency:'), _('Canadian dollar')),
    (_('Updated:'), '2026-09-25'),
]

