
# -*- encoding: utf-8 -*-
##############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################
{
    'name': 'MRP Lot Reserve',
    'version': "1.0",
    "category": "Manufacturing",
    "author": "OdooMRP team,"
              "AvanzOSC,"
              "Serv. Tecnol. Avanzados - Pedro M. Baeza",
    'contributors': ["Daniel Campos <danielcampos@avanzosc.es>",
                     "Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>",
                     "Ana Juaristi <ajuaristio@gmail.com>"],
    'website': "http://www.odoomrp.com",
    'depends': ["mrp_production_editable_scheduled_products"],
    'data': ["views/mrp_production_view.xml"],
    'installable': False,
}
