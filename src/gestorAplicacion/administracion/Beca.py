import pickle

class Beca:
    becas = []

    def __init__(self, cupos, convenio, promedio_requerido, avance_requerido, estrato_minimo,
                 creditos_inscritos_requeridos, ayuda_economica, necesita_recomendacion):
        self.cupos = cupos
        self.convenio = convenio
        self.promedio_requerido = promedio_requerido
        self.avance_requerido = avance_requerido
        self.estrato_minimo = estrato_minimo
        self.creditos_inscritos_requeridos = creditos_inscritos_requeridos
        self.ayuda_economica = ayuda_economica
        self.necesita_recomendacion = necesita_recomendacion
        Beca.becas.append(self)

    # Getters y Setters
    def get_cupos(self):
        return self.cupos

    def set_cupos(self, cupos):
        self.cupos = cupos

    def get_convenio(self):
        return self.convenio

    def set_convenio(self, convenio):
        self.convenio = convenio

    def get_promedio_requerido(self):
        return self.promedio_requerido

    def set_promedio_requerido(self, promedio_requerido):
        self.promedio_requerido = promedio_requerido

    def get_avance_requerido(self):
        return self.avance_requerido

    def set_avance_requerido(self, avance_requerido):
        self.avance_requerido = avance_requerido

    def get_estrato_minimo(self):
        return self.estrato_minimo

    def set_estrato_minimo(self, estrato_minimo):
        self.estrato_minimo = estrato_minimo

    def get_creditos_inscritos_requeridos(self):
        return self.creditos_inscritos_requeridos

    def set_creditos_inscritos_requeridos(self, creditos_inscritos_requeridos):
        self.creditos_inscritos_requeridos = creditos_inscritos_requeridos

    def get_ayuda_economica(self):
        return self.ayuda_economica

    def set_ayuda_economica(self, ayuda_economica):
        self.ayuda_economica = ayuda_economica

    def get_necesita_recomendacion(self):
        return self.necesita_recomendacion

    def set_necesita_recomendacion(self, necesita_recomendacion):
        self.necesita_recomendacion = necesita_recomendacion

    # Métodos estáticos
    @staticmethod
    def get_becas():
        return Beca.becas

    @staticmethod
    def eliminar_beca(beca):
        Beca.becas.remove(beca)

# Ejemplo de serialización y deserialización con pickle
def save_becas(filename):
    with open(filename, 'wb') as file:
        pickle.dump(Beca.get_becas(), file)

def load_becas(filename):
    with open(filename, 'rb') as file:
        Beca.becas = pickle.load(file)
