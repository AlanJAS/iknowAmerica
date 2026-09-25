# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        8,
        _('Provinces'),
        ['lineasDepto'],
        [],
[
    (1, _('Is northwest')),
    (2, _('Is west')),
    (3, _('Is southwest')),
    (4, _('Is southwest')),
    (5, _('Is south')),
    (6, _('Is southeast')),
    (7, _('Is southeast')),
    (8, _('Is east')),
    (9, _('Is southeast')),
    (10, _('Is northwest')),
    (15, _('Is southeast'))
]
]

LEVEL2 = [
        2,
        _('Provincial capitals'),
        ['lineasDepto', 'capitales'],
        [],
[
    (20, _('Is southeast')),
    (21, _('Is southeast')),
    (22, _('Is southwest')),
    (23, _('Is southeast')),
    (24, _('Is southeast')),
    (25, _('Is southeast')),
    (26, _('Is southwest')),
    (27, _('Is east')),
    (28, _('Is southeast')),
    (29, _('Is southwest')),
    (30, _('Is northwest')),
    (31, _('Is south')),
    (32, _('Is northwest'))
]
]

LEVEL3 = [
        2,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (20, _('Is southeast')),
    (21, _('Is southeast')),
    (22, _('Is southwest')),
    (23, _('Is southeast')),
    (24, _('Is southeast')),
    (25, _('Is southeast')),
    (26, _('Is southwest')),
    (27, _('Is east')),
    (28, _('Is southeast')),
    (29, _('Is southwest')),
    (30, _('Is northwest')),
    (31, _('Is south')),
    (32, _('Is northwest')),
    (33, _('Is north')),
    (34, _('Is southwest')),
    (35, _('Is north')),
    (36, _('Is southeast')),
    (37, _('Is southeast')),
    (38, _('Is in the center')),
    (39, _('Is northwest')),
    (40, _('Is northwest')),
    (41, _('Is west')),
    (42, _('Is northeast')),
    (43, _('Is east')),
    (44, _('Is east')),
    (45, _('Is southeast')),
    (46, _('Is west')),
    (47, _('Is northwest')),
    (48, _('Is southwest')),
    (49, _('Is southeast')),
    (50, _('Is southeast')),
    (51, _('Is west')),
    (52, _('Is west')),
    (53, _('Is in the center')),
    (54, _('Is north')),
    (55, _('Is southwest')),
    (56, _('Is east')),
    (57, _('Is southeast')),
    (58, _('Is southeast')),
    (59, _('Is south')),
    (60, _('Is southwest')),
    (61, _('Is west')),
    (62, _('Is south'))
]
]

LEVEL4 = [
        4,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (63, _('Is northwest')),
    (64, _('Is northwest')),
    (65, _('Is southwest')),
    (66, _('Is south')),
    (67, _('Is southwest')),
    (68, _('Is northwest')),
    (69, _('Is northwest')),
    (70, _('Is west')),
    (71, _('Is southwest')),
    (72, _('Is southeast')),
    (73, _('Is south')),
    (74, _('Is south')),
    (75, _('Is southeast')),
    (76, _('Is southeast')),
    (77, _('Is southeast')),
    (78, _('Is south')),
    (79, _('Is southeast')),
    (80, _('Is west')),
    (81, _('Is northwest')),
    (82, _('Is northwest')),
    (83, _('Is northeast')),
    (84, _('Is northeast')),
    (85, _('Is northeast')),
    (86, _('Is in the center')),
    (87, _('Is north')),
    (88, _('Is northeast'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4]

