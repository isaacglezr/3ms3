# -*- coding: utf-8 -*-

from odoo import models, fields

class Objetivo(models.Model):

    _name = 'compensacion.mind'

    name = fields.Char(string="Descripcion", required=True)
    x_tipocompensacion = fields.Selection([('1', 'Medio Dia'), ('2', 'Dia Completo')], required=True, string="Tipo de Compensacion")
    x_fecha_inicio = fields.Datetime(string="Fecha de Inicio")
    x_fecha_fin = fields.Datetime(string="Fecha de Fin")
    x_notecomp = fields.Text(string="Comentarios")
    x_Empleado = fields.Many2one('hr.employee', string="Empleado")
    x_vigentes = fields.Boolean(string="Vigente")
