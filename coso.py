#!/usr/bin/env python
# -*- coding: utf-8 -*-

a="""
experiment itself was interessting
Were you personally engaged achieving good results
dificult understanding and solving the problem
Was it obvious what to do
short feedback
""".strip()

lines = a.splitlines()

for l in lines:
    l = l.lower().split()
    l = "_".join(l)
    print "q3_{} = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))".format(l)

print ""
lista = ["q3_"+"_".join(l.lower().split()) for l in lines]
import pprint;pprint.pprint(lista)
print map(len, lista)
