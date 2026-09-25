# -*- coding: utf-8 -*-

from gettext import gettext as _

NAME = _('Canada')

STATES = [
    (_('Yukon'), 254, 72, 298, 0),
    (_('British Columbia'), 253, 74, 467, 60),
    (_('Alberta'), 252, 155, 489, 0),
    (_('Saskatchewan'), 251, 229, 527, 70),
    (_('Manitoba'), 250, 305, 542, 70),
    (_('Ontario'), 249, 403, 594, 0),
    (_('Québec'), 248, 547, 560, 0),
    (_('Newfoundland'), 247, 634, 501, 0),
    (_('New Brunswick'), 246, 634, 625, 45),
    (_('Northwest Territories'), 245, 234, 367, 0),
    (_('Banks Island'), 244, 235, 213, 0),
    (_('Victoria Island'), 243, 280, 272, 0),
    (_('Baffin Island'), 242, 475, 293, -45),
    (_('Ellesmere Island'), 241, 406, 142, 70),
    (_('Nova Scotia'), 240, 689, 646, 45),
    (_('Greenland'), 239, 558, 157, 0),
    (_('Iceland'), 238, 728, 128, 45),
    (_('Alaska'), 237, 42, 197, 0),
    (_('United States'), 236, 195, 775, 0)
]

CAPITALS = [
    (_('Ottawa'), 541, 671, 0, -15, -14),
    (_('Charlottetown'), 672, 610, 1, -30, -16),
    (_('Edmonton'), 161, 516, 1, 30, -14),
    (_('Fredericton'), 640, 637, 1, 0, 14),
    (_('Halifax'), 673, 638, 1, 35, 0),
    (_('Québec'), 585, 639, 1, -43, 0),
    (_('Regina'), 230, 589, 1, 0, 14),
    (_("Saint John's"), 758, 544, 1, -25, 14),
    (_('Toronto'), 500, 703, 1, -50, 0),
    (_('Victoria'), 34, 545, 1, 0, 14),
    (_('Whitehorse'), 61, 325, 1, 0, 14),
    (_('Winnipeg'), 305, 612, 1, 0, 14),
    (_('Yellowknife'), 205, 380, 1, 0, -14)
]

CITIES = [
    (_('Alert'), 432, 78, 2, 0, 14),
    (_('Calgary'), 142, 552, 2, -10, 14),
    (_('Cambridge Bay'), 294, 298, 2, 20, 14),
    (_('Chibougamau'), 539, 599, 2, 0, 14),
    (_('Chisasibi'), 484, 540, 2, 0, -14),
    (_('Churchill'), 344, 476, 2, 0, 14),
    (_('Dawson'), 75, 262, 2, 0, 14),
    (_('Echo Bay'), 210, 319, 2, 0, 14),
    (_('Fort Smith'), 209, 423, 2, 0, 14),
    (_('Frobisher Bay'), 522, 369, 2, 0, 14),
    (_('Gander'), 735, 528, 2, 0, -14),
    (_('Goose Bay'), 650, 499, 2, 0, -14),
    (_('Hamilton'), 498, 719, 2, 40, 0),
    (_('Hay River'), 185, 403, 2, -25, 14),
    (_('Inuvik'), 143, 236, 2, 0, 14),
    (_('Lethbridge'), 148, 580, 2, 0, 14),
    (_('Montreal'), 564, 666, 2, 25, 14),
    (_('Moosonee'), 469, 587, 2, -15, -14),
    (_('Prince George'), 88, 472, 2, -10, 14),
    (_('Prince Rupert'), 32, 432, 2, 25, 14),
    (_('Rankin Inlet'), 362, 408, 2, 0, 14),
    (_('Resolute'), 359, 219, 2, 0, 14),
    (_('Saskatoon'), 217, 560, 2, 30, -14),
    (_('Schefferville'), 588, 501, 2, 0, 14),
    (_('Sudbury'), 481, 664, 2, 0, 14),
    (_('Sydney'), 698, 605, 2, 20, 14),
    (_('Thunder Bay'), 385, 640, 2, 0, 14),
    (_('Vancouver'), 49, 539, 2, 10, -14),
    (_('Watson Lake'), 93, 362, 2, 0, 14),
    (_('Windsor'), 469, 736, 2, 0, 14)
]

RIVERS = [
    (_('Yukon River'), 254, 45, 183, -45),
    (_('Mackenzie River'), 253, 133, 320, -80),
    (_('Saskatchewan River'), 248, 214, 515, -20),
    (_('Nelson River'), 247, 330, 497, 30),
    (_('Columbia River'), 246, 91, 591, 60),
    (_('Lake Great Bear'), 252, 194, 309, -45),
    (_('Lake Great Slave'), 251, 203, 415, 0),
    (_('Lake Athabasca'), 250, 226, 453, 0),
    (_('Lake Reindeer'), 249, 262, 486, 0),
    (_('St. Lawrence River'), 243, 566, 634, 60),
    (_('Lake Superior'), 242, 398, 627, 0),
    (_('Lake Michigan'), 241, 406, 714, -60),
    (_('Lake Huron'), 240, 465, 690, 45),
    (_('Lake Erie'), 239, 495, 753, 45),
    (_('Lake Ontario'), 238, 533, 710, 0),
    (_('Lake Winnipeg'), 237, 305, 579, 0),
    (_('Atlantic Ocean'), 236, 683, 776, 60),
    (_('Pacific Ocean'), 235, 19, 419, 90),
    (_('Beaufort Sea'), 234, 167, 179, -45),
    (_('Chukchi Sea'), 233, 70, 65, 0),
    (_('Greenland Sea'), 232, 673, 50, 0),
    (_('Labrador Sea'), 231, 625, 379, 0),
    (_('Baffin Bay'), 230, 492, 240, -45),
    (_('Hudson Bay'), 229, 413, 455, 0),
    (_('Arctic Ocean'), 228, 268, 66, 0),
    (_('Norwegian Sea'), 227, 744, 259, 90)
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

