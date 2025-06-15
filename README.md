## Actividad 1: API Solo Get

**Ruta 1: /carrera/genero/promedio**

Parámetros
```json
carrera (string)
genero (string)
promedio (float)
```

Respuesta:
```json
[
  {
    "nombre": "AGUILAR MENDOZA, JOAB A.",
    "carrera": "Lic. Ciencias Computación",
    "genero": "Masculino",
    "promedio": 9
  },
  {
    "nombre": "AMADOR LAGUNES, ALEJANDRO",
    "carrera": "Ing. Tecnologias de la Información",
    "genero": "Masculino",
    "promedio": 7
  }
  ]
```
---
**Ruta 2: /matricula/edad/semestre**

Parámetros:
```json
matricula (int)
edad (int)
semestre (int)
```
Respuesta: 
```json
[
  {
    "matricula": 202116739,
    "edad": 22,
    "semestre": 8
  },
  {
    "matricula": 202213377,
    "edad": 21,
    "semestre": 6
  },
  {
    "matricula": 202132799,
    "edad": 22,
    "semestre": 8
  }
  ]
```

---

**Ruta 3: /matricula/edad/correo/genero**

Parámetros
```json
matricula (int)
edad (int)
correo (string)
genero (string)
```

Respuesta:
```json
[
  {
    "matricula": 202116739,
    "edad": 22,
    "correo": "joab.aguilar@alumno.buap.mx",
    "genero": "Masculino"
  },
  {
    "matricula": 202213377,
    "edad": 21,
    "correo": "alejandro.amador@alumno.buap.mx",
    "genero": "Masculino"
  }
]
```
