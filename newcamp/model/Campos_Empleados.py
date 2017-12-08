# -*- coding: utf-8 -*- 

from odoo import models, fields

class Campos_Generales(models.Model):

    _inherit = 'hr.employee'

    x_Fecha_Ingr = fields.Date(string = "Fecha de ingreso")
    x_Venc_Pasaporte = fields.Date(string="Vencimiento de Pasaporte")
    x_Clabe_Interb = fields.Char(string = "CLABE")
    x_Nom_Banc = fields.Many2one('res.bank', string="Banco")
    x_Fecha_Baja = fields.Date(string = "Fecha de baja")
    x_Motiv_Baja = fields.Text(string = "Motivo de la baja")
    x_Pade_Enfermedad = fields.Text(string = "Enfermedades/Padecimientos")
    x_Act_Nacimiento = fields.Binary(string = "Acta de Nacimiento")
    x_Termi_Antici = fields.Binary(string = "Terminacion anticipada")
    x_Ident_INE = fields.Binary(string = "INE")
    x_Curp = fields.Binary(string = "CURP")
    x_Pasaporte = fields.Binary(string = "Pasaporte")
    x_Estado_Cuenta = fields.Binary(string = "Estado de cuenta")
    x_Viaje_Extranjero = fields.Binary(string = "Viaje Extranjero")
    x_Contrato = fields.Binary(string = "Contrato Vigente")
    x_ofeton = fields.Binary(string="Oferta Vigente")
    x_Convenio_Confide = fields.Binary(string = "Convenio confidencial")
    x_Prescrip_Medica = fields.Binary(string = "Constancia medica")
    x_Acuerdo_Confi_Salida = fields.Binary(string = "Acuerdo confidencialidad de salida")
    x_ClaveUnica = fields.Char(string="CURP")
    x_rfc_dig = fields.Binary(string = "RFC")
    x_Numero_cta = fields.Char(string="Numero de Cuenta")
    x_alias = fields.Char(string="Alias")
    x_res_partner = fields.Many2one('res.partner', string="Contacto")
    x_ClaveMigracion = fields.Char(string="Clave Tarjeta de Migracion")
    x_TarjetaMigracion = fields.Binary(string="Tarjeta de Migracion")
    x_EncuestaSalida = fields.Binary(string="Encuesta de salida")
    x_NSS = fields.Char(string="NSS")
    x_capacitaciones = fields.Many2many('openacademy.session', string="Capacitaciones")
    x_Seguro_Vida = fields.Char(string="Poliza de Seguro de Vida")
    x_Poliza_Seguro = fields.Binary(string="Poliza de Seguro de Vida")
    x_Objetivos = fields.Many2many('objetivos.mind', string="Objetivos")

    #Campos de Saldos

    x_Ausencias = fields.Many2many('hr.holidays')
    x_Compensaciones = fields.Many2many('compensacion.mind', string="Compensaciones")
    x_Vacaciones = fields.Many2many('vacaciones.mind', string="Vacaciones")
