# -*- coding: utf-8 -*-

from gettext import gettext as _

NAME = _('Bolivia')

STATES = [
    (_('Pando'), 254, 136, 124, 0),
    (_('Beni'), 253, 283, 292, 0),
    (_('La Paz'), 252, 124, 431, 0),
    (_('Oruro'), 251, 146, 609, 0),
    (_('Potosí'), 250, 204, 745, 0),
    (_('Cochabamba'), 249, 279, 503, 0),
    (_('Chuquisaca'), 248, 377, 730, 0),
    (_('Tarija'), 247, 374, 788, 0),
    (_('Santa Cruz'), 246, 529, 513, 0),
    (_('Brazil'), 245, 552, 109, 0),
    (_('Perú'), 244, 23, 271, 90),
    (_('Chile'), 243, 50, 763, 90),
    (_('Paraguay'), 242, 616, 800, 0),
    (_('Argentina'), 241, 331, 884, 0)
]

CAPITALS = [
    (_('La Paz'), 118, 464, 0, 0, -14),
    (_('Cobija'), 66, 104, 1, 0, 14),
    (_('Trinidad'), 318, 352, 1, 0, -14),
    (_('Cochabamba'), 244, 519, 1, 0, -14),
    (_('Oruro'), 193, 557, 1, -10, 14),
    (_('Potosí'), 272, 662, 1, 0, 14),
    (_('Sucre'), 305, 626, 1, 0, -14),
    (_('Tarija'), 342, 789, 1, 0, 14),
    (_('Santa Cruz'), 430, 544, 1, 0, 14)
]

CITIES = [
    (_('Apolo'), 86, 356, 2, 0, -14),
    (_('Reyes'), 159, 323, 2, 10, -14),
    (_('Santa Ana'), 277, 280, 2, 0, -14),
    (_('San Borja'), 202, 355, 2, 0, -14),
    (_('Puerto Heath'), 79, 204, 2, 0, 14),
    (_('Asunción'), 124, 160, 2, 0, -14),
    (_('Riberalta'), 238, 104, 2, -15, -14),
    (_('Magdalena'), 366, 255, 2, 0, -14),
    (_('Loreto'), 330, 376, 2, 0, 14),
    (_('Puerto Acosta'), 48, 403, 2, 30, -14),
    (_('Caranavi'), 155, 419, 2, 0, 14),
    (_('Guaqui'), 77, 475, 2, -15, 14),
    (_('Ascención'), 435, 405, 2, 0, -14),
    (_('Concepción'), 500, 434, 2, 0, -14),
    (_('San Ignacio'), 563, 443, 2, 0, 14),
    (_('Tarabuco'), 324, 634, 2, 0, 14),
    (_('Aiquile'), 307, 569, 2, 0, -14),
    (_('Villazón'), 289, 816, 2, 15, 14),
    (_('Uyuni'), 209, 723, 2, 0, -14),
    (_('Yucuiba'), 407, 809, 2, 0, 14),
    (_('Villa Montes'), 421, 762, 2, 0, -14),
    (_('Camiri'), 409, 694, 2, 20, -14),
    (_('Santa Rosa del Sara'), 402, 497, 2, 15, -14),
    (_('Montero'), 425, 513, 2, 0, 14),
    (_('Las Petas'), 680, 449, 2, 0, 14),
    (_('San José de Chiquitos'), 583, 544, 2, 0, -14),
    (_('Roboré'), 643, 576, 2, 0, -14),
    (_('Puerto Suárez'), 758, 614, 2, -30, -14)
]

RIVERS = [
    (_('Pilcomayo River'), 254, 462, 796, -45),
    (_('Parapetí River'), 253, 444, 690, 30),
    (_('Sécure River'), 252, 260, 407, 30),
    (_('Ichoa River'), 251, 296, 434, 40),
    (_('Piray River'), 250, 406, 520, 90),
    (_('Ichilo River'), 249, 311, 470, 90),
    (_('Grande River'), 248, 461, 526, -80),
    (_('Yacuma River'), 247, 204, 302, 30),
    (_('Madre de Dios River'), 246, 133, 158, 40),
    (_('Desaguadero River'), 245, 96, 538, -40),
    (_('Grande de Lípez River'), 244, 171, 773, 90),
    (_('San Miguel River'), 243, 400, 392, -45),
    (_('San Martín River'), 242, 505, 332, -45),
    (_('Abuná River'), 241, 176, 41, 30),
    (_('Orton River'), 240, 188, 88, 20),
    (_('Madeira River'), 239, 209, 54, 30),
    (_('Madidi River'), 238, 123, 238, 30),
    (_('Tequeje River'), 237, 118, 275, 20),
    (_('Beni River'), 236, 166, 299, 60),
    (_('Viata River'), 235, 207, 213, 70),
    (_('Apere River'), 234, 260, 338, 30),
    (_('Mamoré River'), 233, 338, 346, -80),
    (_('Blanco River'), 232, 474, 366, -50),
    (_('Paraguá River'), 231, 575, 351, -70),
    (_('Guaporé River'), 230, 524, 244, -25),
    (_('Tucavaca River'), 229, 682, 563, -40),
    (_('Lateriquique River'), 228, 613, 610, -40),
    (_('Lake Titicaca'), 227, 47, 424, -45),
    (_('Lake Poopo'), 226, 180, 610, 0)
]

ROUTES = []

STATS = [
    (_('Capital:'), _('Sucre') + _("(19º2' S - 65º15' W)")),
    (_('Language:'), _('Spanish') + ' , ' + _('Quechua') + ' , ' + _('Guarani')),
    (_('Government:'), _('Presidential republic')),
    (_('President:'), _('Evo Morales Ayma')),
    (_('Vice President:'), _('Álvaro García Linera')),
    (_('Independence:'), _('from Spain')),
    ('', _('declared: %s') % _('August 6, 1825')),
    ('', _('recognized: %s') % _('July 21, 1847')),
    (_('Area:'), '%(sup)s %(u)s (%(p)s)' % {'sup': _('1.098.581'), 'u': _('km²'), 'p': _('27th')}),
    (_('Population:'), '%(v)s (%(p)s)' % {'v': _('11.410.651'), 'p': _('83rd')}),
    (_('GDP:'), '%(c)s %(v)s %(u)s (%(p)s)' % {'c': _('USD'), 'v': _('33.537'), 'u': _('billion'), 'p': _('96th')}),
    (_('HDI:'), '%(l)s - %(v)s (%(p)s)' % {'l': _('Medium'), 'v': _('0,662'), 'p': _('119th')}),
    (_('Currency:'), _('Boliviano')),
    (_('Updated:'), _('April 5, 2016'))
]

