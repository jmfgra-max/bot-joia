import discord
from discord.ext import commands
import random

# 1) COLE AQUI o token do seu bot (Discord Developer Portal)
TOKEN = "COLE_SEU_TOKEN_AQUI"

# 2) Banco de dados de itens — reaproveitado do nosso EcoAmigo 2.0!
# Cada item guarda: (para onde vai, tempo de decomposição)
lixo = {
    "garrafa pet":      ("reciclável", "450 anos"),
    "lata de aluminio": ("reciclável", "200 anos"),
    "papel":            ("reciclável", "3 meses"),
    "vidro":            ("reciclável", "mais de 1 milhão de anos"),
    "sacola plastica":  ("reciclável", "450 anos"),
    "casca de banana":  ("orgânico", "2 anos"),
    "resto de comida":  ("orgânico", "algumas semanas"),
    "fralda":           ("lixo comum", "450 anos"),
    "pneu":             ("lixo comum", "600 anos"),
    "isopor":           ("lixo comum", "400 anos"),
    "pilha":            ("coleta especial", "nunca se decompõe"),
    "celular":          ("coleta especial", "nunca se decompõe"),
}

# 3) Listas com dicas e desafios (o bot sorteia um a cada comando)
dicas = [
    "Use garrafa reutilizável em vez de comprar água toda hora.",
    "Leve sua própria sacola ao mercado.",
    "Prefira produtos com pouca embalagem.",
    "Desligue a luz ao sair do quarto.",
    "Tome banhos mais curtos para economizar água.",
]

desafios = [
    "Essa semana, leve sua própria sacola ao mercado!",
    "Separe o lixo reciclável da sua casa por 7 dias.",
    "Use uma garrafa reutilizável por uma semana inteira.",
    "Convença um amigo a fazer um desafio ecológico com você!",
]

# 4) Cria o bot. O prefixo "!" significa que os comandos são !eco, !lixo, !desafio
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

# 5) Avisa no console quando o bot ligar
@bot.event
async def on_ready():
    print(f"Bot {bot.user} está online!")

# 6) COMANDO 1: !eco — sorteia uma dica ecológica
@bot.command()
async def eco(ctx):
    """Dá uma dica ecológica aleatória."""
    dica = random.choice(dicas)
    await ctx.send(f"🌱 Dica ecológica: {dica}")

# 7) COMANDO 2: !lixo  — diz onde jogar e o tempo de decomposição
@bot.command()
async def lixo(ctx, *, item):
    """Diz onde jogar o item e quanto tempo ele leva para se decompor."""
    item = item.lower().strip()
    if item in lixo:
        destino, tempo = lixo[item]
        await ctx.send(f"♻️ **{item}**: lixo {destino} | ⏳ Decomposição: {tempo}")
    else:
        await ctx.send("🤔 Ainda não sei sobre esse item! Tente: garrafa pet, lata de aluminio, papel, vidro, sacola plastica, casca de banana, resto de comida, fralda, pneu, isopor, pilha ou celular.")

# 8) COMANDO 3: !desafio — propõe um desafio ecológico
@bot.command()
async def desafio(ctx):
    """Propõe um desafio ecológico."""
    desafio = random.choice(desafios)
    await ctx.send(f"🎯 Desafio do dia: {desafio}")

# 9) Liga o bot com o token
bot.run(TOKEN)
