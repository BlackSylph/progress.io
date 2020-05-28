from django.test import TestCase
from progressio.Views.Cryptography import views as Cryptography


class CaesarCipherCases(TestCase):

    def testShiftsNaive(self):
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 1), 'Tbnqmf Ufyu')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 2), 'Ucorng Vgzv')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 3), 'Vdpsoh Whaw')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 4), 'Weqtpi Xibx')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 5), 'Xfruqj Yjcy')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 6), 'Ygsvrk Zkdz')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 7), 'Zhtwsl Alea')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 8), 'Aiuxtm Bmfb')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 9), 'Bjvyun Cngc')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 10), 'Ckwzvo Dohd')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 11), 'Dlxawp Epie')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 12), 'Emybxq Fqjf')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 13), 'Fnzcyr Grkg')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 14), 'Goadzs Hslh')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 15), 'Hpbeat Itmi')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 16), 'Iqcfbu Junj')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 17), 'Jrdgcv Kvok')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 18), 'Ksehdw Lwpl')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 19), 'Ltfiex Mxqm')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 20), 'Mugjfy Nyrn')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 21), 'Nvhkgz Ozso')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 22), 'Owilha Patp')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 23), 'Pxjmib Qbuq')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 24), 'Qyknjc Rcvr')
        self.assertEqual(Cryptography.caesar_cipher_encrypt('Sample Text', 25), 'Rzlokd Sdws')

    def testSpecialCharacters(self):
        self.assertEqual(Cryptography.caesar_cipher_encrypt('!@#$%^&*()_+|\][}{\'":;/?.>,<', 1),
                         '!@#$%^&*()_+|\][}{\'":;/?.>,<')

    def testMixed(self):
        self.assertEqual(Cryptography.caesar_cipher_encrypt('a1!b2@c3#d4$e5%f6^g7&h8*i9(j0)', 2),
                         'c1!d2@e3#f4$g5%h6^i7&j8*k9(l0)')