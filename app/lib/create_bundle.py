from app.lib.docxmerge import docxmerge
from app.models import Matter, Bundle
import os
from datetime import date

def bundle_documents(bundle_id):
	if not os.path.exists('tmp/' + bundle_id):
	    os.makedirs('tmp/' + bundle_id)
	bundle = Bundle.objects.get(pk=bundle_id)
	document_list = bundle.documents.all()
	# print(document_list)
	matter = bundle.matter
	attorney = matter.attorneys.first()
	client = matter.clients.first()
	data_fields = {'client_first_name':client.first_name,'client_last_name':client.last_name,'current_date':str(date.today().isoformat()),'case_number':matter.case_number, 'plaintiff':matter.plaintiff, 'defendant':matter.defendant, 'attorney_first_name': attorney.user.first_name, 'attorney_last_name': attorney.user.last_name, 'attorney_email_address':attorney.user.email, 'attorney_bar_number':str(attorney.bar_number), 'client_mailing_address':client.mailing_address, 'client_phone_number':client.phone_number, 'client_city': client.city, 'client_state': client.state, 'client_zip_code': str(client.zip_code), 'client_name': client.full_name(), 'client_email_address': client.email_address}
	for document in document_list:
		doc_name = os.path.basename(document.document_file.name)
		tmp_file = 'tmp/' + bundle_id + '/' + doc_name
		print(tmp_file)
		if doc_name.endswith('.docx'):
			docxmerge('src/' + doc_name, data_fields, tmp_file)
		else:
			pass