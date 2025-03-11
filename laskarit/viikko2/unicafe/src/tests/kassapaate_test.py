import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassa_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassassa_rahaa_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_lounaiden_maara_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_syo_edullisesti_maksu_riittava(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(250)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(maksu, 10)

    def test_kateisosto_syo_edullisesti_maksu_ei_tarpeeksi(self):
        maksu = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(maksu, 200)

    def test_kateisosto_syo_maukkaasti_maksu_riittava(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(420)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(maksu, 20)

    def test_kateisosto_syo_maukkaasti_maksu_ei_tarpeeksi(self):
        maksu = self.kassapaate.syo_maukkaasti_kateisella(250)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(maksu, 250)

    def test_korttiosto_syo_edullisesti_maksu_riittava(self):
        maksukortti = Maksukortti(1000)
        maksu = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 1000 - 240)
        self.assertEqual(maksu, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_syo_edullisesti_maksu_ei_riittava(self):
        maksukortti = Maksukortti(200)
        maksu = self.kassapaate.syo_edullisesti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(maksu, False)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_korttiosto_syo_maukkaasti_maksu_riittava(self):
        maksukortti = Maksukortti(1000)
        maksu = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 1000 - 400)
        self.assertEqual(maksu, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_syo_maukkaasti_maksu_ei_riittava(self):
        maksukortti = Maksukortti(200)
        maksu = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)

        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(maksu, False)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_lataa_rahaa_kortille_toimii(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 500)

        self.assertEqual(maksukortti.saldo, 1500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 500)

    def test_lataa_rahaa_kortille_ei_toimi_negatiivisena(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1000)

        self.assertEqual(maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)








