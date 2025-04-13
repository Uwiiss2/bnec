import telebot
from time import sleep as sp
from telebot import TeleBot, types
import random
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
    if message.text == "🧘 Respira, calma":
        opcoes = [
        """
*🧘 RESPIRA, CALMA*  

Respirar pode parecer básico, mas quando feito com intenção, vira um superpoder. A mente da Geração Z vive no modo turbo, e essa é a pausa que você tava precisando.  

A técnica 4-7-8 é seu botão de reset:  
→ Inspire por 4 segundos  
→ Segure por 7  
→ Solte lentamente por 8 segundos  
Repita 4 vezes e sente a paz te abraçando.  

Dica extra: feche os olhos, coloque uma música instrumental e respire com o som. É mágico.
""",
        """
*🧘 PAUSA CONSCIENTE*  

Feche os olhos por 10 segundos. Respire fundo e solte bem devagar.  
Agora imagine que você tá num lugar tranquilo, onde nada te apressa.  

A ansiedade não manda em você. Quem manda é sua respiração.
""",
        """
*🧘 REINICIANDO A MENTE*  

Use a técnica 4-7-8 para resetar o corpo:  
• Inspire por 4s  
• Segure 7s  
• Solte por 8s  

Repita até o peito se acalmar. A respiração é seu botão secreto de reset.
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "🎯 Foco turbo":
        opcoes = [
        """
*🎯 FOCO TURBO*  

Focar em um mundo de distrações é tipo ser um herói moderno.  
A técnica Pomodoro te dá uma espada invisível:  
→ 25 minutos de pura atenção  
→ 5 minutos de respiro

Crie uma lista de tarefas, coloque uma playlist de concentração e foque numa coisa por vez.  
Depois de 4 ciclos: pausa maior (15 a 30 min).

> Foco não é rigidez. É escolher com carinho o que merece sua energia.
""",
        """
*🎯 FOCO É RESPEITAR SUA ENERGIA*  

Você não precisa ser produtivo o tempo todo.  
Mas quando decidir focar, faça isso por você.

• Tire distrações do caminho  
• Escolha uma única tarefa  
• Respire antes de começar

Foco não é fazer mais, é fazer melhor.
""",
        """
*🎯 FOCO NA REAL*  

Foco não é sobre “trabalhar até cair”.  
É sobre estar inteiro no que você escolheu fazer agora.

Use o tempo como aliado.  
→ 25 minutos focado  
→ 5 minutos de cuidado  

> Você não é máquina. Mas pode criar seu próprio ritmo de potência.
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "🌪️ Lidando com o caos":
        opcoes = [
        """
*🌪️ ORGANIZANDO O CAOS*  

Nem tudo precisa ser resolvido hoje.  
Às vezes, só de respirar e listar o que está nas suas mãos, metade da ansiedade já se dissolve.

1. Inspire fundo  
2. Escreva 3 coisas que você pode fazer agora  
3. Escolha uma pra focar  

> Um passo de cada vez ainda é movimento.
""",
        """
*🌪️ CALMA NO OLHO DO FURACÃO*  

Mesmo com tudo rodando ao redor, você pode criar um centro de paz.

Use a Respiração da Caixinha:  
→ Inspire 4s  
→ Segure 4s  
→ Solte 4s  
→ Pausa 4s  

Repita. Se precisar, de novo. E mais uma vez.
""",
        """
*🌪️ QUANDO NADA FAZ SENTIDO*  

Pega um papel e uma caneta.  
Escreve tudo que te incomoda, sem filtro.  
Jogue fora, queime ou só rasgue.

Desabafar também é liberar memória RAM da mente.
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "💖 Autoestima sem filtro":
        opcoes = [
        """
*💖 AUTOESTIMA É ACOLHIMENTO*  

Autoestima não é se sentir incrível todos os dias.  
É saber se tratar com respeito mesmo quando a mente sabota.

→ Fale com você como falaria com um amigo que ama.  
→ Reconheça um elogio sem se envergonhar.  
→ Se permita errar sem se odiar por isso.
""",
        """
*💖 SE OLHA COM MAIS GENTILEZA*  

Você é muito mais do que pensa.  
O problema é que a mente só destaca defeitos.

→ Liste 3 coisas que você já superou  
→ Lembre-se: não é aparência, é presença  
→ Cuide de você como quem cultiva uma flor rara
""",
        """
*💖 A BELEZA DE SER REAL*  

Não precisa caber num filtro.  
Não precisa agradar todo mundo.  
Sua versão mais valiosa é a verdadeira.

Autoestima começa no “eu sou suficiente, mesmo com falhas”.
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "📵 Desconecta, respira":
        opcoes = [
        """
*📵 DESLIGA PRA CONECTAR COM VOCÊ*  

5 minutos sem tela. Só isso.  
Sente. Respira. Repara no que está ao redor.  
O mundo digital é barulhento, mas sua alma pede silêncio.

→ Você não precisa responder tudo agora.
""",
        """
*📵 PAUSA DIGITAL = PRESENÇA MENTAL*  

A cada notificação, sua atenção se parte em pedacinhos.  
Hoje, tente:  
→ Deixar o celular no modo avião por 10 min  
→ Fazer algo analógico (escrever, desenhar, olhar o céu)

Você vai ver o quanto sua mente agradece.
""",
        """
*📵 UM TEMPO PRA RESPIRAR*  

Seu tempo não é renovável.  
Gastar tudo em rolagem infinita deixa a mente cansada.

→ Se afasta da tela  
→ Bebe água  
→ Faz 3 respirações profundas

Só isso já muda seu dia.
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "🫂 Fazer novas amizades":
        opcoes = [
        """
*🫂 SE ABRIR É A PONTE*  

Todo mundo sente medo de parecer estranho. Mas a verdade é: todo mundo quer ser notado.

→ Envie um “oi” no grupo  
→ Responda alguém com empatia  
→ Mostre quem você é com leveza

> Gente boa atrai gente boa.
""",
        """
*🫂 CONVERSAS CURAM*  

Quando você compartilha, você liberta.  
E quando você escuta, você acolhe.

→ Conexões profundas começam com escuta leve  
→ Não precisa impressionar, só estar presente

> No fim, todo mundo quer ser ouvido com atenção.
""",
        """
*🫂 SEJA A MÃO QUE SE ESTENDE*  

Talvez alguém no grupo esteja esperando exatamente por alguém como você.

→ Inicie uma conversa real  
→ Pergunte: “como você tá hoje?”  
→ Fale algo que te marcou no dia

O que você cria com presença, vira laço.
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "💌 Conhecer alguém especial":
        opcoes = [
        """
*💌 TUDO COMEÇA EM VOCÊ*  

Quem se cuida, se atrai. Cultive sua vibe. O resto vem.

→ Se conheça antes de querer alguém  
→ Crie uma energia que você mesmo goste de sentir  
→ O que é leve, chega naturalmente
""",
        """
*💌 LEVEZA NO AMOR*  

Antes de amar alguém, esteja leve com você mesmo. O resto acontece.

→ Amor saudável não sufoca  
→ Relacionamento bom soma, não te puxa pra baixo  
→ Se for real, vai fluir
""",
        """
*💌 AMOR NÃO SE FORÇA*  

Respira. Seja você. O que é real encontra um jeito de chegar.

→ Você não precisa correr atrás de quem não quer ficar  
→ Quando você se ama, atrai amor do bom  
→ Leveza primeiro. Paixão depois.
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "🧠 Autocuidado mental extra":
        opcoes = [
        """
*🧠 RITUAL MENTAL*  

Escreva como se sente. Beba água. Respire fundo.  
Coisas simples salvam dias inteiros.

→ Autocuidado é parar de ignorar sua voz interior  
→ Escute seu cansaço sem culpa
""",
        """
*🧠 PRESENÇA*  

Feche os olhos. Respire 5x com intenção.  
Toque no seu próprio peito. Você está aqui. Agora.

→ O futuro pode esperar. Sua paz é agora  
→ Respiração é âncora, não remendo
""",
        """
*🧠 UM MOMENTO PRA VOCÊ*  

O mundo pode esperar 10 minutos. Você não.  
Cuide do seu agora. Ele é tudo que existe.

→ Tome um banho com atenção  
→ Faça uma caminhada em silêncio  
→ Cuide de você como quem rega uma planta rara
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "🎧 Me acalmar com música":
        opcoes = [
        """
*🎧 PAZ EM NOTAS*  

Lofi, sons da natureza ou piano. Dê play e respire com a batida.

→ Escolha uma playlist calma  
→ Deite ou sente confortavelmente  
→ Respire com o som

Você não precisa entender, só sentir.
""",
        """
*🎧 CALMA EM FORMA DE SOM*  

Feche os olhos. Escolha uma música tranquila.  
Se entregue ao som, sem pensar em nada.

→ Sons guiam a mente pra fora do caos  
→ Ouvir também é cuidar
""",
        """
*🎧 SUA TRILHA DE PAZ*  

Fones, música suave, respiração lenta.  
Isso é autocuidado sonoro.

→ Crie sua própria playlist de cura  
→ Use sempre que o mundo parecer demais  
→ Música toca onde as palavras não alcançam
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "✨ O Guia do Carisma":
        opcoes = [
        """
*✨ CARISMA É ENERGIA*  

Presença, escuta, sorriso sincero. O segredo tá nos detalhes. Seja real.

→ Olhe nos olhos  
→ Chame pelo nome  
→ Demonstre interesse real

Você não precisa forçar. Quem brilha de verdade não grita, só aparece.
""",
        """
*✨ GENTE QUE BRILHA*  

Quem se gosta, transborda. Trabalhe seu brilho interno. Isso é magnético.

→ Cuide da sua energia antes de entrar em um lugar  
→ Escute com o coração  
→ Faça perguntas que abrem sorrisos

Carisma é empatia em movimento.
""",
        """
*✨ IMPACTO SEM FORÇAR*  

Carisma é fazer o outro se sentir bem.

→ Dê atenção sincera  
→ Use o humor como ponte, não como escudo  
→ Mostre quem você é com tranquilidade

As pessoas lembram de como você as fez sentir.
"""
    ]
        texto = random.choice(opcoes)

    elif message.text == "📰 Fique por dentro das notícias":
        opcoes = [
        """
*📰 ENTRE NO NOSSO GRUPO*  

@guiadamente — conteúdo novo, desafios, conversas, acolhimento.  
Vem com a gente e fortalece tua mente com a [galera certa](https://t.me/guiadamente).
""",
        """
*📰 GRUPO OFICIAL*  

Quer crescer com outros agentes da mente?  
Aqui rolam dicas diárias, desafios semanais e apoio de verdade:  
Nossa [página oficial](https://t.me/guiadamente)
""",
        """
*📰 CONTEÚDO EXCLUSIVO*  

Quer saber de tudo em primeira mão?  
→ [Clique aqui](https://t.me/guiadamente) 
→ Receba desafios, novidades e aulas especiais direto no grupo!
"""
    ]
        texto = random.choice(opcoes)

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