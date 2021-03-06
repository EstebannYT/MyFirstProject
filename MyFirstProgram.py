import winsound
import os
import time

def playSound(sound):
    winsound.PlaySound(sound, winsound.SND_FILENAME)

def printEgg():
    time.sleep(1)
    print('Egg?')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('''
                               +++++==++++++++++++                              
                           ?+++++++++=++++++++++++++++                          
                         +++++++++++++++++++++++++++++++,                       
                      ~+++++++++++++++++++++++++++++++++++?                     
                    ~==++++++++++++++++++++++++++++++++++++++                   
                   =+++++++++++++++++++++++++++++++++++++++++=                  
                 ~=++++++++++++++++++++++++++++++++++++++++=+?II                
                ++++++++++++++++++++++++++++++++++++++++++?I77777               
               +++++++++++++++++++++++++++++++++++++++++I777777777+             
             ++++++++++++++++++++++++++++++++++++++++?77777777777777            
            +++++++++++++++++++++++++++++++++++++??I77777777777777777           
           +++++++++++++++++++++++++++++++++++?I7777777777777777777777          
          ,=+++++++++++++++++++++++++++++?I7777777777777777777777777777         
          ~=++++++++++++++++++++++++++++II77777777777777777777777777777+        
         ++++++++++++++++++++++++++++++?I7777777777777777777777777777777        
        +++++++++++++++++++++++++++++++I777777777777777777777777777777777       
       ++++++++++++++++++++++++++++++++I777777777777777777777777777777777       
       ++++++++++++++++++++++++++++++++?7777777777777777777777777777777777      
      ++++++++++++++++++++++++++++++++?I77777777777777777777777777777777777     
      +++++++++++++++++++++++++++++++++?II777777777777777777777777777777777=    
     +++++++++++++++++++++++++++++++++++???IIII77777777777777777777777777777    
     :=++++++++++++++++++++++++++++++++++?????II7777777777777777777777777777:   
    :=++++++++++++++++++++++++++++++++++++++????I7IIII?III77777777 7 77 77777   
    ++++???????++++++++++++++=+++=+=++++++++++==========+?II7777777777777777    
   ?????????????+=~~~~~:::::~~~~=====+++======~~~~~~~~==+II777777777777777777   
   ??????????+~::::::,:,:::::~~~~~====++======~=======++?I7777777777777777777   
   :=+????+=~::::~~==~~~::~~~~~~~~====+=+=============+?I777777777777777777777  
  :=====~~~~~===++++++=+=~~===========+++++++=======~~~~==+I7777777777777777777 
  ++++++++++++++??+++++=~~~~~~~~===+++++III?+===~~~~~~~~~?7777?777777777777777  
  ???????????????++=~~===~::,:~~~~=+++?I777I?=~~~~::,   ,,:~+777777777777777777 
  ?IIIIIIIII????+==++:       ,:~~~=+++?77777?==~=,,:~::~=+++=~~~=?7777777777777 
  IIIIIIIIII???++++:  ~,,  ,,,,~===+++I77777I?+=~=======+II77777777777777777777 
  IIIIIIIII????+=,  ,,:~~~~~~~~~===+++777777777++========+I77777777777777777777 
  IIIIIIII???+=~:~++++===~~~~~===+++??7777777777I++=====+++??I77777777777777777~
 :IIIIII?????+?????+===~~~~~====++++??7777777777777777I??IIII777777777777777777I
 :IIIIII?????????+++==+====+++++++++?I777777777777777777777777777777777777777777
 ,IIIIIIIIIII????+++++++++++?+??++++?I7777777777777II?III7I77777777777777777777?
  IIIIIIIIIIII???????????++++++++?????77777777777????????II77777777777777777777:
  IIIIIIIIIIII??????????++++++==?I?????7777777777+=+???????I7777777777777777777 
  IIIIIIIIIIII?????????+++++=~??????+++I7777777777~==++?????I777777777777777777 
  IIIIIIIIIIII?????????+++==~+I?????++++777+~=I777?~=++++????I77777777777777777 
  IIIIIIIIIII?????????++++=~~=?=:,,,++=+7~~,,,:=77~~=~=+++????I7777777777777777 
  IIIIIIIIIIII???????++++=~~==~~~~===========~~~~~==~~~~=+++???I77777777777777  
   IIIIIIIIIII????++++~==~~~====~~~==========++++====~~~~~++++??I7777777777777  
   IIIIIIIIIII????++++==~~~============~~~~~====++===~~~:::=+++??I777777777777  
   IIIII?II?????+++====~:~~==========~~~~~~~===++++++=~~:~::~=++??777777777777  
    IIIIIII????++++==~~::~~============~========++???+==~:::::~=+?77777777777   
    IIIII?????+++++=~~:::~==+++=====~~~~~~~~~~========++=~::::~=++I7777777777   
     III??????++++===~:,:~=+===~~~~==~~~~~~~~~~:~~:~:,,,,:::::~+++I777777777    
     III??????++++===~:,:~~~,,,~==~~~===~~++?++++??=~,,   ,,:~==+?I777777777    
      II???????+++===~::,,    ,~?????III?+II7=77=II~~, ,,,:::~+++?777777777     
      =?????????++++=~~:,,,,   :~I~I+~???:??I,,::~+=~~~==~~~~===+I777777777     
       IIIII?????++++==~:::~::,,,~:~:~:~~~~=+777777777??++======?I77777777      
        IIII????++++===~~~~=======+======??++I777777777??+++===+?I7777777       
         ?I?????+++++==~~~====+++++===========+I7777777777I?+++?I7777777        
          ?????+++++==~~~===+++++++====~~~~===+?7777777777777III7777777         
           ???++++++======+++++++++============+I777777777777777777777          
            ???++++++=====+++===++============++?I7777777777777777777           
             =++++++++++++++++=++++===========+?II777777777777777777            
               ++++++++++++++++++=+++=======+?I7777777777777777777              
                 ++?++++++++++++++++++++++++?II77777777777777777                
                   +++++++++++++++++++++++++?II777777777777777                  
                     ??++++?++++++++++++=++++?II777777777777                    
                        ++++++++++++++++===+++?I777777777                       
                            +++++++++=======+++?IIII7                           
                                  ,===========                                 ''')
    playSound('eggs.wav')
    time.sleep(1)

def printJoey():
    time.sleep(1)
    print('Joey?')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('\nWhere\'s my 7$?')
    time.sleep(1)
    print('''---------------------------------------------------
                Joey's Bank Account
                                                   
---------------------------------------------------''')
    time.sleep(1)
    print('''
                                Fortnite Dances
                                    -$400.00''')
    playSound('joey1.wav')
    print('''

                       Esteban's PS4 Controller
                                    -$20.00''')
    
    playSound('joey2.wav')
    print('''

                               Puyo Puyo Tetris
                                    +$13.00''')
    playSound('joey3.wav')
    print('''---------------------------------------------------
Total:
                                    -$999.99''')
    playSound('joey4.wav')

    time.sleep(1)
    
def printAbalone():
    time.sleep(1)
    print('Abalone?')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('''
                                ,=+=++++=~:,                                    
                            ,=?,=??+IIIIIIIII?=~                                
                       =~~=+?II~~II?~=~=III??I?=++=,                            
                   :,:=??==?IIIII?=+++?777II???+++~++,                          
                ~,,,~????IIIIII7I=?~+?=+IIIIII7I+=~=+??=                        
               ,?==+???IIIIII77?=:~===+~,,:=+II?+==+?II?~,                      
               ,+????IIII???+=,:,====~+++~::::=?+++IIIII: :                     
              ::+?????I??+~:,:=~=+++++++++=~~::~+++???II=~~~                    
            ~,,~??I????=~~~+,,=++++++++++??I??~~~~+?????IIII+                   
            :==+?????+=~~~?+~=+++++++++++?II777+=~~=?++??IIII~                  
          ,,,??I????+==~~=:~=++++++++++++II77777~:~~~+????III,,                 
          :,,~+I?++?=~~~~:==++++++++++++?II7777777:~~==??????  ::               
        ,+=II?I?++?=~~~~===+++++++++++++?II77777777~~===+????+==?               
        =~+II77?+?~~~::====+++++++++++++III777777777:~~~~+??+????+              
        ~~?I777?+=~~~I===+++++++++++++++III777777777777~==??++?II+,             
       ,:~?III??=~~~~=~=++++++++++++++++?II777777777   ====?+++?II=             
       ~, +III?+==~~:=~++++++++++++++++++??I77777777777~??==+==++,:=            
       :,,:??+++==~:=~=+++++++=++++++++++++===++I777777:~+===+=+?+~+            
      =~?????+++==~=~++++=~::::::::~==++======?I777777 7=~?+=+?++?=?,           
      ~=?+???++=====~+++=~==+++=~~=~===++=====+?7777777777I?=+?+++I?=           
      ,,++?II++===+=++++????+==:,,,~=+?77+=~:: ,~=?77777~,~===?+++=:+,          
     ,,,,:III+++~=~:+???I??+=~ ,,,,~=+I7 ?+~==+?77777777I::~==+??+= :+          
     ~+=+?II7++=~~~~?II??+~~??+~~~==++77 777I++??I7777777:~~==+???I+++          
     ~+=+IIII++=~~~~????????+++==+++++777  77777777777777=:~==+???II?+          
     ~~,~~+?I+++~~:==IIII???????++++??I7777I+???I7777777 7~~==+?++++++          
     ~~,,:~??+++=~~=I?III??????++==??++I7777?+???I777777 7~++=+??+++++,         
     ~=+===??+++====++III?????++=~=~~==+==~~~~=++?I77777I~~===++?++??+,         
     ~=+=+???+++=====~+III??+++~~======~==++=~~:=+?77777~=+I=+?+??+==+          
     :~~,,=+??++=====::II??++=~:~==========++?=~::=?I77?:~===+?+??+~:=          
     ~=+:~?III?++===~~:~=??++=~:~+=~~~~~~~~~~:~~::=+I777,~===????I?~~+          
      ~+:,=?III?+=~~~::+==++==~,,  +I?7III?+?,,,:~=?I777::==??????II??          
      ~=,,,?IIII+=~~:::=+~+++==:::,,:::~~=+I7I?+===?I77=,,==?????III?+          
      ~~:==IIIII??=~:,:~~++?++=~==+++=====?77777I?+?I7~:~~=??????=~=+:          
      :====+?II?=??=:,:=~~+++====++++======I777777777,,~==+??????:++:           
       ,~~~+~::=+?I?=:,==~:=~~+++++++======?I77777777~~===?????:,,?+            
        ~~~==,,=++II?+~===~~~~~+++++++===++I77777777~~===+??I???~:+~            
         +=~=:~~+?????++====~~:~+++++++++??777777777:~==++????????~             
          ~=I+??+=+??I?++====~::=++++++++??I777777:::~==??II=~=++?              
          ,~=I????I???????+====,,~+++++++??I7777?:~~===??II?:~=??~              
           :~+I+~:I?:::II???====::~+++++++?I77I::~~==+??+=+==????               
             ~+I?=:~~~?IIII???+==~:==+++++?II?,:~==?++?=,:+?III=                
             ==II+,,~+IIIIIIII??+=~~==++++?I??:~=+?I?=~:,=III?=                 
               =?7??=+=~+?+=IIII?++=~====++++~=???::::~+III?=~                  
               :=+77?+=:~?=,:+III??+=========+?:=+=~=?IIII+==                   
                 ~=?7II~~==~,,+II?~:?+~~~+I:,~+:=+IIIII+==~,                    
                  ,:+I7+=:==::++++:,~===:::~~=+IIII?+===:,                      
                     ~+7?~==~~=+??~:==+++??IIII?+===+=~                         
                       =++++++=~~=+?IIIIII??++=====~:                           
                          ,~++++==============~~                                
                               ::====+=====''')
    playSound('abalone.wav')
    time.sleep(1)


def endSession():
    time.sleep(1)
    print('Thomas?')
    time.sleep(1)
    thomas = '''                                             ,                                  
                                              ,,                                
                         ,   ,                                                  
                        ,,                            ,                         
                    , ,,:                               ,:                      
                   ,,,,                                                         
                 ,,,,                         ,,                                
                ,,,,           ,::::::::::::,,,,             ,                  
                ,,          ,,:~~==~====~~~~~::,,,           :,                 
               ,,,       :::~~~~=~========~~~~~:::::,,,       ,                 
              ,,       ,::~~===============~~~~~~~~~::,, ,    ,,,               
             ,,,     :,~~~=====================~~~~~~::::,,                     
             ::     :~==~=========================~~~~~~:::,                    
             ::   ,,~===========+===================~~~~~~:,                    
             ::   ,~~=========++++=================~~~=~~~::                    
             ::   :~~===========+++==================~~~~~::,                   
             ::  ,:~~================================~=~~~~:,,                  
            :~:   :~~===========+======================~~~~::,     ,            
            :~:  ,~~~===========+++====================~~~~~:,,    :            
           :~~,  :~~======+==+++++++====================~~~~~::                 
             ~:  :~~======++++++++++========++==+====~~~=~~~~~:                 
             ,~  ~~~~~~~~~::::~~~==++===+====~::,,:::~~~::~~:~:                 
              ~~,~~~~~===~~~:~~~~~=======+===~~~~~======~~~~~~:                 
               =,~=~~==========~~~~========================~~~~                 
               =:~=~~~~:::    :~~~~==========~=~,,,~~~~====~=~:                 
               ~:====~:,,~,   ,:,~~~========~~,=    ~, :~===~~~ ,               
               ~~======~~~~~,,=:,======++====,::,,,::~~~~~===~~                 
               =~===========~~~=======++======~~~~===========~~                 
               ~======================+=========~~~==========~~                 
               :=======+++====++======+========+=======++====~~                 
                ======++++++++=======+++==============+++=====:                 
                ====++++++++++=======================+++++====                  
                ~=====++++++++=~~~=========~~~+======++++===~~                  
                ,~=====+++++==~~====+++=+=============++++==~~                  
                 :=~===+++++=~~======++=+==+==~~=====++++====~                  
                  ~~===+++++===============~~===+=====+=+===~                   
                  ~~~=====+++++=~~~~~~~~~~~~~===============~                   
                  :~~~====++=======~======================~=~                   
                   ~~~~~===========~========================:                   
                    ~~~~=====~=~===========================~                    
                    ~~~~===~~~::::::::~~~~~::::,~:~=======~                     
                     ~~~~==~~~:::~:::::::~~~~::~==~=====~~                      
                      ::~===~~~:::~~~~~~~~~~:~~~~~====~=~:                      
                       ::~==~~~~~~~~~~~~~~~~========~~~~                        
                       ,:~~=~~~========~~==========~~~~                         
                         :~~=~~==================~~~~                           
                          ::~~~=================~~~:                            
                           ::~~~~===============~:~                             
                            ::~~~===========~~~~:                               
                              ,~:~~~=~~==~~~~~                                  
                                 ,:~~~,::,::,                                            
'''
    for i in thomas:
        print(i,  end = '')
        time.sleep(0.000000001)
        
    time.sleep(1.5)
    print('''                                             ,                                  
                                               ,                                
                         ,  ,   ,,  ,  , ,  ,, ,                                
                        ,, , ,,,,,,,,,,,,,,,,,,,,,,                             
                    , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                         
                   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                     
                 ,,,,,,,,,,,,,,,,,,,:::::::,,,,,,,,,,,,,,,,,,                   
                ,,,,,,,,,:,,::~~~~~~~=~~~~~:~::::,,,,,,,,,,,,,                  
                ,,,,,,,,,:::~~~~~~=====~~~~~~~::::::::,:,,,,,,                  
               ,,,,,,::::~===============~~~~~~~~~~:::::::,,,,,                 
              ,,::::::~~~=====================~~~~~~:::::::,,,,,,               
             ,,::::~~~~=============================~~~~~::::,,,,,              
             ::::::~=================================~~~~~::::::,,,             
             :::::~===========+++===++==================~~::::::::,,            
             :::::~~========+===++=+++=+==========+======~~::::::::,            
             :::~~~~==========+=++++++++++++=+====+=======~~:::::::             
             :::~~~~=======+=++++++++++++++++++++++=======~~~::::::             
            :~~~~~=======+++++++++++++++++++++++++++++======~~~:::,             
            :~~~~~=====+=++++++++++++++++++++++++++++++=====~~~:~:              
           :~~~~~======+++??+?+?+++++++++++???????++++++=====~~~~:              
             ~~~=====+++++??????????+??????????????+++++=====~~~~:              
             ,~====+++????I??????????????????????I?????++=====~~~:              
              ~===+++?????III?????????????????IIIIII????++++==~~~                               __               _                                   ___                     __          _          _        
               ==+++???II777III?????????????III7777II????+++====,        /\_/\___  _   _ _ __  / _\ ___  ___ ___(_) ___  _ __     /\  /\__ _ ___    / __\ ___  ___ _ __     /__\ __   __| | ___  __| |     
               ==++???II777777II????????????II777777II????+++===,        \_ _/ _ \| | | | '__| \ \ / _ \/ __/ __| |/ _ \| '_ \   / /_/ / _` / __|  /__\/// _ \/ _ \ '_ \   /_\| '_ \ / _` |/ _ \/ _` |       
               ~=++???II777777IIIII????????III777777I????++++==           / \ (_) | |_| | |    _\ \  __/\__ \__ \ | (_) | | | | / __  / (_| \__ \ / \/  \  __/  __/ | | | //__| | | | (_| |  __/ (_| |
               ~+++???II77777III?????????????III777II?????++===           \_/\___/ \__,_|_|    \__/\___||___/___/_|\___/|_| |_| \/ /_/ \__,_|___/ \_____/\___|\___|_| |_| \__/|_| |_|\__,_|\___|\__,_|       
               ===++????IIIIII?????????????????III??????++++==:                 
               ~==+++????I?????????+????????????????????++++==,                 
               :===++++????????++++++??????????????????++++===                  
                ====+++??????++++++++++?+++?????????+++++++==:                  
                ====+++++?++++++++++++++++++++??+++++++++++==,                  
                ~====+++++++++===++++++++++++++?++++++++++===,                  
                ,~===+++++++======++++++++++++++++++++++++===,                  
                 :~==++++++=====+===+++++++++++++===++++++==~,                  
                  ~=====+++++===+=============++++===+++====~                   
                  ~~====+++==+================++++==========:                   
                  :~~~===+===============+========+========~,                   
                   ~~~~====================================~                    
                    ~~~=======~==============~==~=========~:                    
                    ~~~===~~::::~~~~~~~~~~~~~~~~~~~======~,                     
                     ~~~===~~::::~~~~~~~~~~~~~~=========~:                      
                      ~~~===~~~:::~~~~~~~~~~~=======~~~~:                       
                       :~==~~~~~~~~~~~~~~~~========~~~~                         
                       ,:~==~~=======~============~~~:                          
                         :~~~~===================~~~:                           
                          :~~~~=================~~:                             
                           :~~~~~============~~~~:                              
                            ::~~~============~~:                                
                              ,::~~~=~~=~~~~~:                                  
                                 ,,,:, ,, ,                                              
''')
    playSound('hyperbeam.wav')
    
def printMenu():
    print('''                                    I7                                          
                                        ~                                       
                   ++~=::,:~  :     ~   7   =I    =                             
                   =::,,,,,,,~=77II7I777 7+=:=I?I = I                           
                  ~+,:, ,    ,:,:~~:~?77II7I?7I=?7?77?~                         
                =I~,   ,    , ,::,:~:~:~I=+=~?I????=I77?=7I7                    
               =~~+,,          ,:, ,=::,:,?=+?7?~?I~=+?=+I777,                  
            :?=I?::,,,          ,:, ,I   ,:,~==,,::~~I=?I?I77I                  
      I~?  =I=, ,    ,    ,   , , ,,,   ,+ :,,=,:=,:=I++?:I777                  
      +~,,,,,,,      ,         ,,+=  ,,,,:  ,~,,,,,,,:??I+?II77                 
     7:     ,,                 :=7:    ,,,,    , ,,,::=+7?7+I?77                
     ?,7,                       ~+ ~    =,       , ,,::~77?I?+777               
    I,,,,                       :::~   ,, :   ~   ,,=,~,I7777I=7777             
    ?                           ,~+,~, ,, ,        =,,,=?77777I+777             
   7,,                         ,,~:+,~,,:         ,, ,:~+7I77+I?+777            
    ,                    ,,:::::~~I:=:,,    ,    ,,:::::~=I,~I??++777=          
    ,                ,,::~~~~~~~~~+=,:::~,  ,,,,~=+=???~::II:~?7+~I7I7          
   :,               ,:===========~~:,,,,::,:==II77777II7=:~~::~=7?II7I7         
  :~:             ,:~==++++++++===~~~~~~~=??II7777777777I?=,,,,+??7I7?+I        
   ~?,          ,,:===++++++++++=+++++?I77777777777777777II::,,:?++77777        
    ,,         ,:~==++++++++++++++??I777777777777777777777II=+~,,I?:777I7       
    ,,        ,~==+++++++++++++++++?IIII77777777777777777777I?++= I7+IIII       
    ,        ,~=+++++++++++++++++++?I?II7777777777777777   77I==I=~?7?7I7       
    ,       ,:=++++++++++++++++++++++???II777777777777777 77777?=7~=+?II7       
            ,=++++++++++++++++++++++++++++?+++++??I77777   7 77??=?++III,I      
            :++??=====~~~~~=====++++====~=~~~=~=?I7777777 777 7?II+~I+??III     
            ~??~::::,,:::::~~~~==++===========++?I7777777777  7II7?I=~=777II    
    ,,     ,+?~:~=++==~~~~~~~~====++++========+?I77777777     77I?777?=III7     
    ,,     :?==+++++++==~~=~====++++++++===~~~~+777?7777777  7777II?I?III77+    
   ,,,     +++????+=~~=~:::~~~=+++?777?==~~::, ,,:~77777777   777I+I7??I        
   =:,     ?II??+==+:     ,,~~=++?I777I+=~,,~~:~+?+==~=+7777  7777I?77II      , 
  :~,,     III??++:  ~,,:~:::===+?77777?+======++I7777777777  7777II77777       
  ::,,     7I??=:,~=+==~~~~~===++?7777777?=======+?I77777777  7777777?I7        
  :::,,   ,7I?=???++==~~~~===+++?I777 7777777I++?III777777777 7777I777?7        
  ::~,,   ,7I????+++=+==++++++++?7777777777777777777777777777777777777I7        
   ,:,   ,,7II????+++++++++??+++?I777777777I???III777777777 777777I777I7        
    ,,,,,,:IIII????????+++++=+I???777 7777++??????I777777777777777?II77+        
         ::7III???????++++=++???++?77777777~=++????I777777777777777?I77         
         ,:III????????++==~I?++?+++I7=,:?77?~=+++???I77777777777777+I7        , 
          ~7III??????++==~~+=:,,=++?===~~~~~=~~=+++??I7777777777777777          
          =IIII???+++==~~~==~~~~==============~~~=+++?I77777777777777           
           IIII??++++==~~=========~~=~===++==~~~::=+++?77777777777777           
            II???++==~~~========~~~~~~==++++++=~::::=++?7777777777777           
           ?II???++=~::~~==+========~~~=====++?+~:::~=+?777777777 7             
           7II??++==~::~=++=~~~=~~~~~~~~~~~~~::::::::=++777777777               
            II??++==~,::~: ,~==~~+=~~+?++??I~:,   ,:~=+?77777777                
            II??++==~:,,    ~??I?III?I7:IIII::,,::~~=++I77777777                
            ?II??+++=~:::,,,,,:,,,,:,~~~=II7I??++==~==+I77777777                
             +I??++=+=~~~===~===+===?7?I7777777??++===?I7777777                 
              ????++==~~===++++=========?I77777777?++?I7777777                  
               +??++==~==++++++=========+I7777777777II77777777                  
                ???+++==+++==++==========+I777777777777777777                   
                 I?++++++++===+=========+?I777777777777777777                   
                 ,=?+++++++++++++====++?I77777777777777777777              ,,   
                  ,=++++++++++++++++++?II77777777777777777777                   
                    :I+++?+++++++++=+++?I777777777777777777777                  
                      ?++++++++++++===++?I77777777777777777777                  
                    =,?+=++++++++======++??II77777777777777777                  
                  I,  ++============~=====++?III777777777777777+I777            
               I7+,   ==========~~~~~~~~~~===+I77777777777777777~7777777        
             777+=,   +==========~~~~~~~~~~=+?777777777777777777:7777777777:    
           7I==7?~,   ========~=~~~~~~~~~~~=+II7777777777777777I:777777777777   
          I~~~7+~:,  ,~======~~~~~~~~~~~~~~=?IIIIII777777777777~+777777777777777
        :+~:,?=:,    :~~======~~~~~~~~~~~~~=+????III77777777777~I777777777777777
    77:7::,,,+~,,    ~~~~~~===~~~~~~~~~~::~~==+++?II7777777777==7777 77777777777
  IIII=~::::I~,     ,~~~~~~~===~~~~~~~~:::~~~~~=+?III77777777=:I7777777777 77777
  ?+I7777777?:,,,   ,~~~~~~~~==~~~~~~~~~~~~~~~~~=+?I7777777?=~:77777 77777777777
I7?777I7777+++?+~,  ,~~~~~~~~==~~~~~~~~~~~~~~~~~=+?II7777I==~:I77777777777777777
=~~7I?====++=II?~,   :~~~~~~====~~~~~~~~~~~~~~~==+?III7+===~~+I77777777777777777
7777I?=~::~::I?:,,   :~~~~===~~==~~~~~~~~~~~~~===+III=====~~:?777777777777777777
II7??=~::::~?7=:,,   ,~~~========~~~~~~~~~~~~~==+I+======~~:=7777777 777   77777
??I+==~~I77777?:,,,  ,:~============~~~~~======+========~~,~~~=77777777777777777
I????~~7777I??+,, :, ,:~===++===========================, ,+=I7+77 7777777777777
III??IIIII?+??~:,,=:  ,:==+++++++++++==+++============:, ,+?=?777777777777777777''')
    time.sleep(1.5)
    print('''
Who is this?

a) Joey
b) Egg
c) Abalone
d) Thomas''')
    
enter = input('Enter to begin')
printMenu()
usrChoice = input().lower()
while usrChoice != 'd':
    if usrChoice == 'a':
        printJoey()
    if usrChoice == 'b':
        printEgg()
    if usrChoice == 'c':
        printAbalone()
    if usrChoice not in ['a','b','c','d']:
        print('An actual choice stupid')
        time.sleep(1.5)
    printMenu()
    usrChoice = input().lower()
endSession()
os._exit(0)



