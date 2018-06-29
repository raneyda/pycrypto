#!/usr/bin/python3

import sys
import unittest
from mycryptolib import *
#print('\n'.join(sys.path))

pt1 = "abcdefghijklmnopqrstuvwxyz"
pt2 = "The big brown bear walks slowly through the forest sniffing for blackberries with his nose."
pt3 = '"There is no one who loves pain itself, who seeks after it and wants to have it, simply because it is pain..."'
pt4 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam feugiat varius tortor ac convallis. Cras dignissim risus et justo eleifend volutpat. Nam non mauris eros. Ut vulputate ex in nunc convallis, eu venenatis purus ornare. Nulla consectetur enim orci, quis maximus eros vestibulum sit amet. Proin sed tortor dolor. Sed at felis quis mi condimentum tristique. Mauris eu sapien a mauris scelerisque ornare vitae a nulla. Donec sed nunc mattis ante placerat placerat vitae id dolor. Duis ut consequat magna, ut volutpat est. Suspendisse pellentesque orci lobortis lorem aliquet, sed tempor dui hendrerit.

Nunc dolor quam, laoreet quis enim at, auctor auctor dui. Morbi est diam, sagittis ac malesuada ac, imperdiet ut elit. Suspendisse posuere dolor eget ornare tempus. Suspendisse potenti. Suspendisse nibh est, auctor sed leo ac, interdum sollicitudin turpis. Donec egestas ante eget fermentum mattis. Donec nec ligula tellus. Praesent malesuada dolor et mi scelerisque, sagittis tincidunt neque tempor. Aenean imperdiet laoreet neque volutpat rutrum. Proin lobortis, enim et volutpat facilisis, velit lectus auctor sapien, at aliquet erat quam vitae ante. Aenean in mauris pellentesque, euismod nisl sed, rutrum risus. Cras vel lacus ac tortor posuere ultricies. In hac habitasse platea dictumst.

Nullam facilisis ac elit vitae interdum. Sed iaculis lectus ligula, ac rutrum odio vulputate aliquet. Fusce iaculis fringilla enim, ut placerat nisl efficitur a. Vestibulum consequat eleifend sapien, eu auctor est facilisis et. Morbi vitae nunc consectetur neque sollicitudin porttitor vitae et mi. Ut in sem est. Quisque leo massa, consectetur et enim vehicula, pretium euismod elit. Vivamus et ligula condimentum, placerat sem id, laoreet risus. Suspendisse blandit semper enim vitae pulvinar. Integer eu mi efficitur, tincidunt metus at, venenatis tortor. Maecenas molestie tellus vel velit tincidunt congue. Aenean metus enim, convallis et diam sit amet, auctor posuere orci. Maecenas scelerisque ex id erat dictum auctor. Curabitur vel dolor vitae metus convallis fermentum ut at risus.

Nullam et lacinia enim. Sed sit amet semper ex, vel sollicitudin ex. Phasellus a tincidunt sem. Nullam rutrum nunc in ante rutrum varius vel eget quam. Nam porttitor placerat finibus. Sed porttitor blandit erat eget fermentum. Phasellus non sapien consequat, rhoncus odio in, tempus neque.

Ut id ultricies dui, in vestibulum odio. Suspendisse eget iaculis est, sit amet pharetra erat. Fusce suscipit lacus non elementum laoreet. Ut placerat accumsan fringilla. Sed nec felis ut urna porttitor ultrices. Duis sit amet aliquam arcu. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse non feugiat massa. In fermentum nisi quis erat vestibulum tempor. Cras pretium odio nulla, a rutrum nunc vestibulum in. Ut luctus tortor nec velit pellentesque ultricies. Mauris sollicitudin, diam vitae tincidunt iaculis, velit erat posuere diam, ac venenatis sapien justo a nunc. Quisque tincidunt erat non augue scelerisque rutrum. Curabitur placerat, diam ac finibus aliquam, erat est porttitor lacus, quis mollis eros nisl vel nisl. Nam metus nibh, vehicula eu urna at, tincidunt ultricies tellus."""

class CryptoTests(unittest.TestCase):

    def test_text_pt1(self):
        self.assertEqual(pt_parse_text(pt1), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def test_text_pt2(self):
        self.assertEqual(pt_parse_text(pt2), 'THEBIGBROWNBEARWALKSSLOWLYTHROUGHTHEFORESTSNIFFINGFORBLACKBERRIESWITHHISNOSE')

    def test_text_pt3(self):
        self.assertEqual(pt_parse_text(pt3), 'THEREISNOONEWHOLOVESPAINITSELFWHOSEEKSAFTERITANDWANTSTOHAVEITSIMPLYBECAUSEITISPAIN')

    def test_text_pt4(self):
        self.assertEqual(pt_parse_text(pt4), 'LOREMIPSUMDOLORSITAMETCONSECTETURADIPISCINGELITETIAMFEUGIATVARIUSTORTORACCONVALLISCRASDIGNISSIMRISUSETJUSTOELEIFENDVOLUTPATNAMNONMAURISEROSUTVULPUTATEEXINNUNCCONVALLISEUVENENATISPURUSORNARENULLACONSECTETURENIMORCIQUISMAXIMUSEROSVESTIBULUMSITAMETPROINSEDTORTORDOLORSEDATFELISQUISMICONDIMENTUMTRISTIQUEMAURISEUSAPIENAMAURISSCELERISQUEORNAREVITAEANULLADONECSEDNUNCMATTISANTEPLACERATPLACERATVITAEIDDOLORDUISUTCONSEQUATMAGNAUTVOLUTPATESTSUSPENDISSEPELLENTESQUEORCILOBORTISLOREMALIQUETSEDTEMPORDUIHENDRERITXXXXNUNCDOLORQUAMLAOREETQUISENIMATAUCTORAUCTORDUIMORBIESTDIAMSAGITTISACMALESUADAACIMPERDIETUTELITSUSPENDISSEPOSUEREDOLOREGETORNARETEMPUSSUSPENDISSEPOTENTISUSPENDISSENIBHESTAUCTORSEDLEOACINTERDUMSOLLICITUDINTURPISDONECEGESTASANTEEGETFERMENTUMMATTISDONECNECLIGULATELLUSPRAESENTMALESUADADOLORETMISCELERISQUESAGITTISTINCIDUNTNEQUETEMPORAENEANIMPERDIETLAOREETNEQUEVOLUTPATRUTRUMPROINLOBORTISENIMETVOLUTPATFACILISISVELITLECTUSAUCTORSAPIENATALIQUETERATQUAMVITAEANTEAENEANINMAURISPELLENTESQUEEUISMODNISLSEDRUTRUMRISUSCRASVELLACUSACTORTORPOSUEREULTRICIESINHACHABITASSEPLATEADICTUMSTXXXXNULLAMFACILISISACELITVITAEINTERDUMSEDIACULISLECTUSLIGULAACRUTRUMODIOVULPUTATEALIQUETFUSCEIACULISFRINGILLAENIMUTPLACERATNISLEFFICITURAVESTIBULUMCONSEQUATELEIFENDSAPIENEUAUCTORESTFACILISISETMORBIVITAENUNCCONSECTETURNEQUESOLLICITUDINPORTTITORVITAEETMIUTINSEMESTQUISQUELEOMASSACONSECTETURETENIMVEHICULAPRETIUMEUISMODELITVIVAMUSETLIGULACONDIMENTUMPLACERATSEMIDLAOREETRISUSSUSPENDISSEBLANDITSEMPERENIMVITAEPULVINARINTEGEREUMIEFFICITURTINCIDUNTMETUSATVENENATISTORTORMAECENASMOLESTIETELLUSVELVELITTINCIDUNTCONGUEAENEANMETUSENIMCONVALLISETDIAMSITAMETAUCTORPOSUEREORCIMAECENASSCELERISQUEEXIDERATDICTUMAUCTORCURABITURVELDOLORVITAEMETUSCONVALLISFERMENTUMUTATRISUSXXXXNULLAMETLACINIAENIMSEDSITAMETSEMPEREXVELSOLLICITUDINEXPHASELLUSATINCIDUNTSEMNULLAMRUTRUMNUNCINANTERUTRUMVARIUSVELEGETQUAMNAMPORTTITORPLACERATFINIBUSSEDPORTTITORBLANDITERATEGETFERMENTUMPHASELLUSNONSAPIENCONSEQUATRHONCUSODIOINTEMPUSNEQUEXXXXUTIDULTRICIESDUIINVESTIBULUMODIOSUSPENDISSEEGETIACULISESTSITAMETPHARETRAERATFUSCESUSCIPITLACUSNONELEMENTUMLAOREETUTPLACERATACCUMSANFRINGILLASEDNECFELISUTURNAPORTTITORULTRICESDUISSITAMETALIQUAMARCUORCIVARIUSNATOQUEPENATIBUSETMAGNISDISPARTURIENTMONTESNASCETURRIDICULUSMUSSUSPENDISSENONFEUGIATMASSAINFERMENTUMNISIQUISERATVESTIBULUMTEMPORCRASPRETIUMODIONULLAARUTRUMNUNCVESTIBULUMINUTLUCTUSTORTORNECVELITPELLENTESQUEULTRICIESMAURISSOLLICITUDINDIAMVITAETINCIDUNTIACULISVELITERATPOSUEREDIAMACVENENATISSAPIENJUSTOANUNCQUISQUETINCIDUNTERATNONAUGUESCELERISQUERUTRUMCURABITURPLACERATDIAMACFINIBUSALIQUAMERATESTPORTTITORLACUSQUISMOLLISEROSNISLVELNISLNAMMETUSNIBHVEHICULAEUURNAATTINCIDUNTULTRICIESTELLUS')

    def test_shift_cipher_encode(self):
        self.assertEqual(shift_cipher(pt3,5), 'YMJWJNXSTTSJBMTQTAJXUFNSNYXJQKBMTXJJPXFKYJWNYFSIBFSYXYTMFAJNYXNRUQDGJHFZXJNYNXUFNS')

    def test_shift_cipher_decode(self):
        self.assertEqual(shift_cipher('YMJWJNXSTTSJBMTQTAJXUFNSNYXJQKBMTXJJPXFKYJWNYFSIBFSYXYTMFAJNYXNRUQDGJHFZXJNYNXUFNS',-5), str(pt_parse_text(pt3)))

    def test_playfair_key_test(self):
        self.assertEqual(playfair_key('notorius'), 'NOTRIUSABCDEFGHKLMPQVWXYZ')

    def test_playfair_encode(self):
        self.assertEqual(playfair_cipher('notorius', pt2, 'enc'), "IF GS RH GB SO RU FS OY SM LU EW SO PW IF IT BD FI DF ET OG AO UO TH HT RD ET BG MS UQ SG TY IN LE ZO IF QC UO SE FW")

    def test_playfair_dencode(self):
        self.assertEqual(playfair_cipher('notorius', "IF GS RH GB SO RU FS OY SM LU EW SO PW IF IT BD FI DF ET OG AO UO TH HT RD ET BG MS UQ SG TY IN LE ZO IF QC UO SE FW", 'dec'), "TH EB IG BR OW NB EA RW AL KS SL OW LY TH RO UG HT HE FO RE ST SN IF FI NG FO RB LA CK BE RX RI ES WI TH HI SN OS EX")

if __name__ == '__main__':
    unittest.main()
