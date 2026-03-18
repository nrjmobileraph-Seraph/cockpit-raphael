from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any, Iterable

DB_PATH = Path(__file__).parent / 'cockpit.db'


def _translate_sql(sql: str) -> str:
    return sql.replace('%s', '?')


class CursorProxy:
    def __init__(self, cursor: sqlite3.Cursor):
        self._cursor = cursor

    def execute(self, sql: str, params: Iterable[Any] | None = None):
        sql = _translate_sql(sql)
        if params is None:
            self._cursor.execute(sql)
        else:
            self._cursor.execute(sql, tuple(params))
        return self

    def executemany(self, sql: str, seq_of_params):
        self._cursor.executemany(_translate_sql(sql), seq_of_params)
        return self

    def fetchone(self):
        return self._cursor.fetchone()

    def fetchall(self):
        return self._cursor.fetchall()

    @property
    def description(self):
        return self._cursor.description

    def __iter__(self):
        return iter(self._cursor)

    def __getattr__(self, name: str):
        return getattr(self._cursor, name)


class ConnectionProxy:
    def __init__(self, conn: sqlite3.Connection):
        self._conn = conn

    def cursor(self):
        return CursorProxy(self._conn.cursor())

    def execute(self, sql: str, params: Iterable[Any] | None = None):
        return self.cursor().execute(sql, params)

    def commit(self):
        return self._conn.commit()

    def rollback(self):
        return self._conn.rollback()

    def close(self):
        return self._conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.close()

    def __getattr__(self, name: str):
        return getattr(self._conn, name)


def _create_schema(conn: sqlite3.Connection) -> None:
    c = conn.cursor()
    c.executescript(
        '''
        CREATE TABLE IF NOT EXISTS profil (
            id INTEGER PRIMARY KEY,
            nom TEXT DEFAULT 'Raphaël',
            date_naissance TEXT DEFAULT '1975-08-26',
            age_cible INTEGER DEFAULT 92,
            capital_cible REAL DEFAULT 50000,
            taux_mdph INTEGER DEFAULT 75,
            aah_mensuel REAL DEFAULT 625,
            pch_mensuel REAL DEFAULT 0,
            loyer_net REAL DEFAULT 325,
            rail_mensuel REAL DEFAULT 2500,
            rendement_annuel REAL DEFAULT 0.0345,
            rvd_mensuel REAL DEFAULT 0,
            aspa_mensuelle REAL DEFAULT 0,
            revenus_pro REAL DEFAULT 0,
            autres_rentes REAL DEFAULT 0,
            mdph_80plus INTEGER DEFAULT 0,
            updated TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS capital (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT DEFAULT CURRENT_DATE,
            cc REAL DEFAULT 22732,
            livret_a REAL DEFAULT 22950,
            ldds REAL DEFAULT 12000,
            lep REAL DEFAULT 10000,
            av1 REAL DEFAULT 130000,
            av2 REAL DEFAULT 130000,
            av3 REAL DEFAULT 148550,
            av1_date_ouverture TEXT DEFAULT '2016-01-01',
            av2_date_ouverture TEXT DEFAULT '2026-01-01',
            av3_date_ouverture TEXT DEFAULT '2010-01-01',
            av1_versements REAL DEFAULT 120000,
            av2_versements REAL DEFAULT 130000,
            av3_versements REAL DEFAULT 120000,
            av1_rendement REAL DEFAULT 0.035,
            av2_rendement REAL DEFAULT 0.035,
            av3_rendement REAL DEFAULT 0.035,
            av4 REAL DEFAULT 0,
            av5 REAL DEFAULT 0,
            pea REAL DEFAULT 0,
            crypto REAL DEFAULT 0,
            note TEXT DEFAULT '',
            updated TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS surplus_affectation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT DEFAULT CURRENT_DATE,
            montant REAL DEFAULT 0,
            destination TEXT DEFAULT '',
            note TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS lmnp (
            id INTEGER PRIMARY KEY,
            date_acquisition TEXT DEFAULT '2010-01-01',
            valeur_acquisition REAL DEFAULT 180000,
            valeur_terrain REAL DEFAULT 30000,
            travaux REAL DEFAULT 33000,
            loyer_brut_mensuel REAL DEFAULT 900,
            charges_annuelles REAL DEFAULT 2400,
            duree_amort_immeuble INTEGER DEFAULT 30,
            duree_amort_mobilier INTEGER DEFAULT 7,
            valeur_mobilier REAL DEFAULT 8000,
            taux_irl_dernier REAL DEFAULT 0.026,
            date_derniere_revalorisation TEXT DEFAULT '2025-01-01',
            updated TEXT DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS jalons_notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age_jalon INTEGER,
            note TEXT DEFAULT '',
            fait INTEGER DEFAULT 0,
            date_fait TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS chronologie (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_cible TEXT DEFAULT '',
            age_cible REAL DEFAULT 0,
            action TEXT DEFAULT '',
            montant REAL DEFAULT 0,
            sens TEXT DEFAULT 'info',
            categorie TEXT DEFAULT 'autre',
            auto INTEGER DEFAULT 0,
            fait INTEGER DEFAULT 0,
            note TEXT DEFAULT '',
            montant_reel REAL DEFAULT 0,
            date_reelle TEXT DEFAULT '',
            confirme_1mois INTEGER DEFAULT 0,
            date_confirme_1mois TEXT DEFAULT '',
            confirme_6mois INTEGER DEFAULT 0,
            date_confirme_6mois TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS devis_artisans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            corps_metier TEXT DEFAULT '',
            artisan TEXT DEFAULT '',
            devis_montant REAL DEFAULT 0,
            statut TEXT DEFAULT 'a_faire',
            paye_montant REAL DEFAULT 0,
            note TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS aah_suivi (
            mois TEXT PRIMARY KEY,
            montant_prevu REAL DEFAULT 0,
            montant_reel REAL DEFAULT 0,
            date_saisie TEXT DEFAULT ''
        );

        CREATE TABLE IF NOT EXISTS depenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT DEFAULT CURRENT_DATE,
            montant REAL DEFAULT 0,
            categorie TEXT DEFAULT '',
            priorite TEXT DEFAULT 'secondaire',
            description TEXT DEFAULT '',
            source TEXT DEFAULT 'manuel'
        );
        '''
    )

    # Soft migrations for legacy DBs
    migrations = [
        ("ALTER TABLE profil ADD COLUMN pch_mensuel REAL DEFAULT 0",),
        ("ALTER TABLE profil ADD COLUMN rvd_mensuel REAL DEFAULT 0",),
        ("ALTER TABLE profil ADD COLUMN capital_cible REAL DEFAULT 50000",),
        ("ALTER TABLE profil ADD COLUMN aspa_mensuelle REAL DEFAULT 0",),
        ("ALTER TABLE profil ADD COLUMN revenus_pro REAL DEFAULT 0",),
        ("ALTER TABLE profil ADD COLUMN autres_rentes REAL DEFAULT 0",),
        ("ALTER TABLE profil ADD COLUMN mdph_80plus INTEGER DEFAULT 0",),
        ("ALTER TABLE capital ADD COLUMN av1_date_ouverture TEXT DEFAULT '2016-01-01'",),
        ("ALTER TABLE capital ADD COLUMN av2_date_ouverture TEXT DEFAULT '2026-01-01'",),
        ("ALTER TABLE capital ADD COLUMN av3_date_ouverture TEXT DEFAULT '2010-01-01'",),
        ("ALTER TABLE capital ADD COLUMN av1_versements REAL DEFAULT 120000",),
        ("ALTER TABLE capital ADD COLUMN av2_versements REAL DEFAULT 130000",),
        ("ALTER TABLE capital ADD COLUMN av3_versements REAL DEFAULT 120000",),
        ("ALTER TABLE capital ADD COLUMN av1_rendement REAL DEFAULT 0.035",),
        ("ALTER TABLE capital ADD COLUMN av2_rendement REAL DEFAULT 0.035",),
        ("ALTER TABLE capital ADD COLUMN av3_rendement REAL DEFAULT 0.035",),
        ("ALTER TABLE capital ADD COLUMN av4 REAL DEFAULT 0",),
        ("ALTER TABLE capital ADD COLUMN av5 REAL DEFAULT 0",),
        ("ALTER TABLE capital ADD COLUMN pea REAL DEFAULT 0",),
        ("ALTER TABLE capital ADD COLUMN crypto REAL DEFAULT 0",),
    ]
    for (sql,) in migrations:
        try:
            c.execute(sql)
        except sqlite3.OperationalError:
            pass

    if not c.execute('SELECT id FROM profil LIMIT 1').fetchone():
        c.execute(
            '''INSERT INTO profil
               (id, nom, date_naissance, age_cible, capital_cible, taux_mdph, aah_mensuel, pch_mensuel, loyer_net, rail_mensuel, rendement_annuel, rvd_mensuel, aspa_mensuelle, revenus_pro, autres_rentes, mdph_80plus)
               VALUES (1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            ('Raphaël', '1975-08-26', 92, 50000, 75, 625, 0, 325, 2500, 0.0345, 0, 0, 0, 0, 0),
        )

    if not c.execute('SELECT id FROM capital LIMIT 1').fetchone():
        c.execute(
            '''INSERT INTO capital
               (date, cc, livret_a, ldds, lep, av1, av2, av3,
                av1_date_ouverture, av2_date_ouverture, av3_date_ouverture,
                av1_versements, av2_versements, av3_versements,
                av1_rendement, av2_rendement, av3_rendement, note)
               VALUES (CURRENT_DATE, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (22732, 22950, 12000, 10000, 130000, 130000, 148550,
             '2016-01-01', '2026-01-01', '2010-01-01',
             120000, 130000, 120000, 0.035, 0.035, 0.035, 'Initialisation locale'),
        )

    if not c.execute('SELECT id FROM lmnp LIMIT 1').fetchone():
        c.execute('INSERT INTO lmnp (id) VALUES (1)')

    if not c.execute('SELECT mois FROM aah_suivi LIMIT 1').fetchone():
        c.executemany(
            'INSERT INTO aah_suivi (mois, montant_prevu, montant_reel, date_saisie) VALUES (?, ?, ?, ?)',
            [
                ('2026', 625, 0, ''),
                ('2027', 0, 0, ''),
                ('2028', 1033, 0, ''),
                ('2029', 1033, 0, ''),
            ],
        )

    conn.commit()


def connect() -> ConnectionProxy:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    _create_schema(conn)
    return ConnectionProxy(conn)
