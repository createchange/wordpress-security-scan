import subprocess

# Add list of sites to check to the appropriate section. Removed for security sake.
maint_sites = ['https://training.msminc.com']
non_maint_sites = []

subprocess.check_output('cat headers/web_maintenance_header.txt > results.txt', shell=True)

with open('results.txt','a') as f:
    for site in maint_sites:
        scan_results = subprocess.check_output('docker run -it --rm wpscanteam/wpscan --url %s --enumerate u -f cli-no-color' % site, shell=True)
        f.write(scan_results)
        f.write('---------------------------------------------------------------\n')


subprocess.check_output('cat headers/non_web_maintenance_header.txt >> results.txt', shell=True)

with open('results.txt','a') as f:
    for site in non_maint_sites:
        scan_results = subprocess.check_output('docker run -it --rm wpscanteam/wpscan --url %s --enumerate u -f cli-no-colour' % site, shell=True)
        f.write(scan_results)
        f.write('---------------------------------------------------------------\n')



