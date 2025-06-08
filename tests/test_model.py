import unittest
from app.models import datos_model
from database.conexion import obtener_conexion

class TestModeloDatos(unittest.TestCase):

    def setUp(self):
        self.conexion = obtener_conexion()
        self.cursor = self.conexion.cursor()
        self.cursor.execute("""
            INSERT INTO areas_protegidas (no, area_protegida, tipo_area, ubicacion_latitud_longitud,
            invasiones_previas, año_ultima_invasion, proximidad_urbana, nivel_alerta)
            VALUES (29, 'Balcones', 'Parque colina', '0.0000,0.0000', 0, 2020, 'Media', 'Media')
        """)
        self.conexion.commit()

    def tearDown(self):
        self.cursor.execute("DELETE FROM areas_protegidas WHERE no = 29")
        self.cursor.execute("DELETE FROM areas_protegidas WHERE no = 30")
        self.conexion.commit()
        self.cursor.close()
        self.conexion.close()

    def test_actualizar_dato(self):
        datos_model.modificar_dato(29, "nivel_alerta", "Alta")
        self.cursor.execute("SELECT nivel_alerta FROM areas_protegidas WHERE no = 29")
        resultado = self.cursor.fetchone()
        self.assertEqual(resultado[0], "Alta")

    def test_guardar_dato(self):
        dato = {
            "no": 30,
            "area_protegida": "balcones",
            "tipo_area": "Parque colina",
            "ubicacion_latitud_longitud": "1.1111,1.1111",
            "invasiones_previas": 1,
            "año_ultima_invasion": 2020,
            "proximidad_urbana": "Alta",
            "nivel_alerta": "Alta"
        }
        datos_model.insertar_dato(dato)
        self.cursor.execute("SELECT area_protegida FROM areas_protegidas WHERE no = 30")
        resultado = self.cursor.fetchone()
        self.assertEqual(resultado[0], "balcones")

if __name__ == '__main__':
    unittest.main()