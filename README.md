<p align="center">
    <a href="" rel="noopener">
    <img width=200px height=200px src="https://i.imgur.com/XEtKsqS.png" alt="Project logo" style="border-radius: 15px"></a>
</p>

# 🎵 PyTune - Bot de Música para Discord

Um bot de música simples e eficiente para Discord que permite reproduzir músicas do YouTube em canais de voz.

## ✨ Funcionalidades

- 🎶 Reproduzir músicas do YouTube
- ⏸️ Pausar e retomar reprodução
- ⏭️ Pular músicas
- 🛑 Parar reprodução e desconectar
- 📋 Sistema de fila de músicas
- 🗑️ Limpar fila de reprodução
- ⏱️ Desconexão automática após 3 minutos de inatividade
- 📝 Sistema de logs para monitoramento

## 🚀 Comandos

| Comando | Aliases | Descrição |
|---------|---------|-----------|
| `!play <url/termo>` | `!p` | Toca uma música do YouTube |
| `!pause` | - | Pausa a música atual |
| `!resume` | - | Retoma a música pausada |
| `!skip` | - | Pula para a próxima música |
| `!stop` | - | Para a reprodução e desconecta |
| `!queue` | - | Mostra a fila atual |
| `!clear` | - | Limpa a fila de reprodução |

## 📋 Pré-requisitos

- Python 3.8+
- FFmpeg instalado no sistema
- Token de bot do Discord
- Acesso à API do Discord

## 🛠️ Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/jvfonseca1/PyTune
cd PyTune
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Configure as variáveis de ambiente:**
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione seu token do Discord:
```env
DISCORD_TOKEN=seu_token_aqui
```

4. **Opcional: Configure cookies para vídeos restritos:**
   - Crie um arquivo `cookies.txt` na raiz do projeto com cookies do YouTube
   - Isso permite acessar vídeos com restrição de idade ou conteúdo privado

5. **Execute o bot:**
```bash
python main.py
```

## ⚙️ Configuração do Bot Discord

1. Acesse o [Discord Developer Portal](https://discord.com/developers/applications)
2. Crie uma nova aplicação
3. Vá para a seção "Bot" e crie um bot
4. Copie o token e adicione ao arquivo `.env`
5. Em "OAuth2 > URL Generator":
   - Selecione "bot" em Scopes
   - Selecione as permissões necessárias:
     - Connect
     - Speak
     - Use Voice Activity
     - Send Messages
     - Read Message History

## 📦 Dependências Principais

- `discord.py` - Biblioteca para interação com Discord
- `yt-dlp` - Download e extração de áudio do YouTube
- `python-dotenv` - Gerenciamento de variáveis de ambiente
- `logging` - Sistema de logs para monitoramento

## 🏗️ Estrutura do Projeto

```
PyTune/
├── commands/              # Comandos do bot
│   ├── play.py            # Comando de reprodução
│   ├── pause.py           # Comando de pausa
│   ├── resume.py          # Comando de retomar
│   ├── skip.py            # Comando de pular
│   ├── stop.py            # Comando de parar
│   ├── queue.py           # Comando de fila
│   └── clear.py           # Comando de limpar fila
├── utils/                 # Utilitários
│   ├── audio_handler.py   # Manipulação de áudio
│   └── logger.py          # Sistema de logs
├── main.py                # Arquivo principal
├── requirements.txt       # Dependências
├── cookies.txt            # Cookies para autenticação no YouTube (opcional)
├── .env                   # Variáveis de ambiente
└── .gitignore             # Arquivos ignorados pelo Git
```

## 🎯 Como Usar

1. Convide o bot para seu servidor Discord
2. Entre em um canal de voz
3. Use `!play <URL do YouTube>`
4. Controle a reprodução com os comandos disponíveis

### Exemplos:
```
!play https://www.youtube.com/watch?v=dQw4w9WgXcQ
!pause
!resume
!skip
!queue
!stop
```

## 🔧 Solução de Problemas

### FFmpeg não encontrado
- **Windows:** Baixe o FFmpeg e adicione ao PATH do sistema
- **Linux:** `sudo apt install ffmpeg`
- **macOS:** `brew install ffmpeg`

### Bot não conecta ao canal de voz
- Verifique se o bot tem permissões para conectar e falar no canal
- Certifique-se de estar em um canal de voz antes de usar comandos

### Problemas com vídeos restritos do YouTube
- Alguns vídeos podem exigir autenticação
- Crie um arquivo `cookies.txt` na raiz do projeto com cookies do YouTube para acessar conteúdo restrito

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 🎉 Agradecimentos
Agradeço em especial [@helpmeagain](https://github.com/helpmeagain) e [@Coriast](https://github.com/Coriast) pela motivação e ajuda futura. 
>"O duvido já moveu montanhas maiores."

## ⚠️ Aviso Legal

Este bot é apenas para uso educacional e pessoal. Respeite os termos de serviço do YouTube e do Discord ao usar este bot.