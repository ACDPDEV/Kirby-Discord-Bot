# KIRBY - Discord Bot
> Kirby es un bot de discord personalizado para el servidor GatoCraftMC

> ## ALPHA 1.0.1
>
> ### Cambios:
>
> - **Mejora del OUTPUT.RANDOM:** Se amplió el margen de la list tras remplazar a random_meme() por random_choice(): 
>
> **Antes:**
> ```python 
> if message.content.startswith(COMMANDS.RANDOM):
>   OUTPUTS.RANDOM = random_meme(random.randint(0, 50)) # Movida rara
> ```
> **Después:**
> ```python
> if message.content.startswith(COMMANDS.RANDOM):
>     OUTPUTS.RANDOM = random.choice(get_meme())
> ```
>
> - **Función obsoleta eliminada:** La función random_meme() ha sido eliminada y remplazada por random.choice()
> 
> **Función obsoleta:**
> ```python
> def random_meme(random_number) -> str:
>    """
>    Get a random item from get_meme()
>    """
>
>    meme_list = get_meme()
>    random_index = random_number
>    try:
>        meme = meme_list[random_index]
>    except IndexError:
>        meme = None
>    if meme:
>        return meme
>    else:
>        random_meme(random_number)
> ```
> Además esta función tenía un error grave, porque si `random_number` era un número que esté fuera del index de la lista `meme_list` se llamaba otra vez con el mismo número `else: random_meme(random_number)`, arrojando el mismo error, esto hacía que el bot pueda quedarse en un bucle infinito y dejara de funcionar.

> ## ALPHA 1.0.0
>
> ### Comandos:
>
> ```
> k! hi
> (OUTPUT: Hi, I'm Kirby)
> ```
> ```
> k! hola
> (OUTPUT: Hola, soy Kirby)
> ```
> ```
> k! random
> (OUTPUT: Random meme de Tenor GIFS)
> ```

> ## Discord server:
> 😺 [GatoCraftMC](https://discord.gg/wR9nUNecDF)
