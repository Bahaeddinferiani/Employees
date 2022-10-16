from odoo import fields, models



class heures(models.Model):
    _name = 'ics.heures'
    _description = 'this tool allow the management of company addition hours'
    name = fields.Many2one("ics.employee")
    heures_ids = fields.One2many('ics.heure','name',string="Hours")
class heure(models.Model):
    _name = 'ics.heure'
    name = fields.Char(string="nom heures")
    date = fields.Date(string="date des heures")
    num = fields.Float(string="nombre des heures",)
    prix = fields.Float(string="Prix de l'heure")
    baha = fields.Char(string="Somme", compute='compute_somme')
    def compute_somme(self):
         self.baha = "bonjour"