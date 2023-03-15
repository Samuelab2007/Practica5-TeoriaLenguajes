class AutomataDePila:

    def __init__(self, cadena):
        self._cadena = cadena
        self._pila = []
        self._listaEstados = ["Q0", "Q1", "Q2"]
        self._estadoActual = "Q0"

    def determinaraceptacion(self):
        if len(self._cadena) < 3:
            return "Cadena Inválida"
        for i in self._cadena:
            aceptacioncaracter = self.funciontransicion(i)
            if aceptacioncaracter == 99:
                return "Cadena Inválida"
        return "Cadena Válida"

    def funciontransicion(self, simboloentrada):
        estado = self._estadoActual
        pila = self._pila
        topepila = pila[-1:]
        if estado == "Q0":  # Estado inicial, Verifica la primera parte de la palabra.
            if len(pila) == 0:  # Pila vacía
                if simboloentrada == "a":
                    pila.append(simboloentrada)
                else:
                    return 99
            else:
                if topepila[0] == "a" or topepila[0] == "0" or topepila[0] == "1":
                    # Cuando en el tope de pila hay "a", "0" o "1".
                    if simboloentrada == "0" or simboloentrada == "1":
                        pila.append(simboloentrada)
                    elif simboloentrada == "b":
                        self._estadoActual = "Q1"  # Transición al estado Q1
                    else:
                        return 99
        elif estado == "Q1":  # Estado a partir del pivote "b", desapila y verifica el palíndromo
            if len(pila) == 1:  # Solo está la "a" en la pila, solo permite recibir "c"
                if simboloentrada == "c":
                    self._estadoActual = "Q2"
                    pila.pop()
                else:
                    return 99
            else:
                if simboloentrada == topepila[0]:
                    pila.pop()
                else:
                    return 99
        elif estado == "Q2":  # Estado de aceptación, desde aquí no debe transicionar, si aún queda cadena rechaza.
            if simboloentrada != "":
                return 99


automataPrueba = AutomataDePila("a1001001100b0011001001c")
print(automataPrueba.determinaraceptacion())

# TODO: Conseguir que use topepila como un String, NO COMO ARRAY. De manera correcta, sin machetazos
