from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Tarefa(db.Model):

    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True) # TESTAR COM SERIAL DPS
    titulo = db.Column(db.String(80), nullable=False)
    concluida = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return{
            'id' : self.id,
            'titulo' : self.titulo,
            'concluida' : self.concluida
        }
