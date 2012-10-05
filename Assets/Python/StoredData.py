# Rhye's and Fall of Civilization - Stored Data

from CvPythonExtensions import *
import CvUtil
import PyHelpers  
import cPickle as pickle
import Consts as con

# globals
gc = CyGlobalContext()
PyPlayer = PyHelpers.PyPlayer	


class StoredData:

        def __init__(self):
                self.setup()

        def load(self):
                """Loads and unpickles script data"""
                self.scriptDict = pickle.loads(gc.getGame().getScriptData())

        def save(self):
                """Pickles and saves script data"""
                gc.getGame().setScriptData(pickle.dumps(self.scriptDict))

        def setup(self):
                """Initialise the global script data dictionary for usage."""
                self.scriptDict = {      #------------RiseAndFall
				    'lTempEventList' : [],
                                    'iNewCiv': -1,
                                    'iNewCivFlip': -1,
                                    'iOldCivFlip': -1,
                                    'tTempTopLeft': -1,
                                    'tTempBottomRight': -1,
                                    'iSpawnWar': 0, #if 1, add units and declare war. If >=2, do nothing
                                    'bAlreadySwitched': False,
                                    'lColonistsAlreadyGiven': [0 for i in range(con.iNumPlayers)], #active players
                                    'lAstronomyTurn': [1500 for i in range(con.iNumPlayers)], #active players
                                    'lNumCities': [0 for i in range(con.iNumTotalPlayers)], #total players to contain Byzantium too
                                    'lLastTurnAlive': [0 for i in range(con.iNumTotalPlayers)], #total players to contain Byzantium too
                                    'lSpawnDelay': [0 for i in range(con.iNumPlayers)], #active players
                                    'lFlipsDelay': [0 for i in range(con.iNumPlayers)],
                                    'iBetrayalTurns': 0,
                                    'lLatestRebellionTurn': [0 for i in range(con.iNumPlayers)],
                                    'iRebelCiv': 0,
                                    'lExileData': [-1, -1, -1, -1, -1],
                                    'tTempFlippingCity': -1,
                                    'lCheatersCheck': [0, -1],
                                    'lBirthTurnModifier': [0 for i in range(con.iNumPlayers)],
                                    'lDeleteMode': [-1, -1, -1], #first is a bool, the other values are capital coordinates
                                    'lFirstContactConquerors': [0, 0, 0], #maya, inca, aztecs
				    'lFirstContactMongols': [0, 0, 0, 0, 0], #india, persia, byzantium, arabia, russia
                                    'bCheatMode': False,
				    'tTempFlippingCity': (0, 0),
				    'tTradingCompanyConquerorsTargets': ([], [], [], [], []),
				    'iOttomanSpawnTurn': -1,
				    'lAnarchyTurns': [0 for i in range(con.iNumPlayers)],
				    'lResurrections': [0 for i in range(con.iNumPlayers)],
				    'lPlayerEnabled': [True for i in con.lSecondaryCivs],
                                     #------------Religions
                                    'iSeed': -1,
				    'lReformationDecision': [-1 for i in range(con.iNumPlayers)],
                                    #------------UP
                                    'iImmigrationTurnLength': 0,
                                    'iImmigrationCurrentTurn': 0,
                                    'iLatestFlipTurn': 0,
                                    'lLatestRazeData': [-1, -1, -1, -1, -1],
				    'iRomanVictories': 0,
				    #------------AIWars
                                    'lAttackingCivsArray': [0 for i in range(con.iNumPlayers)], #original RFC had -1 here somewhere??
                                    'iNextTurnAIWar': -1,
                                    #------------Congresses
                                    'bCongressEnabled': False,
                                    'iCivsWithNationalism': 0,
                                    'bUNbuilt': False,
                                    'lInvitedNations': [False for i in range(con.iNumPlayers)],
                                    'lVotes': [0 for i in range(con.iNumPlayers)],
                                    'lTempActiveCiv': [-1 for i in range(con.iNumPlayers)],
                                    'lTempReqCity': [-1 for i in range(con.iNumPlayers)],
                                    'iLoopIndex': 0,
                                    'lTempReqCityHuman': [-1, -1, -1, -1, -1],
                                    'tempReqCityNI': -1,
                                    'tempActiveCivNI': -1,
                                    'lTempAttackingCivsNI': [False for i in range(con.iNumPlayers)],
                                    'iNumNationsTemp': 0,
                                    'lBribe' : [-1, -1, -1],
                                    'lCivsToBribe': [-1 for i in range(con.iNumPlayers)],
                                    'tTempFlippingCityCongress': -1,
                                    'lMemory': [0 for i in range(con.iNumTotalPlayersB)], #total players + barbarians (minors and barbs are not used, but necessary for not going out of range)
                                    #------------Plague
                                    'lPlagueCountdown': [0 for i in range(con.iNumTotalPlayersB)], #total players + barbarians
                                    'lGenericPlagueDates': [-1, -1, -1, -1],# -1],
                                    'lFirstContactPlague': [False for i in range(con.iNumTotalPlayersB)], #total players + barbarians
                                     #------------Victories
                                    'lGoals': [[-1, -1, -1] for i in range(con.iNumPlayers)],
                                    'lReligionFounded': [-1, -1, -1, -1, -1, -1, -1, -1],
                                    'iEnslavedUnits': 0,
                                    'iRazedByMongols': 0,
                                    'lEnglishEras': [-1, -1],
                                    'lGreekTechs': [-1, -1, -1],
                                    'lNewWorld': [-1, -1], #first founded; circumnavigated (still unused)
                                    'iNumSinks': 0,
                                    'lBabylonianTechs': [-1, -1, -1],                                    
                                    #'iMediterraneanColonies': 0,
                                    'iPortugueseColonies': 0,
                                    'iFrenchColonies': 0,
                                    'lWondersBuilt': [0 for i in range(con.iNumPlayers)],
                                    'l2OutOf3': [False for i in range(con.iNumPlayers)],
				    'iChineseGoldenAges' : 0,
				    'lItalianTechs': [-1, -1, -1, -1, -1, -1],
				    'iNumKoreanSinks': 0,
				    'iNumGenerals': 0,
				    'iTechsStolen': 0,
				    'lChineseTechs': [-1, -1, -1, -1],
				    'iEthiopianControl' : -1,
				    'iVikingGold' : 0,
				    'lRussianProjects' : [-1, -1, -1],
				    'iDutchColonies' : 0,
				    'iNumTamilSinks' : 0,
				    'iTamilTradeGold' : 0,
				    'lRomanTechs' : [-1, -1, -1],
				    'iCongoSlaveCounter' : 0,
				    'bMaliGold' : False,
                                    #------------Stability
                                    'lBaseStabilityLastTurn': [0 for i in range(con.iNumPlayers)],
                                    'lPartialBaseStability': [0 for i in range(con.iNumPlayers)],
                                    'lStability': [0 for i in range(con.iNumPlayers)],
                                    'lOwnedPlotsLastTurn': [0 for i in range(con.iNumPlayers)],
                                    'lOwnedOuterPlotsLastTurn': [0 for i in range(con.iNumPlayers)],
                                    'lOwnedForeignCitiesLastTurn': [0 for i in range(con.iNumPlayers)],
                                    'lOwnedCitiesLastTurn': [0 for i in range(con.iNumPlayers)],
                                    'lCombatResultTempModifier': [0 for i in range(con.iNumPlayers)],
                                    'lGNPold': [0 for i in range(con.iNumPlayers)],
                                    'lGNPnew': [0 for i in range(con.iNumPlayers)],
                                    'lGreatDepressionCountdown': [0 for i in range(con.iNumPlayers)],
                                    'lStatePropertyCountdown': [0 for i in range(con.iNumPlayers)],
                                    'lDemocracyCountdown': [0 for i in range(con.iNumPlayers)],
                                    'lStabilityParameters': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2+3+2+3+3
                                    'lLastRecordedStabilityStuff': [0, 0, 0, 0, 0, 0], # total + 5 parameters
				}
                self.save()

# All modules import the following single instance, not the class

sd = StoredData()