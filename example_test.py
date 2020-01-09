import lambda_handler as lh

event ={'domain': 'gsa.gov', 'environment': {'suffix_list': None,'hosts_to_scan': [{'hostname': 'aboutusa.japan.usembassy.gov', 'port': 443, 'starttls_smtp': False}], 'scan_method': 'lambda', 'scan_uuid': 'fe913d5e-d4ce-474e-aace-657fa5899188', 'workers': 900}, 'options': {'sslyze_certs':False,'_': {'cache_dir': '/opt/scan/pulse/data/./output/subdomains/scan/cache', 'lambda_options': {'aws_profile': 'lambda', 'invoke_client': None, 'invoke_config': None, 'lambda_mode': True, 'lambda_session': None, 'logs_client': None, 'logs_config': None}, 'report_dir': '/opt/scan/pulse/data/./output/subdomains/scan', 'results_dir': '/opt/scan/pulse/data/./output/subdomains/scan/results'}, 'cache': False, 'debug': True, 'domains': '/opt/scan/pulse/data/./output/subdomains/gather/results/gathered.csv', 'lambda': False, 'lambda_profile': 'lambda', 'meta': True, 'output': '/opt/scan/pulse/data/./output/subdomains/scan', 'scan': 'pshtt,sslyze', 'serial': False, 'sort': True, 'workers': '900'}, 'scanner': 'sslyze'}

lh.main(event,'')
