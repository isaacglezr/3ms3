# -*- coding: utf-8 -*-

from odoo import models, fields

class Objetivo(models.Model):

    _name = 'objetivos.mind'

    name = fields.Char(string="Objetivo", required=True)
    objetivo = fields.Binary(string="Documento de Objetivos", required=True)
    fecha_inicio = fields.Date(string="Fecha de Inicio")
#   employee_id = fields.Many2one('hr.employee', string="Empleado")
    fecha_fin = fields.Date(string="Fecha de Fin")
    teamleader = fields.Many2one('hr.employee', string="Responsable")
    feedback1 = fields.Binary(string="FeedBack 1")
    feedback2 = fields.Binary(string="FeedBack 2")
    feedback3 = fields.Binary(string="FeedBack 3")
