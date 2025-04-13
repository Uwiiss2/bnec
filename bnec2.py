import telebot
from time import sleep as sp
from telebot import TeleBot, types

# Token do Bot
token = "7864959212:AAHUA3TD-njAcwBLtt2U67voPV_gWd5Ui70"
bot = telebot.TeleBot(token)
# ID do grupo "Agentes da Mente"
grp = -1002519988454
###########

@bot.message_handler(commands=['menu'])
def mostrar_menu(message):
    texto = """
📋 *Menu Principal do Bot - Guia da Mente e do Coração*

Aqui está tudo o que você pode explorar com apenas um toque:

🧘 *Respira, calma*  
→ Aula de respiração consciente para baixar a ansiedade.

🎯 *Foco turbo*  
→ Técnica Pomodoro e dicas pra manter a mente no jogo.

🌪️ *Lidando com o caos*  
→ Aula de concentração e como manter o foco mesmo nos dias difíceis.

💖 *Autoestima sem filtro*  
→ Exercício de amor-próprio e como se acolher.

📵 *Desconecta, respira*  
→ Pausas digitais saudáveis para o bem-estar.

🫂 *Fazer novas amizades*  
→ Dica: se conecta no grupo e conheça outros agentes da mente.

💌 *Conhecer alguém especial*  
→ Um lembrete: quem se cuida atrai o que é leve.

🧠 *Autocuidado mental extra*  
→ Em breve: novos conteúdos personalizados.

🎧 *Me acalmar com música*  
→ Aula com som relaxante para momentos de paz.

📰 *Fique por dentro das notícias*  
→ Entre no grupo oficial: [clique aqui](https://t.me/guiadamente)

Cada aula que você conclui te dá +1 nível e mostra ao grupo sua evolução!

Use o comando /nivel para ver seu nível atual.
"""
    bot.send_message(message.chat.id, texto, parse_mode="Markdown", disable_web_page_preview=True)
     
@bot.message_handler(commands=['start'])
def boas_vindas(msg):
    chat_id = msg.chat.id  # ID do usuário que usou o comando
    nome = msg.from_user.first_name

    bot.send_message(chat_id, f"Olá, {nome}! Este bot foi feito pra você.")
    sp(1)
    bot.send_message(chat_id, "O Guia da Mente é um mapa rápido pra quem vive na correria, sente o cérebro fritando, ou só quer melhorar o foco e viver mais leve.")
    sp(1)
    bot.send_message(chat_id, "O que temos por aqui?")
    bot.send_message(chat_id, "/comecar - bora começar? \n/menu - fique por dentro dos nossos guias!")

    # Envia mensagem no grupo também
    bot.send_message(grp, f"Novo agente conectado: {nome} acabou de iniciar o bot!")

@bot.message_handler(commands=["comecar"])
def menu_inicio(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn1 = types.KeyboardButton("🧘 Respira, calma")
    btn2 = types.KeyboardButton("🎯 Foco turbo")
    btn3 = types.KeyboardButton("🌪️ Lidando com o caos")
    btn4 = types.KeyboardButton("💖 Autoestima sem filtro")
    btn5 = types.KeyboardButton("📵 Desconecta, respira")
    btn6 = types.KeyboardButton("🫂 Fazer novas amizades")
    btn7 = types.KeyboardButton("💌 Conhecer alguém especial")
    btn8 = types.KeyboardButton("🧠 Autocuidado mental extra")
    btn9 = types.KeyboardButton("🎧 Me acalmar com música")
    btn10 = types.KeyboardButton("✨ O Guia do Carisma")
    btn11 = types.KeyboardButton("📰 Fique por dentro das notícias")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)

    bot.send_message(
        message.chat.id,
        "✨ Bem-vindo ao *Guia da Mente e do Coração*.\n\n"
        "Escolha uma das opções abaixo e mergulha no conteúdo que vai cuidar da tua mente com carinho:",
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: True)
def respostas_menu(message):
    texto = ""

    if message.text == "🧘 Respira, calma":
        texto = """
*🧘 RESPIRA, CALMA*  

Respirar pode parecer básico, mas quando feito com intenção, vira um superpoder. A mente da Geração Z vive no modo turbo, e essa é a pausa que você tava precisando.  

A técnica 4-7-8 é seu botão de reset:  
→ Inspire por 4 segundos  
→ Segure por 7  
→ Solte lentamente por 8 segundos  
Repita 4 vezes e sente a paz te abraçando.  

Dica extra: feche os olhos, coloque uma música instrumental e respire com o som. É mágico.
"""

    elif message.text == "🎯 Foco turbo":
        texto = """
*🎯 FOCO TURBO*  

Focar em um mundo de distrações é tipo ser um herói moderno. A técnica Pomodoro te dá uma espada invisível: 25 minutos de pura atenção e 5 minutos de respiro.

Crie uma lista de tarefas, coloque uma playlist de concentração e foque numa coisa por vez.  
→ Depois de 4 ciclos: pausa maior (15 a 30 min).  

Foco não é rigidez. É escolher com carinho o que merece sua energia naquele momento.
"""

    elif message.text == "🌪️ Lidando com o caos":
        texto = """
*🌪️ LIDANDO COM O CAOS*  

Quando tudo parece sair do controle, o segredo é reconectar com o que ainda tá firme dentro de você.  

1. Pare por 1 minuto.  
2. Respire com ritmo (inspira 4s, segura 4s, solta 4s, pausa 4s).  
3. Foque em uma microação: organizar sua mesa, tomar água, escrever o que sente.  

Você não precisa ter todas as respostas hoje. Só precisa de um ponto de apoio. E esse ponto pode ser agora.
"""

    elif message.text == "💖 Autoestima sem filtro":
        texto = """
*💖 AUTOESTIMA SEM FILTRO*  

Autoestima não é se achar perfeito — é saber se abraçar mesmo nos dias em que tudo parece errado.  

Tenta esse exercício:  
• Liste 3 coisas que você gosta em si (por dentro ou por fora)  
• Escreva uma carta pra si como se fosse pra uma pessoa que ama  
• Leia em voz alta.  
• Repita sempre que duvidar de si.  

Você é mais bonito quando se trata com amor.  
"""

    elif message.text == "📵 Desconecta, respira":
        texto = """
*📵 DESCONECTA, RESPIRA*  

A gente vive grudado na tela. Mas seu cérebro precisa de silêncio.  

→ Tire 5 minutos offline. Sem música, sem notificações.  
→ Respire. Alongue. Olhe pela janela.  
→ Coloque a mão no peito e sinta o coração. Ele tá contigo desde sempre.  

Digital detox é mais do que tendência — é um reencontro com a sua paz interior.
"""

    elif message.text == "🫂 Fazer novas amizades":
        texto = """
*🫂 FAZER NOVAS AMIZADES*  

A conexão humana cura. Mas começa com um simples “oi”.  

Se você tá lendo isso, o universo tá dizendo: se abre um pouquinho.  
• Manda uma mensagem no grupo.  
• Conta o que tá sentindo.  
• Responde alguém com carinho.  

Gente real precisa de conversas reais. E você pode ser o início disso pra alguém.
"""

    elif message.text == "💌 Conhecer alguém especial":
        texto = """
*💌 CONHECER ALGUÉM ESPECIAL*  

Antes de encontrar alguém especial, o mais importante é saber que você *já é* especial.  

→ Cuide da sua mente, do seu espaço, do seu tempo.  
→ Se conecte com o que te faz bem.  

O amor saudável chega quando a gente tá em paz consigo. E quando chega, não traz dúvida — traz leveza.
"""

    elif message.text == "🧠 Autocuidado mental extra":
        texto = """
*🧠 AUTOCUIDADO MENTAL EXTRA*  

Quer algo a mais? Então bora de rituais rápidos que fortalecem a mente:  

• Diário da mente (escreve o que tá sentindo, sem filtro)  
• Lista de gratidão (mesmo que só com uma coisa)  
• Ritual de presença: água gelada no rosto, respiração lenta e mantra tipo: “Eu tô aqui. Eu tô bem.”  

Autocuidado é escutar o corpo e a alma com atenção.
"""

    elif message.text == "🎧 Me acalmar com música":
        texto = """
*🎧 ME ACALMAR COM MÚSICA*  

A música certa acalma a alma. Então dá o play em uma dessas vibes:  

→ Sons da natureza  
→ Lofi pra relaxar  
→ Mantras ou instrumentos de piano  
→ White noise (barulho de chuva, por exemplo)  

Coloca o fone, deita um pouco ou só fecha os olhos.  
Deixa a música limpar o que a ansiedade bagunçou.
"""

    elif message.text == "✨ O Guia do Carisma":
        texto = """
*✨ O GUIA DO CARISMA*  

Carisma não é sobre falar bonito. É sobre presença, escuta e energia.  

Dicas que funcionam:  
• Olhe nos olhos (sem forçar)  
• Ouça mais do que fala  
• Sorria com verdade  
• Use o nome da pessoa nas conversas  
• Faça perguntas com interesse real  

E o principal: *goste de quem você é*. Quem se gosta, transborda. E isso é o que atrai.
"""

    elif message.text == "📰 Fique por dentro das notícias":
        texto = """
*📰 NOTÍCIAS E ATUALIZAÇÕES*  

Quer receber conteúdos novos, desafios semanais e aulas especiais?

→ Entre no nosso grupo oficial:  
[clica aqui!](https://t.me/guiadamente)  

Lá você vai ficar por dentro das novidades, conversar com outros agentes da mente e crescer junto com a gente.
"""

    if texto:
        bot.send_message(message.chat.id, texto, parse_mode="Markdown", disable_web_page_preview=True)

@bot.message_handler(commands=['menu'])
def mostrar_menu(message):
    texto = """
📋 *Menu Principal do Bot - Guia da Mente e do Coração*

Aqui está tudo o que você pode explorar com apenas um toque:

🧘 *Respira, calma*  
→ Aula de respiração consciente para baixar a ansiedade.

🎯 *Foco turbo*  
→ Técnica Pomodoro e dicas pra manter a mente no jogo.

🌪️ *Lidando com o caos*  
→ Aula de concentração e como manter o foco mesmo nos dias difíceis.

💖 *Autoestima sem filtro*  
→ Exercício de amor-próprio e como se acolher.

📵 *Desconecta, respira*  
→ Pausas digitais saudáveis para o bem-estar.

🫂 *Fazer novas amizades*  
→ Dica: se conecta no grupo e conheça outros agentes da mente.

💌 *Conhecer alguém especial*  
→ Um lembrete: quem se cuida atrai o que é leve.

🧠 *Autocuidado mental extra*  
→ Em breve: novos conteúdos personalizados.

🎧 *Me acalmar com música*  
→ Aula com som relaxante para momentos de paz.

📰 *Fique por dentro das notícias*  
→ Entre no grupo oficial: [clique aqui](https://t.me/guiadamente)

Cada aula que você conclui te dá +1 nível e mostra ao grupo sua evolução!

Use o comando /nivel para ver seu nível atual.
"""
    bot.send_message(message.chat.id, texto, parse_mode="Markdown", disable_web_page_preview=True)
    
    
@bot.message_handler(commands=['start'])
def boas_vindas(msg):
    chat_id = msg.chat.id  # ID do usuário que usou o comando
    nome = msg.from_user.first_name

    bot.send_message(chat_id, f"Olá, {nome}! Este bot foi feito pra você.")
    sp(1)
    bot.send_message(chat_id, "O Guia da Mente é um mapa rápido pra quem vive na correria, sente o cérebro fritando, ou só quer melhorar o foco e viver mais leve.")
    sp(1)
    bot.send_message(chat_id, "O que temos por aqui?")
    bot.send_message(chat_id, "/comecar - bora começar? \n/menu - fique por dentro dos nossos guias!")

    # Envia mensagem no grupo também
    bot.send_message(grp, f"Novo agente conectado: {nome} acabou de iniciar o bot!")

bot.polling()
