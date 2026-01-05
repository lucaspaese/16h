import streamlit as st
from datetime import datetime

st.title("Vérification de l'heure")


now = datetime.now()
hour = now.hour
weekday = now.weekday()   # lundi = 0 ... dimanche = 6

# --- Partie 1 : Vérifier 16h ---
if hour >= 15:
    st.write("🕓 C'est déjà 16 heures !")
else:
    st.write("⏳ Ce n'est pas encore 16 heures.")

st.write("---")

# --- Partie 2 : Vérifier si c'est vendredi ---
if weekday == 4:  # 4 = vendredi
    st.write("🎉 C'est vendredi !")
    
    # Sous-condition : vérifier midi
    if hour >= 11:
        st.write("🍽️ C'est déjà midi !")
    else:
        st.write("⏳ Ce n'est pas encore midi.")

st.write("---")

st.markdown("Savoir s’il est déjà 16 h revêt une importance particulière dans le cadre de la journée de travail. Cette heure symbolise un seuil, celui où les obligations professionnelles commencent à laisser place au temps personnel. Elle permet de prendre conscience du temps écoulé, d’évaluer l’avancement des tâches en cours et d’anticiper la fin de la journée. Être attentif à l’heure facilite également une meilleure organisation. À l’approche de 16 h, il devient possible de prioriser les actions restantes, de clôturer les dossiers importants et de préparer une transition sereine entre le travail et le retour à la maison. Cela contribue à limiter les imprévus de dernière minute et à éviter le stress lié à une mauvaise gestion du temps.Par ailleurs, connaître précisément l’heure est essentiel pour respecter ses engagements personnels. Le départ du travail conditionne souvent les horaires de transport, les responsabilités familiales ou simplement le besoin légitime de repos. Savoir qu’il est déjà 16 h permet donc de planifier son trajet, d’optimiser son temps de déplacement et de préserver un équilibre sain entre vie professionnelle et vie privée. Enfin, cette attention portée à l’heure traduit une reconnaissance de la valeur du temps. Elle rappelle que le travail, aussi important soit-il, s’inscrit dans une journée plus large où le bien-être personnel a toute sa place. Ainsi, savoir s’il est déjà 16 h n’est pas un simple détail, mais un repère essentiel pour mieux vivre sa journée et rentrer chez soi dans de bonnes conditions.")

