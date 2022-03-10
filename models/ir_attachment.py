from odoo import api, fields, models, tools, _

class PurchasePurchase(models.Model):
    _inherit = 'ir.attachment'

    x_res_id = fields.Char(string=u'关联附件')
