# -*- coding: utf-8 -*-

from odoo import models, fields

class Objetivo(models.Model):

    _name = 'vacaciones.mind'

    name = fields.Char(string='Descripcion', required=True)
    date_st = fields.Date(string="Fecha de Inicio", required=True)
    date_fin = fields.Date(string="Fecha de Fin", required=True)
    not_vac = fields.Text(string="Comentarios")
    x_Emplea_vaca = fields.Many2one('hr.employee', string="Empleado")

