sentence = str(input('Write a sentence:')).strip().upper()

print('The letter A appears {} times in the sentence'.format(sentence.count('A')))

print('The first time that appears is in the position {}'.format(sentence.find('A')))

print('The last time that appears is in the position {}'.format(sentence.rfind('A')))
