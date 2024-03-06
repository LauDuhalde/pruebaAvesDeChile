html_template = '''<!DOCTYPE html>
<html lang="es">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Laura Duhalde" />
    <meta name="description" content="Listado de Aves Chilenas" />
    <meta name="keywords" content="aves, Chile" />
    <title>Aves de Chile</title>
<body>
    <head>
        <div style="display:flex; justify-content:center">
            <h1>Aves de Chile</h1>
        </div>
    </head>
    <main>
        <div style="display:flex; justify-content:center; flex-wrap: wrap;">
            $main
        </div>
    </main>
    
</body>
</html>
                        '''
bird_template='''
            <div style="border: 1px solid #000; margin: 10px; text-align: center;">
                <img src="$url">
                <p><span style="font-weight: bold;">Nombre:</span> $nombre</p>
                <p><span style="font-weight: bold;">Name:</span>: $name</p>
            </div>\n
            '''