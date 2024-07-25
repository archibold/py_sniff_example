from dotenv import load_dotenv
import os
import psycopg2


class Db:
    def __init__(self):
        load_dotenv()
        self._conn = psycopg2.connect(
            dbname=os.environ['POSTGRES_DATABASE'],
            user=os.environ['POSTGRES_USER'],
            host=os.environ['POSTGRES_HOST'],
            password=os.environ['POSTGRES_PASSWORD']
        )

        self._cur = self._conn.cursor()
        self._cur.execute(f"SELECT EXISTS(SELECT relname FROM pg_class WHERE relname = 'exercise');")

        if not self._cur.fetchone()[0]:
            self._cur.execute(
                "CREATE TABLE exercise (_id serial PRIMARY KEY, body_part text, equipment text, gif_url text, "
                "gif_id Int, api_id text, name text, target text, secondary_muscles text[], instructions text[]);")
            self._conn.commit()
            print('Create table...')
        # else:
            # This line is cleaning DB
            # DO NOT UNCOMMENT IT
            ### self.cur.execute('DROP TABLE exercise;')
            ### self.conn.commit()
            print('DB is loaded.')

    def __del__(self):
        self._cur.close()
        self._conn.close()

    def save_exercises(self, exercises):
        for exercise in exercises:
            print('...')
            print(exercise['name'])
            self._cur.execute(
                "INSERT INTO "
                "exercise(body_part, equipment, gif_url, api_id, name, target, secondary_muscles, instructions) "
                "VALUES (%(body_part)s, %(equipment)s, %(gif_url)s, %(api_id)s, %(name)s, %(target)s, "
                "%(secondary_muscles)s, %(instructions)s);",
                {"body_part": exercise['bodyPart'],
                 "equipment": exercise['equipment'],
                 "gif_url": exercise['gifUrl'],
                 "api_id": exercise['id'],
                 "name": exercise['name'],
                 "target": exercise['target'],
                 "secondary_muscles": exercise['secondaryMuscles'],
                 "instructions": exercise['instructions'],
                 }
            )
        print('saving...')
        self._conn.commit()

        print('loaded exec to db')

    def count_exercises(self):
        self._cur.execute('SELECT COUNT(*) FROM exercise')
        return self._cur.fetchone()[0]

    def get_images(self):
        self._cur.execute('SELECT gif_url FROM exercise')
        result = [r[0] for r in self._cur.fetchall()]
        return result


