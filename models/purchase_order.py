from odoo import api, fields, models, tools, _

class PurchasePurchase(models.Model):
    _inherit = 'mrp.bom'

    information_attachment = fields.Many2many('ir.attachment', compute='_get_attachment_ids', string=u'附件')


    def _get_attachment_ids(self):
        att_model = self.env['ir.attachment'] #获取附件模型
        for obj in self:
            query = [('res_model', '=', "product.template"), ('x_res_id', '=', obj.id)]   #根据res_model和res_id查询附件
            obj.information_attachment = att_model.search(query) #取得附件list