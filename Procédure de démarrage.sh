 Procédure de démarrage                                                                                      
                                                            
  Terminal 1 — Serveur (réseau local / 2 ordis)                                                               
   
  cd ~/Developer/projet_olivia                                                                                
  ./start_all.sh                                                                                              
  
  ▎ La première fois, LibreTranslate va télécharger les modèles pour les 12 nouvelles langues — ça peut       
  ▎ prendre quelques minutes.                               
                                                                                                              
  ---                                                       
  Terminal 1 — Serveur (internet via Ngrok)
                                                                                                              
  cd ~/Developer/projet_olivia
  ./start_ngrok.sh                                                                                            
  Puis dans un Terminal 2 :                                 
  ngrok http 8000                                                                                             
  Partage l'URL https://xxxx.ngrok-free.app avec l'autre personne.
                                                                                                              
  ---                                                                                                         
  Test
                                                                                                              
  1. Ouvre https://localhost:8000 (réseau local) ou l'URL ngrok
  2. Entre ton prénom + choix de langue → Rejoindre                                                           
  3. L'autre personne fait pareil sur son appareil
  4. Vous vous voyez dans le header — parlez !        