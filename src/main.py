import datetime
import json
from urllib.request import urlopen
import discord
from discord.ext import commands
from discord.utils import get
import youtube_dl
import os
from urllib import request, parse
import re
import random
from pexels_api import API
from serpapi import GoogleSearch


bot = commands.Bot(command_prefix='!', description='botsito discord')


#Bot de discord
TOKEN_DISCORD = 'OTE0OTYxMjEzODcwNDQ4Njcx.YaUqCA.2l59jK3Sj_cq2FbVa6PbRTlphf8'
#api de la Nasa
KEY = 'FTCG0fbOdWjTk6LFkKzYcR82NDEOQhHlhfQAfu8O'
#api de Pexels
PEXELS_API_KEY = '563492ad6f91700001000001079a8f7f501842409d298d2d16aecb06'
#Serpapi (api para hacer busquedas en google)
sepapi_key = 'e5723dfc8e5b57757b61459488f57843e8b47e61e835948eeb033742e008f894'
#weather api
wheather_api_key = 'f98f73a2c4db4971bb9223924210312'


url = request.Request(f'https://api.nasa.gov/planetary/apod?api_key={KEY}')
url.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:78.0) Gecko/20100101 Firefox/78.0')
url.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')

@bot.command(pass_context=True)
async def elbicho(ctx):
    await ctx.send('''
   asd
    
      ***El bicho⠀⣴⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢻⣿⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣦⠀
⠀⠀⠀⠀⠀⠀⣴⣿⢿⣷⠒⠲⣾⣾⣿⣿
⠀⠀⠀⠀⣴⣿⠟⠁⠀⢿⣿⠁⣿⣿⣿⠻⣿⣄⠀⠀⠀⠀
⠀⠀⣠⡾⠟⠁⠀⠀⠀⢸⣿⣸⣿⣿⣿⣆⠙⢿⣷⡀⠀⠀
⣰⡿⠋⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠉⠻⣿⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣆⠂⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡿⣿⣿⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠿⠟⠀⠀⠻⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⡿⠃⠀⠀⠀⠀⠀⠘⢿⣿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⡀⠀⠀
⠀⠀⠀⠀⢠⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣧⠀⠀
⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣆⠀
⠀⠀⠠⢾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⡤⠄
    ''')

@bot.command(pass_context=True)
async def foto(ctx, busqueda):

    api = API(PEXELS_API_KEY)
    num = random.randint(1, 10)
    api.search(busqueda, page=num, results_per_page=1)

    photos = api.get_entries()

    for photo in photos:

        print('Fotografo: ', photo.photographer)
        print('url: ', photo.url)
        print('Foto en el tamaño original: ', photo.original)
        await ctx.send(photo.url)
        await ctx.send(photo.original)
        await ctx.send('Autor', photo.photographer)
        #response = req.get(photo.original)
        #image = Image.open(BytesIO(response.content))
        #image.show()

@bot.command(pass_context=True)
async def jackie(ctx):
    await ctx.send('''
   *******************************
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠉⠄⠄⠄⠄⠄⠄⠄⢀⣠⣤⡀⠄⠄⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⡀⠄⠄⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣧⠄⠄⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⣰⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠈⢻⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠄⠄⢸⣠⣶⡷⠄⢰⣿⡿⠄⠈⠙⢿⡇⠄⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⣿⣟⣁⣀⡀⢸⣿⡇⠘⠻⢿⡌⡇⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⢰⣿⣿⣿⣍⣵⣿⣿⣷⡰⢤⣄⢻⡇⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢸⣿⣿⡿⢿⣿⣿⣿⣿⢿⣿⣿⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢾⣿⠋⠄⣼⠛⠻⠿⠿⡇⢻⣿⣿⡇⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢸⣧⠄⠄⣿⣄⡀⠄⢠⠃⠄⠙⢿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠈⣿⡇⠄⢈⣉⡉⠉⠛⠃⠄⠄⢸⠁⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⣿⣿⣾⣦⡙⠛⠟⠃⣀⣰⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⣷⣿⣿⣿⡏⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠈⣿⣿⣧⣄⣤⣿⣿⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠄⠄⠸⣿⣿⣿⣿⣿⠇⠄⠄⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠉⠙⠛⠉⠁⠄⠄⠄⠄⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢩⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ''')

@bot.command(pass_context=True)
async def shrek(ctx):
    await ctx.send('''asd
    
 ⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆ Ta weno
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ''')

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title=f'Comandos', description=f'!ayuda',
                          color=discord.Color.blurple())
    embed.add_field(name='!nasa', value=f'Manda la foto del dia')
    embed.add_field(name='!ping', value=f'Devuelve pong')
    embed.add_field(name='!info', value=f'Info del server')
    embed.add_field(name='!youtube', value=f'Busca algo en youtuve y devuelve el primer video')
    embed.add_field(name='!chiste', value=f'kkkkkkkkkk')
    embed.add_field(name='!conectar', value=f'se conecta al chat de voz')
    embed.add_field(name='!desconectar', value=f'se desconecta del chat de voz')
    embed.add_field(name='!elbicho', value=f'elbicho')
    embed.add_field(name='!jackie', value=f'Jackie Chan')
    embed.add_field(name='!shrek', value=f'Shrek')
    embed.add_field(name='!play',
                    value=f'(!play url) (el bot tiene que estar en un chat de voz) reproduce un audio de youtube')
    embed.add_field(name='!pause', value=f'Pone pausa el audio')
    embed.add_field(name='!resume', value=f'Despausa el audio')
    embed.add_field(name='!stop', value=f'Termina el audio que se este reproduciendo')
    embed.add_field(name='!foto', value=f'(Ej !foto tren) Busca una foto en Pexels)')
    embed.add_field(name='!google_imagenes', value=f'(Ej !google_imagenes manzana) Busca una foto en Google imagenes)')
    embed.add_field(name='!negocios', value=f'(Ej !google_imagenes McDonald\'s) Busca un negocio en google (anda como el culo))')
    embed.add_field(name='!clima', value=f'(Mustra el clima de un lugar (si el lugar tiene mas de una palabra hay que separarlas con -)')


    await ctx.send(embed=embed)


@bot.command()
async def nasa(ctx):
    with urlopen(url) as pagina:
        try:
            contenido = pagina.read()
            info_pagina = json.loads(contenido.decode('utf-8'))
            url_foto = info_pagina.get('hdurl')
            persona = info_pagina.get('copyright')
            fecha = info_pagina.get('date')
            descripcion = info_pagina.get('explanation')

            await ctx.send(f'{url_foto}')
            await ctx.send(f'Descripcion de la imagen: {descripcion}')
            await ctx.send(f'Autor: {persona}')
            await ctx.send(f'Fecha: {fecha}')

        except Exception as e:
            print(f'Error: {e}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong pedazo de puto')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name}', description=f'assadssadsad', timestamp=datetime.datetime.utcnow(),
                          color=discord.Color.blurple())
    embed.add_field(name='Servidor creado en: ', value=f'{ctx.guild.created_at}')
    embed.add_field(name='El servidor fue creado por: ', value=f'{ctx.guild.owner}')
    await ctx.send(embed=embed)

@bot.command()
async def youtube(ctx, *, busqueda):
    query_string = parse.urlencode({'search_query': busqueda})
    html = request.urlopen('https://www.youtube.com/results?'+query_string)
    resultado = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    #print(resultado)
    await ctx.send('http://www.youtube.com/watch?v='+resultado[0])

@bot.event
async def on_ready():
    print('El bot esta listo')
    await bot.change_presence(activity=discord.Game(name='!ayuda'))

@bot.command(pass_context=True)
async def conectar(ctx):
    canal = ctx.message.author.voice.channel
    if not canal:
        ctx.send('metete a un canal de voz boludito')
    voz = get(bot.voice_clients, guild=ctx.guild)
    if voz and voz.is_connected():
        await voz.move_to(canal)
    else:
        voz = await canal.connect()
    await ctx.send(r'Ya llegue putos', tts=True)

@bot.command(pass_context=True)
async def desconectar(ctx):
    try:
        voz = get(bot.voice_clients, guild=ctx.guild)
        if voz and voz.is_connected():
            await voz.disconnect()

    except Exception as e:
        ctx.send('No puedo capo')

@bot.command(pass_context=True)
async def chiste(ctx):
    chistes = ['¿Cómo se dice disparo en árabe? Ahí-va-la-bala.', '¿Qué le dice una iguana a su hermana gemela? Somos iguanitas', 'Una mujer le dice a su marido: Cariño, ¿te gusta mi disfraz? Sí, mi amor, contesta el hombre, es un disfraz de vaca muy bonito. ¡Pero si voy disfrazada de dálmata!','¿Qué le dice un techo a otro? Techo de menos', 'El profesor le pregunta a Jaimito: Jaimito, ¿qué fórmula química es H2O+CO+CO? ¡Fácil, profesor! Es agua de coco.','¿Cómo se queda un mago después de comer? Magordito.', '¿Me da un café con leche corto? Se ha roto la máquina, cambio.', '''
    - Ayer llamé a la policía porque unos ladrones robaron en mi casa y se llevaron hasta los vasos.
    - ¿Y los detuvo?-Sí, los de tubo también.''', '''
    - ¿Sabes que mi hermano anda en bicicleta desde los cuatro años?
    - Mmm, ya debe estar lejos.''', '''
    - Jaimito, si en esta mano tengo 8 naranjas y en esta otra 6 naranjas ¿Qué tengo?
    - Unas manos enormes, señorita.''', '''¿Cuál es el animal que tiene entre tres y cuatro ojos? El piojo''', '''¿Alguien sabe algún chiste sobre el sodio? Na…''', '''
    —Niño, sal del coche y mira si funciona el intermitente.
    —Ahora sí, ahora no, ahora sí, ahora no, ahora sí, ahora no…''', '''¿Dónde vas, Antonio?
    —A buscar estiércol para las frutillas.
    —¿Pero por qué no te las comes con crema, como todo el mundo?''', '''El otro día tu señora me contó un chiste tan bueno que de la risa me caí de la cama.''', '¿Como se va el DJ de la fiesta? En remix', 'Un ciego era sospechoso de un asesinato ¿Por que? Porque no tenia nada que ver', '¿Que hace un taper en el desierto? Taperdido']

    ultimo = len(chistes)
    i = random.randint(0,ultimo-1)
    await ctx.send(chistes[i],tts=True)


@bot.command(pass_context=True)
async def play(ctx, url):

    #Reproducir cancion
    cancion_activa = os.path.isfile('cancion.mp3')
    try:
        if cancion_activa:
            os.remove('cancion.mp3')
            print('Cancion eliminada')
    except PermissionError:
        print('Hay una cancion reproduciendose')
        await ctx.send('Error: hay una cancion reproduciendose')
    await ctx.send('Listo')
    voz = get(bot.voice_clients, guild=ctx.guild)
    ydl_op = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }],
    }
    with youtube_dl.YoutubeDL(ydl_op) as ydl:
        print('Empezo la descarga')
        ydl.download([url])
    for file in os.listdir('./'):
        if file.endswith('mp3'):
            name2=file
            os.rename(file,'cancion.mp3')
            print('cancion renombrada')
    voz.play(discord.FFmpegPCMAudio(executable=r"C:\ffmpeg\bin\ffmpeg.exe", source='cancion.mp3'), after=lambda e: print('termino'))
    voz.source = discord.PCMVolumeTransformer(voz.source)
    voz.source.volume = 0.06
    nombre= name2.rsplit('-', 2)
    await ctx.send(f'La cancion es {nombre[0]}')

@bot.command(pass_context=True)
async def pause(ctx):
    voz = get(bot.voice_clients, guild=ctx.guild)

    if voz and voz.is_playing():
        print('cancion pausada')
        voz.pause()
        await ctx.send('Cancion pausada')
    else:
        print('No se esta reproduciendo musica')
        await ctx.send('No se esta reproduciendo musica')

@bot.command(pass_context=True)
async def resume(ctx):

    voz = get(bot.voice_clients, guild=ctx.guild)
    if voz and voz.is_paused():
        voz.resume()
    else:
        print('La cancion no esta en pausa')
        await ctx.send('La cancion no esta en pausa')

@bot.command(pass_context=True)
async def stop(ctx):
    voz = get(bot.voice_clients, guild=ctx.guild)
    if voz and (voz.is_playing() or voz.is_paused()):
        voz.stop()
    else:
        await ctx.send('No hay una cancion pausada o reproduciendoce')
        print('No hay una cancion pausada o reproduciendoce')

@bot.command(pass_context=True)
async def google_imagenes(ctx, busqueda):
    params = {
     'q': busqueda,
     'tbm': 'isch',
     'ijn': '0',
     'api_key': sepapi_key
    }
    i = random.randint(0,100)

    search = GoogleSearch(params)
    resultado = search.get_dict()
    imagenes = resultado['images_results'][i]
    imagen_link = imagenes['original']
    print(i)
    await ctx.send(imagen_link)

@bot.command(pass_context=True)
async def google_negocios(ctx, local):
    params = {
        'q': local,
        "location": 'bahia blanca,buenos aires,argentina',
        "tbm": "lcl",
        'api_key': sepapi_key
    }
    search = GoogleSearch(params)
    resultado = search.get_dict()
    print(resultado)
    negocio = resultado['local_results'][0]



    print(negocio)
    nombre = negocio['title']
    direccion = negocio['address']
    telefono = negocio['phone']
    estado = negocio['hours']
    coordenadas = negocio['gps_coordinates']
    latitud = coordenadas['latitude']
    longitud = coordenadas['longitude']


    #await ctx.send(f'URL {mapa}')
    await ctx.send(f'Nombre: {nombre}')
    await ctx.send(f'Direccion: {direccion}')
    await ctx.send(f'Telefono {telefono}')
    await ctx.send(f'Estado ahora: {estado}')
    await ctx.send(f'Coordenadas: {latitud}, {longitud}')

@bot.command(pass_context=True)
async def clima(ctx,lugar):
    fecha = datetime.datetime.now()
    año = fecha.year
    if fecha.month<10:
        mes = f'0{fecha.month}'
    else:
        mes = fecha.month

    if fecha.day<10:
        dia = f'0{fecha.day}'
    else:
        dia=fecha.day
    print(lugar)
    url =f'http://api.weatherapi.com/v1/forecast.json?key={wheather_api_key}&q={lugar}&dt={año}-{mes}-{dia}'
    with urlopen(url) as api:
        contenido = api.read()
        info= json.loads(contenido.decode('utf-8'))
        lugar= info.get('location').get('name') #nombre del lugar
        lugar_info = info.get('location').get('tz_id')
        clima = info.get('forecast').get('forecastday')[0]
        fecha = clima.get('date')#fecha
        tiempo = clima.get('day')
        temp_max = tiempo.get('maxtemp_c')#temperatura maxima
        temp_min = tiempo.get('mintemp_c')#temperatura minima
        temp_media = tiempo.get('avgtemp_c')#temperatura media
        viento_max = tiempo.get('maxwind_kph')#viendo max
        lluvia =  tiempo.get('totalprecip_mm')
        posib_lluvia = tiempo.get('daily_chance_of_rain')


        await ctx.send(f'El tiempo en {lugar} {lugar_info}. Dia {fecha}')
        await ctx.send(f'Temperatura maxima: {temp_max}')
        await ctx.send(f'Temperatura minima: {temp_min}')
        await ctx.send(f'Temperatura media: {temp_media}')
        await ctx.send(f'Viento: {viento_max} KPH')
        await ctx.send(f'Posibilidad de lluvia: {posib_lluvia}')
        await ctx.send(f'Cantidad de lluvia: {lluvia}mm')


bot.run(TOKEN_DISCORD)
