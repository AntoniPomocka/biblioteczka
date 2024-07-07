# Domowa Biblioteka

To jest prosta aplikacja webowa do zarządzania domową biblioteką. Aplikacja wykorzystuje Flask do obsługi zapytań webowych i SQLAlchemy do interakcji z bazą danych SQLite.

## Instalacja

git clone <https://github.com/AntoniPomocka/biblioteczka)>

1. cd library_app
2. python -m venv venv
3. venv\Scripts\activate
4. pip install -r requirements.txt
5. flask db init
6. flask db migrate -m "Initial migration."
7. flask db upgrade
8. flask run

  Użycie

  Otwórz przeglądarkę i przejdź do http://127/0/0/1:5000/.

  Możesz dodawać nowe książki, edytować istniejące oraz zarządzać wypożyczeniami.

  Jeśli masz jakiekolwiek pytania dotyczące tego projektu lub potrzebujesz dalszej pomocy, daj mi znać!