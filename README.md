# Domowa Biblioteka

To jest prosta aplikacja webowa do zarządzania domową biblioteką. Aplikacja wykorzystuje Flask do obsługi zapytań webowych i SQLAlchemy do interakcji z bazą danych SQLite.

## Instalacja

   git clone <https://github.com/AntoniPomocka/biblioteczka)>
   cd library_app
   python -m venv venv
  .venv\Scripts\activate
  pip install -r requirements.txt
  flask db init
  flask db migrate -m "Initial migration."
  flask db upgrade
  flask run

  Użycie

  Otwórz przeglądarkę i przejdź do http://127/0/0/1:5000/.

  Możesz dodawać nowe książki, edytować istniejące oraz zarządzać wypożyczeniami.

  Jeśli masz jakiekolwiek pytania dotyczące tego projektu lub potrzebujesz dalszej pomocy, daj mi znać!