from underlight_api import utils
import underlight_api
#0=Dreamsoul 1=Willpower 2=Insight 3=Resilience 4=Lucidity 5=NoStat
STATS = (
    "DREAMSOUL",
    "WILLPOWER",
    "INSIGHT",
    "RESILIENCE",
    "LUCIDITY",
    "NOSTAT"
)

ARTS_TABLE = (
    ("Join_Party", 0),
    ("Gatekeeper", 1),
    ("Dreamseer", 2),
    ("Soulmaster", 3),
    ("Fatesender", 4),
    ("Random", 0),
    ("Meditation", 1),
    ("Resist_Fear", 1),
    ("Protection", 1),
    ("Free_Action", 1),
    ("Ward", 1),
    ("Amulet", 1),
    ("Shatter", 1),
    ("Return", 1),
    ("Know", 2),
    ("Judgement", 2),
    ("Identify", 2),
    ("Identify_Curse", 2),
    ("Chamele", 2),
    ("Vision", 2),
    ("Blast", 2),
    ("Blend", 2),
    ("Forge_Talisman", 0),
    ("Recharge_Talisman", 2),
    ("Restore", 3),
    ("Reweave", 3),
    ("Purify", 3),
    ("Drain_Self", 3),
    ("Abjure", 3),
    ("Poison", 3),
    ("Antidote", 3),
    ("Curse", 3),
    ("Drain_Essence", 3),
    ("Banish_Nightmare", 3),
    ("Enslave_Nightmare", 3),
    ("Trap_Nightmare", 3),
    ("Dreamblade", 2),
    ("Trail", 4),
    ("Scare", 4),
    ("Stagger", 4),
    ("Deafen", 4),
    ("Blind", 4),
    ("Darkness", 4),
    ("Paralyze", 4),
    ("Firestorm", 4),
    ("Razorwind", 4),
    ("Recall", 0),
    ("Push", 0),
    ("Soulevoke", 0),
    ("Dreamstrike", 0),
    ("Nightmare_Form", 0),
    ("Locate_Avatar", 0),
    ("Train", 0),
    ("Initiate", 0),
    ("Knight", 0),
    ("Support_Ascension", 0),
    ("Ascend", 0),
    ("Instance_Collapse", 5),
    ("Grant_XP", 5),
    ("Terminate", 5),
    ("Sphere", 0),
    ("Support_Demotion", 0),
    ("Demote", 0),
    ("Invisibility", 2),
    ("Give", 0),
    ("Gatesmasher", 1),
    ("Fateslayer", 4),
    ("Soulreaper", 3),
    ("Flameshaft", 1),
    ("Tranceflame", 2),
    ("Flamesear", 3),
    ("Flameruin", 4),
    ("Inscribe", 0),
    ("Destroy_Talisman", 0),
    ("Mind_Blank", 0),
    ("Show_Talisman", 0),
    ("Awaken", 5),
    ("Untrain", 5),
    ("Grant_RP_XP", 5),
    ("Dreamquake", 1),
    ("Hypnotic_Weave", 4),
    ("Vampiric_Draw", 3),
    ("Terror", 4),
    ("Healing_Aura", 3),
    ("Telepathy", 5),
    ("Dreamsmith_Mark", 0),
    ("Support_Train", 0),
    ("Support_Sphere", 0),
    ("Train_Self", 0),
    ("Soul_Shield", 0),
    ("Summon", 5),
    ("Suspend", 5),
    ("Reflect", 1),
    ("Sacrifice", 3),
    ("Cleanse_Nightmare", 3),
    ("Create_ID_Token", 0),
    ("Sense_Dreamer", 0),
    ("Expel", 0),
    ("Locate_New_Dreamer", 0),
    ("Combine", 2),
    ("Create_Power_Token", 0),
    ("Show_Gratitude", 5),
    ("Quest", 0),
    ("Bequeath", 0),
    ("Radiant_Blaze", 0),
    ("Poison_Cloud", 0),
    ("Break_Covenant", 0),
    ("Peace_Aura", 0),
    ("Sable_Shield", 0),
    ("Entrancement", 0),
    ("Shadow_Step", 0),
    ("Dazzle", 0),
    ("Guild_House", 5),
    ("Corrupt_Essence", 3),
    ("Tehthus_Oblivion", 0),
    ("Chaos_Purge", 0),
    ("Wordsmith_Mark", 0),
    ("Cup_Summons", 0),
    ("House_Members", 0),
    ("Freesoul_Blade", 0),
    ("Illuminated_Blade", 0),
    ("Summon_Prime", 0),
    ("Grant_PPoint", 5),
    ("Scan", 2),
    ("Passlock", 2),
    ("Heal", 3),
    ("Sanctify", 1),
    ("Lock", 1),
    ("Key", 1),
    ("Break_Lock", 1),
    ("Repair", 3),
    ("Remove_Curse", 3),
    ("Hold_Avatar", 4),
    ("Sanctuary", 0),
    ("Shove", 0),
    ("Scribe_Not", 0),
    ("Forge_Master", 5),
    ("Merge_Talisman", 2),
    ("NP_Symbol", 5),
    ("Sense_Datoken", 2),
    ("Tempest", 4),
    ("Kinesis", 1),
    ("Misdirection", 0),
    ("Chaotic_Vortex", 0),
    ("Chaos_Well", 0),
    ("Rally", 0),
    ("Channel", 0),
    ("Bulwark", 1),
    ("Sprint", 1),
    ("Enfeeblement", 4),
    ("Dreamwise_Evoke", 5),   
)

def id_from_name(skill):
    return ARTS_TABLE.index[skill]
	
def check_player_skill_exists(self, player_id, skill, skill_level):
    cxn = self.connect(db =' ul_player')
    stmt = 'SELECT count(* )FROM Skill where player_id = %s'
    cursor = cxn.cursor(cursor_class=MySQLCursorPrepared)
    cursor.execute(stmt,(player_id))
    countarts = cursor.rowcount
    return countarts

def add_player_skill(self, player_id, skills, skill_level):
    cxn = self.connect(db = 'ul_player')
    stmt = 'INSERT INTO Skill (player_id, skill skill_level) VALUES'+\
    '(%s, %s, %s)'
    cursor = cxn.cursor(cursor_class=MySQLCursorPrepared)
    skillset = (id_from_name("Trail"), id_from_name("Meditation"), focus[0], focus[1], id_from_name("Know"), id_from_name("Locate_Avatar"), id_from_name("Show_Talisman"), id_from_name("Random"))
    for skill in skillset:
        cursor.execute(stmt,(player_id, skill, skill_level))
    id = cursor.lastrowid
    cxn.commit()
    cursor.close()
    return id

focusselect=(GateKeeper / SoulMaster / FateSender / DreamSeer) 
focus = focusselect

GateKeeperT = ("Gatekeeper","Gatesmasher")
SoulMasterT = ("Soulmaster","Soulreaper")
FateSenderT = ("Fatesender","FateSlayer")
DreamSeerT = ("Dreamseer","Dreamblade")

if check_player_skill_exists(self, player_id, focus[1], 1) == 0: 
    add_player_skill(player_id, focus, 1)