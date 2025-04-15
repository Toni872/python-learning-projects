import json
from flask import Flask, jsonify, request

# Crear la aplicación Flask
app = Flask(__name__)

# Lista global de empleados
employees = [
    {'id': 1, 'name': 'Ashley'},
    {'id': 2, 'name': 'Kate'},
    {'id': 3, 'name': 'Joe'}
]

# Función para obtener un empleado por ID
def get_employee(id):
    return next((e for e in employees if e['id'] == id), None)

# Ruta GET para obtener todos los empleados
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# Ruta DELETE para eliminar un empleado
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id: int):
    global employees
    # Buscar el empleado por ID
    employee = get_employee(id)
    if employee is None:
        # Si no existe, devolver un error 404
        return jsonify({'error': 'Employee does not exist.'}), 404
    # Eliminar el empleado de la lista
    employees = [e for e in employees if e['id'] != id]
    # Devolver los detalles del empleado eliminado
    return jsonify(employee), 200

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(port=5000)