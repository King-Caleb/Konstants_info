PlayerList = {1:{'name':'Marc-André ter Stegen',
                    'position':'Goalkeeper',
                    'citizenship':'Germany',
                    'appearances':'24',
                    'goals':'0'
                        },
              2:{'name':'Nélson Semedo',
                    'position':'Right-Back Defender',
                    'citizenship':'Portugal',
                    'appearances':'13',
                    'goals':'0'
                        },
              3:{'name':'Gerard Piqué',
                    'position':'Centre-Back Defender',
                    'citizenship':'Spain',
                    'appearances':'102',
                    'goals':'5'
                        },
              4:{'name':'Ivan Rakitić',
                    'position':'Defensive Midfielder',
                    'citizenship':'Switzerland',
                    'appearances':'106',
                    'goals':'15'
                        },
              5:{'name':'Sergio Busquets',
                    'position':'Defensive Midfielder',
                    'citizenship':'Spain',
                    'appearances':'116',
                    'goals':'2'
                        },
              6:{'name':'Jean-Clair Todibo',
                    'position':'Center-Back/ Defensive Midfielder',
                    'citizenship':'French Guiana',
                    'appearances':'33',
                    'goals':'1'
                        },
              8:{'name':'Arthur Melo',
                    'position':'Midfielder',
                    'citizenship':'Brazil',
                    'appearances':'138',
                    'goals':'10'
                        },
              9:{'name':'Luis Alberto Suárez Diaz',
                    'position':'Striker',
                    'citizenship':'Urugauy',
                    'appearances':'634',
                    'goals':'411'
                        },
              10:{'name':'Lionel Andrés Messi Cuccittini',
                    'position':'Forward',
                    'citizenship':'Argentina',
                    'appearances':'751',
                    'goals':'639'
                        },
              11:{'name':'Masour Ousmane Dembélé',
                    'position':'Forward',
                    'citizenship':'France',
                    'appearances':'175',
                    'goals':'54'
                        },
              13:{'name':'Norberto Murara Neto',
                    'position':'Goalkeeper',
                    'citizenship':'Brazil',
                    'appearances':'243',
                    'goals':'0'
                        },
              15:{'name':'Clément Nicolas Laurent Lenglet',
                    'position':'Center-Back',
                    'citizenship':'France',
                    'appearances':'232',
                    'goals':'11'
                        },
              16:{'name':'Moussa Wagué',
                    'position':'Right-Back',
                    'citizenship':'Senegal',
                    'appearances':'74',
                    'goals':'3'
                        },
              17:{'name':'Antoine Griezmann',
                    'position':'Forward',
                    'citizenship':'France',
                    'appearances':'496',
                    'goals':'199'
                        },
              18:{'name':'Jordi Alba Ramos',
                    'position':'Left-Back',
                    'citizenship':'Spain',
                    'appearances':'471',
                    'goals':'27'
                        },
              19:{'name':'Carles Aleñá Castillo',
                    'position':'Central Midfielder',
                    'citizenship':'Spain',
                    'appearances':'140',
                    'goals':'21'
                        },
              20:{'name':'Sergi Roberto Carnicer',
                    'position':'Midfielder/Full-Back',
                    'citizenship':'Spain',
                    'appearances':'381',
                    'goals':'16'
                        },
              21:{'name':'Frenkie de Jong',
                    'position':'Midfielder',
                    'citizenship':'Netherlands',
                    'appearances':'176',
                    'goals':'15'
                        },
              22:{'name':'Arturo Erasmo Vidal Pardo',
                    'position':'Midfielder',
                    'citizenship':'Chile',
                    'appearances':'580',
                    'goals':'106'
                        },
              23:{'name':'Samuel Yves Um Titi',
                    'position':'Center-Back',
                    'citizenship':'Cameroon',
                    'appearances':'305',
                    'goals':'7'
                        },
              24:{'name':'Héctor Junior Firpo Adames',
                    'position':'Left-Back',
                    'citizenship':'Dominican Republic',
                    'appearances':'106',
                    'goals':'8'
                        },
                      }

def getPlayerData(jerseyNumber):
    return PlayerList.get(jerseyNumber,
                          {'name':'???',
                           'position':'???',
                           'citizenship':'???',
                           'appearances':'???',
                           'goals':'???'})


