# -*- coding: utf-8 -*-

from gettext import gettext as _

LEVEL1 = [
        8,
        _('Provinces'),
        ['lineasDepto'],
        [],
[
    (1, _('Is west')),
    (2, _('Is in the center')),
    (3, _('Is in the center')),
    (4, _('Is west')),
    (5, _('Is southeast')),
    (6, _('Is southwest')),
    (7, _('Is south')),
    (8, _('Is east')),
    (9, _('Is southwest')),
    (12, _('Is east'))
]
]

LEVEL2 = [
        2,
        _('Provincial capitals'),
        ['lineasDepto', 'capitales'],
        [],
[
    (15, _('Is in the center')),
    (16, _('Is west')),
    (17, _('Is southwest')),
    (18, _('Is in the center')),
    (19, _('Is west')),
    (20, _('Is northeast')),
    (21, _('Is east')),
    (22, _('Is south')),
    (23, _('Is in the center')),
    (24, _('Is southwest'))
]
]

LEVEL3 = [
        2,
        _('Cities'),
        ['lineasDepto', 'capitales', 'ciudades'],
        [],
[
    (15, _('Is in the center')),
    (16, _('Is west')),
    (17, _('Is southwest')),
    (18, _('Is in the center')),
    (19, _('Is west')),
    (20, _('Is northeast')),
    (21, _('Is east')),
    (22, _('Is south')),
    (23, _('Is in the center')),
    (24, _('Is southwest')),
    (25, _('Is southwest')),
    (26, _('Is west')),
    (27, _('Is west')),
    (28, _('Is in the center')),
    (29, _('Is east')),
    (30, _('Is west')),
    (31, _('Is west')),
    (32, _('Is in the center')),
    (33, _('Is southwest')),
    (34, _('Is in the center')),
    (35, _('Is west')),
    (36, _('Is in the center')),
    (37, _('Is south')),
    (38, _('Is in the center')),
    (39, _('Is west')),
    (40, _('Is in the center')),
    (41, _('Is west')),
    (42, _('Is west')),
    (43, _('Is west')),
    (44, _('Is southwest')),
    (45, _('Is southeast'))
]
]

LEVEL4 = [
        4,
        _('Waterways'),
        ['lineasDepto', 'rios'],
        [],
[
    (46, _('Is west')),
    (47, _('Is southwest')),
    (48, _('Is southwest')),
    (49, _('Is in the center')),
    (50, _('Is in the center')),
    (51, _('Is east')),
    (52, _('Is east')),
    (53, _('Is east')),
    (54, _('Is southeast')),
    (55, _('Is southeast')),
    (56, _('Is southwest')),
    (57, _('Is southwest')),
    (58, _('Is southwest')),
    (59, _('Is south')),
    (60, _('Is southeast')),
    (61, _('Is southeast')),
    (62, _('Is northeast')),
    (63, _('Is in the center')),
    (64, _('Is southwest')),
    (65, _('Is west')),
    (66, _('Is north')),
    (67, _('Is south'))
]
]

LEVELS = [LEVEL1, LEVEL2, LEVEL3, LEVEL4]

