import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")

    def test_rahan_ottaminen_toimii_rahaa_tarpeeksi(self):
        value = self.maksukortti.ota_rahaa(400)

        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)
        self.assertEqual(value, True)

    def test_rahan_ottaminen_saldo_pysyy_samana_kun_rahaa_ei_tarpeeksi(self):
        value = self.maksukortti.ota_rahaa(1100)

        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(value, False)


