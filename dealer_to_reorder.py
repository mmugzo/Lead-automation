existing_opportunity = env['crm.lead'].search([('partner_id', '=', record.id), ('type', '=', 'opportunity')], limit=1)
if not existing_opportunity:
    opportunity = env['crm.lead'].create({
            'name': f"Opportunity for {record.name}",
            'partner_id': record.id,
            'type': 'opportunity',
            'stage_id': 18,
            'user_id': record.user_id.id if record.user_id else False,})
            
        
    contact_activities = env['mail.activity'].search([('res_id', '=', record.id), ('res_model', '=', 'res.partner')])
    res_model_id = env['ir.model'].search([('model', '=', 'crm.lead')], limit=1).id 
    for activity in contact_activities:
        # Create a new activity for the CRM opportunity with the same values as the contact activity
        env['mail.activity'].create({
            'res_id': opportunity.id,
            'res_model': 'crm.lead',
            'res_model_id': res_model_id,
            'activity_type_id': activity.activity_type_id.id,
            'summary': activity.summary,
            'note': activity.note,
            'date_deadline': activity.date_deadline,
            'user_id': activity.user_id.id,
        })