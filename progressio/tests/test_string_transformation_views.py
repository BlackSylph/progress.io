from django.test import TestCase
from progressio.Views.StringTransforms import views as StringTransforms


class StringOccurenceCases(TestCase):


	def testBaseCases(self):
		self.assertEqual(StringTransforms.count_words_in_string('a                 a'), 2)
		self.assertEqual(StringTransforms.count_words_in_string('A-B,C+D=E:F"G\H|I/J.K?L<M>N!O@P#Q$R%S^T&U*V(W)X_Y[Z]1{2}3'), 4)