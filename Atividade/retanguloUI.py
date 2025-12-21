import streamlit as Heitor
from retangulo import Retangulo

class RetanguloUI: 
    def main(): 
        Heitor.header("Cálculos com retângulo")
        base = Heitor.text_input("Informe a base: ")
        altura = Heitor.text_input("Informe a altura: ")
        if Heitor.button("Calcular"):
            b = float(base)
            h = float(altura)
            r = Retangulo(b,h)
            Heitor.write(r)
            Heitor.write(r.calc_area())
            Heitor.write(r.calc_diagonal())

