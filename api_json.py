import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def get_users():
    response = requests.get(BASE_URL)
    print(f"\n✅ GET /users - Status: {response.status_code}")
    try:
        users = response.json()
        for user in users:
            print(f"ID: {user['id']}, Nombre: {user['name']}, Email: {user['email']}")
    except Exception as e:
        print("Error al procesar la respuesta:", e)

def create_user():
    name = input("Nombre: ")
    username = input("Nombre de usuario: ")
    email = input("Email: ")
    user_data = {
        "name": name,
        "username": username,
        "email": email
    }
    response = requests.post(BASE_URL, json=user_data)
    print(f"\n✅ POST /users - Status: {response.status_code}")
    try:
        print(response.json())
    except Exception:
        print("La API devolvió una respuesta vacía o inválida.")

def update_user():
    user_id = input("ID del usuario a actualizar: ")
    name = input("Nuevo nombre: ")
    username = input("Nuevo nombre de usuario: ")
    email = input("Nuevo email: ")
    user_data = {
        "name": name,
        "username": username,
        "email": email
    }
    url = f"{BASE_URL}/{user_id}"
    response = requests.put(url, json=user_data)
    print(f"\n✅ PUT /users/{user_id} - Status: {response.status_code}")
    try:
        print(response.json())
    except Exception:
        print("La API devolvió una respuesta vacía o inválida.")

def delete_user():
    user_id = input("ID del usuario a eliminar: ")
    url = f"{BASE_URL}/{user_id}"
    response = requests.delete(url)
    print(f"\n✅ DELETE /users/{user_id} - Status: {response.status_code}")
    if response.status_code == 200:
        print("Usuario eliminado correctamente (simulado).")
    else:
        print("Error al eliminar usuario.")

def menu():
    while True:
        print("\n--- JSONPlaceholder API - Usuarios ---")
        print("1. Ver usuarios (GET)")
        print("2. Crear usuario (POST)")
        print("3. Actualizar usuario (PUT)")
        print("4. Eliminar usuario (DELETE)")
        print("5. Salir")
        opcion = input("Selecciona una opción (1-5): ")
        if opcion == "1":
            get_users()
        elif opcion == "2":
            create_user()
        elif opcion == "3":
            update_user()
        elif opcion == "4":
            delete_user()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
