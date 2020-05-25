from django.test import TestCase
from progressio.Views.Cryptography import views as Cryptography

class CaesarCipherCases(TestCase):

    def testShiftsNaive(self):
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 1), 'Tbnqmf Ufyu')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 2), 'Ucorng Vgzv')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 3), 'Vdpsoh Whaw')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 4), 'Weqtpi Xibx')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 5), 'Xfruqj Yjcy')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 6), 'Ygsvrk Zkdz')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 7), 'Zhtwsl Alea')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 8), 'Aiuxtm Bmfb')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 9), 'Bjvyun Cngc')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 10), 'Ckwzvo Dohd')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 11), 'Dlxawp Epie')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 12), 'Emybxq Fqjf')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 13), 'Fnzcyr Grkg')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 14), 'Goadzs Hslh')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 15), 'Hpbeat Itmi')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 16), 'Iqcfbu Junj')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 17), 'Jrdgcv Kvok')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 18), 'Ksehdw Lwpl')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 19), 'Ltfiex Mxqm')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 20), 'Mugjfy Nyrn')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 21), 'Nvhkgz Ozso')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 22), 'Owilha Patp')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 23), 'Pxjmib Qbuq')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 24), 'Qyknjc Rcvr')
        self.assertEqual(Cryptography.caesarcipherencrypt('Sample Text', 25), 'Rzlokd Sdws')
