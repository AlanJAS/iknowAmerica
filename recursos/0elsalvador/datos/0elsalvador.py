# -*- coding: utf-8 -*-

from gettext import gettext as _

NAME = _('El Salvador')

STATES = [
    (_('Ahucachapán'), 254, 83, 390, 45),
    (_('Cabañas'), 253, 456, 386, 0),
    (_('Cuscatlán'), 252, 359, 394, -55),
    (_('Chalatenango'), 251, 363, 304, -20),
    (_('La Libertad'), 250, 255, 439, 90),
    (_('La Paz'), 249, 374, 513, 0),
    (_('La Unión'), 248, 708, 505, 70),
    (_('Morazán'), 247, 644, 423, 45),
    (_('San Miguel'), 246, 614, 523, -45),
    (_('San Salvador'), 245, 312, 431, 90),
    (_('San Vicente'), 244, 454, 458, 0),
    (_('Santa Ana'), 243, 211, 314, 60),
    (_('Sonsonante'), 242, 158, 449, 30),
    (_('Usulután'), 241, 509, 546, 0),
    (_('Guatemala'), 240, 132, 132, 0),
    (_('Honduras'), 239, 572, 158, 0)
]

CAPITALS = [
    (_('San Salvador'), 310, 442, 0, -10, -14),
    (_('Ahuachapán'), 105, 373, 1, -10, 14),
    (_('Chalatenango'), 385, 335, 1, 30, -14),
    (_('Cojutepeque'), 386, 435, 1, 25, -14),
    (_('La Unión'), 724, 561, 1, -15, 14),
    (_('Santa Tecla'), 279, 450, 1, 0, 14),
    (_('San Francisco'), 646, 444, 1, 0, -14),
    (_('San Miguel'), 620, 509, 1, 25, -14),
    (_('San Vicente'), 435, 459, 1, -10, 14),
    (_('Santa Ana'), 194, 350, 1, 10, -14),
    (_('Sensuntepeque'), 480, 387, 1, 0, -14),
    (_('Sonsonante'), 141, 436, 1, -20, 14),
    (_('Usultán'), 539, 551, 1, -20, 14),
    (_('Zacatecoluca'), 410, 501, 1, -10, 14)
]

CITIES = [
    (_('Acajutla'), 112, 474, 2, 0, 14),
    (_('Armenia'), 212, 427, 2, 0, 14),
    (_('Atiquizaya'), 135, 356, 2, -25, -14),
    (_('Cacaopera'), 654, 418, 2, 0, -14),
    (_('Candelaria de la Frontera'), 166, 310, 2, -40, -14),
    (_('Carolina'), 583, 395, 2, 0, -14),
    (_('Chirilagua'), 635, 596, 2, 0, 14),
    (_('Dulce Nombre de María'), 363, 298, 2, 80, -14),
    (_('El Tránsito'), 573, 549, 2, 35, 14),
    (_('Izalco'), 160, 425, 2, 0, -14),
    (_('Jucuapa'), 559, 506, 2, -5, -14),
    (_('San Luis La Herradura'), 387, 554, 2, 0, 14),
    (_('La Libertad'), 267, 507, 2, -10, 14),
    (_('La Palma'), 314, 248, 2, -10, -14),
    (_('La Reina'), 321, 284, 2, -10, -14),
    (_('Ilobasco'), 412, 396, 2, 0, 14),
    (_('Metapán'), 231, 244, 2, -10, 14),
    (_('Nueva Concepción'), 274, 305, 2, -20, 14),
    (_('Nueva Granada'), 526, 462, 2, 55, 14),
    (_('Pasaquina'), 723, 477, 2, 0, -14),
    (_('Perquín'), 622, 361, 2, 0, -14),
    (_('Polorós'), 728, 404, 2, 0, -14),
    (_('San Agustín'), 491, 529, 2, -15, 14),
    (_('San Alejo'), 687, 525, 2, 0, 14),
    (_('San Jorge'), 574, 532, 2, 0, -14),
    (_('San Juan Opico'), 256, 385, 2, 10, 14),
    (_('San Luis Talpa'), 338, 510, 2, 0, -14),
    (_('San Pablo Tacachico'), 264, 359, 2, -10, 14),
    (_('Santa Clara'), 448, 443, 2, 50, 0),
    (_('Sesori'), 563, 434, 2, 0, -14),
    (_('Suchitoto'), 357, 370, 2, 0, -14),
    (_('Tecoluca'), 435, 497, 2, 40, 0),
    (_('Victoria'), 476, 363, 2, 0, -14)
]

RIVERS = [
    (_('Paz River'), 254, 69, 375, 45),
    (_('Lempa River'), 253, 470, 477, 50),
    (_('Sumpul River'), 252, 392, 269, -45),
    (_('Torola River'), 251, 593, 378, 0),
    (_('Jiboa River'), 250, 382, 507, 80),
    (_('Grande de San Miguel River'), 249, 582, 511, 45),
    (_('Goascorán River'), 248, 741, 434, 80),
    (_('Guarajambala River'), 247, 545, 262, 80),
    (_('Lake of Güija'), 246, 206, 266, 0),
    (_('Lake of Coatepeque'), 245, 200, 392, 0),
    (_('Lake of Ilopango'), 244, 352, 452, 45),
    (_('Olomega Lagoon'), 243, 665, 569, 45),
    (_('Cerrón Grande Reservoir'), 242, 354, 324, -45),
    (_('Pacific Ocean'), 241, 298, 708, 0)
]

ROUTES = []

STATS = [
    (_('Capital:'), _('San Salvador') + ' ' + _("(13º40' N - 89º10' W)")),
    (_('Language:'), _('Spanish')),
    (_('Government:'), _('Presidential republic')),
    (_('President:'), _('Nayib Bukele')),
    (_('Vice President:'), _('Félix Ulloa')),
    (_('Independence:'), _('from Spain')),
    ('', _('declared: %s') % _('September 15, 1821')),
    ('', _('recognized: %s') % _('June 12, 1824')),
    (_('Area:'), '21 041' + ' ' + _('km²')),
    (_('Population:'), '6 365 503 (2025)'),
    (_('GDP:'), 'USD 36 710 000 000 (2025)'),
    (_('HDI:'), _('Medium') + ' - 0.678 (2023, #132)'),
    (_('Currency:'), _('United States Dollar')),
    (_('Updated:'), '2026-09-25'),
]

