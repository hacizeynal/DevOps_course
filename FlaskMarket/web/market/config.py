DEV_DB = "sqlite:///market.db"

pg_user = "zhajili"
pg_pass = "Krakow123"
pg_db = "market"
pg_host = "db"
pg_port = 5432

PROD_DB = f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'