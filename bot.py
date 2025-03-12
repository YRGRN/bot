import random
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# 🔹 Token del bot (inserisci il tuo token qui)
TOKEN = "7421925840:AAEfxIYYA1rO8rfG8sCYh2OCzYtFDiyaElw"

# 🔹 Funzione per leggere le frasi da un file di testo
def leggi_frasi(percorsi="frasi.txt"):
    try:
        with open(percorsi, "r", encoding="utf-8") as file:
            return [riga.strip() for riga in file.readlines() if riga.strip()]
    except FileNotFoundError:
        return ["Errore: il file frasi.txt non è stato trovato."]

# 🔹 Funzione che risponde al comando /estrai
async def estrai(update: Update, context: CallbackContext) -> None:
    frasi = leggi_frasi()
    frase = random.choice(frasi)
    await update.message.reply_text(frase)

# 🔹 Impostazione del bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Aggiungiamo il comando /estrai
    app.add_handler(CommandHandler("estrai", estrai))

    # Avvia il bot
    print("Bot avviato! Premi CTRL+C per fermarlo.")
    app.run_polling()

if __name__ == "__main__":
    main()