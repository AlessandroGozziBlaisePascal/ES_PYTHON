#Il flusso locale di Git si basa su tre aree principali: il working tree è praticamente la cartella del progetto in cui modifico i file sul momento, la staging area è una sorta di 
# "zona di preparazione" dove scelgo cosa voglio salvare, e il repository è lo storico definitivo del progetto. 
# Quando lancio git add, sposto le modifiche dal working tree alla staging area per prepararle, mentre con git commit le confermo e le salvo in modo permanente dentro il repository.

#La differenza sostanziale è che git fetch scarica soltanto gli aggiornamenti dal repository remoto per farmi vedere cosa è cambiato, ma senza toccare i miei file locali; 
# invece, git merge prende le modifiche di un altro branch e le fonde direttamente nel branch su cui sto lavorando. Per quanto riguarda git stash, lo uso quando ho delle modifiche a metà 
# che non sono ancora pronte per un commit, ma ho bisogno di cambiare branch al volo o fare altro: lo stash me le mette temporaneamente "nel cassetto", pulisce la cartella di lavoro e mi permette di 
# riprenderle più tardi.

#Quando si lavora in team su GitHub, tutto parte dall'apertura di una Issue per segnalare un bug o proporre una nuova funzione. Per non fare danni sul codice principale, si crea un branch dedicato dove lavorare in isolamento, 
# salvando man mano i progressi con vari commit e caricandoli poi online tramite push. A quel punto si apre una Pull Request per chiedere di unire il proprio lavoro al branch principale: 
# i compagni di team fanno una review per controllare il codice e, se è tutto ok, si fa il merge finale che integra le modifiche e chiude l'issue.

class Sensore:
    def __init__(self, codice: str, grandezza: str, unita: str, soglia_massima: float) -> None:
        self.codice = codice
        self.grandezza = grandezza
        self.unita = unita
        self.soglia_massima = soglia_massima