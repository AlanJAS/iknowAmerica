# -*- coding: utf-8 -*-

from gettext import gettext as _

NAME = _('Chile')

STATES = [
    (1, _('Tarapacá'), 254, 165, 151, 0),
    (2, _('Antofagasta'), 253, 209, 298, 0),
    (3, _('Atacama'), 252, 167, 470, 0),
    (4, _('Coquimbo'), 251, 134, 604, 0),
    (5, _('Valparaíso'), 250, 140, 683, 0),
    (6, _('Metropolitana'), 249, 154, 728, 0),
    (7, _("Libertador General Bernardo O'Higgins"), 248, 158, 768, 0),
    (8, _('Maule'), 247, 118, 824, 0),
    (9, _('Bío-Bío'), 246, 510, 57, 0),
    (10, _('La Araucanía'), 245, 511, 133, 0),
    (11, _('Los Lagos'), 244, 496, 283, 0),
    (12, _('Aysén'), 243, 553, 481, 0),
    (13, _('Magallanes'), 242, 513, 699, 0),
    (14, _('Arica Parinacota'), 241, 185, 81, 0),
    (15, _('Los Rios'), 240, 505, 188, 0),
    (16, _('Argentina'), 239, 667, 163, 90),
    (17, _('Perú'), 238, 152, 25, 0)
]

CAPITALS = [
    (18, _('Santiago'), 151, 720, 0, 0, 14),
    (19, _('Iquique'), 171, 138, 1, 0, 14),
    (20, _('Antofagasta'), 157, 297, 1, 0, 14),
    (21, _('Copiapó'), 166, 451, 1, 0, 14),
    (22, _('La Serena'), 126, 569, 1, 0, 14),
    (23, _('Valparaíso'), 117, 704, 1, 0, -14),
    (24, _('Rancagua'), 138, 757, 1, 0, 14),
    (25, _('Talca'), 116, 805, 1, 0, 14),
    (26, _('Concepción'), 486, 39, 1, 0, 14),
    (27, _('Temuco'), 506, 140, 1, 0, 14),
    (28, _('Puerto Montt'), 498, 247, 1, 0, 14),
    (29, _('Coihaique'), 538, 423, 1, 0, 14),
    (30, _('Punta Arenas'), 559, 763, 1, 0, 14),
    (31, _('Arica'), 162, 71, 1, 0, 14),
    (32, _('Valdivia'), 482, 182, 1, 0, 14)
]

STATS = [
    (_('Capital:'), _('Santiago') + ' ' + _("(33º26' S - 70º39' W)")),
    (_('Language:'), _('Spanish')),
    (_('Government:'), _('Presidential republic')),
    (_('President:'), _('José Antonio Kast')),
    (_('Independence:'), _('from Spain')),
    ('', _('declared: %s') % _('February 12, 1818')),
    ('', _('recognized: %s') % _('February 24, 1844')),
    (_('Area:'), '756 096' + ' ' + _('km²')),
    (_('Population:'), '19 859 921 (2025)'),
    (_('GDP:'), 'USD 357 370 000 000 (2025)'),
    (_('HDI:'), _('Very High') + ' - 0.878 (2023, #45)'),
    (_('Currency:'), _('Peso')),
    (_('Updated:'), '2026-09-25'),
]


