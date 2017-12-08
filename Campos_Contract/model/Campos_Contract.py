# -*- coding = utf-8 -*-
from odoo import models, fields, api

class Campos_Contract(models.Model):

    _inherit = 'hr.contract'

    x_pasaporte = fields.Char(string="No Pasaporte")
    x_direccion = fields.Char(string="Direccion Particular")
    x_nacion = fields.Many2one('res.country', string="Nacionalidad")
    x_birthday = fields.Date(string="Fecha de Nacimiento")
    x_email = fields.Char(string="Correo Electronico")
    x_movil = fields.Char(string="Movil")
    x_rfc = fields.Char(string="RFC")
