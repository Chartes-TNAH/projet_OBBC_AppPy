from app.app import db
import copy
from ..constantes import source_doc

class SongsBB(db.Model):
	__tablename__ = "chansonBB"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title_fr = db.Column(db.String(45))
	title_brz = db.Column(db.String(45))
	dialect = db.Column(db.String(64))
	theme = db.Column(db.String(64))
	song_fr = db.Column(db.Text)
	song_brz = db.Column(db.Text)
	MusicSheetPath = db.Column(db.String(64))

	def __init__(self, id, title_fr, title_brz, dialect, theme, song_fr, song_brz, MusicSheetPath):
		self.id = id
		self.title_fr = title_fr
		self.title_brz = title_brz
		self.dialect = dialect
		self.theme = theme
		self.song_fr = song_fr
		self.song_brz = song_brz
		self.MusicSheetPath = MusicSheetPath

list_song_fr = []
list_song_brz = []
list_title_fr = []
list_title_brz = []
list_dialect = []
list_theme = []
list_lyricsFr = []
list_lyricsBrz =[]
list_MusicSheetPath = ['<img src="/static/images/img_partitions/chansonPR.jpg">',
								 '<img src="/static/images/img_partitions/chansonMA.jpg">',
								 '<img src="/static/images/img_partitions/chansonLR.jpg">',
								 '<img src="/static/images/img_partitions/chansonSG.jpg">',
								 '<img src="/static/images/img_partitions/partitionV.jpg">',
								 '<img src="/static/images/img_partitions/partitionV.jpg">',
								 '<img src="/static/images/img_partitions/partitionV.jpg">',
								 '<img src="/static/images/img_partitions/partitionV.jpg">',
								 '<img src="/static/images/img_partitions/chansonEnfer.jpg">',
								 '<img src="/static/images/img_partitions/chansonParadis.jpg">']


def extraction_lyrics(list_song, list_lyrics):
	for song in list_song:
		list_lyrics.append(song)
		for verse in list_lyrics:
			verses = verse
	return verses




for element in source_doc.xpath("//body/div/div/div[@type='chanson']/@n"):
	node_titre_fr = source_doc.xpath("//text/body/div/div/div[@type='chanson'][@n=" + str(
				element) + "]/div[@type='transcription']/head[@type='titre-français']/text()")
	list_title_fr.append(copy.deepcopy(node_titre_fr[0]))
	node_titre_brz = source_doc.xpath("//div/div/div[@type='chanson'][@n=" + str(
				element) + "]/div[@type='original']/head[@type='titre-breton']/text()")
	list_title_brz.append(copy.deepcopy(node_titre_brz[0]))
	node_dialecte = source_doc.xpath(
				"//body/div/div/div[@type='chanson'][@n=" + str(element) + "]/ancestor::div[@type='D']/head/text()")
	list_dialect.append(copy.deepcopy(node_dialecte[0]))
	node_theme = source_doc.xpath(
				"//body/div/div/div[@type='chanson'][@n=" + str(element) + "]/ancestor::div[@type='T']/head/text()")
	list_theme.append(copy.deepcopy(node_theme[0]))
	node_chanson_fr = source_doc.xpath(
		"//div[@type='chanson'][@n='" + str(element) + "']/div[@type = 'transcription']/lg/l/text()")
	list_song_fr.append(copy.deepcopy(node_chanson_fr))
	node_chanson_brz = source_doc.xpath(
		"//div[@type='chanson'][@n='" + str(element) + "']/div[@type = 'original']/lg/l/text()")
	list_song_brz.append(copy.deepcopy(node_chanson_brz))
	list_verses_fr = extraction_lyrics(list_song_fr, list_lyricsFr)
	list_verses_brz = extraction_lyrics(list_song_brz, list_lyricsBrz)



	db.session.add(SongsBB(element,
					 list_title_fr[int(element) - 1],
					 list_title_brz[int(element) - 1],
					 list_dialect[int(element) - 1],
					 list_theme[int(element) - 1],
					 "".join(list_verses_fr),
					 "".join(list_verses_brz),
					 list_MusicSheetPath[int(element) - 1]))

	db.drop_all()
	db.create_all()

db.session.commit()
