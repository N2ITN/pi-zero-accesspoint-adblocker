import subprocess

with open('home.html', 'w') as page:
    ip = subprocess.check_output("echo $IP", shell=True).decode('utf-8')
    router = 'http://' + subprocess.check_output("echo $ROUTER", shell=True).decode('utf-8')
    routerlink = ''.join(['<a class="button button-outline" href=', router,'> Your Router </a>'])
    dnslabel = ''.join(['<label>Set your DNS to: </label>', '<t>', ip, '</t>'])
    page.write('''
<!-- Google Fonts -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic">



<!-- Milligram CSS minified -->
<link rel="stylesheet" href="milligram/dist/milligram.min.css">

<!-- You should properly set the path from the main file. -->''')

    page.write("\n".join([
        '<html>', 
            '<body>',
                routerlink,
                '<br>',  '<br>',
                dnslabel,
                '<br>', '<br>',
                '<a class="button" href="/admin"> Pi-Hole Dashboard  </a>', 
            '</body>',
        '</html>'
    ]))
