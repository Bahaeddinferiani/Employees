from odoo import fields, models
from odoo.modules import get_module_resource
import base64
def get_default_img():
    with open(get_module_resource('gestion_ics', 'static/img', 'default.png'),'rb') as f:
        return base64.b64encode(f.read())

class ics(models.Model):
    _name = 'ics.employee'
    _description = 'this tool allow the management of ics employees'

    name = fields.Char(string='Nom', required=True)
    email = fields.Char(string='E-mail', required=True)
    martial_status = fields.Selection([('marié', 'marié'), ('Célibataire', 'célibataire')], string='Status civil')
    Kms_to_work = fields.Integer(string="Distance a l'emploi en km", required=True)
    date_of_birth = fields.Date(string='Date de naissance',required=True)
    tel = fields.Char(string='Mobile', required=True)
    department = fields.Selection([('odoo development', 'odoo development'), ('Web development', 'Web development')],string='Departement',required=True)
    salary = fields.Float(string='Salaire', required=True)
    adress = fields.Text(string="Adresse",required=True)
    job = fields.Selection(
        [('Gérant', 'gerant'), ('technicien', 'technicien'), ('ingenieur', 'ingenieur'), ('stagiaire', 'stagiaire')],
        string='Poste')
    photo = fields.Binary(string='Photo',default=get_default_img())