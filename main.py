class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getCoordenadas(self):
        return self.x, self.y


class Forma:

    def __init__(self, color, coorCentro, nombre):
        self.color = color
        self.coorCentro = coorCentro
        self.nombre = nombre

    def imprimir(self):
        print("-------------------------------------------------")
        print("Nombre de la figura ", self.nombre)
        print("Coordenada donde se encuentra el centro ", self.coorCentro)
        print("Color de la figura ", self.color)

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def setCoorCentro(self, coorCentro):
        self.coorCentro = coorCentro


# -------------------------------------------------------------
class Elipse(Forma):

    def __init__(self, color, coorCentro, nombre, radioMayor, radioMenor):
        super().__init__(color, coorCentro, nombre)
        self.radioMayor = radioMayor
        self.radioMenor = radioMenor

    def imprimir(self):
        super().imprimir()
        print("El radio mayor es ", self.radioMayor)
        print("El radio menor es ", self.radioMenor)
        print("La forma es una elipse")

    def calcularArea(self):
        return 3.14 * (self.radioMayor * self.radioMenor)

    def cambiarDimensiones(self, factor):
        self.radioMayor = self.radioMayor * factor
        self.radioMenor = self.radioMenor * factor


# -------------------------------------------------------------------------

class Circulo(Elipse):

    def __init__(self, color, coorCentro, nombre, radio):
        radioMayor = radio
        radioMenor = radio
        super().__init__(color, coorCentro, nombre, radioMayor, radioMenor)

    def imprimir(self):
        super().imprimir()
        print("La elipse es un circulo")

    def calcularArea(self):
        return super().calcularArea()

    def cambiarDimensiones(self, factor):
        super().cambiarDimensiones(factor)


# --------------------------------------------------------------------
class Rectangulo(Forma):

    def __init__(self, color, coorCentro, nombre, ladoMayor, ladoMenor):
        super().__init__(color, coorCentro, nombre)
        self.ladoMayor = ladoMayor
        self.ladoMenor = ladoMenor

    def imprimir(self):
        super().imprimir()
        print("El lado mayor es ", self.ladoMayor)
        print("E lado menor es ", self.ladoMenor)
        print("La forma es un Rectangulo")

    def calcularArea(self):
        return self.ladoMenor * self.ladoMayor

    def calcularPeri(self):
        return 2 * self.ladoMayor + 2 * self.ladoMenor

    def cambiarDimensiones(self, factor):
        self.ladoMayor = self.ladoMayor * factor
        self.ladoMenor = self.ladoMenor * factor


# -------------------------------------------------------------------------

class Cuadrado(Rectangulo):

    def __init__(self, color, coorCentro, nombre, lado):
        ladoMayor = lado
        ladoMenor = lado
        super().__init__(color, coorCentro, nombre, ladoMayor, ladoMenor)

    def imprimir(self):
        super().imprimir()
        print("El rectangulo es un cuadrado")

    def calcularArea(self):
        return super().calcularArea()

    def calcularPeri(self):
        return super().calcularPeri()

    def cambiarDimensiones(self, factor):
        super().cambiarDimensiones(factor)


# ------------------------------------------------------------------------

punto2D = Punto(2, 5)
punto3D = Punto(13, 80)
punto4D = Punto(10, 89)
punto5D = Punto(100, 100)

forma1 = Forma("Rojo", punto2D.getCoordenadas(), "Forma")
forma1.imprimir()
forma1.getColor()
forma1.setColor("Verde")
forma1.imprimir()
forma1.setCoorCentro(Punto(32, 100).getCoordenadas())
forma1.imprimir()

rectangulo1 = Rectangulo("Azul", punto2D.getCoordenadas(), "Rectangulo", 5, 6)
rectangulo1.imprimir()
print("El area es ", rectangulo1.calcularArea())
print("El perimetro es ", rectangulo1.calcularPeri())
rectangulo1.cambiarDimensiones(2)
rectangulo1.imprimir()

cuadrado1 = Cuadrado("Magenta", punto3D.getCoordenadas(), "Cuadrado", 5)
cuadrado1.imprimir()
print("El area es ", cuadrado1.calcularArea())
print("El perimetro es ", cuadrado1.calcularPeri())
cuadrado1.cambiarDimensiones(2)
cuadrado1.setColor("Rosa")
cuadrado1.imprimir()

elipse1 = Elipse("Amarillo", punto4D.getCoordenadas(), "Elipse", 21, 2)
elipse1.imprimir()
print("El area es ", elipse1.calcularArea())
elipse1.cambiarDimensiones(3)
elipse1.imprimir()

circulo1 = Circulo("Negro", punto5D.getCoordenadas(), "Circulo", 6)
circulo1.imprimir()
print("El area es ", circulo1.calcularArea())
circulo1.cambiarDimensiones(5)
circulo1.imprimir()

# -----------------------------------------------------------------------------------------

lista1 = []
lista1.append(forma1)
lista1.append(rectangulo1)
lista1.append(cuadrado1)
lista1.append(elipse1)
print(len(lista1))

for i in range(len(lista1)):
    lista1[i].setColor("Rosa")
    print("------------------------------------------------------------------")
    print("Para el objeto: ", lista1[i].nombre, " con coordenadas ", lista1[i].coorCentro)
    puntoSeleccionX = int(input("Introduce la nueva coordenada x: "))
    puntoSeleccionY = int(input("Introduce la nueva coordenada y: "))
    lista1[i].setCoorCentro(Punto(puntoSeleccionX, puntoSeleccionY).getCoordenadas())
    lista1[i].imprimir()


# -------------------------------------------------------------------------------------

class Coche:
    def __init__(self, matricula, marca, modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

    def getVariables(self):
        return self.matricula, self.marca, self.modelo


class Empleado:

    def __init__(self, nombre, apellido1, apellido2, dni, direccion, antiguedad, telefono, salario, supervisor):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.dni = dni
        self.direccion = direccion
        self.antiguedad = antiguedad
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor

    def imprimir(self):
        print("-------------------------------------------------------------")
        print("Su nombre es ", self.nombre)
        print("Su primer apellido es ", self.apellido1)
        print("Su segundo apellido es ", self.apellido2)
        print("Su dni es ", self.dni)
        print("Su direccion es ", self.direccion)
        print("Su antiguedad en años es de ", self.antiguedad)
        print("Su telefono de trabajo es ", self.telefono)
        print("Su salario es de ", self.salario, " al mes, un total de ", self.salario * 12, "al año")
        print("Su supervisor es el empleado ", self.supervisor.nombre)

    def cambiarSupervisor(self, supervisor):
        self.supervisor = supervisor

    def incrementarSalario(self, factor):
        self.salario = self.salario + (self.salario * (factor / 100) * self.antiguedad)


class Secretario(Empleado):

    def __init__(self, nombre, apellido1, apellido2, dni, direccion, antiguedad, telefono, salario, supervisor,
                 despacho, fax):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, antiguedad, telefono, salario, supervisor)
        self.despacho = despacho
        self.fax = fax

    def imprimir(self):
        print("Es un/a secretario/a")
        print("Su despacho es ", self.despacho)
        print("Su fax es ", self.fax)
        super().imprimir()

    def incrementarSalario(self, factor):
        super().incrementarSalario(5)


class Vendedor(Empleado):

    def __init__(self, nombre, apellido1, apellido2, dni, direccion, antiguedad, telefono, salario, supervisor, coche,
                 movil, areaVenta, listaClientes, porcentajeComision):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, antiguedad, telefono, salario, supervisor)
        self.coche = coche
        self.movil = movil
        self.areaVenta = areaVenta
        self.listaClientes = listaClientes
        self.porcentajeComision = porcentajeComision

    def incrementarSalario(self, factor):
        super().incrementarSalario(10)

    def imprimir(self):
        print("Es un/a vendedor/a")
        print("La matricula del coche es ", self.coche.matricula)
        print("Su telefono movil es ", self.movil)
        print("Su area de venta es ", self.areaVenta)
        print("Hay ", len(self.listaClientes), " clientes, en la lista")
        for i in range(len(self.listaClientes)):
            print("   El numero ", i + 1, "de la lista es", self.listaClientes[i])

        super().imprimir()

    def altaCliente(self):
        print("----------------------------------------------------")
        dni = input("Introduce el dni del nuevo cliente")
        self.listaClientes.append(dni)

    def bajaCliente(self):
        print("----------------------------------------------------------")
        dni = input("Introduce el dni del cliente que quieres borrar")
        if self.listaClientes.count(dni) == 1:
            self.listaClientes.remove(dni)
            print("Borrado con exito")
        else:
            print("En la lista de clientes del vendedor ", super().nombre, " el cliente con dni", dni, " no existe")

    def cambiarCoche(self, newMatri, newMar, newModel):
        self.coche = Coche(newMatri, newMar, newModel)
        print("El nuevo coche del empresario ", super().nombre, " ahora es ", self.coche.getVariables())


# ------------------------------------------------------------------------------------------------------------------

class Jefe_De_Zona(Empleado):
    def __init__(self, nombre, apellido1, apellido2, dni, direccion, antiguedad, telefono, salario, supervisor,
                 despacho, secretario, listaVendedores, coche):
        super().__init__(nombre, apellido1, apellido2, dni, direccion, antiguedad, telefono, salario, supervisor)
        self.despacho = despacho
        self.secretario = secretario
        self.listaVendedores = listaVendedores
        self.coche = coche
