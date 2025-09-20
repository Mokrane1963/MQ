
"""
Created on Wed Nov 22 14:03:33 2023

@author: home
"""

#import pyttsx3
import nltk
from nltk.chat.util import Chat, reflections
import pyttsx3
from tkinter import *
nltk.download('punkt')

class MyChat(Chat):
    def __init__(self, pairs, reflections=None):
        super().__init__(pairs, reflections)
        self.responses = []

    def respond(self, str):
        response = super().respond(str)
        self.responses.append(response)
        return response

def initialiser_moteur(voix_id="com.apple.speech.synthesis.voice.Mathieu", taux_parole=150):
    engine = pyttsx3.init()
    engine.setProperty('voice', voix_id)
    engine.setProperty('rate', taux_parole)
    return engine

def parler(engine, texte):
    engine.say(texte)
    engine.runAndWait()

# Paires de questions et réponses

pairs = [
    
  
    ['Tassa|temlal|turew', ["Temlal tasa d way turew."]],
   ['Comment ça va?', ['Ça va bien, merci!', 'Je suis un programme, donc je n\'ai pas de sentiments, mais merci de demander.']],
   ['Quel est ton langage de programmation préféré?', ['Je suis programmé en Python.', 'Python est mon langage de prédilection.']],
   ['Parle-moi de toi', ['Je suis un chatbot créé avec NLTK.', 'Je suis conçu pour répondre à des questions et engager des conversations.']],
   ['Qui est ton créateur?', ['Je suis créé par OpenAI.', 'Mon créateur est OpenAI, une entreprise de recherche en intelligence artificielle.']],
   ["Quel temps fait-il aujourd'hui?", ["Je ne peux pas fournir d'informations en temps réel."]],
   ["Que penses-tu de l'intelligence artificielle?", ["En tant que programme, je n'ai pas d'opinions. L'intelligence artificielle est un domaine passionnant."]],
   ['Quels sont tes hobbies?', ["Je n'ai pas de hobbies, mais j'aime aider les utilisateurs."]],
   ['Peux-tu me donner des conseils pour apprendre la programmation?', ['Pratiquez régulièrement, suivez des tutoriels, et n\'ayez pas peur de faire des erreurs.']],
   ["au revoir|bye|à bientot|ar tufath",["Au revoir! Si vous avez d'autres questions à l'avenir, n'hésitez pas à demander. Passez une excellente journée" ]],
   ["Merci|tanemirt",["De rien ! Si vous avez besoin d'aide à l'avenir, n'hésitez pas à revenir. Bonne journée !"]],
   ["c'est qui matoub?",["Matoub lounès était un chanteur, poète et musicien algérien, né le 24 janvier 1956 à Taourirt Moussa (Tizi Ouzou) et assassiné le 25 juin 1998. Il est particulièrement connu pour son engagement en faveur de la culture et de la langue berbères, ainsi que pour ses chansons engagées abordant des thèmes sociaux, politiques et culturels."]],
    
    ["ixxamen|medden",["Ixxamen n medden weɛren, ma ur nɣin ad sdeɛfen."]],
    ["tagmat|hamlagh|karhagh|tagmat", ["Ur hemmler gma ur hemmler wara at-yewten."]],
    ['aqrur|dderya|nger|darya', ["W'ur nuriw yugad nnger, win yurwen yeṛwa amdegger."]],
    ["tassusmi|tamusni",["Tasusmi d dwa n tmusni."]],
    ["awal",["Awal am uskfel n wezru  mi tekksed yiwen, ad d-yeɣli wayeḍ"]],
    ["Senned|itkel",["Senndeɣ fell-as, Yeɣli-d fell-i"]],
    ["isugut|awal",["Kra n win yesuguten awal, ala tikarkas i deg yetnawal."]], 
    ["tufaza|llazuq",["Dacu t-teffezid a εemmi? d llazuq n yilindi."]],
    ["yiwen|yamar|suq|ulzuz",["Yiwen warab yamar ulzuz."]],
    ["imi|tasusmi",["Tasusmi d zyen n yimi"]],
    ["aqqarru|iles",["Iles yetthawalitent aqarru yettaɣitent"]],
    ["lqella|argaz",["D lqella n yirgazen i k-yerran, a bu t-xutam d-argaz"]],
    
     
     ["tidet|lekdeb",["Axir tidet yesseqrahen, wala lekdeb yessefrahen"]],
     ["snat|yiwet",["A vu snat, bru i yiwet."]],
     ["asif|zger",["Oulach win izegren assif ur yelxis(yebzig)"]],
     
     ["abbagh",["n.m. (crâne, calotte crânienne); syn. a qecrur"]],
     ["iwzi|iwzan",[" n.m. (grain de semoule, de céréale concassée); pl. iwzan."]],
     
     ["a|A",["adj.dém. (ce, cette); var. agi, agini; a rgaz agi, a rgaz a (cet homme)  article masc.sing. de l’état libre (un, le); a rgaz (un homme, l’homme) . exclam. (ô, hé!); var. ay, devant une voyelle. a t’arwa (ô mes enfants); ay a qcic (hé,garçon!) var. réduite de l’indice du futur ad, employée devant un v. à la première personne du pluriel, les pron.pers., les part. locatives idd et in, la particule de négation   wer; aneddu (nous irons, nous partirons); a-t awin (ils l’emmèneront); a-dd yas (il viendra); a-wer yerebeh’ (puisse-t-il ne pas prospérer) "     ]],
     
     ["     ",["      "     ]],
     
     ["     ",["      "     ]],
     
     ["     ",["      "     ]],
     
     
     
     
    ]


# Créer un objet MyChat avec la liste de paires
chatbot = MyChat(pairs, reflections)

# Initialiser le moteur de synthèse vocale en dehors de la boucle
engine = initialiser_moteur(voix_id="com.apple.speech.synthesis.voice.mathieu", taux_parole=150)

# Exécutez la conversation et stockez les réponses dans une variable
historique = []

# Créer une fenêtre Tkinter pour l'interface graphique
fenetre = Tk()
fenetre.title("Chatbot  Citations berberes Hachemi mokrane 2023")

def effacer_contenu_entry():
    entry.delete(0, 'end')

# Ajouter un bouton "Effacer"
bouton_effacer = Button(fenetre, text="Effacer", command=effacer_contenu_entry)
bouton_effacer.grid(row=1, column=5, pady=10)

# Ajouter des champs et un bouton
entry_label = Label(fenetre, text="Mokrane:")
entry_label.grid(row=1, column=0, pady=5)

entry = Entry(fenetre)
entry.grid(row=1, column=1, pady=5)

resultat_label = Label(fenetre, text="")
resultat_label.grid(row=2, column=0, columnspan=2, pady=10)

# Fonction pour mettre à jour l'affichage lorsque le bouton est cliqué
def mettre_a_jour():
    user_input = entry.get()
    response = chatbot.respond(user_input)
    historique.append((user_input, response))
    fenetre.update_idletasks()
    print(f"Chatbot: {response}")
    parler(engine, f"{user_input}")
    parler(engine, f"{response}")
    resultat_label.config(text=response)

# Ajouter un bouton pour envoyer la question
bouton_envoyer = Button(fenetre, text="Envoyer", command=mettre_a_jour)
bouton_envoyer.grid(row=3, column=0, columnspan=2, pady=10)

# Lancer la boucle principale Tkinter
fenetre.mainloop()

print("Historique:")
for entry in historique:
    print(f"{entry[0]} - {entry[1]}")
