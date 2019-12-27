'''
Created on 01-Apr-2019

@author: elango
'''
import pypandoc
output = pypandoc.convert(source='path/to/file', format='html', to='docx', outputfile='path/to/docx', extra_args=['-RTS'])
