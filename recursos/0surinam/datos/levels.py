# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        9,
        _('Districts'),
        ['lineasDepto'],
        [],
[
    (1, _('Is northwest')),
    (2, _('Is northwest')),
    (3, _('Is north')),
    (4, _('Is north')),
    (5, _('Is northeast')),
    (6, _('Is northeast')),
    (7, _('Is northeast')),
    (8, _('Is northeast')),
    (9, _('Is south'))
]
]

LEVEL2 = [
        2,
        _('Provincial capitals'),
        ['lineasDepto', 'capitales'],
        [],
[
    (13, _('Is north')),
    (14, _('Is northeast')),
    (15, _('Is northeast')),
    (16, _('Is north')),
    (17, _('Is north')),
    (18, _('Is north')),
    (19, _('Is northwest')),
    (20, _('Is north')),
    (21, _('Is northwest'))
]
]

LEVEL3 = [
        2,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (13, _('Is north')),
    (14, _('Is northeast')),
    (15, _('Is northeast')),
    (16, _('Is north')),
    (17, _('Is north')),
    (18, _('Is north')),
    (19, _('Is northwest')),
    (20, _('Is north')),
    (21, _('Is northwest')),
    (22, _('Is southeast')),
    (23, _('Is southeast')),
    (24, _('Is northwest')),
    (25, _('Is northwest')),
    (26, _('Is east')),
    (27, _('Is northwest')),
    (28, _('Is north')),
    (29, _('Is northeast')),
    (30, _('Is west')),
    (31, _('Is in the center')),
    (32, _('Is northwest')),
    (33, _('Is southwest')),
    (34, _('Is northeast')),
    (35, _('Is south')),
    (36, _('Is in the center')),
    (37, _('Is northwest')),
    (38, _('Is north'))
]
]

LEVEL4 = [
        4,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (39, _('Is north')),
    (40, _('Is northwest')),
    (41, _('Is north')),
    (42, _('Is in the center')),
    (43, _('Is northeast')),
    (44, _('Is northeast')),
    (45, _('Is east')),
    (46, _('Is southeast')),
    (47, _('Is southeast')),
    (48, _('Is south')),
    (49, _('Is southeast')),
    (50, _('Is southwest')),
    (51, _('Is west')),
    (52, _('Is southwest')),
    (53, _('Is southwest')),
    (54, _('Is west')),
    (55, _('Is north'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4]

