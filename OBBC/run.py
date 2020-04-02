"""
Script run.py pour permettre démarrer l'application.

Author : Lucas Terriel
Date: 31/03/2020
"""

from app.app import app


if __name__ == '__main__':
    app.run(debug=True)

    # Le paramètre debug permet de se mettre en mode dévellopement

    # port =  3000 (dev)
