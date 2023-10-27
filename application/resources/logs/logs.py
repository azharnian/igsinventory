from application import db
from application.models.logs.logs import Log

def create_log(log_data):
    new_log = Log(
        user_id=log_data["user_id"],
        affected_user_id=log_data["affected_user_id"],
        event_id=log_data["event_id"],
        component_id=log_data["component_id"],
        ip_address=log_data["ip_address"],
    )
    db.session.add(new_log)
    db.session.commit()
    return new_log

def get_all_logs():
    return Log.query.all()

def get_log_by_id(log_id):
    return Log.query.get(log_id)